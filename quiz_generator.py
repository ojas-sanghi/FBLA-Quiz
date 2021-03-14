import json
import random
from requests.models import Response
import rsa
import rsa.randnum
import requests
from Crypto.Cipher import AES
import pickle
import codecs

from question import Question

"""
The questions file is stored on a server, and must be delivered to the client in an encrypted format.
It is too big to be encrypted by RSA, so instead the file is encrypted with an AES key, and then the AES key itself is encrypted by the recipient's public RSA key. After that, the encrypted key and file are sent to the recipient, who decrypts them respectively.

Outline of how it is done here:

- The client generates a RSA keyset and sends the public key to the server

- The server generates an AES key (AES is symmetric so the key must be private)
- The server encrypts the question file with the AES key
- The server encrypts the AES key with the client's public RSA key
- The server sends back the encrypted question file and encrypted AES key (and other AES data: the tag and nonce)

- The client decrypts the AES key with its private RSA key (and the given AES tag and nonce)
- The client decrypts with the question file with the AES key
"""
def load_data():
    # 900 bits chosen because it is slightly higher than RSA-260, RSA-270 and RSA-896, none of which have been factored yet
    # We could theoretically go as low as 862 but extra bits were added for assurance, as well as due to the fact that 
    # "accurate" is set to False, meaning the number of bits may fall a bit below the amount specified; a tradeoff made for speed
    # 900 bits is enough to ensure that even with "accurate" set to False, the actual number of bits will remain uncrackable
    (rsa_pubkey, rsa_privkey) = rsa.newkeys(900, False);

    # serialize pubkey into pickle
    pickled_pubkey = pickle.dumps(rsa_pubkey)
    # encode pickle in base64 to be sent across network
    encoded_pickled_pubkey = codecs.encode(pickled_pubkey, "base64").decode()
    # get rid of newlines (does not mess up the encoding), and
    # flask interprets extra "/" this as a subpage, which we don't want; so
    # we replace it with a \, which we change back in the server code
    encoded_pickled_pubkey = encoded_pickled_pubkey.replace("\n", "").replace("/", "\\") 
    
    # request questions from server and give it our public key
    response: Response = requests.get("http://127.0.0.1:5000/get_questions/" + encoded_pickled_pubkey)
    # get JSON representation of data
    encoded_data = response.json()
    # decode each item back into a bytes object
    decoded_data = []
    for data in encoded_data:
        decoded_data.append(codecs.decode(data.encode(), "base64"))
    
    # unpack list into indivdual varibales
    encrypted_raw_data, aes_tag, encrypted_aes_key, aes_nonce = decoded_data

    # decrypt AES key with RSA private key
    decrypted_aes_key = rsa.decrypt(encrypted_aes_key, rsa_privkey)

    # create AES instance with AES key
    decrypt_cipher = AES.new(decrypted_aes_key, AES.MODE_EAX, nonce=aes_nonce)
    # decrypt questions with AES instance
    decrypted_questions: bytes = decrypt_cipher.decrypt(encrypted_raw_data)
    
    # convert bytes to str
    decrypted_questions: str = decrypted_questions.decode("utf8")

    try:
        # ensure data has not been tampered with
        decrypt_cipher.verify(aes_tag)
    except ValueError:
        print("Been tampered with!")

    #? We return it regardless of authenticity
    # Return JSON representation of questions
    return json.loads(decrypted_questions)

    


# function which returns specified number of unique questions
def get_questions(num: int) -> list:
    # data loaded from question.json file
    data = load_data()

    # list of `num` questions, returned to caller
    question_list = []

    # lists to keep track of question ids (to ensure each is unique)
    # and to keep track of question types (to ensure each question type is unique)
    ids_used = []
    types_used = []

    i = 0
    while i < num:
        new_q = get_question(data)

        # if we already used this question, then skip it
        if new_q.id in ids_used or new_q.type in types_used:
            continue
        # if it's a unique question, add it to the lists
        else:
            question_list.append(new_q)

            ids_used.append(new_q.id)
            types_used.append(new_q.type)

            i += 1

    return question_list


# return random question from questions lists
def get_question(data: list) -> Question:
    return Question(random.choice(data))

load_data()
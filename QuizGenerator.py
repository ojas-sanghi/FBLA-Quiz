import json
import random
from typing import List


data: list = []

def load_data():
    global data

    with open("questions.json", "r") as questions:
        raw_data = questions.read()
    data = json.loads(raw_data)
    

def begin_quiz():
    questions = get_questions(5)

    # print(questions)

    for q in questions:
        print_question(q)
    
    # answer = get_input()
    # if answer == new_q['answer']:
    #     print("nice!")
    # else:
    #     print("no.")


def get_questions(num: int) -> list:
    question_list = []

    ids_used = []
    types_used = []

    i = 0
    while i < num:
        new_q = get_question()

        if new_q["id"] in ids_used or new_q["type"] in types_used:
            continue
        else:
            question_list.append(new_q)

            ids_used.append(new_q["id"])
            types_used.append(new_q["type"])

            i += 1
    
    return question_list
        

def get_question():
    return random.choice(data)

    
    
def print_question(q: dict):
    print(q['id'])
    print(q['question'])

def get_input():
    raw_input = input("> ")
    raw_input = raw_input.strip().lower()

    return raw_input

def main():
    load_data()
    begin_quiz()

if __name__ == "__main__":
    main()    
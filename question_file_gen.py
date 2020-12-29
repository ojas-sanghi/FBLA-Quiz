import json

"""
File used to generate questions.json
This was used during development when the format of 
the questions and their associated data (options, answer etc) were
in flux.

This file makes a .json file with 50 questions of 6 different types
To change the format of a particular type of question change the
associated function.
"""


def make_mcq(q_id):
    s = {
        "id": q_id, 
        "type": "mcq", 
        "question": "What does FBLA stand for?",
        "options": ["Future Blooming Leaders of America", "Future Business Leaders of America", "Future Bundle Leaders of America", "Future Business Leaders of Austria"],
        "answer": "Future Business Leaders of America"
    }
    return s

def make_tf(q_id):
    s = {
        "id": q_id, 
        "type": "tf", 
        "question": "True/False: FBLA holds regional competitions",
        "options": ["True", "False"],
        "answer": "True"
    }
    return s

def make_blank(q_id):
    s = {
        "id": q_id, 
        "type": "blank", 
        "question": "FBLA stands for: Future ________ Leaders of America",
        "answer": "business"
    }
    return s


def make_matching(q_id):
    s = {
        "id": q_id, 
        "type": "matching", 
        "question": "Match the animals to their diets",
        "options": ["A) Carnivore", "B) Omnivore", "C) Herbivore"], 
        "words": ["Pig", "Lion", "Zebra", "Horse", "Hedgehog"],
        "answer": {"Pig": "B", "Lion": "A", "Zebra": "C", "Horse": "C", "Hedgehog": "B"}
    }
    return s

def make_checkbox(q_id):
    s = {
        "id": q_id, 
        "type": "checkbox", 
        "question": "Which of the following are true about FBLA? (Choose all that apply)",
        "options": ["Has the BAA program", "It is a college program", "It is a high school program", "It has an entry fee of $150"],
        "answer": ["Has the BAA program", "It is a high school program"]
    }
    return s

def make_saq(q_id):
    s = {
        "id": q_id,
        "type": "saq",
        "question": "What is the full form of the BAA?",
        "answer": "business achievement awards"
    }
    return s

def generate():
    question_list = []
    i = 0

    while i < 50:
        question_list.append(make_mcq(i))
        i += 1
        if not i < 50:
            break
        
        question_list.append(make_tf(i))
        i += 1
        if not i < 50:
            break
            
        question_list.append(make_blank(i))
        i += 1
        if not i < 50:
            break

        question_list.append(make_checkbox(i))
        i += 1
        if not i < 50:
            break

        question_list.append(make_saq(i))
        i += 1
        if not i < 50:
            break
        
        question_list.append(make_matching(i))
        i += 1
        if not i < 50:
            break

    return json.dumps(question_list, indent = 4)

f = open("questions.json", "w+")
f.write(generate())

print("Done.")
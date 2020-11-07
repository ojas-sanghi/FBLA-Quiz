import json

def make_mcq(q_id):
    s = {
        "id": q_id, 
        "type": "mcq", 
        "question": "what does fbla stand for",
        "options": ["future dumb", "future smart", "future scammers", "future leaders"],
        "answer": "future leaders"
    }
    return s

def make_tf(q_id):
    s = {
        "id": q_id, 
        "type": "tf", 
        "question": "True/False: FBLA is goated",
        "answer": "t"
    }
    return s

def make_blank(q_id):
    s = {
        "id": q_id, 
        "type": "blank", 
        "question": "fbla stands for future _ leaders of america",
        "answer": "business"
    }
    return s


def make_matching(q_id):
    s = {
        "id": q_id, 
        "type": "matching", 
        "question": "match the animals to their diets",
        "options": ["carnivore", "omnivore", "herbivore"], 
        "words": ["pig", "lion", "zebra", "horse", "hedgehog"],
        "answer": ["omnivore", "carnivore", "herbivore", "herbivore", "omnivore"]
    }
    return s

def make_dropdown(q_id):
    s = {
        "id": q_id, 
        "type": "dropdown", 
        "question": "where do you live",
        "options": ["arizona", "alaska", "arkansas"],
        "answer": "arizona"
    }
    return s

def generate():
    question_list = []
    
    i = 0
    while i < 50:
        question_list.append(make_mcq(i))
        i += 1
        question_list.append(make_tf(i))
        i += 1
        question_list.append(make_blank(i))
        i += 1
        question_list.append(make_matching(i))
        i += 1
        question_list.append(make_dropdown(i))
        i += 1
    return json.dumps(question_list)

f = open("qqqqq", "w+")
f.write(generate())

print(generate())
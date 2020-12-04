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
        "answer": ["true", "t"]
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

def make_checkbox(q_id):
    s = {
        "id": q_id, 
        "type": "checkbox", 
        "question": "which of the following are true about fbla?",
        "options": ["has BAA", "is college program", "is high school program", "costs $20,000"],
        "answer": ["has BAA", "is high school program"]
    }
    return s

def make_saq(q_id):
    s = {
        "id": q_id,
        "type": "saq",
        "question": "full form of BAA",
        "answer": "business achievemnt awards"
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

        question_list.append(make_matching(i))
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

    return json.dumps(question_list, indent = 4)

f = open("questions.json", "w+")
f.write(generate())

print(generate())
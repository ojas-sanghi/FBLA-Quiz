import json
import random

from question import Question


def load_data():
    with open("questions.json", "r") as questions:
        raw_data = questions.read()
    return json.loads(raw_data)


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

import quiz_generator

def begin_quiz():
    questions = quiz_generator.get_questions(5)
    question_num = 1

    num_correct = 0
    num_incorrect = 0

    for q in questions:
        print("\nQUESTION " + str(question_num))
        q.print_question()

        if q.is_answer_correct(get_input()):
            print("Correct!\n")
            num_correct += 1
        else:
            print("Incorrect")
            num_incorrect += 1
        
        question_num += 1
    
    print("\nTotal: " + str(num_correct) + " / " + str(num_incorrect + num_correct))
    print("GOOD JOB!!!!")


def get_input():
    raw_input = input("> ")
    raw_input = raw_input.strip().lower()

    return raw_input


def main():
    begin_quiz()

if __name__ == "__main__":
    main()    
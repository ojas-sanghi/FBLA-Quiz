class Question:
    def __init__(self, q: dict) -> None:
        self.id = q["id"]
        self.type = q["type"] # mcq, tf, blank, matching, dropdown

        self.text = q["question"]

        if self.type in ["mcq", "matching", "dropdown"]:
            self.options = q["options"]
        else:
            self.options = []
        
        if self.type == "matching":
            self.words = q["words"]
        else:
            self.words = []
        
        self.answer = q["answer"]
    

    # function which prints out question
    # takes into account question type
    def print_question(self):
        print(self.text)
        print("--------------------")

        if self.type == "mcq":
            # index for option 1), 2), etc
            option_num = 1

            # print options
            for option in self.options:
                print(f"{option_num}) {option}")
                option_num += 1
        
        # we already print self.text
        elif self.type == "tf" or self.type == "blank":
            pass
        
        elif self.type == "matching":
            print("Words: " + ", ".join(self.words))
            print("Options: " + ", ".join(self.options))
            print("\nType your answer in this format: \noption1, option2, option3, etc")

        elif self.type == "dropdown":
            print("Options: ")
            print("- " + ", ".join(self.options[0]))
            print("- " + ", ".join(self.options[1]))
            print("\nType your answer in this format: \noption1, option2, etc")
        

    # function which validates user input to see if it's correct
    # takes into account question type
    def is_answer_correct(self, inp: str) -> bool:
        if self.type == "mcq":
            # position of answer in list 
            # plus one since the options start from 1 but 
            # the list starts from 0
            correct_option_num = self.options.index(self.answer) + 1
            # input is the option number or the string of the answer itself
            return inp == self.answer or inp == str(correct_option_num)
        
        # a list of ["t", "true"]
        # either should be acceptable
        elif self.type == "tf":
            return inp in self.answer
        
        elif self.type == "blank":
            return inp == self.answer
        
        elif self.type == "matching":
            # comma separateed string of the answer
            # omnivore, carnivore, herbivore, etc
            correct_answer_format = ", ".join(self.answer)
            return inp == correct_answer_format
        
        elif self.type == "dropdown":
            # comma separateed string of the answer
            correct_answer_format = ", ".join(self.answer)
            return inp == correct_answer_format
        
        return inp == str(self.answer)
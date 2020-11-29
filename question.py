class Question:
    def __init__(self, q: dict) -> None:
        self.id = q["id"]
        self.type = q["type"] # mcq, tf, blank, matching, dropdown

        self.text = q["question"]

        if self.text in ["mcq", "matching", "dropdown"]:
            self.options = q["options"]
        else:
            self.options = []
        
        if self.text == "matching":
            self.words = q["words"]
        else:
            self.words = []
        
        self.answer = q["answer"]
    

    # function which prints out question
    # takes into account type
    def print_question(self):
        print(self.type)
        print(self.text)

    def is_answer_correct(self, inp: str) -> bool:
        return inp == str(self.answer)
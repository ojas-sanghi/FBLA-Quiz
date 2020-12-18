class Question:
    id: str
    type: str
    text: str
    options: list
    words: list

    # no type for this because it can be a list or a string
    response: any
    answer: any

    def __init__(self, q: dict) -> None:
        self.id = q["id"]
        self.type = q["type"] # mcq, tf, blank, matching, checkbox, saq

        self.text = q["question"]
        self.answer = q["answer"]
        self.response = []

        if self.type in ["mcq", "matching", "checkbox"]:
            self.options = q["options"]
        else:
            self.options = []
        
        if self.type == "matching":
            self.words = q["words"]
        else:
            self.words = []
        
    def is_correct(self) -> bool:
        if self.type == "checkbox":
            return sorted(self.response) == sorted(self.answer)
        
        return self.response == self.answer

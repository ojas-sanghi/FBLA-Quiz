class Question:
    def __init__(self, q: dict) -> None:
        self.id = q["id"]
        self.type = q["type"] # mcq, tf, blank, matching, checkbox, saq

        self.text = q["question"]

        if self.type in ["mcq", "matching", "checkbox"]:
            self.options = q["options"]
        else:
            self.options = []
        
        if self.type == "matching":
            self.words = q["words"]
        else:
            self.words = []
        
        self.answer = q["answer"]
class Question:
    id: str
    type: str  # mcq, tf, blank, matching, checkbox, saq
    text: str
    options: list
    words: list

    # no type for this because it can be a list or a string
    response: any
    answer: any

    def __init__(self, q: dict) -> None:
        self.id = q["id"]
        self.type = q["type"]

        self.text = q["question"]
        self.answer = q["answer"]
        if self.type == "checkbox":
            self.answer = sorted(self.answer)
        if self.type in ["saq", "blank"]:
            self.answer = self.answer.lower().strip()

        self.response = []
        if self.type == "matching":
            self.response = {}

        if self.type in ["mcq", "matching", "checkbox", "tf"]:
            self.options = q["options"]
        else:
            self.options = []

        if self.type == "matching":
            self.words = q["words"]
        else:
            self.words = []

    def is_correct(self) -> bool:
        return self.response == self.answer

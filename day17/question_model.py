# create the class with the __init__ method with the text and answer attribute

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# creating terh list of question  from tjhe data's , below is the list of dictionary


Question_bank = [
    Question("What is the capital of India?", "New Delhi"),
    Question("What is the capital of USA?", "Washington DC"),
    Question("What is the capital of UK?", "London"),
    Question("What is the capital of France?", "Paris"),
    Question("What is the capital of Germany?", "Berlin"),
    Question("What is the capital of Italy?", "Rome"),
    Question("What is the capital of Canada?", "Ottawa"),
    Question("What is the capital of Australia?", "Canberra"),
    Question("What is the capital of Japan?", "Tokyo"),
    Question("What is the capital of China?", "Beijing"),
]
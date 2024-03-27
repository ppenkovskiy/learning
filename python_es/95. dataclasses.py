from dataclasses import dataclass


class Question:

    def __init__(self, text, is_true, explanation):
        self.text = text
        self.is_true = is_true
        self.explanation = explanation


@dataclass
class Question:
    text: str = ""
    is_true: bool = False
    explanation: str = ""


q = Question('test', True, 'because')
print(q.text)

q = Question()
print(q.text)


@dataclass(frozen=True)
class Question:
    text: str
    is_true: bool
    explanation: str


q = Question('test', True, 'because')
# q.text = 'test_2' # raise an exception
print(q.text)

# habr.com/ru/post/415829

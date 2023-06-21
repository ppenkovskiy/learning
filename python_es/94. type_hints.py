from random import random
from typing import Optional, Any, Union, List, Tuple, Iterable


class Character:
    def __init__(self, armor: int, power: int):
        self.armor = armor
        self.power = power
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(10, 20)
c1.hit(20)

amount: int
# amount = None  # expected int type, get "None" instead
amount = 10

price: Optional[int]
price = None
# price = 'abcdef'

attack: Any = 'Hi'

length: Union[int, float]
length = 1.0

quotes: List[int] = [1, 2, 3]

player: Tuple[str, int] = ('Kramnik', 2750)

changes_in_rating: Tuple[int, ...]
changes_in_rating = (1, 2, 3, 4)


def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)

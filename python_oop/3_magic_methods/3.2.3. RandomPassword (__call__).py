import random


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        password_length = random.randint(self.min_length, self.max_length)
        return ''.join(random.choice(self.psw_chars) for _ in range(password_length))


psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
min_length = 5
max_length = 20
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for _ in range(3)]

class DigitRetrieve:
    def __call__(self, data, *args, **kwargs):
        try:
            return int(data)
        except:
            return None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))
# print(*digits)
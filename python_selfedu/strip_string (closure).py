def strip_string(string_chars=" "):
    def do_strip(string):
        return string.strip(string_chars)

    return do_strip


strip_1 = strip_string()
strip_2 = strip_string(" !,.;")

print(strip_1(' hello python!..'))
print(strip_2(' hello python!..'))

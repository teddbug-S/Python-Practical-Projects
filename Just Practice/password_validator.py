from string import punctuation


def validate_password(word):
    if len(word) >= 8:
        digit_count = 0
        symbol_count = 0
        for i in word:
            digit_count += 1 if i.isdigit() else 0
            symbol_count += 1 if i in punctuation else 0
        # print(digit_count, symbol_count)
        if digit_count >= 2 or symbol_count >= 2:
            return "Strong Password"
        elif digit_count == 1 and symbol_count == 1:
            return "Good Password"
        elif digit_count == 1 or symbol_count == 1:
            return "Not bad"
        elif not digit_count and not symbol_count:
            return "Weak Password"
    else:
        return "Extremely Weak Password"


if __name__ == '__main__':
    password = "Helloworld"
    print(validate_password(password))

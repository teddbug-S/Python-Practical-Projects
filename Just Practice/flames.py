# FLAMES

def analyze_names(firstname, lastname):
    # to analyze we must make sure both strings are same in terms of case.
    firstname, lastname = list(firstname.strip().lower()), list(lastname.strip().lower())
    result = dict.fromkeys(firstname, 0)
    for letter in firstname:
        if letter in lastname:
            lastname.remove(letter)
            result[letter] += 1

    def neutralize_firstname(data, code):
        for key, value in code.items():
            for _ in range(value):
                data.remove(key)
        return data

    neutralized_names = neutralize_firstname(firstname, result) + lastname
    return len(neutralized_names)


def get_flame(number):
    flames = "FLAMES"
    flames_data = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Admirers',
        'M': 'Married Couples',
        'E': 'Enemies',
        'S': 'Siblings',
    }
    return flames_data.get(flames[(number % len(flames))-1])


def main():
    firstname = input("Enter your name: ")
    secondname = input("Enter a friends name: ")
    result = analyze_names(firstname, secondname)
    print(get_flame(result))


if __name__ == '__main__':
    main()



def replace(seq, new, pos=0, old=None):
        if not pos and old:
            pos = seq.index(old)
        seq.pop(pos)
        seq.insert(pos, new)


def analyze_names(name1, name2):
    name1 = list(name1)
    name2 = list(name2)
    for letter in name1:
        if letter in name2:
            replace(seq=name2, new='', old=letter)
            replace(seq=name1, new='', old=letter)
    result = [letter for letter in [*name1, *name2] if letter]
    return result

def get_flame(letters):
    flames = ['Friends', 'Lovers', 'Admirers', 'Married Couples', 'Enemies', 'Siblings']
    result = flames[len(letters)%len(flames)-1]
    return result


if __name__ == '__main__':
    name1 = input("Enter a name: ").lower()
    name2 = input('Enter a second name: ').lower()
    letters = analyze_names(name1, name2)
    flames = get_flame(letters)
    print(f'\n\t{flames}\n')

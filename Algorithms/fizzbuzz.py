

def fizzbuzz(iterable: list) -> list:
    """ the famous fizzbuzz algorithm """
    def replace(items, pos, new_item) -> None:
        """ Replaces an item in a list """
        items.remove(items[pos])
        items.insert(pos, new_item)
    
    iterable = iterable[:]
    for num in iterable:
        num_pos = iterable.index(num)
        if num % 15 == 0:
            replace(iterable, num_pos, "fizzbuzz")
        elif num % 3 == 0:
            replace(iterable, num_pos, "fizz")
        elif num % 5 == 0:
            replace(iterable, num_pos, 'buzz')
        else:
            pass
    
    return iterable
    

my_list = [i for i in range(1, 16)]
result = fizzbuzz(my_list)
for num, res in zip(my_list, result):
    print(f"{num} --> {res}")
from itertools import zip_longest

def arithmetic_table(value, end, operator = '**'):
    print(f"\n!{'TABLE':-^30}!")
    for val, factor in zip_longest([value], [i for i in range(1, end+1)], fillvalue=value):
        print(val, factor, end=f" = {eval(f'{val} {operator} {factor}')}\n", sep=f' {operator} ')


arithmetic_table(5, 100)
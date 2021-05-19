
nums = [5, 3, 2, 7, 6, 22, 19, 4]

def b_search(target, sequence):
    while True:
        mid = len(sequence)//2
        if target != sequence[mid]:
            try:
                halves = sequence[:mid], sequence[mid:]
                sequence = [i for i in halves if target in i][0]
            except IndexError:
                print(f'Cannot find {target} in {sequence}')
                break
        else:
            print(f"Found {target} in {sequence} at {mid}.")
            break

b_search(7, nums)

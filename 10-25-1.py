with open(f'{input()}.txt', 'r') as file_from:
    with open(f'{input()}.txt', 'w') as file_to:
        data_new = []
        lines = file_from.readlines()
        for line in lines:
            file_to.write(line.split('#')[1])


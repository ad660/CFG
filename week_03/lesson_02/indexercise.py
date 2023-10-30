def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.readlines())
    except FileNotFoundError as exc:
        print(exc)

read_file('reg.txt')
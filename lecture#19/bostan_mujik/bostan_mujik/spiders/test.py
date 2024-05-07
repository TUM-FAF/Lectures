def return_list():
    return [1, 2, 3]


def generate_list():
    yield 1

    yield 2

    yield 3


for item in return_list():
    print(item)


for item in generate_list():
    print(item)

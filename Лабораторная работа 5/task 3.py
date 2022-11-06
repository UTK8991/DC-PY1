from random import randint

def get_unique_list_numbers() -> list[int]:
    set_list = set()
    while len(set_list) < 15:
        set_list.add(randint(-10, 10))
    return list(set_list)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

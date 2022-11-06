from string import ascii_lowercase, ascii_uppercase, digits
from random import sample

def get_random_password(n: int = 8) -> str:
    list_symbol = list(ascii_uppercase + ascii_lowercase + digits)
    return "".join(sample(list_symbol, k=n))

print(get_random_password())

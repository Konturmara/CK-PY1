from random import sample


def get_random_password(n: int = 8) -> str:
    mylist_ = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
    return "".join(sample(mylist_, k=n))


print(get_random_password())

from random import randint


def rand_arr(minn, maxx):
    res = [randint(minn, maxx - 1) for _ in range(19)]
    return res

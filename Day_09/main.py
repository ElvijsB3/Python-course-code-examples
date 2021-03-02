import random


def random_gen():
    res_1 = [random.randrange(0, 20, 1) for i in range(5, 25)]
    res_2 = [random.randrange(0, 20, 1) for i in range(5, 25)]

    return res_1+res_2


def max_list_value(input):
    return max(input)


if __name__ == '__main__':
    list_value = random_gen()
    print(max_list_value(list_value))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

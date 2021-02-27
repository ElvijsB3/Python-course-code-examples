import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def generate_file(count):
    lst_rows = []
    for i in range(count):
        result = ""
        for j in range(6):
            result += str(random.randint(1, 10)) + ","
        result = result.rstrip(",")
        result += "\n"
        lst_rows.append(result)
    f = open("task1.txt", "w")
    f.writelines(lst_rows)


def average_file():
    try:
        num_lines = sum(1 for line in open("task1.txt", "r"))
        f = open("task1.txt", "r")

        file = f.readlines()
        count = 0
        # print(file)
        for i in range(num_lines):
            # print(file[i])
            file[i] = file[i].rstrip('\n')
            num_list = file[i].split(',')

            num_list_len = len(num_list)

            line_sum = 0
            total_sum = 0
            for val in num_list:
                line_sum += int(val)
                total_sum += line_sum
            print(f'Line summ: {line_sum}')
            print(f'Line leng: {num_list_len}')
            print(f'Line average: {line_sum/num_list_len}')


    finally:
        f.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    average_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

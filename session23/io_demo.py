import os


def read_data(filepath):
    # file = open("data/pride and prejudice.txt", "r", encoding="utf-8")
    # # print(file.read())
    # # print(file.readline())
    # # print(file.readlines())
    # print(len(file.readlines()))

    # context manager (it will take care of closing, etc.)
    with open(filepath, "r", encoding="utf-8") as file:
        first_line = file.readline()
        print(first_line)


def write_data(filepath):
    with open(filepath, "w", encoding="utf8") as file:
        # file.write('Hey Jude\n')
        # file.write("Don't make it bad\n")
        lyrics = [
            "Hey Jude\n",
            "Don't make it bad\n",
            "Take a sad song\n",
            "and make it better\n",
        ]
        file.writelines(lyrics)


def os_demo():
    cwd = os.getcwd()
    # print(cwd)
    # print(os.path.isfile('data'))
    # print(os.path.isdir('data'))
    datafile_list = os.listdir("data")
    # print(datafile_list)
    for file in datafile_list:
        read_data("data/" + file)
        if file.endswith('.csv'):
            pass # process the csv file


def main():
    # files = ['data/output.txt', 'data/pride and prejudice.txt']
    # filepath = "data/output.txt"
    # write_data(filepath)
    # read_data(filepath)

    os_demo()


main()

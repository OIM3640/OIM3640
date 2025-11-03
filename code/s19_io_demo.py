import os


def read_data(filepath):
    """"""
    # file = open(filepath, "r", encoding="utf8")
    # # data = file.read()  # read the file as one big string
    # # data = file.readline()  # read the first line
    # data = file.readlines()  # read the entire file and load it by lines into a list
    # print(len(data))
    # print(type(data))
    # print(data)

    # context manager
    with open(filepath, "r", encoding="utf8") as file:
        # data = file.read()  # read the file as one big string
        # data = file.readline()  # read the first line
        data = file.readlines()  # read the entire file and load it by lines into a list
        print(len(data))
        print(type(data))
        print(data)


def write_data(filepath):
    """"""
    with open(filepath, "w", encoding="utf8") as file:
        # file.write("Hey Jude\n")
        # file.write("Dont make it bad\n")
        lyrics = [
            "Hey Jude\n",
            "Dont make it bad\n",
            "Take a sad song\n",
            "And make it better\n",
        ]
        file.writelines(lyrics)


def os_demo():
    """"""
    cwd = os.getcwd()
    # print(cwd)

    print(os.path.isdir("data"))
    print(os.path.isdir("data/words.txt"))
    print(os.path.isfile("data/words.txt"))
    print(os.listdir("data"))
    for file in os.listdir("data"):
        if file.endswith(".txt"):
            print(file)  # process the file


def main():
    # filepath = "data/words.txt"
    # read_data(filepath)

    # filepath = "data/lyrics.txt"
    # write_data(filepath)
    os_demo()


if __name__ == "__main__":
    main()

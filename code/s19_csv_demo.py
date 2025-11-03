def read_csv(filepath):
    """
    TODO: Read a CSV file and return the data in best format
    """
    with open(filepath, "r", encoding="utf8") as file:
        # data = file.read()  # read the file as one big string
        # data = file.readline()  # read the first line
        data = file.readlines()  # read the entire file and load it by lines into a list
        return data


def process_data(data):
    """Extract useful information from the raw data."""
    for line in data:
        # Process each line
        print(line.strip().split(","))


def main():
    file = "data/portfolio.csv"
    data = read_csv(file)
    # process_data(data)


main()

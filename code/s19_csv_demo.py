import csv


def write_data(data, filepath):
    """"""
    with open(filepath, "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file)
        header = ["name", "shares", "price"]
        writer.writerow(header)
        writer.writerows(data)
        # for row in data:
        #     writer.writerow(row)


def read_csv(filepath):
    """
    Read a CSV file and return the data in best format using csv module.
    """
    with open(filepath, "r", encoding="utf8") as file:
        reader = csv.reader(file)
        data = []  # a list of dicts
        # read the first row as keys

        # skip the first row, data will be a list of lists
        next(reader)
        for row in reader:
            data.append([row[0], int(row[1]), float(row[2])])
        return data


def find_expensive_stocks(filepath):
    with open(filepath, "r", encoding="utf8") as file:
        reader = csv.reader(file)
        data = []
        next(reader)
        for row in reader:
            if float(row[2]) > 250:
                print([row[0], int(row[1]), float(row[2])])


def calculate_total_value(filepath):
    """"""




def main():
    stocks = [
        ["AAPL", 200, 250],
        ["NVDA", 100, 500],
        ["META", 150, 200],
    ]
    file = "data/stocks.csv"  # https://github.com/OIM3640/resources/blob/main/code/data/portfolio.csv
    write_data(stocks, file)
    data = read_csv(file)
    print(data)
    # process_data(data)
    # find_expensive_stocks(file)


main()

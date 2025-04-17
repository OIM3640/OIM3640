import csv


def write_data_to_csv(data, filepath):
    """"""
    with open(filepath, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        header = ["Ticker", "Shares", "Price"]
        csv_writer.writerow(header)
        for row in data:
            csv_writer.writerow(row)


def read_data_from_csv(filepath):
    with open(filepath, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        # skip the header row
        next(csv_reader)
        data = []
        for row in csv_reader:
            data.append([row[0], int(row[1]), float(row[2])])
        return data


def find_expensive_stock(filepath):
    with open(filepath, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        # skip the header row
        next(csv_reader)
        data = []
        for row in csv_reader:
            price = float(row[2])
            if price > 150:
                data.append([row[0], int(row[1]), float(row[2])])
        return data


def main():
    # stocks = [
    #     ["AAPL", 100, 195.28],
    #     ["NVDA", 50, 100.62],
    #     ["GOOG", 200, 152.21],
    # ]
    file = "data/stocks.csv"
    # write_data_to_csv(stocks, file)
    # stocks = read_data_from_csv(file)
    # print(stocks)
    print(find_expensive_stock(file))


main()

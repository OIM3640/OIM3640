import sqlite3


def create_portfolio_db(db_path):
    """Create a database, stocks, then create an empty table to store portfolio data"""
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS portfolio (symbol TEXT, shares INTEGER, price REAL)"
        )


def insert_data(data, db_path):
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        cursor.executemany("INSERT INTO portfolio VALUES (?, ?, ?)", data)


def display_data(db_path):
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        for row in cursor.execute("SELECT * FROM portfolio"):
            print(row)


def find_expensive_stocks(threshold_price, db_path):
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        result = cursor.execute(
            "SELECT * FROM portfolio WHERE price > ?", (threshold_price,)
        )
        for row in result:
            print(row)


def main():
    db_path = "data/stocks.db"
    # create_portfolio_db(db_path)
    stocks = [
        ["AAPL", 100, 195.28],
        ["NVDA", 50, 100.62],
        ["GOOG", 200, 152.21],
    ]
    # insert_data(stocks, db_path)
    display_data(db_path)

    threshold = 180
    print("\nExpensive stocks:")
    find_expensive_stocks(threshold, db_path)


main()

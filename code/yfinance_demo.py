import yfinance as yf
import pprint

dat = yf.Ticker("MSFT")

# print(dat.info['shortName'])
# print(dat.info['marketCap'])
# print(dat.history(period="5d"))
pprint.pprint(dat.info)
print(dat.info["regularMarketPrice"])

from forex_python.converter import CurrencyRates
import datetime as dt

date = dt.datetime(2022, 10, 3)
c = CurrencyRates()

#countries = ["EUR", "USD"]

print('Currency as of {}'.format(date))
print(c.convert('USD','EUR',1),"eur")


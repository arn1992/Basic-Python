s={
        'AAPL':201,
    'GOOG':800,
    'F':54,
    'MSFT':313,
    'TUNA':68,
}


print(min(s))

#(434,goog) (325,aapl)

min_price=min(zip(s.values(),s.keys()))
print(min_price)

min_price1=min(zip(s.keys(),s.values()))
print(min_price1)

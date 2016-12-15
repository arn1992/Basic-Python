stocks={
    'GOOG': 520.54,
    'FB':76.45,
    'Yahoo':39.28,
    'Amazon': 306.21,
    'AApl': 99.76
}

print(min(zip(stocks.values(),stocks.keys())))
print(max(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.keys(),stocks.values())))

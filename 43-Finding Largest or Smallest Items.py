import  heapq


number=[500,700,200,900,600,100]

print(heapq.nlargest(3,number))

print(heapq.nsmallest(6,number))

stocks=[
    {'ticker':'AAPL','price':201},
    {'ticker': 'GOOG', 'price':800},
    {'ticker': 'F', 'price':54},
    {'ticker':'MSFT','price':313},
    {'ticker':'TUNA','price':68}
]

print(heapq.nsmallest(3,stocks,key=lambda stocks:stocks['price']))
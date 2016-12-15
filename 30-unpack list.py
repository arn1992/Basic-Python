date,item,price=['december 23,2015','bread gloves',8.51]

print(item)

def drop_first_last(grades):
    first,*middle,last=grades
    avg=sum(middle)/len(middle)
    print(avg)

drop_first_last([65,76,98,54,21])
drop_first_last([65,76,98,45,80,69,54,21])
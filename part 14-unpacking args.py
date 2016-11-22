def health(age, fruit_eat, drinks):
    ans=(50-age)+(fruit_eat*3.4)-(drinks/2)
    print(ans)

my_data=[24,5,2]

health(my_data[0],my_data[1],my_data[2])
health(*my_data)
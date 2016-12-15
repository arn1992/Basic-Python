from operator import itemgetter

users=[
    {'fname': "aminur","lname": "ratul"},
    {'fname': "nunu", "lname": "gomes"},
    {'fname': "fucking","lname": "kidding"},
    {'fname': "really", "lname": "awsome"},
    {'fname': "vodka", "lname":"needs"},
    {'fname': "dont","lname":"help him"},
    {'fname': "vodka", "lname": "police"},
    {'fname': "vodka", "lname": "devis"},
]

for x in sorted(users,key=itemgetter('fname')):
    print(x)
print("2nd things:")
for x in sorted(users,key=itemgetter('lname')):
    print(x)

print("..........")

print("real sort")

for x in sorted(users,key=itemgetter('fname',"lname")):
    print(x)
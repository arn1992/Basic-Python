from operator import attrgetter

class  user:
    def __init__(self,x,y):
        self.name=x
        self.user_id=y

    def __repr__(self):
        return self.name +" : "+str(self.user_id)


users=[
    user('ratul',43),
    user('montu',34),
    user('jhontu',9),
    user('lala',88),
    user('gala',98)
]

for x in  users:
    print(x)

print("....sort by name......")

for c in sorted(users,key=attrgetter("name")):
    print(c)

print("....sort by user_id......")

for s in sorted(users,key=attrgetter("user_id")):
    print(s)
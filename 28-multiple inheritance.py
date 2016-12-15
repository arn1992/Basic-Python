class mario():
    def eat(self):
        print('i want food')
class mama():
    def  mia(self):
        print('mama mia very cool')


class bigboy(mario,mama):
    pass


bb=bigboy()
bb.eat()
bb.mia()
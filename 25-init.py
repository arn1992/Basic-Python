class Tuna:
    def __init__(self):
        print("blderiofgt")
    def swim(self):
        print('i love tuna')
flip=Tuna()
flip.swim()

class enemy:
    def __init__(self,x):
        self.energy=x

    def get_energy(self):
        print(self.energy)

vin_desel=enemy(5)
the_rock=enemy(10)

vin_desel.get_energy()
the_rock.get_energy()

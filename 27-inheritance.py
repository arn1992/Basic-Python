class parent():
    def print_first_name(self):
        print("aminur")
class child(parent):
    def print_last_name(self):
        print("ratul")
  #  def print_first_name(self): over-riding
   #     print('ffffffff')
r=child()
r.print_first_name()
r.print_last_name()
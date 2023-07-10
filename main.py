
#lets make a quick edit here

with open('hello.txt') as text_file:
    text_data = text_file.readline()

class Employee():
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
  def say_id(self):
    print("My id is " + str(self.id))

e1 = Employee()
e2 = Employee()
e1.say_id()
e2.say_id()

    




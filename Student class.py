#Studnet class
#=============

class Student():
    def __init__(self,s_name,s_class,year_group):
        self.s_name = s_name
        self.s_class = s_class
        self.year_group = year_group

    def display(self):
        print(self.s_name)
        print(self.s_class)
        print(self.year_group)
        


S_object = Student("mustafa","10B","Year 10")
S_object.display()


#Car class
#=========
class Car(Student):
    def __init__(self,company,color,model,year,seats,s_name,s_class,year_group):
        super().__init__(s_name,s_class,year_group)
        self.color = color
        self.model = model
        self.company = company
        self.year = year
        self.seats = seats
    
    def display(self):

        print(self.company)
        print(self.model)
        print(self.color)
        print(self.year)
        print(self.seats)

    
c_object = Car("Bmw","Black","340i","2025","5 seats","Mustafa","13A","Year 13")
#c_object.dis_car()
c_object.display()


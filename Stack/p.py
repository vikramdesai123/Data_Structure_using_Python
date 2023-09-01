# class Emp:
#     def __init__(self,nm="sachin",ag=20) -> None:
#         #instance variable
#         self.name=nm
#         self.age=ag
        
#     def r_d(self):
#         self.role="QA"
#         print("my name is ",self.name)
#         print("%s's role is %s and salary is %d"%(self.name,self.role,self.sal))
        
#     def j_d(self):
#         self.role="QA"
#         print("my name is",self.name)
#         print("my salary is",self.sal)
        
# class Company(Emp):
#     def __init__(self) -> None:
#         self.company_name="PTC"
#         super().__init__()
#     def salesForce(self):
#         print("%s is an employee of %s"%(e2.name,self.company_name))
    
    
    
# e1=Emp()

# #set attribute value by using object
# e1.name="vikram"
# e1.age=20
# setattr(e1,"sal",20000)#add new variable by using object
# e1.r_d()

# e2=Emp()
# e2.name="shantanu"
# e2.age=23
# setattr(e2,"sal",25000)
# e2.j_d()

# print("----------------------------")

# c=Company()
# c.salesForce()


        #class variable

class Game:
    Gname="cricket"
    @classmethod
    def play(cls):
        print(cls.Gname)
Game.Gname="football"
Game.play()
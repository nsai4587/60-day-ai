#classes and object 
class Patient:
    def __init__(self, patient_id, age, sex):
        self.patient_id= patient_id
        self.age = age
        self.sex=sex 
    def is_male(self):
        return self.sex == "male"
P1 = Patient("P001", 45, "male")
P2 = Patient("P002", 16, "female")

print(P1.patient_id, P1.sex)
print(P2.age, P2.sex)
print(P1.is_male())
print(P2.is_male())

# type hints:
class ChatMessage:
    def __init__(self, role: str, content:str):
        self.role=role
        self.content =content
        
    def show(self )->str:
        return self.role+": "+self.content
  
m1= ChatMessage("user", "what is a class?")
m2= ChatMessage("assistant", "A class is a template for objects.") 

print(m1.show())
print(m2.show())

conversation  = [m1, m2]

for message in conversation :
    print(message.show())
# today's topic functions and loops:
def square(a):
    a=a*a 
    return a

a=int(input("enter a number: ")) 
print(square(a))



def biweekly_salary(hours_worked, base_salary):
    total_salary = hours_worked*base_salary
    return total_salary

name=input("Enter person name: ")
hours_worked = int(input("Enter the hours he worked: "))
base_salary= int(input("enter his base pay: "))
print(name, "earns", biweekly_salary(hours_worked, base_salary))

def clean_word(word):
    word = word.lower()
    word = word.strip(".,!?#$%")
    return word 
messy = ["RAMA", "Sita", "LaKsHma", "Bartha@", "hanuma@$%"]
for w in messy:
    print(clean_word(w))

 
print("\n")
file=[
     {"name":"Shaikat","score":95},
     {"name":"dipto","score":79},
     {"name":"akhi","score":89},
     {"name":"pulok","score":60}
     ]

print("Here is the student info")
print("--------------------------")
print("\n")
print(f"{"name":<6}\t\t{"score"}")
print("--------------------------")
for info in file:
        print(f"{info['name']}\t\t{info['score']}")
print("\n")
def calculate_grade(marks):
        if marks>90:
                return"Golden A+"
        elif marks>70:
                return"A"
        elif marks>80:
                return"A+"
        elif marks>50:
                return"A-"
        



print(f"{"Name":<6}\t\t{"Score":5}\t\t{"Grade"}")
print("-------------------------------------------")
for list in file:
        grade=calculate_grade(list['score'])
        print(f"{list['name']}\t\t{list['score']}\t\t{grade}")

print("Choose the correct answere")
print("----------------------------")
print("\n")
print("Who First invent Python")
name={"A)":"Shaikat","B)":"Rudro","C)":"Bikron","D)":"Sagor"}
ans=["A","B","C"]
cans=[]
wans=[]



print("-------------------------")
for x,y in name.items():
        print(f"{x}{y}")
name1=input("Choose your answere A\B\C\D: ") 
if name1=="A":
   cans.append(name1)
elif name1=="B":
      wans.append(name1)
elif name1=="C":
      wans.append(name1)
else:
      wans.append(name1) 
print("-----------------------")


print("\n")
print("-----------------------")
print("Who First invent Java")
name={"A)":"Shaikat","B)":"Rudro","C)":"Bikron","D)":"Sagor"} 


for x,y in name.items():
        print(f"{x}{y}")
name1=input("Choose your answere A\B\C\D: ") 
if name1=="B":
   cans.append(name1)
elif name1=="A":
      wans.append(name1)
elif name1=="C":
      wans.append(name1)
else:
      wans.append(name1) 
print("-----------------------")



print("\n")
print("-----------------------")
print("Who First invent C")
name={"A)":"Shaikat","B)":"Rudro","C)":"Bikron","D)":"Sagor"} 


for x,y in name.items():
        print(f"{x}{y}")
name1=input("Choose your answere A\B\C\D: ") 
if name1=="B":
   wans.append(name1)
elif name1=="A":
      wans.append(name1)
elif name1=="C":
      cans.append(name1)
else:
      wans.append(name1)
print("-----------------------")
print("\n")
print("Your correct answere list",cans)
print("\n")


print("Actual Answere is=",ans)
print("Your total correct answere is",len(cans),"/3")





print("\n"*5)
file={
        "chal":80,
        "dal":90,
        "tel":100,
        "peyaj":120
     }
info=[]
alpha=[]

print("Welcome to The Super Shop")
print("-------------------------")
for x,y in file.items():
        print(f"{x}\t\t{y}")
print("-------------------------") 
print("\n")

item=input("Enter the item name: ").split()
weight=[int(x) for x in input("Enter the weight ").split()]
print("\n")
print(f"{"item":<5}\t\t{"price":<6}\t\t{"amount":<6}\t\t{"Total price"}")



for index,(x,y) in enumerate(zip(item,weight)):
        print(f"{x}\t\t{file[x]}\t\t{y}\t\t{file[x]*y}")
        info.append(file[x]*y)
        dipto=sum(info)

print("------------------------------------------------------")       
print(f"{"Price":<31}",dipto)
print(f"{"VAT 5%":<31}",((5*dipto)/100))
alpha.append(dipto)
sk=alpha
pk=(5*dipto)/100
dk=sum(sk,pk)
print("\n")
print("-------------------------")
print(f"{"total price":<31}",dk)
print("------------------------")
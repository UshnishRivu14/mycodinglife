names = ["Milo","Sarah","Bruno","Anastasia","Rosa"]
nameswith_o = [item for item in names if "o" in item]
print(nameswith_o)

nameswith_morelength = [item for item in names if len(item)>4]
print(nameswith_morelength)

lst = [0,1,2,3,4,5,6,7,8,9]
lst1 = [i for i in range(4)]
print(lst1)

lst2 = [i*i for i in range(4)]
print(lst2)

lst3 = [i*i for i in range(10) if i%2==0]
print(lst3)



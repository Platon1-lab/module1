my_dict={"Платон":1979, "Савва":2010}
print(my_dict)
print(my_dict["Платон"])
print(my_dict.get("Вася"))
my_dict.update({"Настя":1982, "Анна":2008})
print(my_dict)
a=my_dict.pop("Анна")
print(a)
print(my_dict)

my_set={1,"salad", 1,2, "salad", True}
print(my_set)
my_set.add(4)
my_set.add(5)
print(my_set)
my_set.remove("salad")
print(my_set)
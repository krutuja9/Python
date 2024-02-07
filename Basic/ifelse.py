# age = int(input("enter your age: "))

# if(age >= 18):
#   print("You can drive")

# elif(age == 1):
#   print("You are a kid") 
# else:
#   print("You can't drive")

# print("End")

a = 4
match a:
  case 1:
    print("Case is 1")

  case 2:
    print("case is 2")

  case 3 : 
    print("case is 3")

  case _:
    print("No Match found")
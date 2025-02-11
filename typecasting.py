#typecasting - the process of converting a variable from one
#              data type to another. str(), int(), float(), bool()

name = 'Shriya'
age = 20
gpa = 3.4
room_no = 54
is_student = True

#type() function - tells the type of variable
gpa = int(gpa)
age = float(age)
room_no = str(room_no)

name = bool(name)
# will return false if the string is empty.

print(gpa)
print(age)
print(room_no)
print(type(room_no))
print(name)
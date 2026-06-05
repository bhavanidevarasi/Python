
with open("student.txt", "a+") as file:
    file.write("How are you!!")
    file.seek(0)
    print(file.read())
    
with open("students.csv", "w") as file:
    file.write("Name,Age\n")
    file.write("Bhavani,21")

with open("students.csv", "r") as file:
    print(file.read())
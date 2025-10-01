'''f-string yordamida float qiymatni 2 xonagacha formatlang'''

name = input("Ismingizni kiriting: ")
gpa = float(input("Gpaningizni kiriting: "))

result = f"Name: {name}, GPA: {gpa:.2f}"

print(result)
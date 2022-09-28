salary = int(input("enter number:"))
if salary <= 5000:
    tax = 0
elif salary <= 8000:
    tax = (salary - 5000) * 3 / 100
elif salary <= 17000:
    tax = 3000 * 3 / 100 + (salary - 5000 - 3000) * 0.1
elif salary <= 30000:
    tax = 3000 * 3 / 100 + 9000 * 0.1 + (salary - 5000 - 12000) * 0.2
elif salary <= 40000:
    tax = 3000 * 3 / 100 + 9000 * 0.1 + 13000 * 0.2 + (salary - 25000 - 5000) * 0.25
print("Tax is", tax, "RMB")
print("The after-tar salary is", salary - tax, "RMB")

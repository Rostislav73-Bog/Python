num1 = int(input("Введите первое число = "))
num2 = int(input("Введите второе число = "))


def Addition(num1,num2):
    summa = (num1+num2)
    return summa
print ("Сложение = ",Addition(num1,num2))


def Subtracrion(num1,num2):
    if (num1>=num2):
        subraction = (num1-num2)
        return subraction
    else:
        subraction = (num2-num1)
        return subraction
print("Вычитание = ", Subtracrion(num1,num2))


def Division(num1,num2):
    division = (num1/num2)
    return division
print("Умножение = ",Division(num1,num2))


def Multiplication(num1,num2):
    multiplication = (num1*num2)
    return multiplication
print("Умножеие = ", Multiplication(num1,num2))


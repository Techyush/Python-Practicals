try:
    print("Try Block")
    x = int(input("Enter a number: "))
    y = int(input("Enter second number: "))
    z = x / y
except ZeroDivisionError:
    print("except Zero Division Error Block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("Finally Block")
    x = 0
    y = 0
print("Out of try, except, else and finally blocks")

# Task 1 - Input errors
value = int(input('Enter an integer:\n'))
print('The half of', value, 'is', value/2)

# Task 2 - Remove error
value = input('Enter an integer:\n')
if value.isdecimal():
    value = int(value)
    print('The half of', value, 'is', value/2)
else:
    print("The input value is not an integer.")

# Task 3 - Try-except
try:
    value = int(input('Enter an integer:\n'))
    print('The reciprocal of', value, 'is', 1/value)
except:
    print("I can't do this.")


# Task 4-5 - Try-except-except
try:
    value = int(input('Enter an integer:\n'))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print("I can't do this.")
except ZeroDivisionError:
    print("You tried to divide by 0. I don't like it.")
except:
    print("I have no idea what just happened.")

# Task 6 - Missing the error
value = int(input("Enter an integer:\n"))
if value > 0:
    print("It is a positive number.")
elif value < 0:
    print("It is a negative number.")
else:
    print("The number is zero.")

# Task 7 - Enter 0
try:
    value = int(input("Enter a value: "))
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except:
    print("Booo!")

# Task 8 - Try-except-else
def division(a, b):
    try:
        c = a / b
        print("The division of", a, "/", b, "is", c, ".")
    except TypeError:
        print("At least one parameter is incorrect.")
    except ZeroDivisionError:
        print("You divided with 0, that is not wise.")
    else:
        print("Well done.")
division(0, "a")

# Task 9 - Finally
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# Task 10 - Sum of list
myList = [4, 8, "paper", 15, "code", 16, " ", 23, 42]
value = 0
numbers = 0
for i in range(0, len(myList)):
    try:
        value += myList[i]
    except TypeError:
        print("I can't add", myList[i], "to the sum.")
        print("This value is at index", i, ".")
        print("-------------")
    else:
        numbers += 1
print("There are", numbers, "numbers in the list.")
print("The sum of the numbers is", value, ".")

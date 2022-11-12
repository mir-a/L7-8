try:
    print("start code")
    print(10/0)
    print("No errors")
except NameError:
    print("we have an error")
except ZeroDivisionError:
    print("we have an ZeroDivisionError")

print("code after capsule")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

try:
    print("start code")
    print(10/0)
    print("No errors")
except (NameError, ZeroDivisionError) as error:
    print(error)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

try:
    try:
        print("start code")
        print(dima)
        print("No errors")
    except SyntaxError:
        print("syntax")
except NameError as dima:
    print(dima)

    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

try:
    print("start code")
    print(dima)
    print("No errors")
except NameError as dima:
    print(dima)
else:
    print("I am ELSE")
finally:
    print("THE END")
def add(num):
    try:
        result = 100 / num
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("program is running")
    if num < 0:
        raise ValueError("Number cannot be negative")
    else:
        print("you entered:", num)
add(0)
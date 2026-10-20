## mini project multiplication table 

multiplication_table = int(input("which multipliation table you want : "))


for i in range(1,11):
    if i == 1:
        print("|=============|")
    print(f"{"|"} { multiplication_table} x {i} = {multiplication_table * i } {"|"}")
    if i == 10:
        print("|=============|")

your_name = input("enter your name : ")
your_frd_name = input("enter your frd name : ")
name = []
true = ['t','r','u','e']
love = ['l','o','v','e']

new_count1 = []
new_count2 = []
count1 = 0
    
for i in your_name:
        name.append(i)
for i in your_frd_name:
        name.append(i)
for i in range(4):
    count = 0
    for letter in name:
        if love[i] == letter:
            count+=1
    new_count1.append(count)
for i in range(4):
    count1 = 0
    for letter in name:
        if true[i] == letter:
            count1+=1
    new_count2.append(count1)    

print(f"so your love no is {sum(new_count1)}{sum(new_count2)}")


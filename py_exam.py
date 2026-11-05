name=input("Enter student name")

a=int(input("Enter marks in maths"))
b=int(input("Enter marks in biology"))
c=int(input("Enter marks in physics"))
d=int(input("Enter marks in social sci"))
e=int(input("Enter marks in accounts"))

total = a+b+c+d+e
percentage=total/5
avg=total/5

print("STUDENT REPORT CARD")
print("Name ",name)
print("Percentage %",percentage)
print("Average ",avg)

mark=[a,b,c,d,e]


for i in mark: 
  if(i<0 or i>100):
    print("Invalid mark")
    break
    


for i in mark:
    if i>= 90:
        print(i,"grade A+")
    elif i>=80:
        print(i,"grade A")
    elif i>=70:
        print(i,"grade B")
    elif i>=60:
        print(i,"grade c")
    elif i>=40:
        print(i,"grade D")
    else:
        print(i,"grade F")

    if i >= 40:
        print("PASS")
    else:
        print("FAIL")


if a >= 40 and b >= 40 and c >= 40 and d >= 40 and e >= 40:
    print("Final Result -PASS")
else:
    print("Final Result - FAIL")









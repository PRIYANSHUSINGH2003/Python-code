 name = input("what is your name ?")
 print('singh' in name)   #/name.upper,find,lower and true and false using in 
 old_age = input("Enter your ald age : ")
 new_age = int(old_age) + 2
 print(new_age)
                                         #/sum value
 print("write a program print sum of two number ") 
 first = input("Enter fist number : ")
 second = input("Enter second number : ")
 sum = int(first) + int(second)
 print("This is your answer : " + str(sum))
                                         # althmatic opprater 
 print(5 ** 2)  #(// ,**) ,(%,+,-,/,*);
 i = 5 
 i = i + 2 # same (i +=2)
 # Condition oppreter
 print(3==2)
 print(3!=2)
 print(3!=3)
 print(3>2 or 3<2)
 print(3>2 and 2>6)
 print(not 2>3)
 print(not 3>2)
 # if-else condition
 age=16
 if age >= 18:
     print("you are an adult")
     print("you can vate")
 elif age < 18 and age > 3:
     print("you are in school")
 else:
     print("you are a child")
 #make a calculater  
 a = input("Enter first number : ")
 operator = input(" Enter operator (+,-,%,*,/) :")
 b = input("Enter a second number : ")
 a = int(a)
 b =int(b)
 if operator=="+":
     print(a + b)
 elif operator=="-":
     print(a - b)
 elif operator=="%":
     print(a % b)
 elif operator=="*":
     print(a * b)
 elif operator ==("/"):
     print(a / b)
 else:
     print("This is not valid please try agen!")
 # range calculatr
 range(5)
 number = range(10) 
 # loop concept
 k = 1
 while k <= 5:
     print(k)
     k = k + 1
     # * disgen
 i = 1
 while i <= 5:
     print(i * "*")
     i = i + 1
     # beckword
 j = 5
 while j >= 0:
     print(j * "*")
     j = j - 1

 for item in range(5):
     print(item + 1)

 # list your marks
 marks = [95,65,44,22,11]
 print(marks)
 print(marks[0])
 print(marks[-1])
 print(marks[-2])
 print(marks[0:2])

 marks.append(99)
 print(marks)
 mark = [95,65,44,22,11]
 mark.insert(0,(99))
 print(99 in mark)
 print(93 in mark)

 print(len(marks))
 marks.clear()
 print(marks)

  for score in marks:
       print(score)

  break stement ,continue
students = ["raja","ram","karan","kishan","kamal"]
for student in students:
    if student == "karan":
     continue;
print(student)
for student in students:
   if student == "kishan":
        break;
print(student)



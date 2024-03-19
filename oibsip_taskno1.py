def BMI():
   weight=float(input("enter weight in kilograms"))
   height=float(input("enter height in meters"))
   result=weight/(height**2)
   if result< 18.5:
      print(f"Your weight is {result},You are Underweight!")
   elif result>=18.5 and result<25:
      print(f"Your weight is{result},You are Normal")
   elif result>=25 and result<30:
      print(f"Your weight is{result},You are OverWeight!")
   else:
      print(f"{result}Is an Invalid Input,Enter proper values")

BMI()      



num_1= int(input("number1:"))
num_2= int(input("number2:"))
z = (input(""))
print(num_1)
print(num_2)
if z == "+":
 num_1+num_2
 print ("сума=",num_1+num_2) 

if z == "-":    
   num_1-num_2
   print ("різниця=",num_1-num_2)


elif z == "/":  
   num_1/num_2
   print ("ділення=",num_1/num_2)
   if num_1==0:
      print("на нуль ділити не можна" )
   if num_2==0:
      print("на нуль ділити не можна" )  

if z == "*":  
   num_1*num_2
   print ("множення=",num_1*num_2) 

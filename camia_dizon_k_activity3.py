import math
#Asks the user to enter the length of side a and side b.
length_a = float(input("Enter the length of side a: "))
length_b = float(input("Enter the length of side b: "))


#Computes the answer using the Hypotenuse Formula
c= math.sqrt(pow(length_a,2) + pow(length_b,2))
#Display result rounded to 2 decimal points
print(f"The hypotenuse is : {c:.2f}")

import math
#----------------Arithmetic Expressions------------------#
a = 2.3
b = -1.8
c = 4.15

#/Arithmetic Expressions A
Answer1 = (a-b) / (a+c)
print("Answer 1: ", Answer1)

#/Arithmetic Expressions B
Answer2 = b**3 + a*(a+c)
print("Answer 2: ", Answer2)

#/Arithmetic Expressions C
Answer3 = (-a)*b**2-(c/a)**(1/3)
print("Answer 3: ", Answer3)

#/Arithmetic Expressions D
Answer4 = math.sqrt(a**2+b**2+c**2)
print("Answer 4: ", Answer4)

#----------------Triangle Review------------------#
side_a = 8.3
side_b = 6.5
angle_gammaDEG = 40
angle_gammaRAD = math.radians(angle_gammaDEG)

#/Triangle Review Question A
Height = side_b * math.sin(angle_gammaRAD)
print("Height: ", Height)

#/Triangle Review Question B
side_c = math.sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_gammaRAD))
print("Side c: ", side_c)

#/Triangle Review Question C
#/arcsin was hard to figure out from ^-1
angle_betaRAD = math.asin(Height / side_c)
angle_betaDEG = math.degrees(angle_betaRAD)
print("Angle Beta (degrees): ", angle_betaDEG)

#/Triangle Review Question D
#/arctan was hard to figure out from ^-1
angle_gamma2RAD = math.atan(Height / (side_a - side_c * math.cos(angle_betaRAD)))
angle_gamma2DEG = math.degrees(angle_gamma2RAD)
print("Angle Gamma (degrees): ", angle_gamma2DEG)

#/Triangle Review Question EXTRA CREDIT lol
angle_alphaDEG = 180-(angle_gamma2DEG + angle_betaDEG)
print("Angle Alpha (degrees): ", angle_alphaDEG)

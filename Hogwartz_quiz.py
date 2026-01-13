Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Hello and Welcome to the  Hogwarts")
print("School of Witchcraft and Wizardry!")
print( )
print("Do you like Dawn or Dusk?")
print("1 - Dawn")
print("2 - Dusk")
q1 = int(input("Your answer(1-2): "))
if q1 == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif q1 == 2:
  Hufflepuff  = Hufflepuff + 1
  Slytherin  = Slytherin  + 1
else:
  print('Wrong input')
print( )
print("When I’m dead, I want people to remember me as? ")
print("1 - The Good")
print("2 - The Great")
print("3 - The Wise")
print("4 - The Bold")
q2 = int(input("Your answer(1-4): "))
if q2 == 1:
  Hufflepuff = Hufflepuff + 2
elif q2 == 2:
  Slytherin = Slytherin  + 2
elif q2 == 3:
  Ravenclaw = Ravenclaw  + 2
elif q2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print('Wrong input')
print( )
print("Which kind of instrument most pleases your ear? ")
print("1 - The violin")
print("2 - The trumpet")
print("3 - The piano")
print("4 - The drum")
q3 = int(input("Your answer(1-4): "))
if q3 == 1:
  Slytherin = Slytherin + 4
elif q3 == 2:
  Hufflepuff  = Hufflepuff + 4
elif q3 == 3:
  Ravenclaw  = Ravenclaw + 4
elif q3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print("Wrong input")
print( )
# print("Gryffindor: " + str(Gryffindor))
# print("Ravenclaw: " + str(Ravenclaw))
# print("Hufflepuff: " + str(Hufflepuff))
# print("Slytherin: " + str(Slytherin))

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
  print("GRYYYYYYYYYYFFINDOR!!!🦁")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
  print("Ravenclaw!🦅")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
  print("Hufflepuff!🦨")
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
  print("SLyThErIN!!🐍")

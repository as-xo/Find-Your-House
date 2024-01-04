# total = 6, house with most points win
Gryffindor = int(0)
Ravenclaw = int(0)
Hufflepuff = int(0)
Slytherin = int(0)

ans1 = int(input(""" Q1) Do you like:
       Dawn?: 1 
       Dusk?: 2 
       Answer:  """))

if ans1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif ans1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")

ans2 = int(input("""Q2) When I'm dead, I want people to remember me as:
     The Good: 1
     The Great: 2
     The Wise: 3
     The Bold: 4
     Answer: """))

if ans2 == 1:
    Hufflepuff += 2
elif ans2 == 2:
    Slytherin += 2
elif ans2 == 3:
    Ravenclaw += 2
elif ans2 == 4:
    Gryffindor += 2
else:
    print("Wrong input.")

ans3 = int(input("""Which kind of instrument most pleases your ear?:
     The Violin: 1
     The Trumpet: 2
     The Piano: 3
     The Drum: 4
     Answer: """))
   
if ans3 == 1:
    Slytherin += 4
elif ans3 == 2:
    Hufflepuff += 4
elif ans3 == 3:
    Ravenclaw += 4
elif ans3 == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

max_points = max(Slytherin, Hufflepuff, Ravenclaw, Gryffindor)

if Slytherin == max_points:
    print("You are Slytherin!")
elif Hufflepuff == max_points:
    print("You are Hufflepuff!")
elif Ravenclaw == max_points:
    print("You are Ravenclaw!")
elif Gryffindor == max_points:
    print("You are Gryffindor!")


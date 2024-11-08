

Creatures = [
    [],
    [],
    []
]

for i in range(0, 3):
    
    #print("\nCreature "+ str(i+1) +" Name: ")
    Name = input()
    #print("Creature "+ str(i+1) +" HP: ")
    Hp = int(input())
    #print("Creature "+ str(i+1) +"Level: ")
    CreatureLevel = int(input())

    Creatures[i].append(Name)
    Creatures[i].append((Hp, CreatureLevel))
    

print(Creatures)


#printing by lvl desc.. not finding a better way right now aaaaaaaaaaaa
if Creatures[0][1][1] > Creatures[1][1][1] and Creatures[0][1][1] > Creatures[2][1][1]:
    print(Creatures[0][0])
    if Creatures[1][1][1] > Creatures[2][1][1]:
        print(Creatures[1][0])
        print(Creatures[2][0])
    else:
        print(Creatures[2][0])
        print(Creatures[1][0])
elif Creatures[1][1][1] > Creatures[0][1][1] and Creatures[1][1][1] > Creatures[2][1][1]:
    print(Creatures[1][0])
    if Creatures[0][1][1] > Creatures[2][1][1]:
        print(Creatures[0][0])
        print(Creatures[2][0])
    else:
        print(Creatures[2][0])
        print(Creatures[0][0])
else:
        print(Creatures[2][0])
        if Creatures[0][1][1] > Creatures[1][1][1]:
            print(Creatures[0][0])
            print(Creatures[1][0])
        else:
            print(Creatures[1][0])
            print(Creatures[0][0])




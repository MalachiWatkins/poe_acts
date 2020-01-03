Act1dict = {
    1: "Lioneye's Watch",
    2: "The Coast",
    3: "Mud Flats",
    4: "Tidal Island",
    5: "Submerged Passage",
    6: "The Ledge",
    7: "Flooded Depths ",
    8: "The Climb",
    9: "The Lower Prison",
    10: "The Upper Prison",
    11: "Prisoner's Gate",
    12: "The Ship Graveyard",
    13: "The Cavern of Wrath",
    14: "The Cavern of Anger",
}
place_1 = 1
place1 = place_1
search1 = Act1dict[place1] ## find places in act 1 dict

 ## while loop var





## while loop

while place_1 < 14:
    print('PH')
    place_1 += 1
    with open('Client.txt') as logfile:
        if search1 in logfile.read():
            print('PH')
            print(search1)
        else:
            print("PH_NO")




else:
    print('PH')
with open('Client.txt') as logfile:
    if search1 in logfile.read():
        print('PH')
        print(search1)
    else:
        print("PH_NO")

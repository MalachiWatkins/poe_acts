percent1 = 100

def check():
    global percent1
    place_1 = Place
    search_for = Act1dict[place_1]
    print(search_for)

    with open('Client.txt') as myfile:
        if search_for in myfile.read():
            print('Completed')

        else:
            print("No")
            percent1 -= 10
            print(percent1)
        return

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

Place = 1
while Place < 14:
    check()
    Place += 1

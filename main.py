percent1 = 100
## percentage of acts as well as overall completen
def check():
    loop_2 = 1
    loop2 = loop_2
    while loop2 < 3:
        global percent1
        place_1 = Place

        actsdict = Act_names[loop2]
        Acts = actsdict
        search_for = Acts[place_1]
        print(search_for)






        with open('Client.txt') as myfile:
            if search_for in myfile.read():
                print('Completed')

            else:
                print("No")
                percent1 -= 7.14

                print('pERCENT OF ACT 1 ', percent1, '%')
        loop2 += 1
    return


def acts_loop():

    return





Act1 = {
    1: "Lioneye's Watch",
    2: "The Coast",
    3: "Mud Flats",
    4: "Tidal Island",
    5: "Submerged Passage",
    6: "The Ledge",
    7: "Flooded Depths",
    8: "The Climb",
    9: "The Lower Prison",
    10: "The Upper Prison",
    11: "Prisoner's Gate",
    12: "The Ship Graveyard",
    13: "The Cavern of Wrath",
    14: "The Cavern of Anger",

}
Act2 = {
    1: "The Southern Forest",
    2: "The Old Fields",
    3: "The Crossroads",
    4: "The Chamber of Sins Level 1",
    5: "The Chamber of Sins Level 2",
    6: "Broken Bridge",
    7: "The Riverways",
    8: "The Western Forest",
    9: "Weavers Chambers",
    10: "The Wetlands",
    11: "The Vaal Ruins",
    12: "The Northern Forest",
    13: "The Caverns",
    14: "Ancient pyramid",
}
Act3 = {
    1: "The City of Sarn",
    2: "The Slums",
    3: "The Crematorium",
    4: "The Chamber of Sins Level 1",
    5: "The Chamber of Sins Level 2",
    6: "Broken Bridge",
    7: "The Riverways",
    8: "The Western Forest",
    9: "Weavers Chambers",
    10: "The Wetlands",
    11: "The Vaal Ruins",
    12: "The Northern Forest",
    13: "The Caverns",
    14: "Ancient pyramid",
}
Act4 = {

}
Act5 = {

}
Act6 = {

}
Act7 = {

}
Act8 = {

}
Act9 = {

}
Act10 = {

}
Act_names = {
    1: Act1 ,
    2: Act2,
}

Place = 1
while Place < 15:
    check()
    Place += 1

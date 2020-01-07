percent1 = 100
## ahk to run this and display prob trough tkinter
notinuse1 = 1
def check():
    loop_2 = 1
    loop2 = loop_2

    while loop2 < 6:
        global percent1
        global notinuse1
        place_1 = Place
        actsdict = Act_names[loop2]
        Acts = actsdict
        search_for = Acts[place_1]

        with open('Client.txt') as myfile:
            if search_for in myfile.read():
                notinuse1 = 1
            else:
                print("No")
                percent1 -= 1.52
                print('Percentage of Campaign Completed', percent1,'%')
        loop2 += 1
    return
def check2():


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
    15: 'Got Instance Details from login server'
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
    15: 'Got Instance Details from login server'
}
Act3 = {
    1: "The City of Sarn",
    2: "The Slums",
    3: "The Crematorium",
    4: "The Sewers",
    5: "The Markteplace",
    6: "The Battlefront",
    7: "The Docks",
    8: "The Solaris Temple 1",
    9: "The Solaris Temple 2",
    10: "The Ebony Barracks",
    11: "Lunaris Temple 1",
    12: "Lunaris Temple 2",
    13: "Imperial Gardens",
    14: "The Sceptre of God",
    15: "Upper Sceptre of God"
}
Act4 = {
1: "The Aqueduct",
2: "The Dried Lake",
3: "The Mines 1",
4: "The Mines 2",
5: "The Crystal Veins",
6: "Daresso's Dream",
7: "The Grand Arena",
8: "The Kaom's Dream   ",
9: "The Kaom's Stronghold  ",
10: "Belly of the Beast 1",
11: "Belly of the Beast 2",
12: "The Harvest",
13: "The Ascent",
14: "Got Instance Details from login server",
15: "Got Instance Details from login server"
}
Act5 = {
1: "The Slave Pens",
2: "The Control Blocks",
3: "Oriath Square",
4: "The Templar Courts",
5: "Chamber of Innocence",
6: "The Torched Courts",
7: "The Ruined Square",
8: "The Ossuary",
9: "The Reliquary",
10: "Cathedral Rooftop",
11: "Got Instance Details from login server",
12: "Got Instance Details from login server",
13: "Got Instance Details from login server",
14: "Got Instance Details from login server",
15: "Got Instance Details from login server"
}

###Second half
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



























##
Act_names = {
    1: Act1,
    2: Act2,
    3: Act3,
    4: Act4,
    5: Act5,
}

Place = 1
while Place < 16:
    check()
    Place += 1

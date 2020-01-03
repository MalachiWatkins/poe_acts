def check():
    place = 1
    find1 = place
    search_for = Act1dict[find1]
    search1 = find1
    percent1 = 100
    while place < 14:
        with open('Client.txt') as log_file:
            if search_for in log_file.read():
                print('Completed')
                print(percent1)
                print(search_for)
            else:
                percent1 - 7.14
                print("No")
                print(percent1)
        place += 1

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
check()

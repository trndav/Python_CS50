import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    dictam = {"12" : "00",
            "1" : "01",
            "2" : "02",
            "3" : "03",
            "4" : "04",
            "5" : "05",
            "6" : "06",
            "7" : "07",
            "8" : "08",
            "9" : "09",
            "10" : "10",
            "11" : "11",
            }
    dictpm = {"1" : "13",
            "2" : "14",
            "3" : "15",
            "4" : "16",
            "5" : "17",
            "6" : "18",
            "7" : "19",
            "8" : "20",
            "9" : "21",
            "10" : "22",
            "11" : "23",
            "12" : "12",
    }

    item = s.split(" ")
    if len(item) != 5:
        raise ValueError
    # if item[2] != "to":
    #     raise ValueError
    if " to " not in s:
        raise ValueError

    # Start hours
    if ":" in item[0]:
        item1split = item[0].split(":")
        if int(item1split[0]) > 12:
            #print(f"item1split[0] is: {item1split[0]}")
            raise ValueError
        if int(item1split[1]) > 59:
            raise ValueError

    # End hours
    if ":" in item[3]:
        item2split = item[3].split(":")
        if int(item2split[0]) > 12:
            raise ValueError
        if int(item2split[1]) > 59:
            #print(f"item2split[1] is: {item2split[1]}")
            raise ValueError

    # If : in both
    if ":" in item[0] and ":" in item[3]:
        if item[1] == "AM":
            item1split[0] = dictam[item1split[0]]
            if item[4] == "AM":
                item2split[0] = dictam[item2split[0]]
                return f"{item1split[0]}:{item1split[1]} to {item2split[0]}:{item2split[1]}"
            elif item[4] == "PM":
                item2split[0] = dictpm[item2split[0]]
                return f"{item1split[0]}:{item1split[1]} to {item2split[0]}:{item2split[1]}"

        # If : and PM
        if item[1] == "PM":
            item1split[0] = dictpm[item1split[0]]
            if item[4] == "PM":
                item2split[0] = dictpm[item2split[0]]
                return f"{item1split[0]}:{item1split[1]} to {item2split[0]}:{item2split[1]}"
            elif item[4] == "AM":
                item2split[0] = dictam[item2split[0]]
                return f"{item1split[0]}:{item1split[1]} to {item2split[0]}:{item2split[1]}"

    # If : in NONE
    elif ":" not in item[0] and ":" not in item[3]:
        if item[1] == "AM":
            item1split = dictam[item[0]]
            if item[4] == "AM":
                item2split = dictam[item[3]]
                return f"{item1split}:00 to {item2split}:00"
            elif item[4] == "PM":
                item2split = dictpm[item[3]]
                return f"{item1split}:00 to {item2split}:00"

        # If PM
        if item[1] == "PM":
            item1split = dictpm[item[0]]
            if item[4] == "PM":
                item2split = dictpm[item[3]]
                return f"{item1split}:00 to {item2split}:00"
            elif item[4] == "AM":
                item2split = dictam[item[3]]
                return f"{item1split}:00 to {item2split}:00"

    # If : in last BUT NOT IN FIRST
    elif ":" not in item[0] and ":" in item[3]:
        if item[1] == "AM":
            item1split = dictam[item[0]]
            if item[4] == "AM":
                item2split[0] = dictam[item2split[0]]
                return f"{item1split}:00 to {item2split[0]}:{item2split[1]}"
            elif item[4] == "PM":
                item2split[0] = dictpm[item2split[0]]
                return f"{item1split}:00 to {item2split[0]}:{item2split[1]}"

        # If PM
        if item[1] == "PM":
            item1split = dictpm[item[0]]
            if item[4] == "PM":
                item2split[0] = dictpm[item2split[0]]
                return f"{item1split}:00 to {item2split[0]}:{item2split[1]}"
            elif item[4] == "AM":
                item2split[0] = dictam[item2split[0]]
                return f"{item1split}:00 to {item2split[0]}:{item2split[1]}"

    # If : in FIRST  BUT NOT IN LAST
    elif ":" in item[0] and ":" not in item[3]:
        if item[1] == "AM":
            item1split[0] = dictam[item1split[0]]
            if item[4] == "AM":
                item2split = dictam[item[3]]
                return f"{item1split[0]}:{item1split[1]} to {item2split}:00"
            elif item[4] == "PM":
                item2split = dictpm[item[3]]
                return f"{item1split[0]}:{item1split[1]} to {item2split}:00"

        # If PM
        if item[1] == "PM":
            item1split[0] = dictpm[item1split[0]]
            if item[4] == "PM":
                item2split = dictpm[item[3]]
                return f"{item1split[0]}:{item1split[1]} to {item2split}:00"
            elif item[4] == "AM":
                item2split = dictam[item[3]]
                return f"{item1split[0]}:{item1split[1]} to {item2split}:00"
    else:
        pass

if __name__ == "__main__":
    main()

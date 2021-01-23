START_STR = "On the {} day of Christmas my true love gave to me: "

def recite(start_verse, end_verse):
    lines = []
    for i in range(start_verse, end_verse+1):
        lines.append(START_STR.format(date(i)) + items(i))
    return lines

def items(num):
    num_to_items = {
        1: "and a Partridge in a Pear Tree.",
        2: "two Turtle Doves, ",
        3: "three French Hens, ",
        4: "four Calling Birds, ",
        5: "five Gold Rings, ",
        6: "six Geese-a-Laying, ",
        7: "seven Swans-a-Swimming, ",
        8: "eight Maids-a-Milking, ",
        9: "nine Ladies Dancing, ",
        10: "ten Lords-a-Leaping, ",
        11: "eleven Pipers Piping, ",
        12: "twelve Drummers Drumming, "
    }

    str = ""
    for i in reversed(range(1, num+1)):
        str = str + num_to_items.get(i)

    if num == 1:
        str = str.replace("and ", "")

    return str

def date(num):
    num_to_suffix = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }

    return num_to_suffix.get(num)
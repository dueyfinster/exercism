START_STR = "On the {} day of Christmas my true love gave to me: "

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


def recite(start_verse, end_verse):
    lines = []
    for i in range(start_verse, end_verse+1):
        lines.append(START_STR.format(num_to_suffix.get(i)) + items(i))
    return lines


def items(num):
    verses = []
    for i in reversed(range(1, num+1)):
        verses.append(num_to_items.get(i))

    if len(verses) == 1:
        verses[0] = verses[0].replace("and ", "")

    return ''.join(verses)

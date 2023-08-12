#!/usr/bin/env python
import itertools
import secretpy

steb_letters = [
    "nprtx",
    "ae",
    "dhlnrtx",
    "qrsty",
    "jhgi",
    "x",
    "ae",
    "nprtx",
]


def permute_steb(letters):
    letters = [list(x) for x in letters]
    perms = itertools.product(*letters)

    return list(perms)


def get_english():
    words = []
    with open("american-english", "r") as e_dict:
        for line in e_dict:
            words.append(line.strip())

    return words


def check_stebs(possibs, english_words):
    all_chances = []
    for chance in possibs:
        if chance in english_words:
            all_chances.append(chance)
            print(chance)

    return all_chances


def caesar_them(possibs, shift_amt):
    cipher = secretpy.Caesar()
    pts = []
    for pos in possibs:
        pt = cipher.decrypt(pos, shift_amt, secretpy.alphabets.ENGLISH)
        pts.append(pt)

    return pts


def main():
    possibs = permute_steb(steb_letters)
    possibs = ["".join(x) for x in possibs]
    english_words = get_english()
    eight_words = [x for x in english_words if len(x) == 8]
    for i in range(26):
        pts = caesar_them(possibs, i)
        pts = check_stebs(pts, eight_words)
        print("\n".join(pts))


main()

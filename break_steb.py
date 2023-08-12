#!/usr/bin/env python
import itertools

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


def main():
    possibs = permute_steb(steb_letters)
    possibs = ["".join(x) for x in possibs]
    english_words = get_english()
    # eight_words = [x for x in english_words if len(x) == 8]
    matching_stebs = check_stebs(possibs, english_words)
    print(matching_stebs)
    breakpoint()


main()

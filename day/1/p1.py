# Code for part 1

from pathlib import Path


def main():
    print("empty")

def unsorted_list_difference(list1, list2):
    intlist1 = map(int, list1)
    intlist2 = map(int,list2)
    return sum([y-x for x,y in zip(intlist1, intlist2)])

if __name__ == "__main__":
    main()

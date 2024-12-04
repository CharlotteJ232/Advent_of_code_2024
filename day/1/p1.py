# Code for part 1

from pathlib import Path


def main():
    input_file_path = Path(__file__).parent / "input.txt"
    print(file_column_difference(input_file_path))

def unsorted_list_difference(list1, list2):
    intlist1 = map(int, list1)
    intlist2 = map(int, list2)
    return sum([y-x for x,y in zip(intlist1, intlist2)])

def read_lists_from_file(input_path):
    list1 = []
    list2 = []

    with open(input_path) as file:
        for line in file:
            numbers = line.split()
            list1.append(numbers[0])
            list2.append(numbers[1])
    
    return (list1,list2)

def file_column_difference(input_path):
    return unsorted_list_difference(*read_lists_from_file(input_path))

if __name__ == "__main__":
    main()

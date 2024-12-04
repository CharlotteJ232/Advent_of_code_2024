# Code for part 1

from pathlib import Path


def main():
    input_file_path = Path(__file__).parent / "input.txt"
    print(file_column_difference(input_file_path))


def list_difference(list1, list2):
    intlists = (map(int, list1), map(int, list2))
    sortedlists = map(sorted, intlists)
    return sum([abs(y - x) for x, y in zip(*sortedlists)])


def read_lists_from_file(input_path):
    list1 = []
    list2 = []

    with open(input_path) as file:
        for line in file:
            numbers = line.split()
            list1.append(numbers[0])
            list2.append(numbers[1])

    return (list1, list2)


def file_column_difference(input_path):
    return list_difference(*read_lists_from_file(input_path))


if __name__ == "__main__":
    main()

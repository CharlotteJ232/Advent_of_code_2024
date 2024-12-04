from p1 import read_lists_from_file
from pathlib import Path

def main():
    input_file_path = Path(__file__).parent / "input.txt"
    print(similarity_score_from_file(input_file_path))


def similarity_score(list1, list2):
    score = 0
    for number in list1:
        occurrence = len(list(filter(lambda x: x==number, list2)))
        score += number*occurrence
    return score

def similarity_score_from_file(file_path):
    list1, list2 = read_lists_from_file(file_path)
    intlists = (list(map(int, list1)), list(map(int, list2)))
    return similarity_score(*intlists)

if __name__ == "__main__":
    main()

from p1 import read_lists_from_file
from p2 import similarity_score, similarity_score_from_file
from pathlib import Path

def test_similarity_score_lists():
    list1 = [2,1,3]
    list2 = [2,3,3]

    assert similarity_score(list1, list2) == 8

def test_similarity_score_lists_2():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    assert similarity_score(list1, list2) == 31

def test_similarity_score_from_file():
    input_file_path = Path(__file__).parent / "test_input.txt"

    assert similarity_score_from_file(input_file_path) == 31
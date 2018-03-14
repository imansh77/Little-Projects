from collections import Counter


def solution(A):
    list_dict = Counter(A)
    for k, v in list_dict.items():
        print(k, v == 1)


solution([9, 3, 9, 3, 9, 7, 9])

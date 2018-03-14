def solution(A):
    if sum(A) == ((len(A) * (max(A) + 1)) / 2):
        print("A is a permutation")
    else:
        print("A is NOT a permutation")


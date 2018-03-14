def solution(X, A):
    for i in range(len(A)):
        if (A[i] == X) or (A[i] >= X):
            print(i)
            break


solution(4, [1, 3, 1, 4, 2, 3, 5, 4])

def solution(A):
    sorted_list = sorted(A)
    minimum = min(A)
    for i in range(len(A)):
        while minimum in sorted_list:
            minimum += 1
            break
        else:
            print("Not Consecutive")
            return
    print("Consecutive")


solution([4, 1, 5, 2])

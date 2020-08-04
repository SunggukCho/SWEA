T = int(input())

for i in range(T):
    channel = list(map(int, input().split()))

    size = channel[0]
    A = channel[1]
    B = channel[2]

    # subs_max = 둘 중에서 더 작은 값
    # subs_min = 1) 둘 더한 값이 전체 값보다 클 때, 둘 더한 값 - 전체 값 2) 더 작을 때: 0

    subs_max = min(A, B)

    if A+B > size:
        subs_min = (A+B) - size
    else:
        subs_min = 0

    print(f'#{i+1} {subs_max} {subs_min}')

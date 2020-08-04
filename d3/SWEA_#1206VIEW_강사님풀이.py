import sys
sys.stdin = open('input.txt', 'r')                      #파일로 input받기

T = 10

for tc in range(1, T+1):
    #입력
    N = int(input())                                    #빌딩 수
    arr = list(map(int, input().split()))               #입력받기
    #print(arr)                                         #입력 코드 한 번 확인해보기

    #계산
    view = 0
    for i in range(2, N-2):                                    #제일 끝 2개씩은 안봐야 함(index 오류)
        left = arr[i-2] if (arr[i-2]>arr[i-1]) else arr[i-1]   #왼쪽 빌딩 중 높은 빌딩 찾기
        right = arr[i+2] if (arr[i+2]>arr[i+1]) else arr[i+1]  #오른쪽 빌딩 중 높은 빌딩 찾기
        t = right if (right > left) else left
        if arr[i] > t:
            view += arr[i]-t

    #출력
    print('#{} {}'.format(tc, view))
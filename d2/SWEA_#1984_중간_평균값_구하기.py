T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    numbers.remove(max_num) 
    numbers.remove(min_num)


    avg = sum(numbers) / len(numbers)
    avg = int(round(avg, 0))
    print(f'#{i+1} {avg}')
from itertools import permutations

def aa(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
            if n%i == 0:
                return False
    return True
                

def solution(numbers):
    answer = 0
    num_set = set()
    
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers,i):
            num = int(''.join(j))
            num_set.add(num)

    cnt = 0
    for i in num_set:
        
        if aa(i):
            cnt += 1
    
    
    return cnt
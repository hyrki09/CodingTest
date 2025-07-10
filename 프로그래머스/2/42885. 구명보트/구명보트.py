def solution(people, limit):
    answer = 0
    i = 0
    j = len(people) - 1
    count = 0
    
    people.sort()
    print(people)
    while i <= j:
        
        if people[i]+people[j] <= limit:
            i += 1
        
        j -= 1
        count += 1
    return count
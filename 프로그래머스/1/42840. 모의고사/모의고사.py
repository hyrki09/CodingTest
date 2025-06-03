def jungdap(answers, personal_arr):
    n = len(personal_arr)
    count = 0
    
    for i in range(len(answers)):
        if answers[i] == personal_arr[i%n]:
            count += 1
    return count
    
    

def solution(answers):
    answer = []
    
    su_1 = [1,2,3,4,5]
    su_2 = [2,1,2,3,2,4,2,5]
    su_3 = [3,3,1,1,2,2,4,4,5,5]
    result = []
    result.append(jungdap(answers,su_1))
    result.append(jungdap(answers,su_2))
    result.append(jungdap(answers,su_3))
    
    max_val = max(result)
    
    
    return [i+1 for i,v in enumerate(result) if v == max_val]
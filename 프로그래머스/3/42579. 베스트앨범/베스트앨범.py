from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    dict_genres = defaultdict(list)
    total = defaultdict(int)
    
    for i,(g,p) in enumerate(zip(genres, plays)):
        dict_genres[g].append((i,p))
        total[g] += p
        

    sorted_total=sorted(total.items(), key=lambda x : x[1], reverse=True)
    
    for part,val in sorted_total:
        sorted_genres = sorted(dict_genres[part], key=lambda x:(-x[1], x[0]))
        
        answer += [i for i,_ in sorted_genres[:2]]
        
    
    return answer
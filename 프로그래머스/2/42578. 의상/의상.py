from collections import defaultdict

def solution(clothes):
    c_dic = {}
    category = set([cate for wear, cate in clothes])
    for i in category:
        c_dic[i] =[]
        
    for wear, cate in clothes:
        c_dic[cate].append(wear)

    count = 1
        
    for key, val in c_dic.items():
        count *= len(val) + 1
        
    return count-1
def solution(players, m, k):
    answer = 0
    com_list = [0 for _ in range(len(players))]
    
    
    for idx, player in enumerate(players):
        allow_user_count = (com_list[idx]+1) * m
        if player >= allow_user_count:
            add_server = player//m - com_list[idx]
            next_idx = idx
            answer += add_server
            for _ in range(k):
                if next_idx < len(players):
                    com_list[next_idx] += add_server
                    next_idx += 1
                    
    return answer
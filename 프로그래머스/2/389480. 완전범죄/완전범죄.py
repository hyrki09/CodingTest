def solution(info, n, m):
    answer = 0
    dp = [[False] *m for _ in range(n)]
    dp[0][0] = True
    
    
    for ai,bi in info:
        next_dp = [[False] * m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue
                na = ai + a
                if na < n:
                    next_dp[na][b]=True
                
                nb = bi + b
                if nb < m:
                    next_dp[a][nb]=True
                    
        dp = next_dp    
                
    
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a

    
    return -1
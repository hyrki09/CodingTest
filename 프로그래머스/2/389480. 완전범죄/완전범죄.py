def solution(info, n, m):

    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True
    
    for ai,bi in info:
        next_dp = [[False] * m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue
                
                na = a + ai
                if na < n:
                    next_dp[na][b] = True
                nb = b + bi
                if nb < m:
                    next_dp[a][nb] = True
                
        dp = next_dp
        
        
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a
    return -1
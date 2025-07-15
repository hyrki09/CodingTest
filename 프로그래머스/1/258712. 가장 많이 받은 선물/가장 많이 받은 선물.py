def solution(friends, gifts):
    answer = 0

    count = [0 for i in friends]
    gifts_list = [i.split() for i in gifts]

    recordList = [[0,0,0,0] for i in friends]
    recordList = [[0 for i in friends] for j in friends]

    for s,g in gifts_list:
        sendH = friends.index(s)
        getH = friends.index(g)
        recordList[sendH][getH] += 1


    for i in range(len(recordList)):
        for j in range(len(recordList[i])):
            if recordList[i][j] > recordList[j][i]:
                count[i] += 1
            elif i != j and recordList[i][j] == recordList[j][i]:
                Aexponential = sum(recordList[i]) - sum([recordList[k][i] for k in range(len(recordList))])
                Bexponential = sum(recordList[j]) - sum([recordList[k][j] for k in range(len(recordList))])
                if Aexponential > Bexponential:
                    count[i] += 1
    
    return max(count)
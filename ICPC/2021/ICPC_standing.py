import heapq
import sys 


def output(rank, team, prob, time):
    print('{:<4}'.format(rank)+'{:<4}'.format(team)+'{:>3}'.format(prob)+'{:>5}'.format(time))
dim = sys.stdin.readline().split()
n_teams = int(dim[0])
n_prob = int(dim[1])
n_submission = int(dim[2])
n_rank = int(dim[3])
team=[]
rankhash=dict()
for i in range(n_teams):

    team.append(dict())
    rankhash [i+1] = (0,0)

for i in range(n_submission):
    dim = sys.stdin.readline().split() #dim[0] team#, dim[1] problem#, dim[2] timestamp, dim[3] solved or not
    teamnum = int(dim[0])-1
    
    if(int(dim[1]) in team[teamnum]):
        if( team[teamnum][int(dim[1])][1]!=1):
            if(int(dim[3])==1): #check this
                team[teamnum][int(dim[1])]= (team[teamnum][int(dim[1])][0]+int(dim[2]),1)
                rankhash[teamnum+1]= (rankhash[teamnum+1][0]+1,rankhash[teamnum+1][1]+team[teamnum][int(dim[1])][0])
            else:
                team[teamnum][int(dim[1])]= (team[teamnum][int(dim[1])][0]+20,0)
    else:
        if(int(dim[3])==1):
            team[teamnum][int(dim[1])] =  (int(dim[2]),1)
            rankhash[teamnum+1]= (rankhash[teamnum+1][0]+1,rankhash[teamnum+1][1]+team[teamnum][int(dim[1])][0])
        else:
            team[teamnum][int(dim[1])] =  (20,0)
#rankhash[16]= (10,975)    
#rankhash[16]= (10,rankhash[16][1])
#print({k: v for k, v in sorted(rankhash.items(), key=lambda item: (item[1][0],-item[1][1]),reverse=True)}) #if want to sort decreasing then just change sign
order = [(k, v) for k, v in sorted(rankhash.items(), key=lambda item: (item[1][0],-item[1][1]),reverse=True)] #if want to sort decreasing then just change sign
#print(order)
ranking = 1
counter = 0
tiebreaker=dict()
while ranking <= n_rank:
    curr = order[counter]
    temp = counter+1
    tiebreaker.clear()
    tiebreaker = dict()
    tiebreaker[order[counter][0]] = team[order[counter][0]-1]
    while temp < n_teams:
        if (order[temp][1]==order[counter][1]):
            tiebreaker[order[temp][0]] = team[order[temp][0]-1]
            temp+=1
        else:
            break
    if(temp!=counter+1):
        '''
        print(tiebreaker)
        tiebreaker = [(k, v) for k, v in sorted(tiebreaker.items(), key=lambda item: (item[:][0]),reverse=True)]
        print(tiebreaker)
        counter+=1
        '''
        pass
    else:
        output(ranking,order[counter][0],order[counter][1][0],order[counter][1][1])
        counter+=1
    ranking+=1


#print(team)
'''
50 12 45 2
16 1 2 1
50 1 5 1
3 1 5 1
16 11 8 0
16 7 10 1
3 7 11 1
50 7 11 1
16 8 14 1
3 11 16 0
3 9 24 1
50 8 27 1
16 11 29 0
50 11 39 1
16 9 41 1
3 8 42 1
50 9 50 1
3 11 52 1
3 10 56 1
16 5 62 1
16 11 72 1
3 3 75 1
50 3 77 1
16 3 103 1
3 3 132 0
3 5 138 1
16 2 147 0
16 2 155 0
16 10 169 1
16 2 188 0
16 2 197 1
50 5 232 1
3 4 253 1
50 10 270 0
50 10 270 0
50 10 270 0
50 10 270 0
50 10 270 0
50 10 270 0
50 10 270 0
50 10 270 0
50 10 270 0
50 10 270 0
50 10 270 0
3 6 299 1
50 10 299 1
'''
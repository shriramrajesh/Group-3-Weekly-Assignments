from random import randint
c={'rock':0,'paper':1,'scissors':2 }
d1= ['rock','paper','scissors']
d2={}
q=0
t=0
d='y'
for i in range(1,11):
    p=input("Enter player's choice")
    u = d1[randint(0,2)]
    print("Computer's choice=%s" %(u))
    outcomes = {0: {0: "Tie", 1: "Computer won", 2: "Player won"},1: {0: "Player won", 1: "Tie", 2: "Computer won"},2: {0: "Computer won", 1: "Player won", 2: "Tie"}}
    if((c[p]==0 and c[u]==2) or (c[p]==1 and c[u]==0) or (c[p]==2 and c[u]==1)):
        q=q+1
    else:
        if ((c[p] == 0 and c[u] == 1) or (c[p] == 1 and c[u] == 2) or (c[p] == 2 and c[u] == 0)):
            t=t+1
    result = outcomes[c[p]][c[u]]
    d2[i] = [p,u,result]
    print(result)
print("Player's points= %d and Computer's points= %d" % (q, t))
if(q>t):
    print("Player won")
elif(q<t):
    print("Computer Won")
else:
    print("Tie")
while (d == 'y'):
    try:
        x = int(input("Enter the round for which you need the information >>"))
        print("Player's's choice=%s" %(d2[x][0]))
        print("Computer's choice=%s" %(d2[x][1]))
        print(d2[x][2])
    except KeyError:
        print("Value should be of given range (1-10)")
    except ValueError:
        print("Value should be of correct type (integer) ")
    finally:
        d = input("Would you like to try again? Press y for yes and any other key for no")

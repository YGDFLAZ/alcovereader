#botalcove reader
from collections import Counter

with open('botalcove.txt') as file:
    file_contents = file.read()
    lines = file_contents.split("\n")
    print(lines[1])
    joined=[]
    left =[]
    banned = []
    count=0
    datetimelistthing=[]  
    for i in lines:
        count +=1
        if (count == len(lines)):
            break
        if ("Dyno#0000" in i):
            datetimelistthing.append(i)
        if  ("joined" in lines[count]):
            joined.append(i)
            
        elif ("left the" in lines[count]):
            left.append(i)
            
        elif("banned" in lines[count]):
            banned.append(i)   
            
    print("total joined: ", len(joined))
    print("total left: ", len(left))
    print("total banned: ", len(banned))
    cleaneddatetimelistthing = []
    for q in datetimelistthing:
        cleaneddatetimelistthing.append(q[0:14]+q[17:19])    
    
    seen = set()
    result = []
    for item in cleaneddatetimelistthing:
        if item not in seen:
            seen.add(item)
            result.append(item)    
   
    print("Now looking at Joined dates/times")
    newJoined = []
    for j in joined:
        newJoined.append(j[0:14]+j[17:19])  
    newJoined= Counter(newJoined)
    for ja in result:
        if (ja in newJoined):
            print(ja + " " +str(newJoined[ja]))
        else:
            print(ja + " 0")              
    
    print("Now looking at Left dates/times")
    newLeft = []
    for l in left:
        newLeft.append(l[0:14]+l[17:19])  
    newLeft= Counter(newLeft)
    for la in result:
        if (la in newLeft):
            print(la + " " +str(newLeft[la]))
        else:
            print(la + " 0")          
    print("Now looking at Banned dates/times")
    newBanned = []
    for b in banned:
            newBanned.append(b[0:14]+b[17:19])  
    newBanned= Counter(newBanned)
    for ba in result:
        if (ba in newBanned):
            print(ba + " " +str(newBanned[ba]))
        else:
            print(ba + " 0")
         
    
   
    
    
    
   

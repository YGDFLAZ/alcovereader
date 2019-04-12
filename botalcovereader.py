#botalcove reader

with open('botalcove.txt') as file:
    file_contents = file.read()
    lines = file_contents.split("\n")
    print(lines[1])
    joined=[]
    left =[]
    banned = []
    count=0
    for i in lines:
        count +=1
        if (count == len(lines)):
            break
        
        if  ("joined" in lines[count]):
            joined.append(i)
        elif ("left the" in lines[count]):
            left.append(i)
        elif("banned" in lines[count]):
            banned.append(i)         
    print("total joined: ", len(joined))
    print("total left: ", len(left))
    print("total banned: ", len(banned))
    
    
    print banned
    print("Now looking at Joined dates/times")
    count =0
    current_datetime= joined[0][0:14]
    datetime_counter =1
    #print(current_datetime)
    for j in joined:
        count +=1
        current_datetime=j[0:14]
        
        if (count == len(joined)):
            break 
        if (joined[count][0:14]!=current_datetime):
            print (current_datetime, datetime_counter)
            datetime_counter =1
        else:
            datetime_counter +=1
    
    print("Now looking at Left dates/times")
    count =0
    current_datetime= left[0][0:14]
    datetime_counter =1
    #print(current_datetime)
    for l in left:
        count +=1
        current_datetime=l[0:14]
                
        if (count == len(left)):
            break 
        if (left[count][0:14]!=current_datetime):
            print (current_datetime, datetime_counter)
            datetime_counter =1
        else:
            datetime_counter +=1            
    print("Now looking at Banned dates/times")
    count =0
    current_datetime= banned[0][0:14]
    datetime_counter =1
    #print(current_datetime)
    for b in banned:
        count +=1
        current_datetime=b[0:14]
    
        if (count == len(banned)):
            break 
        if (banned[count][0:14]!=current_datetime):
            print (current_datetime, datetime_counter)
            datetime_counter =1
        else:
            datetime_counter +=1         
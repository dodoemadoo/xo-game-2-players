arr_1=[1,2,3,4,5,6,7,8,9]
arr_2=[0,1,2,3,4,5,6,7,8,9]
arr_3=[]
z=True
i=0
x=["x"]
o=["o"]
print("instructions :")
print ("This is a x o game")
print ("To play the game you choose a number from 1 to 9 ")
print ("There are 8 cases to be the winner: ")
print ("       1-you put x or o in 1 and 2 and 3 togther ")
print ("       2-you put x or o in 4 and 5 and 6 togther ")
print ("       3-you put x or o in 7 and 8 and 9 togther ")
print ("       4-you put x or o in 1 and 4 and 7 togther ")
print ("       5-you put x or o in 2 and 5 and 8 togther ")
print ("       6-you put x or o in 3 and 6 and 9 togther ")
print ("       7-you put x or o in 1 and 5 and 9 togther ")
print ("       8-you put x or o in 3 and 5 and 7 togther ") 
print("\n")
for m in range(1,10):
    if (m%3==0):
        print(arr_2[m])
    else:
        print(arr_2[m],end=" | ")
print("\n")
player_1=input("enter the sign of player 1 : ")
if player_1==x[0]:
    player_2=o[0]
else:
    player_2=x[0]
while i<9:
    if i%2==0:
          postion=int(input("enter the position of player 1 from [1:9] : "))
          if postion<1 or postion >9:
            postion=int(input("enter anthor position between 1 and 9 : "))
          else:  
             for r in range(i):
                if arr_3[r]==postion:
                     postion=int(input("enter another postion : "))
             arr_3.append(postion)
          
          
    else :
        
        postion=int(input("enter the position of player 2 from [1:9] : "))
        if postion<1 or postion >9:
            postion=int(input("enter anthor position between 1 and 9 : "))
        
        else :
            for r in range(i):
                if arr_3[r]==postion:
                     postion=int(input("enter another postion : "))
            arr_3.append(postion)
        
    
    if i%2==0:
          
          arr_2[postion] = player_1
          arr_1[postion-1]=player_1
          for m in range(1,10):
              if (m%3==0):
                  print(arr_2[m])
              else:
                 print(arr_2[m],end=" | ")
    else:
          
          arr_2[postion] = player_2
          arr_1[postion-1]=player_2
          for m in range(1,10):
              if (m%3==0):
                  print(arr_2[m])
              else:
                 print(arr_2[m],end=" | ")    

    i+=1   
    if player_1==x[0]:
      
       if arr_1[0]==arr_1[1]==arr_1[2]==x[0] or arr_1[0]==arr_1[3]==arr_1[6]==x[0] or arr_1[0]==arr_1[4]==arr_1[8]==x[0] or arr_1[1]==arr_1[4]==arr_1[7]==x[0] or arr_1[2]==arr_1[5]==arr_1[8]==x[0] or arr_1[2]==arr_1[4]==arr_1[6]==x[0] or arr_1[3]==arr_1[4]==arr_1[5]==x[0] or arr_1[6]==arr_1[7]==arr_1[8]==x[0] :
           print ("player 1 won")
           break
       elif arr_1[0]==arr_1[1]==arr_1[2]==o[0] or arr_1[0]==arr_1[3]==arr_1[6]==o[0] or arr_1[0]==arr_1[4]==arr_1[8]==o[0] or arr_1[1]==arr_1[4]==arr_1[7]==o[0] or arr_1[2]==arr_1[5]==arr_1[8]==o[0] or arr_1[2]==arr_1[4]==arr_1[6]==o[0] or arr_1[3]==arr_1[4]==arr_1[5]==o[0] or arr_1[6]==arr_1[7]==arr_1[8]==o[0] :
           print ("player 2 won")
           break
       else:
           if i==9:
               print("the game is darw")
       
       
    elif(player_1==o[0]):
        if arr_1[0]==arr_1[1]==arr_1[2]==x[0] or arr_1[0]==arr_1[3]==arr_1[6]==x[0] or arr_1[0]==arr_1[4]==arr_1[8]==x[0] or arr_1[1]==arr_1[4]==arr_1[7]==x[0] or arr_1[2]==arr_1[5]==arr_1[8]==x[0] or arr_1[2]==arr_1[4]==arr_1[6]==x[0] or arr_1[3]==arr_1[4]==arr_1[5]==x[0] or arr_1[6]==arr_1[7]==arr_1[8]==x[0] :
           print ("player 2 won")
           break
        elif arr_1[0]==arr_1[1]==arr_1[2]==o[0] or arr_1[0]==arr_1[3]==arr_1[6]==o[0] or arr_1[0]==arr_1[4]==arr_1[8]==o[0] or arr_1[1]==arr_1[4]==arr_1[7]==o[0] or arr_1[2]==arr_1[5]==arr_1[8]==o[0] or arr_1[2]==arr_1[4]==arr_1[6]==o[0] or arr_1[3]==arr_1[4]==arr_1[5]==o[0] or arr_1[6]==arr_1[7]==arr_1[8]==o[0] :
           
           print ("player 1 won")
           break
        else:
           if i==9:
               print("the game is darw")
    
        
print ("done")


       

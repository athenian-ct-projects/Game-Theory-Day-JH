# Below is the code for a machine that uses optimal strategy for winning at Nim.
pilesize = int(input('how big do you want your pile to be? (please do not choose a negative number or 0)'))
#Throughout the program, pilesize denotes the current size of the pile.
print('The pile has size '+str(pilesize))
last1 = 0
#Last1 will be our way to remember who took the last turn. This is important when deciding who won and who lost.
while pilesize > 0:
  if pilesize % 4 == 0:
    pilesize = pilesize - 3
    if pilesize > 0:
      print('I took 3 and the pile now has size '+str(pilesize))
    last1 = 1
  elif pilesize % 4 == 1:
    pilesize = pilesize - 3
    if pilesize > 0:
      print('I took 3 and the pile now has size '+str(pilesize))
    last1 = 1
  elif pilesize % 4 == 2:
    pilesize = pilesize - 1
    if pilesize > 0:
      print('I took 1 and the pile now has size '+str(pilesize))
    last1 = 1
  elif pilesize % 4 == 3:
    pilesize = pilesize - 2
    if pilesize > 0:
      print('I took 2 and the pile now has size '+str(pilesize))
    last1 = 1
#Everything above is the optimization part of the program. It makes sure that whenever 
#possible, the computer takes the right amount to get the player to a P value.
  if pilesize > 0:
    num = int(input('how much do you want to take? (please choose 1, 2 or 3)'))
    pilesize = pilesize - num
    last1 = 2
    if pilesize > 0:
      print('You took '+ str(num) +' and the pile now has size '+str(pilesize))
#above here is simply what allows the player to take certain amounts. I could make it so that 
#they can only take a maximum of 3, but 

if last1 == 1:
  print('I take 1 and the pile now has size 0')
  print('Well, you beat me. Good job.')
elif last1 == 2:
  print('You took everything remaining and the pile now has size 0')
  print('I won. Hooray!')
else:
  print('Please rerun the cell and choose a non-negative number.')
#The above checks to see who took last, and therefore who won.


# Now to the Prisoner's Dilemma.
#This function is what allows us to pit strategies against each other.
#We have access to four strategies: IETT, IGTT, C, and D.
#IETT does whatever the opponent did last, starting with defecting.
#IGTT is the same as IETT, except they start with staying loyal.
#C always stays loyal and D always defects.
#round(x,y) will display the results of a matchup between strategies x and y.

def round(x,y):
  
  #These are starting values for us to store results in.
  list1 = []
  list2 = []
  a = 0
  b = 0
  
  
  #This confirms which strategy gets played when.
  if y == 'IGTT' or y == 'IETT':
    mb = 0
    nb = 1
  elif y == 'C':
    mb = 0
    nb = 0
  elif y == 'D':
    mb = 1
    nb = 1
    
  if x == 'IGTT' or x == 'IETT':
    ma = 0
    na = 1
  elif x == 'C':
    ma = 0
    na = 0
  elif x == 'D':
    ma = 1
    na = 1
  
  
  if y == 'IGTT':
    lasta = 0
  else:
    lasta = 1
  if x == 'IGTT':
    lastb = 0
  else:
    lastb = 1
    
    
  #This is the system that runs each simulation 
  for i in range(100):
    if lastb == 0:
      a = ma
    else:
      a = na
    if lasta == 0:
      b = mb
    else:
      b = nb
    lasta = a
    lastb = b
    if a == b:
      if a == 1:
        #print("They both got 10 years.")
        list1.append(10)
        list2.append(10)
      else:
        #print("They both got 3 years.")
        list1.append(3)
        list2.append(3)
    else:
      if a == 1:
        #print("A got 1, B got 15.")
        list1.append(1)
        list2.append(15)
      else:
        #print("A got 15, B got 1.")
        list1.append(15)
        list2.append(1)
      
  print(x+" had a total of " + str(sum(list1)))
  print(y+" had a total of " + str(sum(list2)))
  if sum(list1) > sum(list2):
    print(y+" won")
  elif sum(list1) < sum(list2):
    print(x+" won")
  else:
    print("Tie")
    
solved = 0
while solved != 1:
  first = input('1')
  second = input('2')
  round(first,second);
  co = input("continue? (y/n)")
  if co == "n":
    solved = 1

# And finally, the Pirate Game.
print('There are ten pirates. You are the first one.')
print('There are 100 coins.')
n = 10
k = 100
pmoney = []
votes = []

#Above: n is the number of pirates, k is the number of coins. pmoney keeps track of 
#who has how much money and votes keeps track of what each pirate votes for.

for pirate in range(10):
  if pirate == 0:
    inc = int(input('How many coins do you want to give to yourself? (please do not total to above 100 coins)  '))
  else:
    inc = int(input('How many coins do you want to give to pirate '+str(pirate+1)+'?   '))
  pmoney.append(inc)
  
#Above: The user (the first pirate) proposes how to distribute the money.
  
for v in pmoney:
  if pmoney.index(v) == 0:
    votes.append(1)
  elif pmoney.index(v) == 1:
    if v < (k-(n/2))+1:
      votes.append(0)
    else:
      votes.append(1)
  else:
    if v > 0:
      votes.append(1)
    else:
      votes.append(0)
      
#Above: Each pirate checks to see if it's worth it for them to vote yea or nay 

yes = 0
no = 0
for vote in votes:
  if vote == 1:
    yes += 1
  else:
    no +=1
    
#Above: The program tallies the votes.

if yes < no:
  print('The council has decided to throw you into the ocean and you lose everything.')
else:
  print('You keep all '+str(pmoney[0])+' coins you got.')
  
#Above: The program displays the results.

#create original list
l = []
#create list for names
second_lowest_names = []
#create a set for scores to have multiple elements in our set
scores = set()

#line 9-11 is original code from HackerRank
for _ in range(int(input())):
    name = input()
    score = float(input())
    #append the name and score to our 'l' list
    l.append([name, score])
    #use add to add of the score inputed from line 11 to our set named "scores"
    #this will continue to loop until all scores that have been input from HackerRank are added to our "scores" set
    scores.add(score)
        
#once first loop is complete it will take the scores, sort them, and assign the score in the [1] position (second lowest score)
#to our variable named "second_lowest"
second_lowest = sorted(scores)[1]

#now we are going to refernce our key and value in a for statement and then sort our appended list named "l"
for name, score in sorted(l): 
    #if the score given from HackerRank is == to line 20 "second_lowest" it will print the name associated with it in our "l" list
    if score == second_lowest: 
        print(name)
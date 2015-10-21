__author__ = 'Chenxi'
#!/usr/bin/py

#year_with_max_population(path) is the function I came up to solve the problem
#via dynamic programming
#I have considered the death year as the alive year of a person
# since a person still live in that year before he dies sometime during that year

import pandas as pd
import collections
#the below 2 are global variables
people = []
path = None

#readfile is to read in all the data in order, population is for the total number of rows
#BirthYr and DeathYr is for the data in Birth-Year and Death-Year columns in the csv file
def readfile(path):
    test_db = pd.read_csv(path)
    population = len(test_db.axes[0])
    BirthYr = test_db['Birth-Year'].dropna()
    DeathYr = test_db['Death-Year'].dropna()
    return population,BirthYr,DeathYr

#the year_with_max_population(path) is the core function of the program to find the
#max population year and it applies dynamic programming to speed up the program
#It has a O(N) time complexity
# since there are only single loops for the processes(no nested loops)
def year_with_max_population(path):
    population,BirthYr,DeathYr = readfile(path)
    #create a nested array to store people's info
    for i in xrange(population):
        people.append([i,BirthYr[i],DeathYr[i]])
    #this line is to get an all zeros array to store population change later on
    population_diff = [0 for _ in xrange(1900, 2002)]
    #this line is to store persons position and its counts to the population_diff array
    #and person[1] means person["BirthYr"] whereas person[2] means person["DeathYr"]
    #and we add  1 to the value of the position in population_diff array
    #while subtract 1 to the value of (the position +1) in population_diff array
    #since the people is still counted as an alive during the death year
    for person in people:
        population_diff[person[1] - 1900] += 1
        population_diff[person[2] - 1900+1] -= 1
        #print population_diff

    # Now we need to iterate through the sequence sum of the population_diff array and
    #get its max value and store them to the max_population_Yr_arr array
    #However,we only peak the biggest one from there
    #Note:by using max_population_Yr_arr, we could collect the max population year
    #when there are more than 1 max population year

    #max_population_Yr=0
    max_population_arr = []
    max_population_Yr_arr=[]
    max_population = 0
    population = 0
    for index, population_change in enumerate(population_diff):
        population += population_change
        if population == max_population:
            max_population_arr.append(max_population)
            max_population_Yr_arr.append(index)
        elif population > max_population:
            max_population = population
            max_population_Yr = index
            max_population_Yr_arr.append(max_population_Yr)
            max_population_arr.append(max_population)
    #print max_population_Yr_arr
    #print max_population_arr
    peaks = (max_population_arr.count(max_population_arr.pop())+1)
    ANS = []
    for _ in xrange(peaks):
        ANS.append(max_population_Yr_arr.pop() + 1900)

    #the below "print" is to check the answers
    #print ANS
    ANS.sort()

    del people[:]
    #print ANS
    return ANS

# the test_result is the Brute force solution, it is correct I have done it
#through collection all the integer years when a person lives into a single
#array and seeking the year(s) for the largest count of lives
#However, this approach to the problem run very slow as it has a nested loop
#where has a O(n**2) time complexity, so this solution is just used for testing
def test_result(path):
    population,BirthYr,DeathYr = readfile(path)
    livesInYr = []
    for j in range(0,population):
        for yr in range(BirthYr[j],DeathYr[j]+1):
             livesInYr.append(yr)
    #print livesInYr
    #the collection method here is to count the year(s) for the largest count of lives
    #m is the largest count in the livesInYr array

    m = collections.Counter(livesInYr).most_common()[0][1]
    #print m
    result = []
    result.append(collections.Counter(livesInYr).most_common()[0][0])
    i = 1
    while(collections.Counter(livesInYr).most_common()[i][1]==m ):
        result.append(collections.Counter(livesInYr).most_common()[i][0])
        i+=1
    #sort the result for output testing

    result.sort()
    #print result
    return result

if __name__ == "__main__":
    if path is None:
        #path = 'C:\\Users\\Chenxi\\Desktop\\python\\Projects\\testMultiplePeaks.csv'
        path = 'C:\\Users\\Chenxi\\Desktop\\python\\Projects\\testStar.csv'
    year_with_max_population(path)
    #test_result(path)


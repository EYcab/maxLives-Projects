__author__ = 'Chenxi'
#!/usr/bin/py

import pandas as pd
import collections
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

def year_with_max_population(path):
    population,BirthYr,DeathYr = readfile(path)
    for i in xrange(population):
        people.append([i,BirthYr[i],DeathYr[i]])

    population_diff = [0 for _ in xrange(1900, 2002)]

    for person in people:
        population_diff[person[1] - 1900] += 1
        population_diff[person[2] - 1900+1] -= 1
        #print population_diff

    max_population_Yr=0
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
    #print ANS
    ANS.sort()

    del people[:]
    print ANS
    return ANS

def test_result(path):
    population,BirthYr,DeathYr = readfile(path)
    livesInYr = []
    for j in range(0,population):
        for yr in range(BirthYr[j],DeathYr[j]+1):
             livesInYr.append(yr)
    #print livesInYr
    m = collections.Counter(livesInYr).most_common()[0][1]
    #print m
    result = []
    result.append(collections.Counter(livesInYr).most_common()[0][0])
    i = 1
    while(collections.Counter(livesInYr).most_common()[i][1]==m ):
        result.append(collections.Counter(livesInYr).most_common()[i][0])
        i+=1

    result.sort()
    #print result
    return result

if __name__ == "__main__":
    if path is None:
        #path = 'C:\\Users\\Chenxi\\Desktop\\python\\Projects\\testMultiplePeaks.csv'
        path = 'C:\\Users\\Chenxi\\Desktop\\python\\Projects\\testStar.csv'
    year_with_max_population(path)
    #test_result(path)


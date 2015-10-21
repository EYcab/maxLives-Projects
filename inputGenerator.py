__author__ = 'Chenxi'
#below is for writing out a csv file with people's id,Birth-Year and Death-Year in columns

import random,csv
people = []

def writeTo_csv(arr):
    """
    :wtype : csv file
    """
    with open('superTest.csv', 'wb') as csvfile:
        fieldnames = ['id', 'Birth-Year', 'Death-Year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0,population):
            writer.writerow({'id': arr[i][0],'Birth-Year': arr[i][1],'Death-Year': arr[i][2],}),
    csvfile.close()

if __name__ == "__main__":
    #dataFile1 = open('dataset.txt', 'w')
    population = 99000
    for i in xrange(population):
        birthYr = random.randint(1900, 2000)
        deathYr = random.randint(birthYr,2000)
        person = [i,birthYr,deathYr]
        people.append(person)
    writeTo_csv(people)
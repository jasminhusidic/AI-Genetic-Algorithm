import random

def fitness(genome,key):
    seed = 'ztVvDguRAQDaSXXmLeJkUxRejhCGKfRjWDJCwowiSioIwtDqDHwelMnDfsXlhceWgMKXBUbsqlDVvXhpXXgtTjNmdBQfVsacmEvbHxQXodqKLaeFsrwlyMTkvziWPOAbgDjMXZRpUyrMVRmKhZotMIQtZHuzkvrlpgYgYAjFgOHYhrDquFTKxfargRnZDtISDpvEZqQJgLmRlyJrnqMiampUBMlcyyLqKJypCAiKhFIxuYlZkiYeOtVQCktDJAvgjiickEOvISfiaJqHUjOfuaRpdGFysIgoyXnVbjIVfDQhpgtVDIvHRmRnApMTDFQIPFWLNMkCWoMPgvNCpAFFDIEzxIWAodRAOrErfuTzdbRjMroKhomBBEzvraoKpAMeQXlzantpvUhWPNNCodmpJaThVTFYevCCwVahUpUncRDKpWhoogIUcpBcSSudgHrsIjQAcNjWFjOITSBWeASqotPMBIjzomMsdWEnyIkrfPgnbnYXgrwfZlNfYyAvBsUxQgVoLnHkWtXaKrGiDjEbJeMcOqTpCzFuSmRhIwPd'
    mult = list(range(-33,0))+list(range(1,33))
    s = 0
    for x in range(len(genome)):
        s+=(ord(seed[x+key])-ord(seed[key-1]))*(mult[int(genome[x])+32])+10
    return s

######################################################
#  Do not change the code above this section
#  Modify the code BELOW this section
######################################################

"""
Part One
Method:  newChromosome() 
Inputs:  None
Outputs: A single, length 32 string of 1s and 0s
"""
def newChromosome():
    chromosome = ""
    for i in range(32):
        temp = str(random.randint(0,1))
        chromosome += temp
    return chromosome
    

"""
Part Two
Method:  mutation() 
Inputs:  A length 32 string
Outputs: A length 32 string that only differs by one "bit" from the input
"""
def mutation(originalChromosome):
    mutatedChromosome = ""
    mutationIndex = (random.randint(0,31))
    for i in originalChromosome:
        mutatedChromosome = mutatedChromosome + i
    if mutatedChromosome[mutationIndex] == "1":
        value = "0"
    else:
        value = "1"
    mutatedChromosome = mutatedChromosome[:mutationIndex] + value + mutatedChromosome[mutationIndex+1:]
    return mutatedChromosome


"""
Part Three
Method:  crossover() 
Inputs:  Two length 32 strings
Outputs: Two length 32 strings that were formed by using a random crossover point
NOTE: Crossover point should be a number from 1-31 and the point should indicate HOW MANY
      characters to take from the front of one string.  Obviously, you would take 32-Crossover point
      characters from the second string
"""
def crossover(orig1, orig2):
    select1 = ""
    select2 = ""
    crossoverPoint = (random.randint(0,31))
    select1 = orig1[:crossoverPoint] + orig2[crossoverPoint:]
    select2 = orig2[:crossoverPoint] + orig1[crossoverPoint:]
    return select1,select2


        
"""
Part Four
Method:  bestFits() 
Inputs:  A list of chromosomes - one population
         The key to be used by the fitness function
Outputs: A single chromsome from the list of chromsomes
         The fitness score for that chromosome
NOTE: The outputs should be the BEST score found in the list of chromosomes
"""
def bestFits(population,key):
    bestChromosome=""
    bestScore=-1000

    for chromosome in population:
        score = fitness(chromosome,key)
        if score > bestScore:
            bestChromosome=""
            bestScore = score
            bestChromosome = bestChromosome + chromosome
            
    return bestChromosome,bestScore



"""
Part Five
Method:  lottery() 
Inputs:  A list of chromosomes - one population
         The key to be used by the fitness function
Outputs: A significantly larger list of chromsomes.  
NOTE: The length of the output list is variable depending on the chromsomes in the input
       population and their fitness functions.
       Each chromosome from the input population will likely occur
       multiple times in the output list.
"""
def lottery(population,key):
    outputList=[]

    for chromosome in population:
        score = fitness(chromosome,key)
        if score < 10:
            pass
        elif score >= 10:
            score = score // 10
            for i in range(score):
                outputList.append(chromosome)
    return outputList


"""
Part Six
Method:  GARunner()
Inputs: pSize - an int, the number of chromsomes in each population
        gen - the number of generations for which the GA is run
        sel - the number of members of gen N who automatically pass to gen N+1 (selection)
        mut - the number of members of gen N who are mutated and moved on to gen N+1 (mutation)
        nb  - the number of brand new chromosomes introduced each generation (new blood)
        co  - the number of PAIRS of chromosomes that undergo crossover each generation (crossover)
        key - the key used by the fitness function
Outputs:    bestChromosome - The best length 32 chromsome from the final generation
            bestScore - The fitness value of that best Chromosome
NOTE : sel + mut + nb + 2*co must equal pSize.  If not, you should return "" and -1000 for the output values
"""
def GARunner(pSize,gen,sel,mut,nb,co,key):
    bestChromosome=""
    bestScore = -1000
    initialPop = []
    fitPop = []
    count = 0
    #Checks to ensure that the inputed values are valid. If they are valid, it generates a
    #list of 32 bit binary strings.
    if pSize != (sel+mut+nb+(co*2)):
        print("error")
        return bestChromosome,bestScore
    else:
        for i in range(pSize):
            initialPop.append(newChromosome())
    
   #Loop that will continue until the appropriate number of generations is met
    while count <= gen:
        lottoList = lottery(initialPop,key)
        initialPop = [] #initialPop is cleared out for the next gen to be appended

        #Generates the lottery list and appends the appropriate number of fit invividuals to a seperate list
        for i in range(pSize):
            temp = len(lottoList)
            index = random.randint(0, temp-1)
            fitPop.append(lottoList[index])

        #Generates offspring using two random parents from lottery list
        for i in range(co):
            temp1,temp2 = crossover(random.choice(lottoList),random.choice(lottoList))
            initialPop.append(temp1)
            initialPop.append(temp2)
            
        #Mutates a random chromosome from the list of fit population and adds it to next gen
        for i in range(mut):
            temp = len(lottoList)
            index = random.randint(0,temp-1)
            initialPop.append(mutation(lottoList[index]))
            
        #Chooses a random chromosome from fit population and inverts the genomes    
        for i in range(nb):
            nbChromo = ""
            temp = len(lottoList)
            index = random.randint(0,temp-1)
            for i in lottoList[index]:
                if i == "0":
                    i = "1"
                    nbChromo = nbChromo + i
                else:
                    i = "0"
                    nbChromo = nbChromo + i
            initialPop.append(nbChromo)

        #Choose a random chromosome from fit popualtion to move on    
        for i in range(sel):
            temp = len(lottoList)
            index = random.randint(0,temp-1)
            initialPop.append(lottoList[index])
            

        answer = bestFits(initialPop,key)
        fitPop = []
        print("Best in generation {} is {}".format(count,answer))
        count += 1
    return answer



            
                
                
                
    



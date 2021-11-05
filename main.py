'''
Condiciones
~~~~~~~~~~~
1. Hay 5 casas.
2. El Matematico vive en la casa roja.
3. El hacker programa en Python.
4. El Brackets es utilizado en la casa verde.
5. El analista usa Atom.
6. La casa verde esta a la derecha de la casa blanca.
7. La persona que usa Redis programa en Java
8. Cassandra es utilizado en la casa amarilla
9. Notepad++ es usado en la casa del medio.
10. El Desarrollador vive en la primer casa.
11. La persona que usa HBase vive al lado de la que programa en JavaScript.
12. La persona que usa Cassandra es vecina de la que programa en C#.
13. La persona que usa Neo4J usa Sublime Text.
14. El Ingeniero usa MongoDB.
15. EL desarrollador vive en la casa azul.

Quien usa vim?


Resumen:
Colores = Rojo, Azul, Verde, Blanco, Amarillo
Profesiones = Matematico, Hacker, Ingeniero, Analista, Desarrollador
Lenguaje = Python, C#, JAVA, C++, JavaScript
BD = Cassandra, MongoDB, Neo4j, Redis, HBase
editor = Brackets, Sublime Text, Atom, Notepad++, Vim
'''

import random
import time
import re

colors =      {'001' : 'red',          '010' : 'blue',          '011' : 'green',    '100' : 'white',    '101' : 'yellow'}
profession =  {'001' : 'Mathematician','010' : 'Hacker',        '011' : 'Engineer', '100' : 'Analyst',  '101' : 'Developer'}
languaje =    {'001' : 'Python',       '010' : 'C#',            '011' : 'Java',     '100' : 'C++',      '101' : 'JavaScript'}
database =    {'001' : 'Cassandra',    '010' : 'MongoDB',       '011' : 'HBase',    '100' : 'Neo4j',    '101' : 'Redis'}
editor =      {'001' : 'Brackets',     '010' : 'Sublime Text',  '011' : 'Vim',      '100' : 'Atom',     '101' : 'Notepad++'}

colorsRow = 0
professionRow = 1
languajeRow = 2
databaseRow = 3
editorRow = 4

colorsKeys = list(colors.keys())
professionKeys = list(profession.keys())
languajeKeys = list(languaje.keys())
databaseKeys = list(languaje.keys())
editorKeys = list(editor.keys())

colorsValues = list(colors.values())
professionValues = list(profession.values())
languajeValues = list(languaje.values())
databaseValues = list(languaje.values())
editorValues = list(editor.values())

chromosomeProto = [colorsKeys, professionKeys, languajeKeys, databaseKeys, editorKeys]

n_population = 2000
crossOverLiveness = 200
mutants = 200
ok_score = 1
fail_score = 0.5
punish_score = 1
crossOverLivenessProbability = 70

class Phenotype:

    def __init__(self):
        # crear un individuo
        self.chromosome = [[0 for x in range(5)] for x in range(5)]
        self.score   =  20
        self.approved = 0
        self.approvedArray = [] # OK
        self.punishedArray = [] # Castigo 
        self.randomInit()

    def randomInit(self):
        for x in range(0,5):
            for y in range(0,5):
                self.chromosome[x][y] = random.sample(chromosomeProto[x], 1)[0]
                pass
            pass

    def decode(self):
        ''' traduce 0's y 1's (conjunto de genes: 3) en valores segun un diccionario '''
        colorsList = []
        professionList = []
        languajeList = []
        databaseList = []
        editorList = []

        chromosome = []

        for x in range(0,5):
            for y in range(0,5):
                if x == 0:
                    self.chromosome[x][y] = colors[self.chromosome[x][y]]
                    colorsList.append(self.chromosome[x][y])
                if x == 1:
                    self.chromosome[x][y] = profession[self.chromosome[x][y]]
                    professionList.append(self.chromosome[x][y])
                if x == 2:
                    self.chromosome[x][y] = languaje[self.chromosome[x][y]]
                    languajeList.append(self.chromosome[x][y])
                if x == 3:
                    self.chromosome[x][y] = database[self.chromosome[x][y]]
                    databaseList.append(self.chromosome[x][y])
                if x == 4:
                    self.chromosome[x][y] = editor[self.chromosome[x][y]]
                    editorList.append(self.chromosome[x][y])
        
        chromosome.append(colorsList)
        chromosome.append(professionList)
        chromosome.append(languajeList)
        chromosome.append(databaseList)
        chromosome.append(editorList)

        return chromosome

    def encode(self):
        pass

    def getChromosome(self, x, y):
        return self.chromosome[x][y]

    def mutate(self):
        ''' muta un fenotipo, optimizado'''
        variablesY = [0,1,2,3,4]
        x  = random.randint(0,4)
        y1 = random.choice(variablesY)
        variablesY.remove(y1)
        y2 = random.choice(variablesY)
        temp = self.chromosome[x][y1]
        self.chromosome[x][y1] = self.chromosome[x][y2]
        self.chromosome[x][y2] = temp
        pass

    def fitness_function(self):
        ''' calcula el valor de fitness del cromosoma segun el problema en particular '''

        self.score = 0

        ok_score = 1
        fail_score = 1
        punish_score = 1

        num_format = re.compile(r'^\-?[1-9][0-9]*$')
        it_is = re.match(num_format,self.chromosome[0][0]) 
        
        if it_is:
            chromosome = self.decode()
        else:
            chromosome = self.chromosome

        # 1. Hay 5 casas.
        #Check consistency
        for x in range(0,5):
            if len(chromosome[x])!=len(set(chromosome[x])):
                self.score -= 2*punish_score
            pass

        # 2. El Matematico vive en la casa roja.
        try:
            i = chromosome[professionRow].index('Mathematician')
            if chromosome[colorsRow][i] == 'red':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(2)
            else:
                self.score -= fail_score
                self.punishedArray.append(2)
        except:
            self.score -= punish_score
        pass

    # 3. El hacker programa en Python.
        try:
            i = chromosome[professionRow].index('Hacker')
            if chromosome[languajeRow][i] == 'Python':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(3)
            else:
                self.score -= fail_score
                self.punishedArray.append(3)
        except:
            self.score -= punish_score

        # 4. El Brackets es utilizado en la casa verde.
        try:
            i = chromosome[editorRow].index('Brackets')
            if chromosome[colorsRow][i] == 'green':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(4)
            else:
                self.score -= fail_score
                self.punishedArray.append(4)
        except:
            self.score -= punish_score

        # 5. El analista usa Atom.
        try:
            i = chromosome[professionRow].index('Analyst')
            if chromosome[editorRow][i] == 'Atom':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(5)
            else:
                self.score -= fail_score
                self.punishedArray.append(5)
        except:
            self.score -= punish_score

        # 6. La casa verde esta a la derecha de la casa blanca.
        try:
            i = chromosome[colorsRow].index('green')
            if chromosome[colorsRow][i-1] == 'white':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(6)
            else:
                self.score -= fail_score
                self.punishedArray.append(6)
        except:
            self.score -= punish_score

        # 7. La persona que usa Redis programa en Java
        try:
            i = chromosome[databaseRow].index('Redis')
            if chromosome[languajeRow][i] == 'Java':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(7)
            else:
                self.score -= fail_score
                self.punishedArray.append(7)
        except:
            self.score -= punish_score

        # 8. Cassandra es utilizado en la casa amarilla
        try:
            i = chromosome[databaseRow].index('Cassandra')
            if chromosome[colorsRow][i] == 'yellow':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(8)
            else:
                self.score -= fail_score
                self.punishedArray.append(8)
        except:
            self.score -= punish_score

        # 9. Notepad++ es usado en la casa del medio.
        try:
            if chromosome[editorRow][2] == 'Notepad++':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(9)
            else:
                self.score -= fail_score
                self.punishedArray.append(9)
        except:
            self.score -= punish_score

        # 10. El Desarrollador vive en la primer casa.
        try:
            if chromosome[professionRow][0] == 'Developer':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(10)
            else:
                self.score -= fail_score
                self.punishedArray.append(10)
        except:
            self.score -= punish_score

        # 11. La persona que usa HBase vive al lado de la que programa en JavaScript.
        try:
            i = chromosome[databaseRow].index('HBase')
            if chromosome[languajeRow][i-1] == 'JavaScript' or chromosome[languajeRow][i+1] == 'JavaScript':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(11)
            else:
                self.score -= fail_score
                self.punishedArray.append(11)
        except:
            self.score -= punish_score

        # 12. La persona que usa Cassandra es vecina de la que programa en C#.
        try:
            i = chromosome[databaseRow].index('Cassandra')
            if chromosome[languajeRow][i+1] == 'C#' or chromosome[languajeRow][i-1] == 'C#':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(12)
            else:
                self.score -= fail_score
                self.punishedArray.append(12)
        except:
            self.score -= punish_score

        # 13. La persona que usa Neo4J usa Sublime Text.
        try:
            i = chromosome[databaseRow].index('Neo4j')
            if chromosome[editorRow][i] == 'Sublime Text':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(13)
            else:
                self.score -= fail_score
                self.punishedArray.append(13)
        except:
            self.score -= punish_score

        # 14. El Ingeniero usa MongoDB.
        try:
            i = chromosome[professionRow].index('Engineer')
            if chromosome[databaseRow][i] == 'MongoDB':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(14)
            else:
                self.score -= fail_score
                self.punishedArray.append(14)
        except:
            self.score -= punish_score

        # 15. EL desarrollador vive en la casa azul.
        try:
            i = chromosome[professionRow].index('Developer')
            if chromosome[colorsRow][i] == 'blue':
                self.score += ok_score
                self.approved += 1
                self.approvedArray.append(15)
            else:
                self.score -= fail_score
                self.punishedArray.append(15)
        except:
            self.score -= punish_score

class Riddle:

    def __init__(self):
        self.start_time = time.time()
        self.population = []


    '''
    proceso general
    '''
    def solve(self, n_population, max_generations):
        
        self.generate(n_population)
        print(f"Poblacion creada con {len(self.population)} individuos")

        ''' descomentame '''
        print(self.population[0].chromosome)
        print(self.population[0].decode())

        print("Inicio del proceso iterativo")
        fit, indi = self.iterar(n_population, max_generations)

        print(f"Fin del proceso, mejor resultado \n - Fitness: {fit} \n - Individuo {indi.chromosome} \n - Individuo {indi.decode()}")
        

    def iterar(self, n_population, max_generations):

        counter = 0
        break_condition = False

        crossover_prop = 0.80
        
        while not(break_condition):
            counter += 1
            print('Iteracion  %d' %counter)
            self.fitness_function()
            approved = self.population[0].approved
            
            # seleccion y crossover
            self.selectionAndCrossOver(crossOverLiveness, n_population)

            # mutate
            self.mutate()
            if (approved == 14):
                print(self.population[0].approvedArray)

            # condicion de corte
            if approved >= 14 or counter > max_generations:
                break_condition = True
            pass

        self.fitness_function()
        return self.population[0].score, self.population[0]

    '''
    operacion: generar individuos y agregarlos a la poblacion
    '''
    def generate(self, i):
        for x in range(0,i):
            newbie = Phenotype()
            self.population.append(newbie)

    '''
    operacion: mutación. Cambiar la configuración fenotipica de un individuo
    '''
    def mutate(self):
        for x in range(0,mutants):
            y = random.randint(0,len(self.population)-1)
            self.population[y].mutate()
            pass


    '''
    operacion: selección y cruazamiento. Intercambio de razos fenotipicos entre individuos y selección del más apto
    '''
    def selectionAndCrossOver(self, i, limit):
        goodPopulation = []
        i = 0
        while len(goodPopulation) < crossOverLiveness:
            if random.randint(0,100) < crossOverLivenessProbability:
                goodPopulation.append(self.population[i])
            i += 1
            i %= len(self.population)
        newGeneration = []
        while len(newGeneration) <= limit:
            first = goodPopulation[random.randint(0,len(goodPopulation)-1)]
            second = goodPopulation[random.randint(0,len(goodPopulation)-1)]
            third = goodPopulation[random.randint(0,len(goodPopulation)-1)]
            newborn = self.crossOver(first, second, third)
            newGeneration.append(newborn)
        self.population = newGeneration

    '''
    operacion: cruzamiento. Intercambio de razos fenotipicos entre individuos
    '''
    def crossOver(self, first, second, third):
        newborn = Phenotype()
        for x in range(0,5):
            for y in range(0,5):
                i = random.randint(0,2)
                if i == 0:
                    newborn.chromosome[x][y] = first.getChromosome(x,y)
                elif i == 1:
                    newborn.chromosome[x][y] = second.getChromosome(x,y)
                else:
                    newborn.chromosome[x][y] = third.getChromosome(x,y)
                pass
            pass
        return newborn

    '''
    operacion:
    '''
    def fitness_function(self):
        for x in range(0,len(self.population)):
            self.population[x].fitness_function()
            pass

        self.population.sort(key=lambda x: x.score, reverse=True)
        for x in range(0,1):
            print('Approved  %d' %self.population[x].approved)
            pass

start = time.time()

rid = Riddle()
rid.solve(n_population, 1000)

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Tiempo transcurrido {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
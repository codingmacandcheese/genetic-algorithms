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


colors =      {'001' : 'red',          '010' : 'blue',          '011' : 'green',    '100' : 'white',    '101' : 'yellow'}
profession =  {'001' : 'Mathematician','010' : 'Hacker',        '011' : 'Engineer', '100' : 'Analyst',  '101' : 'Developer'}
languaje =    {'001' : 'Python',       '010' : 'C#',            '011' : 'Java',     '100' : 'C++',      '101' : 'JavaScript'}
database =    {'001' : 'Cassandra',    '010' : 'MongoDB',       '011' : 'HBase',    '100' : 'Neo4j',    '101' : 'Redis'}
editor =      {'001' : 'Brackets',     '010' : 'Sublime Text',  '011' : 'Vim',      '100' : 'Atom',     '101' : 'Notepad++'}

genes = ['001', '010', '011', '100', '101']

colorsRow = 0
professionRow = 1
languajeRow = 2
databaseRow = 3
editorRow = 4

def getScore(element):
    return element.score

def getMutationAmount():
  prob = random.random()
  if prob < 0.8  : return 1
  if prob < 0.95 : return 2
  return 3

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    if leftSpan == 0:
        return 0.1
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

class Phenotype:

    def __init__(self, chromosome=False):
        # crear un individuo
        self.chromosome = chromosome 
        if not(chromosome):
            self.random_chromosome()
        self.score = 0
        self.fitness = 0

    def random_chromosome(self):
        self.chromosome = [random.choice(genes) for i in range(25)]

    def decode(self):
        ''' traduce 0's y 1's (conjunto de genes: 3) en valores segun un diccionario '''
        colorsArray = [colors[self.chromosome[i*5+0]] for i in range(5)]
        professionArray = [profession[self.chromosome[i*5+1]] for i in range(5)]
        languageArray = [languaje[self.chromosome[i*5+2]] for i in range(5)]
        databaseArray = [database[self.chromosome[i*5+3]] for i in range(5)]
        editorArray = [editor[self.chromosome[i*5+4]] for i in range(5)]
        return [colorsArray, professionArray, languageArray, databaseArray, editorArray]
        

    def encode(self):
        pass


    def mutate(self, mutationRate):
        ''' muta un fenotipo, optimizado'''
        prob = random.random()
        if prob < mutationRate:
            for mutationAmount in range(getMutationAmount()):
                geneIndex = random.randint(0, 24)
                self.chromosome[geneIndex] = random.choice(genes)

    def fitness_function(self):
        ''' calcula el valor de fitness del cromosoma segun el problema en particular '''
        self.score = 0

        ok_score = 1
        fail_score = -1
        punish_score = -1 
        
        chromosome = self.decode()

        # 1. Hay 5 casas.
        #Check consistency
        for x in range(0,5):
            if len(chromosome[x])!=len(set(chromosome[x])):
                self.score += punish_score

        # 2. El Matematico vive en la casa roja.
        try:
            i = chromosome[professionRow].index('Mathematician')
            if chromosome[colorsRow][i] == 'red':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

    # 3. El hacker programa en Python.
        try:
            i = chromosome[professionRow].index('Hacker')
            if chromosome[languajeRow][i] == 'Python':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 4. El Brackets es utilizado en la casa verde.
        try:
            i = chromosome[editorRow].index('Brackets')
            if chromosome[colorsRow][i] == 'green':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 5. El analista usa Atom.
        try:
            i = chromosome[professionRow].index('Analyst')
            if chromosome[editorRow][i] == 'Atom':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 6. La casa verde esta a la derecha de la casa blanca.
        try:
            i = chromosome[colorsRow].index('green')
            if chromosome[colorsRow][i-1] == 'white':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 7. La persona que usa Redis programa en Java
        try:
            i = chromosome[databaseRow].index('Redis')
            if chromosome[languajeRow][i] == 'Java':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 8. Cassandra es utilizado en la casa amarilla
        try:
            i = chromosome[databaseRow].index('Cassandra')
            if chromosome[colorsRow][i] == 'yellow':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 9. Notepad++ es usado en la casa del medio.
        try:
            if chromosome[editorRow][2] == 'Notepad++':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 10. El Desarrollador vive en la primer casa.
        try:
            if chromosome[professionRow][0] == 'Developer':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 11. La persona que usa HBase vive al lado de la que programa en JavaScript.
        try:
            i = chromosome[databaseRow].index('HBase')
            if chromosome[languajeRow][i-1] == 'JavaScript' or chromosome[languajeRow][i+1] == 'JavaScript':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 12. La persona que usa Cassandra es vecina de la que programa en C#.
        try:
            i = chromosome[databaseRow].index('Cassandra')
            if chromosome[languajeRow][i+1] == 'C#' or chromosome[languajeRow][i-1] == 'C#':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 13. La persona que usa Neo4J usa Sublime Text.
        try:
            i = chromosome[databaseRow].index('Neo4j')
            if chromosome[editorRow][i] == 'Sublime Text':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 14. El Ingeniero usa MongoDB.
        try:
            i = chromosome[professionRow].index('Engineer')
            if chromosome[databaseRow][i] == 'MongoDB':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass

        # 15. EL desarrollador vive en la casa azul.
        try:
            i = chromosome[professionRow].index('Developer')
            if chromosome[colorsRow][i] == 'blue':
                self.score += ok_score
#             else:
#                 self.score += fail_score
        except:
            pass
            
class Riddle:

    def __init__(self):
        self.start_time = time.time()
        self.population = []
        self.maxGenerations = 2000
        self.mutationRate = 0.3

    '''
    proceso general
    '''
    def solve(self, n_population):
        
        self.generate(n_population)
        print(f"Población creada con {len(self.population)} individuos")

        ''' descomentame '''
        #print(self.population[0].chromosome)
        #print(self.population[0].decode())

        print("Inicio del proceso iterativo")
        fit, indi = self.iterar()

        print(f"Fin del proceso, mejor resultado \n - Fitness: {fit} \n - Individuo {indi.chromosome} \n - Individuo {indi.decode()}")
        

    def iterar(self):

        counter = 0
        break_condition = False

        random.seed(time.time())

        crossover_prop = 0.80
        
        while not(break_condition):
            
            # if counter % 100 == 0:
            #     print("--------------------------------")
            #     print(counter)
            #     print(self.population[0].decode())
            
            # seleccion
            matingPool = []

            minScore = 100000
            maxScore = -100000
            for i, x in enumerate(self.population):
                x.fitness_function()
                if x.score < minScore:
                    minScore = x.score
                if x.score > maxScore:
                    maxScore = x.score

            for i, ind in enumerate(self.population):
                fitness = translate(ind.score, minScore, maxScore, 0, 1)
                n = round(fitness * 100)
                for j in range(0, n):
                    matingPool.append(ind)

            print(f"Mejor calificación: {maxScore}")
            
            # crossover
            for index in range(0, len(self.population)):
                [parentA, parentB] = random.choices(matingPool, k=2)
                childGenes = self.crossOver(parentA, parentB)
                child = Phenotype(childGenes)
                self.population[index] = child
       
            # mutate
            for ind in self.population:
                ind.mutate(self.mutationRate)

            # condicion de corte
            
            counter += 1
            print(f"Iteración nro {counter}")
            
            if counter > self.maxGenerations or maxScore > 13:
                break_condition = True            

        sortedPopulation = sorted(self.population, key=getScore, reverse=True)
        return sortedPopulation[0].score, sortedPopulation[0]

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
    def mutate(self, crossed, prob=0.5):
        print("programame")
        pass


    '''
    operacion: cruazamiento. Intercambio de razos fenotipicos entre individuos
    '''
    def crossOver(self, progenitor_1, progenitor_2):
        genes1 = progenitor_1.chromosome
        genes2 = progenitor_2.chromosome
        limit = random.randint(0, len(genes1))
        return [*genes1[:limit], *genes2[limit:]]


start = time.time()

rid = Riddle()
rid.solve(n_population = 1000)

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Tiempo transcurrido {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
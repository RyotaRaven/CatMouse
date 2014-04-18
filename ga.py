import random
import math

from brain_dna import dna 

#dna class
# mutate
# crossover
# evaluate

population = []
pop_size = 100
generations = 300

for x in range(pop_size):
 population.append( dna() )

best=None
for generation in range(generations):
 for individual in population:
  individual.evaluate()
 population.sort(key=lambda x:x.fitness,reverse=True)
 population=population[0:pop_size/2]
 best=population[0]
 print generation, population[0].fitness
 new_population = [best]
 for x in range(1,pop_size):
  if random.random()<0.5:
   child=random.choice(population).mutate()
   new_population.append(child)
  else:
   p1 = random.choice(population)
   p2 = random.choice(population)
   child=p1.crossover(p2)
   new_population.append(child)
 population=new_population


from Bricks import game_function
ann=best.create_neuron()
print game_function(ann,True)

#from pylab import *
#xlabel("Generations")
#ylabel("Avg Fitness")
#plot(fitness)
#show()    

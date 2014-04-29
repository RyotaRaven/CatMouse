import random
import catandmouse

#Aritficial Neural Network
class dna:
    problem_size=4
    def __init__(self):
        self.x=[]
        for k in range(0,dna.problem_size):
            self.x.append(random.uniform(-3.0,3.0)) 
    def copy(self):
        new_indiv=dna()
        new_indiv.x=self.x[:]
        return new_indiv

    def mutate(self):
        new_indiv = self.copy()
        to_mutate=random.randint(0,dna.problem_size-1)
        new_indiv.x[to_mutate]+=random.uniform(-1,1)
        return new_indiv

    def crossover(self,other):
        new_indiv = dna()
        for k in range(0,dna.problem_size):
            if random.random()>0.5:
                new_indiv.x[k]=self.x[k]
            else:
                new_indiv.x[k]=other.x[k]
        return new_indiv

    def create_neuron(self):
        new_neuron = neuron()
        new_neuron.weights=self.x
        return new_neuron

    def evaluate(self):
        new_neuron=self.create_neuron()
        self.fitness=evaluate_ann(new_neuron)


class neuron:
    def __init__(self):
        self.weights=[random.uniform(-1.0,1.0),
                random.uniform(-1.0,1.0),
                random.uniform(-1.0,1.0),
                random.uniform(-1.0,1.0)]

    def run(self,input1, input2, mOrC):
        total_signal=0.0
        val = 0.0
        for i in range (len(input1)):
            rand = random.randint(0, len(self.weights) - 1)
            total_signal+=self.weights[rand]*input1[i]
        """if total_signal>0.0:
            val = 1.0
        elif total_signal < 0.0:
            val =  -1.0"""
        #If it is a mouse
        #if (mOrC == 0):
        for k in range (len(input2)):
            rand = random.randint(0, len(self.weights) - 1)
            total_signal-=self.weights[rand]*input2[k]
            
        if total_signal>0.0:
            val = 1.0
        elif total_signal < 0.0:
            val = -1.0
        return val


def evaluate_ann(ann):
    score = catandmouse.game_function(ann, True)
    return score


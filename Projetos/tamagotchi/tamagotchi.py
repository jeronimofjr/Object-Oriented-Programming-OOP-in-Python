class Pet:

    def __init__(self, energy, hungry, clean, diamonds=0, age=0, alive=True):
        self.energy = energy
        self.hungry = hungry
        self.clean = clean
        self.alive = alive
        self.diamonds  = diamonds
        self.age = 0
        self.energyMax =  energy
        self.hungryMax = hungry
        self.cleanMax = clean
    
    def show(self):
        return 'E:'  + str(self.energy) + '/' + str(self.energyMax) + ', S:' + str(self.hungry) + '/' + str(self.hungryMax) + ', L:' + str(self.clean) + '/' + str(self.cleanMax) + ', D:' + str(self.diamonds) + ', A:' + str(self.age)
 
    def getEnergy(self):
        return self.energy
    
    def getHungry(self):
        return self.hungry

    def getClean(self):
        return self.clean
    
    def getDiamonds(self):
        return self.diamonds
    
    def getAge(self):
        return self.age

    def setEnergy(self, value):
        if value + self.getEnergy() >= self.energyMax:
            self.energy = self.energyMax
        else:
            self.energy = self.getEnergy() + value
        if self.getEnergy() <= 0:
            self.energy = 0
            self.setAlive()
    
    def setHungry(self, value):
        if value + self.getHungry() >= self.hungryMax:
            self.hungry = self.hungryMax
        else:
            self.hungry = self.getHungry() + value
        
        if self.getHungry() <= 0:
            self.hungry = 0
            self.setAlive()
    
    def setClean(self, value):
        if value + self.getClean() >= self.cleanMax:
            self.clean = self.cleanMax
        else:
            self.clean = self.getClean() + value
        
        if self.getClean() <= 0:
            self.clean = 0
            self.setAlive()
    
    def setDiamongs(self, value):
        self.diamonds = self.getDiamonds() + value

    def setAge(self, value):
        self.age = self.getAge() + value 
    
    def getAlive(self):
        return self.alive
    
    def setAlive(self):
        self.alive = False
    # # O comando "$play" altera em -2 energia, -1 saciedade, -3 limpeza, +1 diamante, +1 idade.
    def play(self):
        if not self.getAlive():
            print ('fail: pet esta morto')
        else:
            self.setEnergy(-2)
            if self.getEnergy() == 0:
                print('pet morreu de cansaço')
            self.setHungry(-1)
            if self.getHungry() == 0:
                print('pet morreu de fome')
            self.setClean(-3)
            if self.getClean() == 0:
                print('pet morreu de sujeira')
            self.setDiamongs(1)
            self.setAge(1)
            return ''
    
    # # O Comando "$eat" altera em -1 a energia, +4 a saciedade, -2 a limpeza, +0 diamantes,  +1 a idade
    def eat(self):
        if not self.getAlive():
            print ('fail: pet esta morto')
        else:
            self.setEnergy(-1)
            self.setHungry(4)
            self.setClean(-2)
            self.setAge(1)

    # O Comando "$sleep" aumenta energia até o máximo e idade aumenta do número de turnos que o pet dormiu.
    def sleep(self):
        if not self.getAlive():
            print ('fail: pet esta morto')
        else:
            aux = self.energyMax - self.getEnergy()
            if(aux) >= 5:
                self.setEnergy(aux)
                self.setAge(aux)
                return True
            print('fail: nao esta com sono')
            return False
    
    # O comando "$clean" alteram em -3 energia, -1 na saciedade, MAX na limpeza, +0 diamantes, +2 na idade.
    def clean_(self):
        if not self.getAlive():
            print ('fail: pet esta morto')
        else:
            self.setEnergy(-3)
            self.setHungry(-1)
            self.setClean(self.cleanMax - self.getClean())
            self.setAge(2)



def controller():
    while True:
        string = input('$').split()
        if string[0] == 'init':
            energy, hungry, clean = list(map(int , string[1:]))
            pet = Pet(energy, hungry, clean)
        elif string[0] == 'show':
            print(pet.show())
        elif string[0] == 'end':
            break
        elif string[0] == 'play':
            pet.play()
        elif string[0] == 'eat':
            pet.eat()
        elif string[0] == 'clean':
            pet.clean_()
        elif string[0] == 'sleep':
            pet.sleep()
        else:
            print('fail: error')

controller()
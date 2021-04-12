class Car:
    def __init__(self, gas, gasMax, passg, passMax, km):
        self.gas = gas
        self.gasMax = gasMax
        self.passg = passg
        self.passMax = passMax
        self.km = km

    def in_(self):
        if self.getPass() == self.getPassMax():
            return 'fail: limites de pessoas atingido' 
        self.passg += 1
        return 'sucess: passageiro entrou'

    def out(self):
        if self.getPass() == 0:
            return 'fail: não há ninguém no carro'
        self.passg -= 1
        return 'sucess: passageiro removido'

    def fuel(self, value):
        if value >= self.getGasMax():
            self.gas = self.getGasMax()
        else:
            self.gas = self.getGasMax()

    def drive(self, distance):
        if self.getPass() == 0:
            return 'fail: nao tem passageiro'
        litros = (distance // 10)
        if  litros > self.getGas():
            return 'fail: nao tem gasolina suficiente'
        self.km += (distance)
        self.gas -= litros
        return 'sucess'  

    def __str__(self):
        return 'pass: ' + str(self.getPass()) + ', Gas: ' + str(self.getGas()) + ', km: ' + str(self.getKm())

    def getGas(self):
        return self.gas

    def getGasMax(self):
        return self.gasMax

    def getPass(self):
        return self.passg
    
    def getPassMax(self):
        return self.passMax

    def getKm(self):
        return self.km


def controller():
    car = Car(0, 10, 0, 2, 0)
    while True:
        init = input('$').split()
        if init[0] == 'show':
            print(car)
        elif init[0] == 'end':
            break
        elif init[0] == 'in':
            print(car.in_())
        elif init[0] == 'out':
            print(car.out())
        elif init[0] == 'fuel':
            car.fuel(int(init[1]))
        elif init[0] == 'drive':
            print(car.drive(int(init[1])))

controller()


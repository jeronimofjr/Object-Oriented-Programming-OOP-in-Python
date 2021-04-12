class Calculadora:
    def __init__(self, maxBattery):
        self.maxBattery = maxBattery
        self.battery = 0

    def charge(self, value):
        if value + self.getbattery() >= self.maxBattery:
            self.battery = self.maxBattery
        else: 
            self.battery += value

    def usebattery(self):
        self.battery -= 1

    def show(self):
        print('Battery = {}'.format(self.battery))

    def getbattery(self):
        return self.battery

    def sum(self, a, b):
        if self.getbattery() > 0:
            self.usebattery()
            return a + b
        else:
            return 'fail: bateria insuficiente'
    
    def div(self, a, b):
        if b == 0:
            return 'fail: divisao por zero'
        if self.getbattery() > 0:
            self.usebattery()
            return a/b
        else:
            return 'fail: bateria insuficiente'

def controller():
    while True:
        input_ = input('$').split()
        if input_[0] == 'init':
            calc =  Calculadora(int(input_[1]))
        elif input_[0] == 'show':
            calc.show()
        elif input_[0] == 'charge':
            calc.charge(int(input_[1]))
        elif input_[0] == 'sum':
            print(calc.sum(int(input_[1]), int(input_[2])))
        elif input_[0] == 'div':
            print(calc.div(int(input_[1]), int(input_[2])))
        elif input_[0] == 'end':
            break

controller()

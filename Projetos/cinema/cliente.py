class Cliente:

    def __init__(self, name, fone):
        self.name = name
        self.fone = fone

    def getId(self):
        return self.name

    def toString(self):
        return self.name + ':' + self.fone
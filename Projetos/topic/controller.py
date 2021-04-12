from topic import *

def controller():
    topic = Topic(0, 0)
    while True:
        line = input('$').split()
        if line[0] == 'init':
            topic = Topic(int(line[1]), int(line[2]))
        elif line[0] == 'show':
            print(topic.show())
        elif line[0] == 'in':
            print(topic.gerenciaEntradas(line[1], int(line[2])))
        elif line[0] == 'usu':
            print(*topic.getIds())
        elif line[0] == 'out':
            print(topic.out(line[1]))
        elif line[0] == 'pass':
            print(topic.numeroTotalDePassageiros)
        elif line[0] == 'end':
            break

            

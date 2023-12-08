import serial 
import re
from SerialApp import SerialApp
import pddl
from pddl.logic import Predicate, constants, variables
from pddl.core import Domain, Problem
from pddl.action import Action
from pddl.formatter import domain_to_string, problem_to_string
from pddl.requirements import Requirements


serialP = SerialApp()
serialP.serialPort.port = 'COM5'

serialP.serialPort.baudrate = 9600
print(serialP.connectSerial())

with open('D:/Matérias da faculdade/2023-1/TCC/Arquivos/Programa_PRD/PRD by Guilherme Vitor(TM)/Percepcao_Planejamento_Modulo2_3/notes.txt','w') as writer:
    writer.write(serialP.receiveData())
serialP.closePort()
arq = open('D:/Matérias da faculdade/2023-1/TCC/Arquivos/Programa_PRD/PRD by Guilherme Vitor(TM)/Percepcao_Planejamento_Modulo2_3/notes.txt','r')
texto = arq.read()
init = re.findall(":init\(\w on \w+\)",texto)
init = [i[5:] for i in init]
objective = re.findall(":objective-0\(\w on \w+\)",texto)
objective = [i[12:] for i in objective]
print(init)
print(objective)







    



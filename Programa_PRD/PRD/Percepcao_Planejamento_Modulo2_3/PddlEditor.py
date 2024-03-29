import pddl
from pddl.logic import Predicate, constants, variables
from pddl.core import Domain, Problem
from pddl.action import Action
from pddl.formatter import domain_to_string, problem_to_string
from pddl.requirements import Requirements
from pddl import parse_domain,parse_problem
import re
from pddl.logic import Predicate, constants, variables,terms,Constant
from pddl.logic.base import And

class PddlEditor:
    def __init__(self):
        pass

    def editar_problema(self,arquivo):
        pddl1 = PddlEditor()
        
        #Procura de predicados Iniciais
        file = open(arquivo,'r')
        ar1 = file.read()

        init = re.findall(":init\(on \w \w+\)",ar1)#Predicados dos iniciais
    
        init = [i[5:] for i in init]
        
        objective = re.findall(":objective-0\(on \w \w+\)",ar1)#Predicados dos objetivos
        tables = [f"t{i}" for i in range(1,6)]
        
        objective = [i[12:] for i in objective]
        blocos = [i[4] for i in init] 
        posicoes = [j[6:8] if j[7] != ')' else j[6] for j in init]
        tablesFile = [i for i in tables if i not in posicoes]
        blocos = blocos + tablesFile
        clear = []
        pos = []
        c =0
        pred =[]

        
            
        problem = parse_problem('TestesExemplo/problem_copy.pddl')
        domain = parse_domain('TestesExemplo/domain_copy.pddl')
        lista1 = [Constant(i[4]) for i in init]
        lista2 =[Constant(i[6:8]) if i[7]!=')' else Constant(i[6]) for i in init]
        


        
        for ini in range(0,5):

            pred.append(Predicate("on",lista1[ini],lista2[ini]))

        for i in blocos:
            c=0
            for j in posicoes:

                if(i==j):
                    
                    for a in range(0,5):
                        for b in range(0,5):
                            if (a==b and posicoes[b] == i):
                                pos.append(f'(on {blocos[a]} {posicoes[b]})')
                    break
                else:
                    c += 1
            
            if(c==5):
                clear.append(f'clear {i}')


        for c in clear:
            pred.append(Predicate(c.split(' ')[0],Constant(c.split(' ')[1])))

        piso = {
            "t1":"table",
            "t2":"table",
            "t3":"table",
            "t4":"table",
            "t5":"table",
        }

        for k,v in piso.items():
            pred.append(Predicate(v,Constant(k)))

        pred.append(Predicate('emptyhand'))
        pred =(frozenset(pred))


        #Fim de procura para predicados iniciais

        #Predicados de objetivo

        obj = [o[1:8] if o[7]!=')' else o[1:7] for o in objective]
        predObj = []

        for o in obj:
            predObj.append((Predicate(o.split(' ')[0],Constant(o.split(' ')[1]),Constant(o.split(' ')[2]))))

        aux = predObj[0]
        for i in predObj:
            aux = aux & i


        new_problem = Problem('problemPDDL',domain,domain.name,domain.requirements,problem.objects,pred,aux)
        problem_to_stringA = problem_to_string(new_problem).replace(":fluents","")
        
        with open('TestesExemplo/problem_copy.pddl','w') as arquivos:
            arquivos.write(problem_to_stringA)

editor = PddlEditor()
editor.editar_problema('TestesExemplo/arquivo1.txt')

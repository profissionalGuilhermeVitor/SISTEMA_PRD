import re

relacoesFixo = {
            "t1":("0x0","1x0","2x0","3x0","4x0"),
            "t2":("0x1","1x1","2x1","3x1","4x1"),
            "t3":("0x2","1x2","2x2","3x2","4x2"),
            "t4":("0x3","1x3","2x3","3x3","4x3"),
            "t5":("0x4","1x4","2x4","3x4","4x4") 
        }
class CheckException:
    def __init__(self,file):
        self.file = file
        
        

    def tratarArquivo(self):
        arq = open(self.file,'r')
        texto = arq.read()
        return texto
    
    def exception1(self):#Pegar objetivos e inits e verificar se posições batem
        txt1 = CheckException(self.file).tratarArquivo()
        #Listas para exceções
        excecao1 = []
        excecao3 =[]
        #Filtro para inicio e objetivos
        init = re.findall(":init\(on \w \w+\)",txt1)#Predicados dos iniciais
        init = [i[5:] for i in init]
        objective = re.findall(":objective-0\(on \w \w+\)",txt1)#Predicados dos objetivos
        objteste = re.findall(":objective-0(\w+\s)",txt1)
        
        objective = [i[12:] for i in objective]
        #Criação de dicionarios com relações
        relacoesPiso = {
            "t1":"0x0",
            "t2":"0x1",
            "t3":"0x2",
            "t4":"0x3",
            "t5":"0x4",
        }

        filpos = re.findall(r'o: \wx\w',txt1)#Filtro de posições encontradas
        
        #Filtragem de posições repetidas no arquivo
        pos=[]
        repetidos = set()
        for i in filpos:
            if i not in pos:
                pos.append(i[3:6])
            else:
                repetidos.add(i)

        for i in pos:#Checar posições iguais colhidas-Exceção 0
            if(pos.count(i)>1):
                return '0'
        #Criar relação da posição com o bloco
        blocosIniciais = re.findall(":init\(on \w \w+\)",txt1)
        blocosIniciais = [i[9] for i in blocosIniciais]
        posicoesIniciaisI = re.findall(":init\(on \w \w+\)",txt1)
        posicoesIniciais = [i[11] if i[12]==')' else i[11:13] for i in posicoesIniciaisI]
        blocosOBJ = re.findall(":objective-0\(on \w \w+\)",txt1)
        blocosOBJ = [i[9] for i in blocosOBJ]
        posicoesOBJI = re.findall(":objective-0\(on \w \w+\)",txt1)
        posicoesOBJ = [i[18] if i[19]==')' else i[18:20] for i in posicoesOBJI]

        
        zipBV = list(zip(blocosIniciais,pos))
        mapa = [list(i) for i in relacoesFixo.values()]

        relacao ={}

        for elemento1, elemento2 in zipBV:#Cria relação por meio de dicionário
            relacao[elemento1] = elemento2
            relacao[elemento2] = elemento1
        for i in range(0,5):
            for j in range(0,5):
                if mapa[i][j] in pos:
                    mapa[i][j] = relacao[mapa[i][j]]
                else:
                    mapa[i][j] = '0'

        #Objetivos e Posições iniciais iguais-Exceçao 1
        relacao.update(relacoesPiso)
        
        listaBoa = []
        blc =[]

        for i in list(enumerate(posicoesIniciais)):
            if((posicoesIniciais).count(i[1])>1):
                blc.append(blocosIniciais[i[0]])

        if(len(blc)!=0):
            return ['1i'] + [mapa] + [list(relacao)] + [listaBoa] + [blc]
            

        
        for i in posicoesOBJ:
            if(posicoesOBJ.count(i)>1):
                return ['1o']

        #Inconsistências em objetivos ou iniciais-Blocos na mesma posição que outros-Exceção 2
        counto =0
        counti = 0

        for a in objective:
            for j in objective:
                if(j[6] == a[4] and j[4]==a[6]):
                    counto +=1
        
        for a in init:
            for j in init:
                if(j[6] == a[4] and j[4]==a[6]):
                    counti +=1

        if(counto > 1 or counti > 1):return ['2']
        #Objetivo vazio-Exceção 3
        
        if len(objective)<5 or len(init)<5:return ['3']
        #Situações Impossíveis
        
        #Checagem de exceções por meio de mapa-Exceção 4
        #Checar posições impossíveis-Exceção 4_Parte 1 - blocos vazios no piso
        for checkImpossible in mapa:
            if(checkImpossible[0] == '0'):
                for index in checkImpossible:
                    if(checkImpossible.index(index)!=0 and index !='0'):
                        return ['4']
                    
        #Checar posições impossiveis em todo o mapa-Exceção 4_Parte 2 - blocos vazios em posições inferiores a existentes
        for checkImpossible2 in mapa:
            for i in checkImpossible2:
                if (i=='0'):
                    if(checkImpossible2[checkImpossible2.index(i)+1] !='0'):
                        return ['4_2']

exception = CheckException('testando.txt')
print(exception.exception1() is not None)

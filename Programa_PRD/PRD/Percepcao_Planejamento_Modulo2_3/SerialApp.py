import serial
import serial.tools.list_ports


class SerialApp ():
    def __init__(self):
        self.serialPort = serial.Serial()#Cria um objeto para a comunicação serial
        self.baudrate = [9600,115200] #Baudrates necessários
        self.portlist = []
        

    def updatePort(self):
        self.portlist =[port.device for port in serial.tools.list_ports.comports() ]
        return self.portlist

    #Estabelecer Conexão
    def connectSerial(self):
        try:
            self.serialPort.open()
        except:
            print("ERRO!!!")

    #Receber Dados
    def receiveData(self):
        dataRead = ""
        dataRead = self.serialPort.read().decode("latin-1")
        print(dataRead)
        return dataRead

    #Enviar Dados
    def sendData(self,data):
        if(self.serialPort.isOpen()):
            dataSend = str(data) + '\n'
            print("Mensagem " +dataSend)
            self.serialPort.write(dataSend.encode())
            self.serialPort.flushOutput()
            return dataSend

    #Fechar a porta

    def closePort(self):
        self.serialPort.close()

    def portIsUsable(portName):
        try:
            ser = serial.Serial(port=portName)
            return True
        except:
            return False
        
    def readSerial(self):
        dataRead = self.serialPort.read(10).decode('utf-8')


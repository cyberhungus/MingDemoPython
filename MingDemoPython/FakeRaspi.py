
class fakeGPIO:
    HIGH = 1
    LOW = 0

    OUTPUT = 1
    INPUT = 0

    def __init__(self, gpios):
        self.GPIOS = []
        self._gpionum = gpios
        for num in range(0,gpios):
            self.GPIOS.append([num, fakeGPIO.LOW, fakeGPIO.OUTPUT])

    def __str__(self):
        return self.GPIOS

    def __iter__(self):
        return self.GPIOS.__iter__()

    def WritePin(self, pin, state):
        if state == 0 or state == 1 and pin in range(0,self._gpionum):
            if self.GPIOS[pin][2] == fakeGPIO.INPUT:
                self.GPIOS[pin][1]=state

    def setPinMode(self, pin, mode):
        if mode == 0 or mode == 1 and pin in range(0,self._gpionum):
            self.GPIOS[pin][2]=mode
            if mode == fakeGPIO.OUTPUT:
                self.GPIOS[pin][1]=fakeGPIO.LOW

    def ReadPin(self, pin):
        if pin in range(0,self._gpionum):
            if self.GPIOS[pin][2] == fakeGPIO.OUTPUT:
                return self.GPIOS[pin][1]
            else:
                return -1;


            

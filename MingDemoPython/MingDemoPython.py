#Python demo für Mings 

#A: Python sieht komisch aus 
a = 3 
if a >= 2:
    print("Hello Mings")

print('#'*20)
#B:Lose typisierung - nix mit int a = 23! Alles ist immer alles! 
b = 3
print("First: " , b)
b = "Hello Mings again"
print("Second:" + b)

print('#'*20)
#C: Listen <3
listeA = []
listeA.append("Adding element 1")
listeA.append("Adding element 2")
print(listeA)
#pop schmeißt letzes element raus 
listeA.pop()
print("Removing last element")
print(listeA)

print('#'*20)
#D Iterieren durch listen <3
listeB = []
for number in range(0,100):
    listeB.append(number)
print(str(len(listeB)), " Nummern in Liste" )
for item in listeB:
    if item == 77:
        print("Found 77")
    #Im Land Python sagt man "elif" statt else if !?
    elif item == 420:
        #wird nicht erreicht
        print("Found 420")
if 22 in listeB or True:
    #In Python Schreibt man True und False groß
    b = True;
    print("22 is in List?" , b)
        
    
#listen sind die typen egal 
listeB.append("Ich bin ein String in Liste B! lol!")
print(listeB[100])
#listen können sogar andere listen enthalten und allen möglichen kram <3
listeB[0] = ["Hello", 33, True, ("Blood Type", "A")]


print('#'*20)
#E Weirde neue Datentypen
#tupel
tup = ("two", 2)
print(tup)
#dictionary 
computer = {
  "CPU": "Am-Tel Shy-Zen 300",
  "RAM": 32,
  "Graphics": "Roydyon XD9600"
}
print("Graphics: " + computer["Graphics"])
print("RAM" +  str(computer["RAM"]))
#set ???? WTF nie benutzt 
thisset = set(("What", "is", " a set?!")) 
print(thisset)

print('#'*20)

#F: python = libraries
import imp
from itertools import count
import time
from traceback import print_list
print("Time from library")
print(time.ctime())

print('#'*20)

#F1: PIP ZEIGEN
print("PIP zeigen (pythonPackageinstaller)")
print('#'*20)
#G eigene funktion iseven sagt ob zahl gerade/ungerade
def isEven(a):
    if a%2 == 0:
        return True
    else:
       return False
print("Is even test with 8: ", isEven(8))
print("Is even test with 3: ", isEven(3))
print('#'*20)
#H eigene Klasse student
class student:
    #kein private oder so 
    firstName = ""
    lastName = ""
    semester = 7
    #wir machen ein '_' und respektieren das, statt private zu haben :D 
    _enrolled = True

    #überschreiben von systemfunktionen
    def __init__(self, fN, lN):
        self.firstName = fN
        self.lastName = lN

    def __str__(self):
        return "Student with first Name : {} , last Name: {}".format(self.firstName,self.lastName)

    #self immer mit dabei
    def isEnrolled(self):
        return self._enrolled

Johann = student("Johann", "Immerdrauf")

print(Johann)
print("Is johann enrolled? " , Johann.isEnrolled())
print('#'*20)

#H: Python python timer timer:
print("waiting 5 seconds")
#time.sleep(5)
print("slept 5 seconds")

#I: easy input für kommandozeilen
#typed=input("Bitte passwort eingeben: ")
#if typed == "passwort":
#    print("passwort eingegeben ")
#else:
#    while 1:
#        print("du musst passwort eingeben")

#J: Klasse aus anderer Datei 
#b = False
#while b == False:
#    print("Datei Zeigen")
#    inp = input("Datei gezeigt Y/N? ")
#    if inp == "Y" or inp == "y":
#        b = True

#lädt klasse aus anderer datei und zeigt ein bild
from ImageShower import ImageShower
imageShower = ImageShower("anleger.jpg")
#imageShower.showImage()

print('#'*20)
#K: Erste Aufgabe (Gedächtnisprotokoll des Kurses )
#LED Mit Button 

from FakeRaspi import fakeGPIO

#fake raspi klasse
raspi = fakeGPIO(40)

#welche pins machen was - button ist mit pin 1 verbunden
buttonPin = 0 
ledPin = 1
raspi.setPinMode(buttonPin,fakeGPIO.INPUT)
raspi.setPinMode(ledPin,fakeGPIO.OUTPUT)


#for item in raspi:
#    print(item)
#inp = input(" LICHT IST AUS! Raspi knopf drucken? Y/N :")
#if inp == "Y":
#    raspi.GPIOS[buttonPin]=1
#    print("Licht angeschaltet")

#for item in raspi:
#    print(item)
#inp = input(" LICHT IST AN! Raspi knopf drucken? Y/N :")
#if inp == "Y":
#    raspi.GPIOS[buttonPin]=1
#    print("Licht ausgeschaltet")


print('#'*20)

#L threading <3
from threading import Thread

#beispiel für einen worker (sowas macht man viel )
class TimeWorker:
    def __init__(self, delay, name):
        self.delay = delay
        self.name = name
        self.nexttime = 0
        self.alive = True

    def switchOff(self):
        self.alive =False

    def run(self):
        while self.alive:
            t = time.time()
            if self.nexttime < t:
                self.nexttime=t + self.delay
                print("Timeworker {} with delay {} next fired at is {} in ".format(self.name,self.delay,self.nexttime))

#WorkerA = TimeWorker(3,"-Three Seconds-")
#threadA = Thread(target = WorkerA.run)
#WorkerB = TimeWorker(7,"-SEVEN SECONDS-")
#threadB = Thread(target = WorkerB.run)
##starte thread
#threadA.start()
#threadB.start()
#print("Start Sleeping")
#time.sleep(10)
#print("End Thread A")
##müssen den loop unterbrechen mit switchoff 
#WorkerA.switchOff()
##join beendet dann den thread - erst den einen
#threadA.join()
#time.sleep(5)
##dann den anderen
#WorkerB.switchOff()
#threadB.join()
#print("End Thread B")

print('#'*20)

#M Schrittmotor

class motor:

    movementPattern = [[0,0,1,1],[1,0,1,0],[0,1,0,1],[1,1,0,0]]
    #pins = der motortreiber hat 4 eingänge, die in einem muster geschaltet werden müssen, damit sich der motor dreht 
    def __init__(self, pins):
        self.pins = pins
        self.stepSelector = 0
        self.position = 0
        self.delay = 20

    #mache einen schritt vor 
    def stepForward(self):
        self.stepSelector+=1
        self.position+=1
        time.sleep(self.delay/1000)
        if self.stepSelector > 3:
            self.stepSelector = 0
        #hier würde man movementPattern[stepselector] auf die pins anwenden
        print("F")

    #move step backward 
    def stepBackward(self):
        self.stepSelector-=1
        self.position-=1
        time.sleep(self.delay/10000)
        if self.stepSelector < 0:
            self.stepSelector = 3
        print("B")

    def __str__(self):
        return "Motor on pins {} at position {} with steppattern {} , selector {}".format(self.pins, self.position, motor.movementPattern[self.stepSelector], self.stepSelector)
   
    def __repr__(self):
        return "Motor on pins {} at position {} with steppattern {} , selector {}".format(self.pins, self.position, motor.movementPattern[self.stepSelector], self.stepSelector)
    
    def toString(self):
         return "Motor on pins {} at position {} with steppattern {} , selector {}".format(self.pins, self.position, motor.movementPattern[self.stepSelector], self.stepSelector)
    
     #bewegt x schritte vorwärts oder rückwärts
    def moveSteps(self,steps):
        if steps < 0:
            for num in range(steps, 0):
                self.stepBackward()
            print("Moved ",steps, " backwards")
        else:
            for num in range( 0, steps):
                self.stepForward()
                print("Moved ",steps, " forwards")


    def moveToPos(self, pos):
        dif = pos  + self.position 
        self.moveSteps(dif)

#erstelle motor
m = motor([0,1,2,3])
print("vor bewegung " , m.toString())
#bewege zu position 10 
m.moveToPos(10)
print("nach bewegung" , m.toString())
#routine erlaubt es mit dem motor herumzuspielen
###while 1:
###    num =input("Move Motor X steps - type quit or exit to end loop ")
###    if num == "Quit" or num  == "quit" or num == "exit":
###        break
###    else:
###        try:
###            toMove = int(num)
###            m.moveSteps(toMove)
###            print("Nach bewegung" , m)
###        except Exception as e:
###            print("Error in move, wrong value")

# N Sind Sockets zur OnlineKommunikation, kann ich schwer zeigen 

# O UI 
#erste UI library ist tkinter
global g
g = 0
def p():
    global g
    g+=1
    print("Button press" , g)
    


#import tkinter as tk
#w = tk.Tk()
#greeting = tk.Label(text="Hallo UI")
#greeting.pack()
#button = tk.Button(text = "Console", command = p)
#button.pack()
#w.mainloop()

#print ("pyqt")

#import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot

#def click():
#    print("Clicked")
#def window():
#   app = QApplication(sys.argv)
#   widget = QWidget()

#   textLabel = QLabel(widget)
#   textLabel.setText("Hello MING! - Ich will euch den pyqt creator zeigen ")
#   textLabel.move(110,85)

#   button = QPushButton(widget)
#   button.setText("Click me")
#   button.move(0,0)
#   button.clicked.connect(click)


#   widget.setGeometry(50,50,320,200)
#   widget.setWindowTitle("PyQt5 Example")
#   widget.show()
#   sys.exit(app.exec_())

#if __name__ == '__main__':
#   window()

# flask erlaubt das einfache erstellen von webservern 
from flask import Flask
app = Flask(__name__)
global c
c = 0
@app.route("/")
def hello():
    global c
    return "Counter: " + str(c) + " hits" 
@app.route("/count")
def count():
    global c
    c+=1
    return "Counter: " + str(c) + " hits " +"<img src=\"https://www.medieningenieur.de/wp-content/uploads/2018/03/Piecart.png\" alt=\"W3Schools.com\">" +"<a href=\"/count\">Count up !</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


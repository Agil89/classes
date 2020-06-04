class Vehicle():
    numofWheels =4
    color="black"
    engine=2.4
    positionX=1
    positionY=1
    speed=50
    isOn=False

    def __init__(self,color,engine,numofWheels):
        self.color=color
        self.engine=engine
        self.numofWheels=numofWheels

    def accelerate(self):
        self.speed = self.speed + 1
        return self.speed

    def moveForward(self,x,y):
        self.positionX = self.positionX + x
        self.positionY = self.positionY + y
        return f"{self.positionX} {self.positionY}"
    def moveBackwards(self,x,y):
        self.positionX = self.positionX - x
        self.positionY = self.positionY - y
        return f"{self.positionX} {self.positionY}"

    def ignition(self):
        if self.isOn == False:
            self.isOn = True
        elif self.isOn == True:
            self.isOn = False

    def getNumofWheels(self):
        return self.numofWheels

    def setNumofWheels(self,num):
        self.numofWheels = num

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
        return self.color

    def __str__(self):
        print(str(f"""tekerlerin sayi:{self.numofWheels}
                  masinin rengi:{self.color}
                  matorun hecmi: {self.engine}
                  x pozisyon: {self.positionX}
                  y pozisyon:  {self.positionY}
                  speed : {self.speed}
                    """))


class Motorcycle(Vehicle):
    brand = 'harley'
    numOfSeats = 1

    def __init__(self,color, engine,wheels, brand, seats):
        self.color = color
        self.engine = engine
        self.wheels = wheels
        self.brand = brand
        self.seats = seats

    def getBrand(self):
        return self.brand
    def getNumOfSeats(self):
        return self.numOfSeats
    def setBrand(self,brand):
        self.brand = brand
    def setnumofSeats(self,numofSeats):
        self.numOfSeats = numofSeats
    def accelerate(self):
        self.speed +=10
        return self.speed
    def decelerate(self):
        self.speed -=10
        return self.speed


my_motor = Motorcycle('red', 1.2,2, 'h-d', '1')

print(my_motor.accelerate())
print(my_motor.accelerate())
print(my_motor.accelerate())

bmw = Vehicle('white',3.0,4)
print(bmw.moveForward(5,5))
print(bmw.moveBackwards(6,6))
print(bmw.setColor('black'))
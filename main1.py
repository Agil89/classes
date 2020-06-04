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

    def moveForward(self,x,y):
        self.positionX = self.positionX + x
        self.positionY = self.positionY + y
    def moveBackwards(self,x,y):
        self.positionX = self.positionX - x
        self.positionY = self.positionY - y

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

    def __str__(self):
        print(str(f"""tekerlerin sayi:{self.numofWheels}
                  masinin rengi:{self.color}
                  matorun hecmi: {self.engine}
                  x pozisyon: {self.positionX}
                  y pozisyon:  {self.positionY}
                  speed : {self.speed}
                    """))




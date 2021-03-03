import random

class player:
    playerPos = 1
    isInPrison = False


class game:
    list <fieldXD> fields

class fieldXD:
    fieldNumber


class miasto(fieldXD):
    value
    cityName

    def setValues(self, cost, name):
        self.value = cost
        self.cityName = name

class blueChance(fieldXD):
    def randomizeBlue(this):
        case = random.randint(1, 16)

        if(case > 3):
            pass
        elif(case == 1):
            this.pozycjaGracza = 1
        elif(case == 2):
            this.pozycjaGracza = 40
        elif(case == 3):
            this.pozycjaGracza = 10
            this.isInPrison = True


class redChance(fieldXD):
    def randomizeRed(this):
        case = random.randint(1,16)

        if(case > 7):
            pass
        elif(case == 1):
            this.pozycjaGracza = ten.pozycjaGracza - 3
        elif(case == 2):
            this.pozycjaGracza = 1
        elif(case == 3):
            this.pozycjaGracza = 10
        elif(case == 4):
            this.pozycjaGracza = 36
        elif(case == 5):
            this.pozycjaGracza = 15
        elif(case == 6):
            this.pozycjaGracza = 24
        elif(case == 7):
            this.pozycjaGracza = 7

class cornerFields(fieldXD):
    def changePos(self, this):
        if(self.fieldNumber != 31):
            pass
        elif(self.fieldNumber == 31):
            this.playerPos = 10
            this.isInPrison = True
import random

def dice(this):
        a = random.randint(1,6)
        b = random.randint(1,6)
        Sum = a + b
        if (a == b):
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            Sum += a + b
            if (a == b):
                this.playerPos = 10
                this.isInPrison = True
                return Sum
        return Sum


class player:
    playerID
    playerPos = 1
    isInPrison = False
    cash = 3000
    map<int, fieldXD> properties

    def buyHouses(this):
        ifToBuy
        print("Do you want to buy any houses/hotels? y/n")
        ifToBuy = input("Enter y/n")
        if(ifToBuy == 'y'):
               var = input("Enter field number: ")
               if(owner[properties[var]] == this):
                   if(properties[var].numberOfHouses < 5):
                    this.cash - properties[var].houseCost
                    properties[var].numberOfHouses = properties[var].numberOfHouses + 1

        else:
               pass

    def move(this):

            


class game:
    map<int, player> players
    map<int, fieldXD> fields
    map<string, country> countries
    number = 0

    def setNumberOfPlayers():
        number = input("Set number of players")

    def setPlayerIDs(number):
        for x in range(1, number):
            new = player()
            new.playerID = x
            players[x] = new

class fieldXD:
    fieldNumber


class city(fieldXD):
    value
    cityName
    isBought = False    # indicates if field is bought
    numberOfHouses = 0  # hotel counts as 5
    map<city, player> owner   # field owner
    map<int, int> housePay # payment depends on how many houses there are
    houseCost   # each house cost       

    def payLoad(self, pay):
        pay = 0
        if(numberOfHouses == 0):
            pay = self.housePay[5]  # basic pay
        elif(numberOfHouses == 1):
            pay = self.housePay[0]  # one-house pay
        elif(numberOfHouses == 2):
            pay = self.housePay[1]  # two houses pay
        elif(numberOfHouses == 3):
            pay = self.housePay[2]  # three houses pay
        elif(numberOfHouses == 4):
            pay = self.housePay[3]  # four houses pay
        elif(numberOfHouses == 5):
            pay = self.housePay[4]

        return pay

    def setValues(self, cost, name, house1, house2, house3, house4, hotel, basicCost, houseCosts):
        self.value = cost
        self.cityName = name
        self.housePay[0] = house1
        self.housePay[1] = house2
        self.housePay[2] = house3
        self.housePay[3] = house4
        self.housePay[4] = hotel
        self.housePay[5] = basicCost
        self.houseCost = houseCosts
        
    def buyCity(self, this):
        if(self.isBought == False):
            print("Do you want to buy this field? y/n")
            wantToBuy = input()
            if(wantToBuy == 'y'):
                this.cash - self.value
        else:
            payment = payLoad(self, pay)
            if(this.cash > payment):
                this.cash = this.cash - payment
                owner[self].cash = owner[self].cash + payment

class country:
    countryName
    countrySize
    countrySide # array of cities in a country

    def setCities(here, city1, city2, city3):
        if(here.countrySize == 3):
            here.countrySide[0] = city1
            here.countrySide[1] = city2
            here.countrySide[2] = city3
        else:
            here.countrySide[0] = city1
            here.countrySide[1] = city2





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
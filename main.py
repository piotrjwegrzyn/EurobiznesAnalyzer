import random

class player:
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
                   this.cash 
        else:
               pass
            


class game:
    map<int, fieldXD> fields

class fieldXD:
    fieldNumber


class miasto(fieldXD):
    value
    cityName
    isBought = False    # indicates if field is bought
    numberOfHouses = 0  # hotel counts as 5
    map<miasto, player> owner   # field owner
    housePay[6] # payment depends on how many houses there are
    houseCost   # each house cost       

    def payLoad(self, pay):
        pay = 0
        if(numberOfHouses == 0):
            pay = self.housePay[5]
        elif(numberOfHouses == 1):
            pay = self.housePay[0]
        elif(numberOfHouses == 2):
            pay = self.housePay[1]
        elif(numberOfHouses == 3):
            pay = self.housePay[2]
        elif(numberOfHouses == 4):
            pay = self.housePay[3]
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
        
    def buyField(self, this):
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
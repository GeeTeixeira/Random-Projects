import random

'''Barber Shop
This program simulates a barber shop business, where customer's walk in at random times.
There are three different service speeds that are assigned to barbers.
In this barber shop there are only three barber's and each service customer's a different speeds.
The final stop is the Cashier's line. It holds the customer final information when they leave the shop.
Time is measured in minutes. Time conversion is done at the end of the day.
'''

'''barber class:
- holds information for the barber queue. This class will hold at most one customer at the time
- There are barber 1, 2, and 3. Barber 1 is faster, 2 is average, and 3 is slow. Time is randomly generated in respective functions in minutes.
'''
class barber:
    def __init__(self):
        self.customerIn = False
        self.currCustomer = 0
        self.serviceTime = 0
    def hasCustomer(self):
        return self.customerIn
    def serviceTimeBarber1(self):
        self.serviceTime = random.randint(10,20)
    def serviceTimeBarber2(self):
        self.serviceTime = random.randint(20,30)
    def serviceTimeBarber3(self):
        self.serviceTime = random.randint(30,40)
        
'''customer class:
- Each customer will be numbered starting at 1
- holds walk in and wait/service time (both are in minutes => 600 minutes = 10 hours)
- Holds what barber helped a particular customer
'''
class customer:
    def __init__(self):
        self.customerNum = 0
        self.waitTime = 0
        self.walkInTime = 0
        self.barber = 0
    def setCustomer(self,numb):
        self.customerNum = numb
    def getCustomer(self):
        return self.customerNum
    def addTime(self, time):
        self.waitTime+= time
    def getTime(self):
        return self.waitTime
    def setWalkIn(self, time):
        self.walkInTime = time
    def getWalkIn(self):
        return self.walkInTime
'''cashier class
- This class is the end of the process. Customers come to this queue once they are done with their service
- There is a wait time for this queue of 0-5 minutes
- All customers are stored in this queue after they "leave" the barber shop. printResult() provides the final information for each customer
'''
class cashier:
    def __init__(self):
        self.cashierLine = []
    def getFinalList(self):
        return self.cashier
    def appendCustomer(self, cust):
        self.time = random.randint(0,5)
        cust.waitTime+=self.time
        self.cashierLine.append(cust)
    def printResult(self, currTime):
        for i in self.cashierLine:
            print("Customer:", i.customerNum)
            print("Barber:",i.barber,"cut this customer's hair.")
            hours = int(i.waitTime/60)
            minutes = int(i.waitTime % 60)
            print("Waited: ",hours,"hours and ",minutes," minutes.",sep="")
            print()

'''main Function:
- This function accepts an integer to indicate how many customers will walk in through the door.
- Uses the barber, customer, and cashier classes to show the flow of customers throughout the day
'''
def main(customerNum):
    customerList = [] #list will be treated like a queue, and will hold all initial customers that are not at the barber shop
    counter = 1 #customer starting at 1
    walkIn = 510 #Barber shop opens at 8:30am = 510 minutes
    #This while loop generate the walk in times for each customer with an interval of 1-10 minutes in between each customer
    while(counter<=customerNum):
        
        a = customer()
        a.setCustomer(counter)
        a.setWalkIn(walkIn)
        
        customerList.append(a)
        
        counter+=1
        walkIn+=random.randint(1,10)
        
    couch = [] #This is a queue for the line inside the barber shop
    '''
    Instance of barber class for each barber at the barber shop
    Each of these barbers will use their respective functions for generating the service time (e.g. serviceTimeBarber1, etc.)
    '''
    barber1 = barber() 
    barber2 = barber()
    barber3 = barber()

    #final queue of customers
    cash = cashier()

    #starting the day at the barber shop
    currTime = 510
    print("Barber shop opened at: %d:%d o'clock." %((int(510/60)),(510%60)))
    #This loop will run while there are still customers to walk in and if there are customers waiting in the lobby (couch)
    while(len(customerList)>0 or len(couch)>0):
        #Checks if the current day time matches the walk in time for the next customer in the customer list
        #if it matches, then customer will "walk-in" the barber shop and go to the couch queue
        if(len(customerList)>0 and customerList[0].walkInTime == currTime):
            couch.append(customerList.pop(0))
        #The next three if statements check if barber1, 2, or 3 have customers
        #if any of them are free, then the next customer will sit in the barber's chair for service
        #first if statement provides a general explanation of what is being done
        if(not(barber1.hasCustomer()) and len(couch)>0):
            #if barber 1 has no customers and there is customer waiting - do the following
            barber1.serviceTimeBarber1() #generate random time for barber 1 service
            barber1.currCustomer = couch.pop(0) # remove customer from couch and put it on the barber
            barber1.customerIn = True # barber 1 has a customer
            barber1.currCustomer.addTime(currTime-barber1.currCustomer.walkInTime+barber1.serviceTime)
            #add the wait time (current time minus the walk in time) for customer to the service time to the barber
            barber1.currCustomer.barber = 1
        if(not(barber2.hasCustomer()) and len(couch)>0):
            barber2.serviceTimeBarber2()
            barber2.currCustomer = couch.pop(0)
            barber2.customerIn = True
            barber2.currCustomer.addTime(currTime-barber2.currCustomer.walkInTime+barber2.serviceTime)
            barber2.currCustomer.barber = 2
        if(not(barber3.hasCustomer()) and len(couch)>0):
            barber3.serviceTimeBarber3()
            barber3.currCustomer = couch.pop(0)
            barber3.customerIn = True
            barber3.currCustomer.addTime(currTime-barber3.currCustomer.walkInTime+barber3.serviceTime)
            barber3.currCustomer.barber = 3

        #The next 3 if statements check if a barber finished helping a customer and moves the customer to the cashier's queue
        #the first if statement provides general explanation of what is being done
            
        if(barber1.currCustomer != 0): # This means that the barber currently has a customer
            if(barber1.currCustomer.waitTime+barber1.currCustomer.walkInTime == currTime): #if the current time matches the customer walk in time + service time (means that service was completed)
                cash.appendCustomer(barber1.currCustomer) #move customer at barber object to cashier queue
                barber1.currCustomer = 0 #set current customer to 0
                barber1.customerIn = False #set barber as available
        
        if(barber2.currCustomer != 0):
            if(barber2.currCustomer.waitTime+barber2.currCustomer.walkInTime == currTime):
                cash.appendCustomer(barber2.currCustomer)
                barber2.currCustomer = 0
                barber2.customerIn = False
        
        if(barber3.currCustomer != 0):
            if(barber3.currCustomer.waitTime + barber3.currCustomer.walkInTime == currTime):
                cash.appendCustomer(barber3.currCustomer)
                barber3.currCustomer = 0
                barber3.customerIn = False
        currTime+=1
    '''
    Main will reach these three if statements once there are no more customers on customerList or lobby(couch)
    Move remaining customers at barber's chair to the chair
    '''
    if(barber1.hasCustomer and barber1.currCustomer != 0):
        barber1.currCustomer.barber = 1
        cash.appendCustomer(barber1.currCustomer)
        barber1.currCustomer = 0
    if(barber2.hasCustomer and barber2.currCustomer != 0):
        barber2.currCustomer.barber = 2
        cash.appendCustomer(barber2.currCustomer)
        barber2.currCustomer = 0
    if(barber3.hasCustomer and barber3.currCustomer != 0):
        barber3.currCustomer.barber = 3
        cash.appendCustomer(barber3.currCustomer)
        barber3.currCustomer = 0

    #print resulting wait+service time for all customers
    cash.printResult(currTime)
    minutes = str(currTime%60)
    if(len(minutes) == 1): #to add proper minute format if there is less than 10 minutes
        minutes = "0"+minutes
    print("%d customers were helped and it is currently %d:%s o'clock." %((customerNum),(int(currTime/60)), minutes))


    

class TicketScenarios:

    # initializing the person / scenario
    def __init__ (self, speed, speedLimit, gender, age, isBirthday, monthsSinceLastTicket, didRunLight):
        self._speed = speed
        self._speedLimit = speedLimit
        self._gender = gender
        self._age = age
        self._isBirthday = isBirthday
        self._monthsSinceLastTicket = monthsSinceLastTicket
        self._didRunLight = didRunLight

    # find the excess speed
    def getExtraSpeed (self):
        extraSpeed = self._speed - self._speedLimit
        return extraSpeed

    # dictionary of possible outcomes
    outcomeDictionary = {0 : "No Ticket",
                         1 : "Warning"  ,
                         2 : "Citation" ,
                         3 : "Get Out of Jail"}

    # get the traffic stop scenario value
    def getScenarioValue (self, extraSpeed):
        outcomeDict = 0
        
        if (self._gender == "Female" and self._age > 50 and self._isBirthday == True) or (self._gender == "Male" and self._age > 60 and self._monthsSinceLastTicket > 3):
            outcomeDict = 3
        elif (extraSpeed > 5 and extraSpeed < 10 and self._didRunLight == False):
            outcomeDict = 1
        elif (extraSpeed > 10 or self._didRunLight == True):
            outcomeDict = 2
        
        return outcomeDict

    # return the outcome from the traffic stop
    def outcome (self):
        extraSpeed = self.getExtraSpeed()
        dictValue = self.getScenarioValue(extraSpeed)
        outcome = self.outcomeDictionary[dictValue]
        return outcome


# speed under 5 over
personOne = TicketScenarios (speed = 43, speedLimit = 40, gender = "Female", 
                             age = 34, isBirthday = True, monthsSinceLastTicket = 5, 
                             didRunLight = False)
print(personOne.outcome())
print()

# speed between 5 and 10 over
personTwo = TicketScenarios (speed = 46, speedLimit = 40, gender = "Female", 
                             age = 34, isBirthday = True, monthsSinceLastTicket = 5, 
                             didRunLight = False)
print(personTwo.outcome())
print()

# speed over 10
personThree = TicketScenarios (speed = 61, speedLimit = 40, gender = "Female", 
                               age = 34, isBirthday = True, monthsSinceLastTicket = 5, 
                               didRunLight = False)
print(personThree.outcome())
print()

# did run light
personFour = TicketScenarios (speed = 47, speedLimit = 40, gender = "Female", 
                              age = 34, isBirthday = True, monthsSinceLastTicket = 5, 
                              didRunLight = True)
print(personFour.outcome())
print()

# female over 50 on her birthday
personFive = TicketScenarios (speed = 47, speedLimit = 40, gender = "Female", 
                              age = 52, isBirthday = True, monthsSinceLastTicket = 5, 
                              didRunLight = True)
print(personFive.outcome())
print()

# male over 60 with no previous tickets in last 3 consecutive months
personSix = TicketScenarios (speed = 47, speedLimit = 40, gender = "Female", 
                             age = 63, isBirthday = True, monthsSinceLastTicket = 5, 
                             didRunLight = True)
print(personSix.outcome())

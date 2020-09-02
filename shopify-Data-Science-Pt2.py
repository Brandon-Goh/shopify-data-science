#By: Brandon Goh
#Date: Sept 1, 2020
import csv
global purchaseAmountErrors

#Object for each purchase. In case other things are needed to be caulcuated it's better to use OOP
class PurchaseInstance:

    def __init__(self, orderID, shopID, userID, orderAmount, totalItems, paymentMethod,timestamp):
        self._orderID = orderID  # int
        self._shopID = shopID  # int
        self._userID = userID  # int
        self._orderAmount = orderAmount  # int
        self._totalItems = totalItems  # int
        self._paymentMethod = paymentMethod  # string
        self._timestamp = timestamp  # int

#Check if the order ID appears twice. If so, don't count it and make sure user knows there is an issue.
def errorOrderID(purchase,orderIDs):
    if(len(orderIDs) != len(set(orderIDs))):
        print("Error: The order ID of: " + purchase._orderID + "appears twice. Please check data.")
        return True
    return False

#Check if the purchase is over $300/sneaker. If so, add it to the error list and don't include it.
def errorTotalItems(purchase):
    if((int(purchase._orderAmount) / int(purchase._totalItems)) > 300):
        global purchaseAmountErrors
        purchaseAmountErrors += purchase._orderID + " , "
        return True
    return False

#Check if everything is valid and return the order amount of the purchase.
def orderAmountSum(purchase,orderIDs, orderSum):
    if(errorOrderID(purchase,orderIDs) == False and errorTotalItems(purchase) == False):
        return int(purchase._orderAmount)
    return 0

#Returns the AOV amount, rounded to 2 decimal places.
def avgOrderValueCalc(orders,orderSum):
    return round((orderSum/orders),2)

#Function that inputs the file and calls most of the functions for calculations/validity in data.
def fileInput(fileName):
    #Read in data from CSV
    with open(fileName, "r", encoding="utf-8") as dataSet:
        dataSet.readline()
        reader = csv.reader(dataSet)
        #Keeps track of order IDs, used for checking if there are duplicates.
        orderIDs = []
        #Total order sum
        orderSum = 0
        #Number of orders
        orders = 0
        for line in reader:
            orderID = line[0].strip()
            shopID = line[1].strip()
            userID = line[2].strip()
            orderAmount = line[3].strip()
            totalItems = line[4].strip()
            paymentMethod = line[5].strip()
            timestamp = line[6].strip()
            #Creates an instance of PurchaseInstance class
            purchase = PurchaseInstance(orderID, shopID, userID, orderAmount, totalItems, paymentMethod,timestamp)
            #Adds ID to list
            orderIDs.append(purchase._orderID)
            #Checks if everything is good, if value of 0 then don't add +1 orders or add to orderSum
            orderChecker = orderAmountSum(purchase,orderIDs,orderSum)
            if(orderChecker != 0):
                orderSum += orderChecker
                orders += 1
    #Returns AOV amount
    return avgOrderValueCalc(orders, orderSum)



if __name__ == '__main__':
    purchaseAmountErrors = "It seems like the order amount is unusually high from order IDs of:  "
    aov = fileInput("data.csv")
    print(purchaseAmountErrors)
    print("A more accurate average order value is $"+ str(aov))
'''
OUTPUT
--------------------


It seems like the order amount is unusually high from order IDs of:  16 , 41 , 61 , 161 , 309 , 410 , 491 , 494 , 512 , 521 , 618 , 692 , 835 , 836 , 939 , 980 , 1057 , 1105 , 1194 , 1205 , 1260 , 1363 , 1365 , 1368 , 1385 , 1420 , 1437 , 1453 , 1472 , 1513 , 1521 , 1530 , 1563 , 1603 , 1912 , 1930 , 2004 , 2019 , 2054 , 2154 , 2271 , 2274 , 2298 , 2453 , 2492 , 2493 , 2496 , 2513 , 2549 , 2565 , 2610 , 2691 , 2767 , 2774 , 2819 , 2822 , 2836 , 2907 , 2923 , 2970 , 2988 , 3086 , 3102 , 3152 , 3168 , 3333 , 3404 , 3441 , 3514 , 3652 , 3698 , 3706 , 3725 , 3781 , 3904 , 3999 , 4041 , 4057 , 4080 , 4193 , 4232 , 4295 , 4312 , 4327 , 4413 , 4421 , 4422 , 4506 , 4585 , 4626 , 4647 , 4716 , 4746 , 4768 , 4869 , 4883 , 4919 ,
A more accurate average order value is $300.16

Process finished with exit code 0



'''

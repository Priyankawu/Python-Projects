from abc import ABC, abstractmethod

class car(ABC): #ABC is the parent
    def paySlip(self,amount):
        print("Your purchase amount: ",amount)
        @abstractmethod
        def payment(self,amount):
            pass
####################################################

class DebitCardPayment(car): #car is the payment
    def payment(self,amount): #need to override the abstract parent class
        print("Your purchase amount of {} exceeded your @100 limit ".format(amount))
####################################################

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
####################################################

    

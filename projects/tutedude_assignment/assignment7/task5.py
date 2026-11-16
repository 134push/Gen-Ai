from abc import ABC,abstractmethod 

class payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class creditcardpayment(payment):
    def process_payment(self):
        print("you choose credit card payment method  :")

class upipayment(payment):    
    def process_payment(self):
        print("you choose upi payment method  :")

method1 = creditcardpayment()
method2 = upipayment()

method1.process_payment()
method2.process_payment()

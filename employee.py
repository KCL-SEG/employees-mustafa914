



class Salary:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        self.commission = 0


    def get_pay(self):
            return self.pay


        

    
    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.pay}. Their total pay is {self.pay}$")


class Contractor(Salary):
    def __init__(self, name, pay, hour_rate, hours):
        super().__init__(name, pay)
        self.hour_rate = hour_rate
        self.hours = hours
        self.commission = 0

    def get_pay(self):
        self.pay = self.hours * self.hour_rate 
        return self.pay
     
    
    def __str__(self):
        return(f"{self.name} works on a contract of {self.hours} hours at {self.hour_rate}/hour. Their total pay is {self.pay}$")

class SalaryBonus(Salary):
    def __init__(self, name, pay, commission):
        super().__init__(name, pay)
        self.commission = commission
        
    
    def get_pay(self):
        self.original_pay = self.pay
        self.pay = self.original_pay + self.commission
        return self.pay

    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.original_pay} and receives a bonus commission of {self.commission}. Their total pay is {self.pay}$")

    
        

class ContractorBonus(Contractor):
    def __init__(self, name, pay, hour_rate, hours, commission):
        super().__init__(name, pay, hour_rate, hours)
        self.commission = commission

    def get_pay(self):
        super().get_pay()
        self.pay = self.pay + self.commission
        return self.pay
        

    def __str__(self):
        return(f"{self.name} works on a contract of {self.hours} hours at {self.hour_rate}/hour and receives a bonus commission of {self.commission}. Their total pay is {self.pay}$")
        
class SalaryComm(Salary):
    def __init__(self, name, pay, contracts_num, contract_rate):
        super().__init__(name, pay) 
        self.contracts_num = contracts_num
        self.contract_rate = contract_rate
        self.commission = self.contract_rate * self.contracts_num
        self.pay = self.pay + self.commission

    def get_pay(self):
        super().get_pay()
        
        return self.pay

    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.pay - self.commission} and receives a commission for {self.contracts_num} contract(s) at {self.contract_rate}/contract. Their total pay is {self.pay}$")
        
class ContractorComm(Contractor):
    def __init__(self, name, pay, hour_rate, hours, comm_num, comm_rate):
        super().__init__(name, pay, hour_rate, hours)
        self.comm_num = comm_num
        self.comm_rate = comm_rate
    
    def get_pay(self):
        super().get_pay()
        self.commission = self.comm_num * self.comm_rate
        self.pay = self.pay + self.commission
        return self.pay

    def __str__(self):
        return (f"{self.name} works on a contract of {self.hours} hours at {self.hour_rate}/hour and receives a commission for {self.comm_num} contract(s) at {self.comm_rate}/contract. Their total pay is {self.pay}$.")

        

        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary('Billie', 4000)
billie.get_pay()




# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Contractor('Charlie', 0, 25, 100)
charlie.get_pay()





# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryComm('Renee', 3000, 4, 200)
renee.get_pay()


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractorComm('Jan', 0, 25, 150, 3, 220)
jan.get_pay()


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryBonus('Robbie', 2000, 1500)
#print(str(robbie))


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractorBonus('Ariel', 0, 30, 120, 600)
ariel.get_pay()


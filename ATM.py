
class Atm (object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def CashWithdrawl(self):
        print("CashWithdrawl")

    def BalanceEnquiry (self):
        print("BalanceEnquiry ")

    
bank=Atm("axis","cardnumber","pinnumber")



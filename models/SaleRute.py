class SaleRute(object):

    def __init__(self,code_rute:str,flight:str,base_price:float,economic_price:float,premium_price:float):
        self.code_rute = code_rute
        self.flight = flight
        self.base_price = base_price
        self.economic_price = economic_price
        self.premium_price = premium_price
    
    def __str__(self) -> str:
        return "Ticket: " + self.code_rute + " " + str(self.base_price) + " " + str(self.economic_price) + " " + str(self.premium_price)
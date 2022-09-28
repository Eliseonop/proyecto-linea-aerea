
class Ticket(object):

    def __init__(self,code_rute:str,price_base:float,ticket_economic:float,ticket_primium:float):
        self.code_rute = code_rute
        self.price_base = price_base
        self.ticket_economic = ticket_economic
        self.ticket_primium = ticket_primium

    def __str__(self) -> str:
        return "Ticket: " + self.code_rute + " " + str(self.price_base) + " " + str(self.ticket_economic) + " " + str(self.ticket_primium)
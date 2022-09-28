from datetime import time
import random


class Travel(object):

    def __init__(self,origin:str,destination:str,deaperture_time:time,flight:str,min_sales_economic:int,max_sales_economic:int,min_sales_premium:int,max_sales_premium:int):
        self.origin = origin
        self.destination = destination
        self.name = origin.capitalize() + " - " + destination.capitalize()
        self.code_rute =  origin[0:3] + "-" + destination[0:3]
        self.flight = flight
        self.departure_time = deaperture_time
        self.min_sales_economic = min_sales_economic
        self.max_sales_economic = max_sales_economic
        self.min_sales_premium = min_sales_premium
        self.max_sales_premium = max_sales_premium

    def __str__(self) -> str:
        information = "Origen: " + self.origin + " Destino: " + self.destination + " Vuelo: " + self.flight + " Hora de salida: " + self.departure_time.strftime("%H:%M")
        return information
    
    def get_rand_sales_economic(self) -> int:
        return random.randint(self.min_sales_economic,self.max_sales_economic)
    
    def get_rand_sales_premium(self) -> int:
        return random.randint(self.min_sales_premium,self.max_sales_premium)
    
    def get_code_rute(self) -> str:
        return self.code_rute
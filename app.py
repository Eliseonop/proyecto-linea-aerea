import random
from models.SaleRute import SaleRute
from models.Ticket import Ticket
from models.Travel import Travel
from typing import Dict, List
from datetime import time

def create_list_travel() -> List[Travel]:
    data_travel:List[Dict[str,str |int  |time]] = [
        {
            "origin": "LIMA",
            "destination": "AYACUCHO",
            "min_sales_economic": 120,
            "max_sales_economic": 130,
            "min_sales_premium": 10,
            "max_sales_premium": 20,
            "flight": "A001",
            "departure_time": time(6, 30),
        },
        {
            "origin": "LIMA",
            "destination": "CUSCO",
            "min_sales_economic": 130,
            "max_sales_economic": 144,
            "min_sales_premium": 15,
            "max_sales_premium": 24,
            "flight": "A002",
            "departure_time": time(7, 25),
        },
        {
            "origin": "LIMA",
            "destination": "AREQUIPA",
            "min_sales_economic": 115,
            "max_sales_economic": 138,
            "min_sales_premium": 16,
            "max_sales_premium": 22,
            "flight": "A003",
            "departure_time": time(8, 10),
        },
        {
            "origin": "AYACUCHO",
            "destination": "LIMA",
            "min_sales_economic": 100,
            "max_sales_economic": 115,
            "min_sales_premium": 10,
            "max_sales_premium": 15,
            "flight": "A001",
            "departure_time": time(15, 45),
        },
          {
            "origin": "CUSCO",
            "destination": "LIMA",
            "min_sales_economic": 105,
            "max_sales_economic": 120,
            "min_sales_premium": 14,
            "max_sales_premium": 20,
            "flight": "A002",
            "departure_time": time(16, 25),
        },
        {
            "origin": "AREQUIPA",
            "destination": "LIMA",
            "min_sales_economic": 100,
            "max_sales_economic": 110,
            "min_sales_premium": 13,
            "max_sales_premium": 18,
            "flight": "A003",
            "departure_time": time(17, 15),
        },
        {
            "origin": "TARAPOTO",
            "destination": "LIMA",
            "min_sales_economic": 90,
            "max_sales_economic": 105,
            "min_sales_premium": 10,
            "max_sales_premium": 15,
            "flight": "A004",
            "departure_time": time(17, 50),
        },]
    
    list_travel:List[Travel] = []
    for key, travel in enumerate(data_travel):
        obj_ticket = Travel( travel["origin"], travel["destination"], travel["departure_time"], travel["flight"], travel["min_sales_economic"], travel["max_sales_economic"], travel["min_sales_premium"], travel["max_sales_premium"])
        list_travel.append(obj_ticket)
    return list_travel

# def Generate_list_tickets_economic() -> List[Ticket]:
#     mylist = create_list_travel()
#     list_tickets_economic:List[Ticket] = []
#     for mytravel in mylist:
#         for i in range(mytravel.min_sales_economic, mytravel.max_sales_economic):
#             obj_ticket = Ticket(mytravel.code_rute, mytravel.flight, "ECONOMIC", mytravel.departure_time)
#             list_tickets_economic.append(obj_ticket)
#     return list_tickets_economic

def Generate_Sale_Rute() -> List[SaleRute]:
   

    data_sale:List[Dict[str,str |int  |time]] = [
        {
            "code_rute": "LIM-AYA",
            "flight": "A001",
            "base_price": 55.19,
            "economic_price": 8.00,
            "premium_price": 16.00,
        },
        {
            "code_rute": "LIM-CUS",
            "flight": "A002",
            "base_price": 136.51,
            "economic_price": 8.00,
            "premium_price": 16.00,
        },
        {
            "code_rute": "LIM-ARE",
            "flight": "A003",
            "base_price": 90.59,
            "economic_price": 8.00,
            "premium_price": 16.00,
        },
        {
            "code_rute": "LIM-TAR",
            "flight": "A004",
            "base_price": 72.89,
            "economic_price": 8.00,
            "premium_price": 16.00,
        },
        {
            "code_rute": "AYA-LIM",
            "flight": "A001",
            "base_price": 40.42,
            "economic_price": 7.00,
            "premium_price": 16.00,
        },
        {
            "code_rute": "CUS-LIM",
            "flight": "A002",
            "base_price": 124.32,
            "economic_price": 7.00,
            "premium_price": 16.00,
        },
        {
            "code_rute": "ARE-LIM",
            "flight": "A003",
            "base_price": 86.59,
            "economic_price": 7.00,
            "premium_price": 16.00,
        },
        {
            "code_rute": "TAR-LIM",
            "flight": "A004",
            "base_price": 68.42,
            "economic_price": 7.00,
            "premium_price": 16.00,
        }        
    ]
    list_sale_rute:List[SaleRute] = []
    
    for key, sale in enumerate(data_sale):
        obj_sale_rute = SaleRute(str(sale["code_rute"]), str(sale["flight"]), float(sale["base_price"]), float(sale["economic_price"]), float(sale["premium_price"]))
        list_sale_rute.append(obj_sale_rute)
   
    return list_sale_rute


def create_list_Tickets_economic(list_sale_rute:List[SaleRute],list_travel:List[Travel]) -> List[Ticket]:
    for k,travel in list_travel:
        rand_economic_Ticket = random.sample(travel["min_sales_economic"], travel["max_sales_economic"])
        flight = travel["flight"]
        deaperture_time = travel["departure_time"]
        code_rute = travel.get_code_rute()


def main():
    list_travel = create_list_travel()
    list_sale_rute = Generate_Sale_Rute()
    list_tickets = create_list_Tickets_economic(list_sale_rute, list_travel)
    for mytravel in list_tickets:
        print(mytravel)

if __name__ == "__main__":
    main()
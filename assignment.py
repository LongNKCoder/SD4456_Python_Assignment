from typing import Dict
from ticket import Ticket
from datetime import datetime
import json


def park() -> None:
    with open("database.json","r") as file:
        database: dict = json.load(file)
        arrival_time: datetime = datetime.now()
    while True:
        id_car: str = input("Vui long nhap ma so xe (bat buoc): ")
        if id_car:
            break
    park_number: str = input("Vui long nhap noi do xe (Khong bat buoc): ")
    ticket: Ticket = Ticket(arrival_time=datetime.strftime(arrival_time, "%Y-%m-%d %H:%M"), id_car=id_car, park_number=park_number)
    data: Dict = {ticket.id_car:ticket.__dict__}
    database.update(data)
    with open("database.json","w") as file:
        file.write(json.dumps(database, indent=4))
    return None


def history():
    print("On Developing, too many things to build.")
    return None


def checkout_car(id_car: str) -> float:
    weekday_dict: dict = {
        0:{"price":2, "max": 8},
        1:{"price":10, "max": 2},
        2:{"price":10, "max": 2},
        3:{"price":10, "max": 2},
        4:{"price":10, "max": 2},
        5:{"price":10, "max": 2},
        6:{"price":3, "max": 4},
    }
    with open("database.json", "r") as file:
        database: Dict = json.load(file)
    ticket: dict = database.get(id_car)
    if not ticket:
        raise Exception("Xe nay khong duoc dau o day")
    arrival_day: datetime = datetime.strptime(ticket.get("arrival_time"), "%Y-%m-%d %H:%M")
    charge_time: float = round((datetime.now() - arrival_day).total_seconds()/3600, 2)
    weekday: dict = weekday_dict.get(arrival_day.weekday())
    if arrival_day.hour >= 0 and arrival_day.hour <= 7:
        price: float = 20.00
    elif arrival_day.hour >= 8 and arrival_day.hour <= 16:
        if charge_time < weekday.get("max"):
            overcharge: int = 0
        else:
            overcharge: float = (charge_time - weekday.get("max")) * 2 * weekday.get("price")
        price: float = weekday.get("price") * charge_time + overcharge
    elif arrival_day.hour >= 17 and arrival_day.hour <= 23:
        price: float = 5 * charge_time
    return price


def pick_up() -> None:
    while True:
        id_car = input("Nhap id xe cua ban vao:")
        if id_car:
            break
    price = checkout_car(id_car)
    print(f"Ban phai tra: {price}")
    while True:
        try:
            amount = float(input("Nhap so tien ban muon tra: "))
            if amount < price:
                print("So tien qua it xin nhap lai")
            else:
                print(f"Tra lai ban so tien {amount - price}")
                break
        except Exception:
            print("nhap sai roi nhap lai")
    return None


def select_options(option: int) -> None:
    option_dict: dict = {"1":park, "2":pick_up, "3":history}
    return option_dict[option]()



if __name__ == "__main__":
    print("This is parking system. Please choose options:")
    print("1. Park")
    print("2. Pick up")
    print("3. History")
    select_options(input("Moi ban nhap vao: "))

from modulus11 import mod11


class Ticket():
    def __init__(self, **kwargs) -> None:
        self.arrival_time: str = kwargs.get("arrival_time")
        self.id_car: str = kwargs.get("id_car")
        try:
            mod11.calc_check_digit(kwargs.get("park_number"))
            self.park_number:int = kwargs.get("park_number") or "Unknow"
        except Exception:
            self.park_number: str = "Unknown"

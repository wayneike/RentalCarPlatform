from datetime import datetime
import Vehicle as v

class RentalCar(v.Vehicle):
    def __init__(self, make, model, year, hourly_rate, daily_rate, weekly_rate, total_quantity):
        v.Vehicle.__init__(self, make, model, year)
        self._hourly_rate = hourly_rate
        self._daily_rate = daily_rate
        self._weekly_rate = weekly_rate
        self._total_quantity = total_quantity
        self.init_rental()

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @property
    def daily_rate(self):
        return self._daily_rate

    @property
    def weekly_rate(self):
        return self._weekly_rate
    
    @property
    def total_quantity(self):
        return self._total_quantity

    @property
    def rental_start_time(self):
        return self._rental_start_time
    
    @property
    def rental_mode(self):
        return self._rental_mode

    def start_rental(self, mode):
        self._rental_start_time = datetime.now()
        self._rental_mode = mode

    def init_rental(self):
        self._rental_start_time = None
        self._rental_mode = None
        self.available_quantity = self.total_quantity
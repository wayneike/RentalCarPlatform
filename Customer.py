import Person as p

class Customer(p.Person):
    def request_car(self, rental_system, car_id, rental_period, quantity):
        rental_system.rent_car(car_id, rental_period, quantity)

    def return_car(self, rental_system, car_id):
        rental_system.return_car(car_id)
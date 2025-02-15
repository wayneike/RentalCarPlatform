from datetime import datetime
import RentalCar as c

class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.cars.append(c.RentalCar("Chevrolet", "Corvette", 2023, 50, 200, 1000, 2))
        self.cars.append(c.RentalCar("Ford", "Mustang", 2021, 20, 100, 400, 2))
        self.cars.append(c.RentalCar("Honda", "Civic", 2019, 12, 60, 220, 3))
        self.cars.append(c.RentalCar("Toyota", "Prius", 2020, 10, 50, 200, 5))

    def display_inventory(self):
        print("Available Cars for Rental:")
        for i, car in enumerate(self.cars, 1):
            print(f"{i}. {car.make} {car.model} ({car.year}) - Available Quantity: {car.available_quantity}")

    def car_exists(self, car_id):
        x = len(self.cars) >= car_id and car_id > 0
        if not x:
            print(f"\nCar ID: {car_id} is not available")
        return x

    def rent_car(self, car_id, rental_period, quantity):      
        if not self.car_exists(car_id):
            return

        car_id -= 1 #compensate for enumerate(x, 1) in display_inventory   
        car = self.cars[car_id]
        if car.available_quantity >= quantity:
            car.available_quantity -= quantity      
            if rental_period == "hourly" or "1":
                bill_amount = car.hourly_rate * quantity
            elif rental_period == "daily" or "2":
                bill_amount = car.daily_rate * quantity
            elif rental_period == "weekly" or "3":
                bill_amount = car.weekly_rate * quantity
            else:
                print("Invalid rental period!")
                return
            car.start_rental(mode = rental_period)
            print(f"You have successfully rented {quantity} {car.make} {car.model}(s) for {rental_period} rental period.")
            print(f"Please pay: ${bill_amount}")
        else:
            print("Not available")

    def return_car(self, car_id):
        if not self.car_exists(car_id):
            return
            
        car_id -= 1 #compensate for enumerate(x, 1) in display_inventory   
        car = self.cars[car_id]
        rental_mode = car.rental_mode
        if rental_mode is None:
            print("You did not rent this car")
            return
            
        rental_end_time = datetime.now()
        rental_duration_hours = (rental_end_time - car.rental_start_time).total_seconds() / 3600
        quantity = car.total_quantity - car.available_quantity

        if rental_mode == "hourly" or "1":
            rental_period = rental_duration_hours
            bill_amount = car.hourly_rate * rental_period * quantity
        elif rental_mode == "daily" or "2":
            rental_period = rental_duration_hours / 24
            bill_amount = car.daily_rate * rental_period * quantity
        elif rental_mode == "weekly" or "3":
            rental_period = rental_duration_hours / (24 * 7)
            bill_amount = car.weekly_rate * rental_period * quantity
        else:
            print("Invalid rental mode!")
            return

        car.init_rental()
        print(f"Thank you for returning {quantity} {car.make} {car.model}(s). Your bill amount is: ${bill_amount}")

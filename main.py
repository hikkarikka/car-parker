class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: str):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
    
class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, "Car")


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, "Motorcycle")


class ParkingLot:
    def __init__(self, car_spots: int, motorcycle_spots: int):
        self.car_spots = car_spots
        self.motorcycle_spots = motorcycle_spots
        self.parked_vehicles = []
        self.free_carspots = car_spots
        self.free_motorcyclespots = motorcycle_spots

    def park_vehicle(self, vehicle: Vehicle):
        if vehicle.vehicle_type == "Car":
            if self.free_carspots > 0:
                self.free_carspots -= 1
                self.parked_vehicles.append((vehicle, "car"))
                return f"машина с номером {vehicle.license_plate} успешно припаркована"
            else:
                return f"на парковке нет мест"
        elif vehicle.vehicle_type == "Motorcycle":
            if self.free_motorcyclespots > 0:
                self.free_motorcyclespots -= 1
                self.parked_vehicles.append((vehicle, "motorcycle"))
                return f"мотоцикл с номером {vehicle.license_plate} успешно припаркован на место мотоцикла"
            elif self.free_carspots > 0:
                self.free_carspots -= 1
                self.parked_vehicles.append((vehicle, "car"))
                return f"мотоцикл с номером {vehicle.license_plate} успешно припаркован на место машины"
            else:
                return f"нет свободных мест для машин и мотоциклов"
            

    def remove_vehicle(self, license_plate: str):
        for i, (vehicle, spot_type) in enumerate(self.parked_vehicles):
            if vehicle.license_plate == license_plate:
                if spot_type == "car":
                    self.free_carspots += 1
                else:
                    self.free_motorcyclespots += 1
                self.parked_vehicles.pop(i)
                return f"транспорт с номером {license_plate} был удален"
        return "транспорт не найден"
            
    def get_parked_vehicles(self):
        if not self.parked_vehicles:
            return "парковка пустая"
        spot =[]
        for vehicle, spot_type in self.parked_vehicles:
            spot.append(f"тип: {vehicle.vehicle_type}, номер: {vehicle.license_plate}, место: {spot_type}")
        return "\n".join(spot)


def main():
    parking = ParkingLot(5,7)
    vehicles = [Car("123aaa"), Car("456vvv"), Car("789ccc"), Car("321ddd"), Motorcycle("1209"), Motorcycle("3487"), Motorcycle("5676")]
    for vehicle in vehicles:
        print(parking.park_vehicle(vehicle))
    print(parking.get_parked_vehicles())

if __name__ == "___main___":
    main()

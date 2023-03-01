if __name__=="__main__":
    cars = 100 
    space_in_car = 4.0
    drivers = 30
    passengers = 90 
    cars_not_driven = cars - drivers 
    cars_driven = drivers
    carpool_capacity = cars_driven * space_in_car
    average_passangers_per_car = carpool_capacity / cars_driven

    print("Number of cars: ", cars)
    print("Number of cars driven: ", cars_driven)
    print("Number of cars not driven:", cars_not_driven)
    print("Carpool capacity: ", carpool_capacity)
    print("Average passangers per car:", average_passangers_per_car)

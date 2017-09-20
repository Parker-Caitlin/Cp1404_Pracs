from car import Car

def main():
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("limo fuel =", limo.fuel)
    limo.drive(115)
    print("limo odo =", limo.odometer)
    print(limo)

main()
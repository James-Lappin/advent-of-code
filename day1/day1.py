import math


def calculate_fuel_required(mass):
    return math.floor(mass / 3) - 2


def calculate_fuel_required_for_fuel(total):
    result = total
    fuel_cost = calculate_fuel_required(total)
    while fuel_cost > 0:
        result = result + fuel_cost
        fuel_cost = calculate_fuel_required(fuel_cost)

    return result


def calculate_fuel_required_for_module(mass):
    fuel = calculate_fuel_required(mass)
    return calculate_fuel_required_for_fuel(fuel)


def main():
    total = 0
    with open('input.txt') as f:
        for line in f:
            total = total + calculate_fuel_required_for_module(int(line))

    print(total)


# 5085852
# 5083024
if __name__ == "__main__":
    main()

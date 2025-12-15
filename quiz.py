#Question 1
inventory = {
    "Tomatoes": {"stock": 150, "price_per_unit": 5.0},
    "Onions": {"stock": 150, "price_per_unit": 3.5},
    "Garden Eggs": {"stock": 200, "price_per_unit": 1.0}
}

transactions = 0
print(inventory)

while True:
    item = input("Enter item to purchase (Tomatoes, Onions, Garden Eggs) or exit: ").title()

    if item == "Exit":
        print("Closing sales. Total transactions completed.")
        break

    if item not in inventory:
        print("Item not found in stock. Check spelling.")
        continue

    quantity = int(input("Enter quantity to buy: "))

    if quantity > inventory[item]["stock"]:
        print(f"Sorry, only {inventory[item]['stock']} units of {item} remaining.")
    else:
        total_cost = quantity * inventory[item]["price_per_unit"]
        inventory[item]["stock"] -= quantity
        transactions += 1
        print(
            f"Sale successful! Cost: GHS {round(total_cost, 2)}. "
            f"{inventory[item]['stock']} units of {item} remaining."
        )

#Question 2 
consumption = float(input("Enter total water consumption for the month (in cubic meters): "))

service_charge = 15.00
consumption_cost = 0.0

if consumption <= 15:
    consumption_cost = consumption * 0.90
elif consumption <= 30:
    consumption_cost = (15 * 0.90) + ((consumption - 15) * 1.20)
else:
    consumption_cost = (15 * 0.90) + (15 * 1.20) + ((consumption - 30) * 1.80)

total_bill = service_charge + consumption_cost

print("\n--- Monthly Water Bill Summary ---")
print(f"Consumption: {consumption} m3")
print(f"Service Charge: GHS {service_charge:.2f}")
print(f"Consumption Cost: GHS {consumption_cost:.2f}")
print(f"Total Bill: GHS {total_bill:.2f}")


        
#Question 3 
recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
SPEED_LIMIT = 100

speeding_violations = []

for speed in recorded_speeds:
    if speed > SPEED_LIMIT:
        print(f"WARNING: Vehicle recorded at {speed} km/h. Exceeded limit of {SPEED_LIMIT} km/h")
        speeding_violations.append(speed)

total_vehicles = len(recorded_speeds)
total_violations = len(speeding_violations)
percentage_speeding = round((total_violations / total_vehicles) * 100, 2)

total_speed = 0
for speed in recorded_speeds:
    total_speed += speed

average_speed = total_speed / total_vehicles

print("\n--- Traffic Speed Analysis Summary ---")
print("Total number of vehicles recorded:", total_vehicles)
print("Total number of speeding violations:", total_violations)
print("Percentage of vehicles speeding:", percentage_speeding, "%")
print("Average speed of all vehicles:", round(average_speed, 2), "km/h")

focused_segment = recorded_speeds[2:8]
print("\nSpeeds for focused inspection segment (3rd to 8th vehicle):", focused_segment)

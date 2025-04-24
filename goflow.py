# project-goflow © 2025 Greyson (gmangameing29)
# Licensed under the GrowFlow Open License (GOL-1.0)
# You may use and remix this code, but NOT rebrand or republish as your own.

import time
import random

class SmartFarm:
    def __init__(self):
        self.soil_moisture = 50
        self.light_level = 70
        self.crop_yield = 0

    def simulate_growth(self):
        water = random.randint(10, 30)
        sunlight = random.randint(40, 100)
        self.soil_moisture += water - 10
        self.light_level = sunlight
        if self.soil_moisture > 60 and self.light_level > 60:
            self.crop_yield += 1
        print(f"🌱 Soil: {self.soil_moisture}%, Light: {self.light_level}, Crops: {self.crop_yield}")

class FoodBankNetwork:
    def __init__(self):
        self.food_storage = 10

    def receive_crops(self, amount):
        self.food_storage += amount
        print(f"📦 Food Bank Storage: {self.food_storage}")

    def distribute_food(self):
        if self.food_storage > 0:
            self.food_storage -= 1
            print("🚚 Food distributed to a community in need.")

class ChatdoggoAI:
    def __init__(self):
        self.name = "Chatdoggo"

    def monitor_hunger(self):
        hunger_zones = random.randint(1, 5)
        print(f"🐶 {self.name} detects {hunger_zones} hunger zones today.")

    def deploy_drones(self, count):
        print(f"✈️ {self.name} launched {count} food drones!")

def run_growflow():
    farm = SmartFarm()
    bank = FoodBankNetwork()
    doggo = ChatdoggoAI()

    for day in range(1, 6):
        print(f"\n🌅 Day {day}")
        farm.simulate_growth()
        bank.receive_crops(farm.crop_yield)
        doggo.monitor_hunger()
        bank.distribute_food()
        doggo.deploy_drones(1)
        time.sleep(1)

if __name__ == "__main__":
    run_growflow()

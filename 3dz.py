import random

class Pet:
    def __init__(self, name, species="dog"):
        self.name = name
        self.species = species
        self.hunger = 50  # 0 - ситий, 100 - дуже голодний
        self.happiness = 50  # 0 - нещасливий, 100 - дуже щасливий
        self.energy = 50  # 0 - дуже втомлений, 100 - повний енергії

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 15
            print(f"{self.name} поїв і тепер менш голодний.")
        else:
            print(f"{self.name} вже ситий.")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            self.energy -= 10
            print(f"{self.name} грається і стає щасливішим.")
        else:
            print(f"{self.name} вже дуже щасливий і не хоче грати.")

    def sleep(self):
        if self.energy < 100:
            self.energy += 20
            self.hunger += 5
            print(f"{self.name} поспав і відновив сили.")
        else:
            print(f"{self.name} вже відпочив.")

    def status(self):
        return f"{self.name} (Вид: {self.species}) - Голодування: {self.hunger}, Щастя: {self.happiness}, Енергія: {self.energy}"

    def is_happy(self):
        return self.happiness > 60 and self.hunger < 40 and self.energy > 30


class Owner:
    def __init__(self, name, pet: Pet):
        self.name = name
        self.pet = pet

    def feed_pet(self):
        print(f"{self.name} годує {self.pet.name}.")
        self.pet.eat()

    def play_with_pet(self):
        print(f"{self.name} грає з {self.pet.name}.")
        self.pet.play()

    def put_pet_to_sleep(self):
        print(f"{self.name} кладе {self.pet.name} спати.")
        self.pet.sleep()

    def check_pet_status(self):
        print(f"Стан улюбленця {self.pet.name}:")
        print(self.pet.status())

    def interact(self):
        actions = [self.feed_pet, self.play_with_pet, self.put_pet_to_sleep]
        action = random.choice(actions)
        action()
        self.check_pet_status()
        if self.pet.is_happy():
            print(f"{self.pet.name} дуже щасливий і задоволений життям!")
        else:
            print(f"{self.pet.name} потребує більше догляду.")

class Pet:
    def __init__(self, name, species="dog", age=0):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = 50  # 0 - не голодний, 100 - дуже голодний
        self.happiness = 50  # 0 - нещасливий, 100 - дуже щасливий
        self.energy = 50  # 0 - дуже втомлений, 100 - повністю відпочив

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            print(f"{self.name} поїв і тепер менше голодний.")
        else:
            print(f"{self.name} вже ситий!")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            self.energy -= 5
            print(f"{self.name} грається і стає щасливішим!")
        else:
            print(f"{self.name} вже дуже щасливий і не хоче грати.")

    def sleep(self):
        if self.energy < 100:
            self.energy += 20
            self.hunger += 5
            print(f"{self.name} поспав і відновив енергію.")
        else:
            print(f"{self.name} вже повний енергії!")

    def status(self):
        print(f"Ім'я: {self.name}")
        print(f"Вид: {self.species}")
        print(f"Вік: {self.age}")
        print(f"Рівень голоду: {self.hunger}")
        print(f"Рівень щастя: {self.happiness}")
        print(f"Рівень енергії: {self.energy}")
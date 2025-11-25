class Animal:
    def __init__(self, species, age, eats):
        self.s = species
        self.a = age
        self.e = eats
        
    def make_sound(self):
        print(f"{self.s} издает какой-то звук!")
    
    def __str__(self):
        return f'Животное: {self.s}\nВ среднем живет: {self.a}\nПитается: {self.e}'
    
animal_1 = Animal("Волк", "14-16 лет", "мясом")
print(animal_1)
animal_1.make_sound()
print(25*".")
class Mammal(Animal):
    def __init__(self, species, age, eats, fur_color):
        super().__init__(species, age, eats)
        self.f = fur_color
        
    def feed_milk(self):
        print(f'{self.s} кормит детенышей молоком')
        
    def __str__(self):
        return super().__str__()+f'\nИмеет цвет шерсти: {self.f}'
animal_2 = Mammal("Кошка", "13-20 лет", "мясом/кормом", "серый")
print(animal_2)
animal_2.feed_milk()
print(25*".")

class Reptile(Animal):
    def __init__(self, species, age, eats, poison):
        super().__init__(species, age, eats)
        self.po = poison
        
    def make_sound(self):
        return (f"{self.s} Шипит: Шшшш!")
        
    def crawwl(self):
        return ("Жиаотное ползает по земле")
    
    def __str__(self):
        return super(). __str__()+f"\nЭта особь: {self.po}"

animal_3 = Reptile("Гадюка", "14 лет", "мясом", "ядовитая")
print(animal_3)
print(animal_3.make_sound())
print(animal_3.crawwl())
print(25*".")

class Zoo_show:
    def __init__(self):
        self.shows = {
            1: {"name": "Шоу млекопитающих", "price": 500, "description": "Медведи танцуют, дельфины прыгают через кольца!"},
            2: {"name": "Шоу рептилий", "price": 300, "description": "Змеи шипят и ползают по арене!"},
            3: {"name": "Птичье шоу", "price": 400, "description": "Попугаи говорят и орлы летают над зрителями!"}
        }

    def show_info(self):
        print("🎪 Добро пожаловать в Зоопарк!\nСегодня у нас есть такие шоу:\n")
        for number, info in self.shows.items():
            print(f"{number}. {info['name']} — {info['description']}")
        print()

    def choose_show(self):
        choice = int(input("Введите номер шоу, которое хотите посетить: "))
        if choice in self.shows:
            info = self.shows[choice]
            print(f"\nВы выбрали: {info['name']}")
            print(f"💵 Цена билета: {info['price']} сом")
            print(f"🎬 Как проходит шоу: {info['description']}")
        else:
            print("Такого шоу нет! 😅")

zoo = Zoo_show()
zoo.show_info() 
zoo.choose_show()
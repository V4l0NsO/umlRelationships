
#UML Relationship - Inheritance
print("UML Relationship - Inheritance")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks: insert dog sound bark effect"

my_dog = Dog("Buddy")
print(my_dog.speak())
print("  ")

#UML Relationship - Association
print("UML Relationship - Association")

class Driver:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, model, driver):
        self.model = model
        self.driver = driver 

    def get_details(self):
        return f"{self.model} is driven by {self.driver.name}"

driver = Driver("Alice")
car = Car("Sedan", driver)
print(car.get_details())
print("  ")

#UML Relationship - Aggregation
print("UML Relationship - Aggregation")

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  

    def add_book(self, book):
        self.books.append(book)

b1 = Book("100 ways to Mog and 67 ways become an Aura Monster")
my_library = Library("City Library")
my_library.add_book(b1)
print(f" The '{my_library.name}' has the book: {my_library.books[0].title}")
print("  ")

#UML Relationship - Composition
print("UML Relationship - Composition")


class Room:
    def __init__(self, room_type):
        self.room_type = room_type

class House:
    def __init__(self):
        self.rooms = [Room("Living Room"), Room("Kitchen"), Room("Bedroom")]

my_house = House()
print("House contains rooms:")
for room in my_house.rooms:
    print(f"- {room.room_type}")
print("  ")

#UML Relationship - Dependency
print("UML Relationship - Dependency")

class Coupon:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount

class ShoppingCart:
    def checkout(self, total_amount, coupon: Coupon):
        final_price = total_amount - (total_amount * coupon.discount)
        return f"Checkout complete with coupon {coupon.code}. Total: ${final_price}"

coupon = Coupon("SAVE10", 0.10)
cart = ShoppingCart()
print(cart.checkout(100.0, coupon))
print(" ")
class Phone:
    brand = input("Бренд вашего телефонона: ")
    price = input("Цена вашего телефона: ")
    def __init__(self, brand, model, price):
        self.brand = brand
        self.price = price

    def make_call(self, phone_number):
        phone_number = input("Введите номер телефона: ")
        print(f"Звонок {phone_number}...")

    def send_message(self, phone_number, message):
        print(f"Отправляем сообщение {phone_number}: {message}")

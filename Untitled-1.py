class GameMenu:
    
    def __init__(self):
        self.start_game = "Добро пожаловать в нашу игру!"
        self.exit_game = "Вы уверены, что хотите выйти из игры?"
    
    def start(self):
        print(self.start_game)
        
    def exit(self):
        answer = input(self.exit_game + " (yes/no): ")
        if answer.lower() == "yes":
            print("До свидания!")
            exit()
        else:
            print("Отлично! Продолжаем играть.")
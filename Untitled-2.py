class Mailbox:
    def __init__(self):
        self.inbox = []

    def receive_mail(self, message):
        self.inbox.append(message)

    def read_mail(self):
        if len(self.inbox) > 0:
            return self.inbox.pop(0)
        else:
            return None
 
 
mailbox = Mailbox()
mailbox.receive_mail("Привет")
mailbox.receive_mail("Как")
mailbox.receive_mail("Дела")
mailbox.receive_mail("Богдан")
mailbox.receive_mail("Где")
mailbox.receive_mail("Стримы")
mailbox.receive_mail("Пока")
 
print(mailbox.read_mail())
print(mailbox.read_mail())
print(mailbox.read_mail())
print(mailbox.read_mail())
print(mailbox.read_mail())
print(mailbox.read_mail())
print(mailbox.read_mail())

print(mailbox.read_mail())
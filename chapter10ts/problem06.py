from random import randint
class train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"train no: {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"ticket fare in train no. {self.trainNo} from {fro} to {to} is {randint (222, 5555)}")

t = train(12399)
t.book("Rampur", "Delhi")
t.getstatus()
t.getfare("Rampur", "Delhi")
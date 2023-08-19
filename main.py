import pandas

df = pandas.read_csv("hotels.csv")


class Hotel:
    def __init__(self, id):
        self.id = id

    def book(self):
        pass


class ReservationTicket:
    def generate(self):
        pass


print(df)
id = input("Enter the id of the hotel")
hotel = Hotel(id)
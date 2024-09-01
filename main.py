import pandas as pd


class Hotel:
    def __init__(self, id):
        self.id = id

    def book(self):
        pass


class ReservationTicket:
    def __init__(self, booked_hotel, customer_name):
        self.booked_hotel = booked_hotel
        self.customer_name = customer_name

    def generate(self):
        print("Reservation made")


if __name__ == "__main__":
    df = pd.read_csv("hotels.csv")

    username = input("Enter your name: ")
    option = input("Do you want to see unavailable hotels? y/n")
    if option == "n":
        print("List of available hotels:")
        new_df = df.loc[df["available"] == "yes"]
        print(new_df)
    else:
        print("All hotels:")
        print(df)
    hotel_id = input("Enter hotel ID: ")
    hotel = Hotel(hotel_id)
    ticket = ReservationTicket(hotel, username)
    ReservationTicket.generate(ticket)


import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        if df.loc[df["id"] == self.hotel_id, "available"].squeeze() == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, booked_hotel, customer_name):
        self.booked_hotel = booked_hotel
        self.customer_name = customer_name

    def generate(self):
        print("Reservation made")


if __name__ == "__main__":
    print(df)
    username = input("Enter your name: ")
    hotel_id = input("Enter hotel ID: ")
    hotel = Hotel(hotel_id)
    if hotel.available():
        hotel.book()
        ticket = ReservationTicket(hotel, username)
        ReservationTicket.generate(ticket)
    else:
        print("Hotel not available")

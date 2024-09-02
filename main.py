import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = (pd.read_csv("cards.csv", dtype=str)
            .to_dict(orient="records"))
df_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        try:
            if df.loc[
                df["id"] == self.hotel_id, "available"].squeeze() == "yes":
                return True
            else:
                print("Hotel not available")

        except ValueError:
            print("That hotel is incorrect")


class ReservationTicket:
    def __init__(self, booked_hotel, customer_name):
        self.booked_hotel = booked_hotel
        self.customer_name = customer_name
        self.hotel = booked_hotel

    def generate(self):
        content = f"""
        Thanks for your reservation.
        Here is the booking data:
        Name: {self.customer_name.upper()}
        Hotel: {self.hotel.name}
        """
        print(content)


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "cvc": cvc, "holder": holder}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, wrote_password):
        try:
            password = df_security.loc[df_security["number"] == self.number,
            "password"].squeeze()
            if wrote_password == password:
                return True
            else:
                return False
        except ValueError:
            return False

if __name__ == "__main__":
    print(df)
    hotel_id = input("Enter hotel ID: ")
    hotel = Hotel(hotel_id)
    if hotel.available():
        credit_card = SecureCreditCard(number="1234")
        if credit_card.validate(expiration="12/26", holder="JOHN SMITH",
                                cvc="123"):
            if credit_card.authenticate(wrote_password="mypass"):
                hotel.book()
                username = input("Enter your name: ")
                ticket = ReservationTicket(hotel, username)
                ticket.generate()
            else:
                print("Credit card authentication error")
        else:
            print("Error, there was a problem with the card")

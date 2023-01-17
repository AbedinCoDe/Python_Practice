#for Clear Screen
import subprocess
import platform
def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)

# For Import Logo From a Moudle

from Auction_Art import logo
print(logo)

Bid_Dict = {}
Biding_Finished = False

def highest_bid(bidding_record):
  highest_bid_amount = 0
  winner= ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid_amount:
      highest_bid_amount = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the bit of {highest_bid_amount}")

while not Biding_Finished:
    Name = input("Write your Name: \n")
    Price = int(input("Write your price: $"))
    Bid_Dict[Name] = Price
    should_continue = input("Are There any Bidder Exit? Write 'Yes' Or 'No'\n")
    if should_continue == 'No':
      Biding_Finished = True
      highest_bid(Bid_Dict)
    elif should_continue == "Yes":
      clear()











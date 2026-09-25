import math
import random

participants = int(input("enter number PP: "))
winners = int(input("enter number winners:"))
ticker = range(1,participants+1)

sheet = math.ceil(participants / 8)
prize_winner = math.floor(8888 / winners)
winner_ticket = random.sample(ticker , winners)

print(f"sheet:{sheet}\n prize:{8888}\nnumber ticket:{winner_ticket}")
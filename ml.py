import pandas
import matplotlib.pyplot as plt
games=pandas.read_csv("games.csv")
print(games[games["average_rating"] == 0].iloc[0])
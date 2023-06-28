import numpy as np
import matplotlib.pyplot as plt

#data from vlr.gg

N = 10
ind = np.arange(N)
width = 0.25

plt.style.use('seaborn-darkgrid')

killvals = [65, 34, 46, 32, 44, 55, 63, 44, 40, 47]
bar1 = plt.bar(ind, killvals, width, color = 'r')

deathvals = [42, 43, 52, 52, 43, 54, 54, 41, 56, 37]
bar2 = plt.bar(ind+width, deathvals, width, color='g')

assistvals = [12, 35, 14, 23, 29, 2, 13, 44, 16, 38]
bar3 = plt.bar(ind+width*2, assistvals, width, color = 'b')

plt.xlabel("Names of Players", fontsize=14)
plt.ylabel("KDA Number", fontsize=14)
plt.title("EG vs FNC Valorant Masters Tokyo Grand Finals KDA Data"
          , fontsize=24)

plt.xticks(ind+width,['FNC Alfajar', 'FNC Boaster', 'EG Boostio', 'EG COM'
                      , 'FNC Chronicle', 'EG Demon1', 'FNC Derke', 'EG Ethan',
                      'EG jawgemo', 'FNC Leo'])
plt.legend( (bar1, bar2, bar3), ('Kills', 'Deaths', 'Assists') )
plt.show()
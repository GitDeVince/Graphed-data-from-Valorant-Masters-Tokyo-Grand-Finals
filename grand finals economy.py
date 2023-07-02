import matplotlib.pyplot as plt
import numpy as np

rounds = [(i) for i in range(22)]
rounds2 = [(i) for i in range(25)]
# lotus data
EG_lotus = [0, 600, 1200, 9200, 1100, 9600, 2400, 4800, 13300, 24700, 24000, 13300, 9100, 400, 10200, 1300, 8500, 2400, 1600, 700, 2100, 12600]
FNC_lotus =[0, 300, 7500, 6900, 13400, 22300, 24900, 14900, 8300, 5900, 3400, 11000, 1800, 500, 800, 10400, 11600, 18300, 22700, 18900, 7800, 7000]

#Split data
EG_split = [0, 300, 9900, 800, 7000, 1800, 8400, 2500, 7200, 13200, 3700, 9800, 500, 100, 1100, 9600, 12500, 19200, 23800, 10000, 3100, 9100, 3700, 7200, 1100]
FNC_split = [0, 200, 1000, 14400, 5400, 6700, 15800, 22800, 12600, 8400, 10200, 2900, 3500, 200, 6200, 700, 6500, 2900, 5700, 8500, 11600, 4300, 12200, 3800, 13400]

#Bind data
EG_bind = [0, 400, 7900, 1000, 6900, 11600, 24900, 16400, 17300, 5800, 14600, 20200, 18600, 100, 1800, 6100, 4500, 10000, 6500, 10400, 6400, 8300, 2500, 7100, 1200] 
FNC_bind = [0, 100, 2200, 12000, 4600, 2300, 6400, 9000, 8900, 5200, 6100, 1100, 200, 7000, 1500, 11300, 21300, 19700, 11600, 6200, 15000, 25800, 22800, 12600, 13400]



#lotus plot
def lotus():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(rounds, EG_lotus, linewidth=3)
    ax.plot(FNC_lotus, linewidth=3, c='red')
    plt.plot(EG_lotus, label = "EG")
    plt.plot(FNC_lotus, label = "FNC")

    ax.set_title("Lotus Map Economy of EG vs FNC Grand Finals", fontsize=24)
    ax.set_xlabel("Rounds", fontsize=14)
    ax.set_ylabel("Economy", fontsize=14)

    # plot lines
    ax.tick_params(axis='both', labelsize=14)
    plt.legend()
    plt.show()

#split plot
def split():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(rounds2, EG_split, linewidth=3)
    ax.plot(FNC_split, linewidth=3, c='red')
    plt.plot(EG_split, label = "EG")
    plt.plot(FNC_split, label = "FNC")

    ax.set_title("Split Map Economy of EG vs FNC Grand Finals", fontsize=24)
    ax.set_xlabel("Rounds", fontsize=14)
    ax.set_ylabel("Economy", fontsize=14)

    # plot lines
    ax.tick_params(axis='both', labelsize=14)
    plt.legend()
    plt.show()

#bind plot
def bind():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    
    ax.plot(rounds2, EG_bind, linewidth=3)
    ax.plot(FNC_bind, linewidth=3, c='red')
    plt.plot(EG_bind, label = "EG")
    plt.plot(FNC_bind, label = "FNC")

    ax.set_title("Bind Map Economy of EG vs FNC Grand Finals", fontsize=24)
    ax.set_xlabel("Rounds", fontsize=14)
    ax.set_ylabel("Economy", fontsize=14)

    # plot lines
    ax.tick_params(axis='both', labelsize=14)
    plt.legend()
    plt.show()


while True:
    print()
    print("Here, you can access to the economy data of the Masters Tokyo Finals of EG vs FNC.")
    decision = input("What do you want to see? 'Lotus', 'Split', 'Bind', or Exit: ")
    decision = decision.lower()

    if decision == "lotus":
        lotus()
    elif decision == "split":
        split()
    elif decision == "bind":
        bind()
    elif decision == 'exit':
        print("Goodbye!")
        break
    else:
        print("You can only choose the 4 options above.")

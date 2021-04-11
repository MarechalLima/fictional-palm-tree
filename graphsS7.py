#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt


# Menu
def main():
    choice = int(input("Escolha a questão a exibir {1, 2, 3, 4, 5, 6, 7}:\n"))

    if choice == 1:
        questOne()
    elif choice == 2:
        print("fodase")
    elif choice == 3:
        print("fodase")
    elif choice == 4:
        print("fodase")
    elif choice == 5:
        print("fodase")
    elif choice == 6:
        print("fodase")
    elif choice == 7:
        print("fodase")

#Questão 1
def questOne():
    data = pd.read_csv("data/weight_chart.txt", usecols=['Age', 'Weight'], delim_whitespace=True)

    data.plot.line(x='Age', y='Weight', marker='o', markerfacecolor='white', color="#000000", legend=False)
    plt.xlabel("Age (months)")
    plt.ylabel("Weight (kg)")

    plt.ylim(1,11)
    plt.savefig("Quest1.png")
    plt.show()

#Questão 2
def questTwo():
    data = pd.read_csv("data/feature_counts.txt", delim_whitespace=True)

    data.plot.barh(x='Feature', y='Count', legend=False, color="lightgray", edgecolor='black')
    plt.xlabel("Number of features")

    plt.xticks([0, (2*10**4), (4*10**4),(6*10**4)])
    # plt.box(False)
    plt.box(y=False)
    plt.tight_layout()
    plt.show()

questTwo()
#!/usr/bin/python3
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Menu
def main():
    while(True):
        choice = int(input("Escolha a questão a exibir {1, 2, 3, 4, 5, 6, 7} \n0 para sair:\n"))

        if choice == 1:
            questOne()
        elif choice == 2:
            questTwo()
        elif choice == 3:
            questThree()
        elif choice == 4:
            questFour()
        elif choice == 5:
            print("fodase")
        elif choice == 6:
            print("fodase")
        elif choice == 7:
            print("fodase")
        elif choice == 0:
            break

## Questão 1
def questOne():
    data = pd.read_csv("data/weight_chart.txt", usecols=['Age', 'Weight'], delim_whitespace=True)

    data.plot.line(x='Age', y='Weight', marker='o', markerfacecolor='white', color="#000000", legend=False)
    plt.xlabel("Age (months)")
    plt.ylabel("Weight (kg)")
    plt.title("The relationship between age and weight in a growing infant", fontweight="bold")

    plt.ylim(1,11)
    plt.savefig("Quest1.png")
    plt.show()

## Questão 2
def questTwo():
    data = pd.read_csv("data/feature_counts.txt", delim_whitespace=True)

    fig, ax = plt.subplots()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    data.plot.barh(x='Feature', y='Count', legend=False, color="lightgray", edgecolor='black', ax=ax)
    plt.xlabel("Number of features")

    plt.xticks([0, (2*10**4), (4*10**4),(6*10**4)])
    plt.tight_layout()
    plt.savefig("Quest2.png")
    plt.show()

    del fig
    del ax


## Questão 3
def questThree():
    data1 = np.random.normal(size=10**4)
    data2 = np.random.normal(loc=4, size=10**4)
    data = np.concatenate([data1, data2])

    fig, ax = plt.subplots()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    plt.xlim(-4,8)
    plt.hist(data, bins=100, edgecolor='black', color="lightgray")

    plt.title("Mixed distribution histogram", fontweight="bold")
    plt.ylabel("Frequency")
    plt.xlabel("Values")
    plt.savefig("Quest3.png")
    plt.show()

    del fig
    del ax

## Questão 4
def questFour():
    data = pd.read_csv("data/male_female_counts.txt", delim_whitespace=True)
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    fig, ax = plt.subplots()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    data.plot.bar(x='Sample', y='Count', legend=False, color=colors, ax=ax)

    plt.yticks([0,5,10,15])
    plt.xticks(rotation=0, fontsize=8)

    plt.xlabel("")
    plt.tight_layout()
    plt.savefig("Quest4.png")
    plt.show()

    del fig
    del ax

# questFour()

main()
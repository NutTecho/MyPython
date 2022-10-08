import matplotlib.pyplot as plt
import numpy as np
# from tkinter import *


def barv():
    # plt.use( 'tkagg' )
    x = range(4)
    y = (20, 25, 40, 30)
    xticks = ("Mocca","latte","Espresso","tea")
    plt.xticks(x,xticks)
    plt.bar(x, y)
    plt.show()

def barh():
    x = range(4)
    y = (20,25,40,30)
    xticks = ("Mocca", "latte", "Espresso", "tea")
    plt.yticks(x,xticks)
    plt.barh(x,y)
    plt.show()

def bar_sub():
    x = range(4)
    y = (20, 25, 40, 30)
    xticks = ("Mocca", "latte", "Espresso", "tea")
    fig, ax = plt.subplots(1, 2)
    ax[0].bar(x,y,color = "orange")
    ax[1].barh(x,y,color = "skyblue")
    plt.sca(ax[0])
    plt.xticks(x, xticks)
    plt.sca(ax[1])
    plt.yticks(x, xticks)
    fig.tight_layout()
    plt.show()

def pie1():
    label = ("China","Japan","Russia","Korea")
    val = (1.8,1,0.8,0.5)
    plt.pie(val,labels=label,startangle=90,autopct= "%1.2f%%",explode=(0,0,0.1,0))
    plt.axis("equal")
    plt.show()

def pie2():
    label = np.array(["China", "Japan", "Russia", "Korea"])
    val = (1.8, 1, .8, .5)
    explode = np.zeros(label.size)
    explode[np.where(label == "Korea")] = 0.1
    color1 = ["red","pink","green","orange"]
    # plt.pie(val,labels=label,startangle=90,autopct= "%1.2f%%",explode=explode,colors = color1)
    plt.pie(val,labels=label,startangle=90,autopct= "%1.2f%%",explode=explode,colors = color1)
    plt.axis("equal")
    plt.show()

def qc_plot():
    n = 100
    x = np.arange(n)
    d = np.random.normal(150,5,n)
    m , sd = np.mean(d), np.std(d)
    plt.plot(x,d, marker = "o", color = ".7",alpha = .7)
    filter = np.where((d>m+2*sd) | (d<m-2*sd))
    plt.plot(x[filter],d[filter], marker = "o", color = "red" , linestyle = "")
    plt.axhline(m,color = "green", linestyle = "--" )
    t = "n = {} , {} = {:.2f} , sd = {:.2f}".format(n,r"$\bar{x}$",m,sd)
    plt.ylabel("weight (grams)")
    plt.title(t)
    ucl = 2*sd
    lcl = -ucl
    plt.fill_between(x, m+ucl, m+5*sd, alpha = .1, color = "red")
    plt.fill_between(x, m+lcl, m-5*sd, alpha = .1 ,color = "red")
    # plt.axhline(m+ucl,color = "red", linestyle ="--")
    # plt.axhline(m+lcl,color = "red", linestyle ="--")
    plt.show()


if __name__ == '__main__':
    # barv()
    # barh()
    # bar_sub()
    # pie1()
    # pie2()
    qc_plot()
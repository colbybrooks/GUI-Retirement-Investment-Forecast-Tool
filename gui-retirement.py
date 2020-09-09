# Folowing code builds a GUI that forecasts your wealth based on investing variables
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
fields = ('Mean Return (%)',' Std Dev Return (%)','Yearly Contribution ($)','No. of Years of Contribution','No. of Years to Retirement','Annual Spend in Retirement')
# Input fields

# Financial is a function that calcs and plots the wealth, also changes the label
def financial(e, label):
    # Declaring the variables based on the inputs in there entry collumns on the GUI
    mean = float(e[0].get())
    std = float(e[1].get())
    contrYears = float(e[2].get())
    years2ctr = float(e[3].get())
    years2ret = float(e[4].get())
    spend = float(e[5].get())

    run = np.arange(0,10, dtype=int)    # 10 runs for the 70 years
    aveWealth = np.zeros(len(run))      # Blank Average Wealth array for the separate runs

    for runs in run:
        years = np.arange(0,71, dtype = int)    # 70 years, 0 for initial conditions
        wealth = np.zeros(len(years))           # Blank array for wealth over 70 years
        for year in range(len(years)-1):
            volatality = std / 100 * np.random.randn()     # Volatality equation
            if ( year < years2ret ): # Not retired
                if ( year < years2ctr ): # Not retired and contributing
                    wealth[year + 1] = wealth[year] * ( 1 + mean/100 + volatality) + contrYears
                if ( year >= years2ctr ): # Not retire but no contributing
                    wealth[year + 1] = wealth[year] * ( 1 + mean/100 + volatality)
            if ( year >= years2ret ):   # Retired and Spending
                wealth[year + 1] = wealth[year] * (1 + mean / 100 + volatality) - spend
            if (wealth[year+1] < 0):    # Broke means break
                break
        plt.plot(years, wealth)             # Plot the wealth vs years for each run
        aveWealth[runs] = np.mean(wealth)   # Calculate the Average Wealth for each run
    averageWealth = np.mean(aveWealth)      # Calculate the average wealth over all runs
    label.configure(text = "Wealth is {0:,.2f} dollars".format(averageWealth))     # Reconfigure the label
    plt.xlabel("Years")     # Plot Characteristics
    plt.ylabel("Wealth")
    plt.show()              # Show plot after the Run for loop

root = Tk()         # Initiate tkinter

e = []      # Blank entry index
for index in range(len(fields)):    # For loop for size of input fields
    Label(root,text = fields[index]).grid(row=index)        # Create labels with fields strings
    e.append(Entry(root))           # Adds to the array for the entry values
    e[index].grid(row = index, column = 1)      # Delegates them on the GUI

labelWealth = Label(root, text = "Wealth")      # Output Wealth Label and grid
labelWealth.grid(row = index+1)

buttonCalculate = Button(root,text='Calculate', command = lambda: financial(e, labelWealth)).grid(row=index+2)
# Calculate Button that executes financial
buttonQuit = Button(root, text ="Quit", command = root.destroy).grid(row=index+2,column=1, sticky=W)
# Quit button that destroys GUI and Script

mainloop()
import math
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from tkinter import *
from matplotlib.artist import Artist
from matplotlib.widgets import Slider


# Declared variables to use
xi: float = 0.0
yi: float = 0.0
totalxi: float = 0.0
totalyi: float = 0.0
valueCount: int = 0
subxMeans: float = 0.0
subyMeans: float = 0.0
totalsubxMeans: float = 0.0
totalsubyMeans: float = 0.0
multiMeans: float = 0.0
totalmultiMeans: float = 0.0
slope: float = 0.0
intercept: float = 0.0
lineEquation: float = 0.0
xMinValue: float = 0.0
xMaxValue: float = 0.0
yMinValue: float = 0.0
yMaxValue: float = 0.0
prevXValue: float = 0.0
prevYValue: float = 0.0
matchedX: float = 0.0
matchedY: float = 0.0
matchedDottedX: float = 0.0
matchedDottedY: float = 0.0
plotted: int = 0
predictX: float = 0.0
predictY: float = 0.0
slope1: float = 0.0
slope2: float = 0.0
plotCount: int = 0
line_1 = (0, 0)
line_2 = (0, 0)
condition: int = 0
figCount: int = 0
allData: str = ""
xSlider: Slider
ySlider: Slider
xSliderState: int = 0
ySliderState: int = 0
plottedAlready: int = 0

# Gets the figure to plot
fig, ax = plt.subplots()
fig.canvas.manager.set_window_title('Machine Learning Using Linear Regression By Umolu John Chukwuemeka')
plt.subplots_adjust(left=0.25, bottom=0.25)


# Plot Horizontal Line(Y-axis)
def plot1(val1):
    # Make outside variables accessible inside the function
    global plotCount
    global line_1
    global line_2
    global xSliderState
    global ySliderState
    global predictX
    global predictY

    ySliderState = 1

    # String variable to store entered split data string
    enteredData: str = str(val1)

    # Removes all white spaces
    if enteredData.find(' ') >= 0:
        enteredData = enteredData.replace(" ", "")

    # Plot remove routine that removes the previous plotted lines in every 2 counts
    plotCount = plotCount + 1
    if plotCount == 2:
        plotCount = 1
        l1 = line_1.pop(0)
        l2 = line_2.pop(0)
        l1.remove()
        l2.remove()

    # Get the user input string and convert to float value
    newYData: float = float(enteredData)
    newYData = round(newYData, 2)

    # Predict the X output value for Y input
    predictX = round((((newYData - intercept) + (slope * xMinValue)) / slope), 1)

    # Round up to closest decimal value
    if slope == slope1 and slope == slope2:
        predictX = round(predictX)

    # print("Predicted XValue:", predictX)

    plt.subplots_adjust(left=0.25, bottom=0.25)

    # Plot Horizontal line
    line_1 = ax.plot([xMinValue, xMaxValue + 1.5], [newYData, newYData], color='grey', linestyle='dashed')

    # Plot Vertical Line
    line_2 = ax.plot([predictX, predictX], [yMinValue, yMaxValue + 1.5], color='grey', linestyle='dashed')

    # giving a title to my graph
    ax.set_title('Speed Data Prediction Using Machine Learning' + '\n' + 'Slider Time Value(x-axis): ' + str(predictX)
                 + ' sec' + '\n' + 'Predicted Distance Value: ' + str(newYData) + ' cm (+/-0.1cm)')

    if xSliderState == 0:
        xSlider.set_val(predictX)

    xSliderState = 0
    ySliderState = 0

    # Maximize plot to fit windows screen
    # mng = plt.get_current_fig_manager()
    # mng.window.state("zoomed")

    # function to show the plot
    plt.show()


# Plot Vertical Line(X-axis)
def plot2(val2):
    # Make outside variables accessible inside the function
    global plotCount
    global line_1
    global line_2
    global xSliderState
    global ySliderState
    global predictX
    global predictY

    xSliderState = 1

    # String variable to store entered split data string
    enteredData: str = str(val2)

    # Removes all white spaces
    if enteredData.find(' ') >= 0:
        enteredData = enteredData.replace(" ", "")

    # Plot remove routine that removes the previous plotted lines in every 2 counts
    plotCount = plotCount + 1
    if plotCount == 2:
        plotCount = 1
        l1 = line_1.pop(0)
        l2 = line_2.pop(0)
        l1.remove()
        l2.remove()

    # Get the user input string and convert to float value
    newXData: float = float(enteredData)
    newXData = round(newXData, 2)

    # Predict the Y output value for X input
    predictY = round(((slope * newXData - slope * xMinValue) + intercept), 1)

    # Round up to closest decimal value
    if slope == slope1 and slope == slope2:
        predictY = round(predictY)

    # print("Predicted YValue:", predictY)

    plt.subplots_adjust(left=0.25, bottom=0.25)

    # Plot Horizontal line
    line_1 = ax.plot([xMinValue, xMaxValue + 1.5], [predictY, predictY], color='grey', linestyle='dashed')

    # Plot Vertical Line
    line_2 = ax.plot([newXData, newXData], [yMinValue, yMaxValue + 1.5], color='grey', linestyle='dashed')

    # giving a title to my graph
    ax.set_title('Speed Data Prediction Using Machine Learning' + '\n' + 'Slider Distance Value(y-axis): ' + str(predictY)
                 + ' cm' + '\n' + 'Predicted Time Value: ' + str(newXData) + ' sec (+/-0.1sec)')

    if ySliderState == 0:
        ySlider.set_val(predictY)

    ySliderState = 0
    xSliderState = 0

    # Maximize plot to fit windows screen
    # mng = plt.get_current_fig_manager()
    # mng.window.state("zoomed")

    # function to show the plot
    plt.show()


def train():
    global xi
    global yi
    global totalxi
    global totalyi
    global valueCount
    global subxMeans
    global subyMeans
    global totalsubxMeans
    global totalsubyMeans
    global multiMeans
    global totalmultiMeans
    global slope
    global intercept
    global lineEquation
    global xMinValue
    global xMaxValue
    global yMinValue
    global yMaxValue
    global prevXValue
    global prevYValue
    global matchedX
    global matchedY
    global matchedDottedX
    global matchedDottedY
    global plotted
    global allData
    global fig
    global figCount
    global xSlider
    global ySlider
    global plottedAlready

    # Clears the last plotted figure when a second call is made
    figCount = figCount + 1
    if figCount == 2:
        figCount = 1
        plt.clf()
        plt.gcf()

    # Gets the new value in the tkinter text box
    allData = str(e.get())

    # Removes any white space in the string
    if allData.find(" ") >= 0:
        allData = allData.replace(" ", "")

    # Replaces the ( characters with an empty value
    if allData.find("(") >= 0:
        allData = allData.replace("(", "")

    # Replaces the ) characters with #
    if allData.find(")") >= 0:
        allData = allData.replace(")", "#")

    # Removes the last character # from the string
    if allData[:-1].find("#"):
        allData = allData[:-1]

    # Split string using the # regex to separate the x and y coordinates from the input data
    splitData = allData.split("#")

    # Foreach Loop Routine
    for newData in splitData:
        # Count the total number of data
        valueCount = valueCount + 1

        # Split xi and yi values
        xValue: str = newData.split(",")[0]
        yValue: str = newData.split(",")[1]
        xi = float(xValue)
        yi = float(yValue)

        # Sum all the xi and yi values
        totalxi = totalxi + xi
        totalyi = totalyi + yi

        # Place the points on the graph using a blue dot
        ax.plot(xi, yi, color='green', marker='o', markerfacecolor='blue', markersize=5)

        # Get the minimum and maximum x-axis values
        if xi < prevXValue and xi < xMinValue:
            xMinValue = xi
        if xi > prevXValue and xi > xMaxValue:
            xMaxValue = xi

        # Get the minimum and maximum y-axis values
        if yi < prevYValue and yi < yMinValue:
            yMinValue = yi
        if yi > prevYValue and yi > yMaxValue:
            yMaxValue = yi

        # Store the previous values
        prevXValue = xi
        prevYValue = yi

    print("xMinValue:", xMinValue, "xMaxValue:", xMaxValue)
    print("yMinValue:", yMinValue, "yMaxValue:", yMaxValue)

    # Calculate the y and x means values
    meansXValue: float = totalxi/valueCount
    meansYValue: float = totalyi/valueCount

    # Foreach Loop Routine
    for newData in splitData:
        # Count the total number of data
        valueCount = valueCount + 1

        # Split xi and yi values
        xValue: str = newData.split(",")[0]
        yValue: str = newData.split(",")[1]
        xi = float(xValue)
        yi = float(yValue)

        # Subtract x-axis values from x-means value
        subxMeans = xi - meansXValue

        # Subtract y-axis values from y-means value
        subyMeans = yi - meansYValue

        # Sum the squre value of subtracted x-axis values from x-means value and y-axis values from y-means value
        totalsubxMeans = totalsubxMeans + (subxMeans * subxMeans)
        totalsubyMeans = totalsubyMeans + (subyMeans * subyMeans)

        # Multiply subtracted x means and y means
        multiMeans = subxMeans * subyMeans

        # Sum multiplied x and y means
        totalmultiMeans = totalmultiMeans + multiMeans

    slope = round((totalmultiMeans/totalsubxMeans), 1)
    print("Slope:", slope)

    # Calculate intercept
    intercept = round((meansYValue - (slope * meansXValue)), 1)
    print("Intercept:", intercept)
    print("---------------------------")

    # Foreach Loop Routine
    for newData in splitData:
        # Split xi and yi values
        xValue: str = newData.split(",")[0]
        yValue: str = newData.split(",")[1]
        xi = float(xValue)
        yi = float(yValue)

        # Sum all the xi and yi values
        lineEquation = round(((slope * xi) + intercept), 4)

        # Subtract calculated line equation value with y-axis value to get positive and negative best values
        posbestValues: float = round((lineEquation - yi), 4)
        negbestValues: float = round((yi - lineEquation), 4)

        # Plot graph when the change in y is equal to the change in x
        if negbestValues == 0 and posbestValues == 0:
            plottedAlready = 1
            # Plot Line Graph
            ax.plot([xMinValue, xi, (xMaxValue + 1.5)], [intercept, yi, (intercept + (slope * (xMaxValue + 1.5)))],
                    color='red')

        #
        if 0 < posbestValues < 0.5:
            if plotted == 1:
                matchedDottedX = xi
                matchedDottedY = yi
            else:
                matchedX = xi
                matchedY = yi

            print("Best Line Plot Point:(", xi, ",", yi, ")")
            print("---------------------------")
            plotted = 1

        elif 0 < negbestValues < 0.5:
            if plotted == 1:
                matchedDottedX = xi
                matchedDottedY = yi
            else:
                matchedX = xi
                matchedY = yi

            print("Best Line Plot Point:(", xi, ",", yi, ")")
            print("---------------------------")
            plotted = 1

    # Calculate slope value positive and negative best line values
    slope1 = round((((intercept + (slope * (xMaxValue + 1.5))) - matchedY)/((xMaxValue + 1.5) - matchedX)), 1)
    slope2 = round((((intercept + (slope * (xMaxValue + 1.5))) - matchedDottedY)/((xMaxValue + 1.5) - matchedDottedX)), 1)
    # print("Slope:", slope, "Slope1:", slope1, "Slope2:", slope2)

    # Compare positive and negative best line slope values with calculated slope for best match
    if slope1 == slope and plottedAlready == 0:
        # Plot Line Graph
        ax.plot([xMinValue, matchedX, (xMaxValue + 1.5)], [intercept, matchedY,
                                                           (intercept + (slope * (xMaxValue + 1.5)))], color='red')
    elif slope2 == slope and plottedAlready == 0:
        # Plot Line Graph
        ax.plot([xMinValue, matchedDottedX, (xMaxValue + 1.5)], [intercept, matchedDottedY,
                                                                 (intercept + (slope * (xMaxValue + 1.5)))], color='red')
    else:
        ax.plot([xMinValue, (xMaxValue + 1.5)], [round(intercept, 1), (intercept + (slope * (xMaxValue + 1.5)))],
                color='red')

    # Setting x and y axis range
    plt.ylim(yMinValue, yMaxValue + 1.5)
    plt.xlim(xMinValue, xMaxValue + 1.5)

    # giving a title to my graph
    plt.title('Speed Data Prediction Using Machine Learning' + '\n' + 'Slider Time Value(x-axis): ' + str(xMinValue)
              + ' sec' + '\n' + 'Predicted Distance Value: ' + str(0.0) + ' cm')

    # Set the slider position on the plot
    ySliderDim = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor='lightgoldenrodyellow')
    xSliderDim = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

    # Make a vertically oriented slider to control the distance
    ySlider = Slider(
        ax=ySliderDim,
        label='Distance(cm)',
        valinit=yMinValue,
        valmin=yMinValue,
        valmax=yMaxValue + 1.5,
        valstep=0.1,
        orientation="vertical"
    )

    # Make a horizontal slider to control the time
    xSlider = Slider(
        ax=xSliderDim,
        label='Time(sec)',
        valinit=xMinValue,
        valmin=xMinValue,
        valstep=0.1,
        valmax=xMaxValue + 1.5
    )

    # Register the update function with each slider
    ySlider.on_changed(plot1)
    xSlider.on_changed(plot2)

    # Maximize plot to fit windows screen
    mng = plt.get_current_fig_manager()
    #mng.window.state("zoomed")

    # Close tkinter dialogue box
    master.destroy()

    # function to show the plot
    plt.show()


# Tkinter dialogue settings
master = Tk()
master.title('Machine Data Input')
master.geometry("400x60")

# Tkinter textbox settings
e = Entry(master, width=50)
e.pack()
e.focus_set()

# Tkinter button settings
b = Button(master, text="Enter New Machine Data", width=30, command=train)
b.pack()

# Start the program loop
master.mainloop()

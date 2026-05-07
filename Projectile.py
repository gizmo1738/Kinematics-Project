import matplotlib.pyplot as plt
import numpy as np

#Finds time of TOTAL flight
def t_flight (v0_y, y0, g):
    a = -.5*g
    b = v0_y
    c = y0
    discriminant = (b**2) - (4*a*c)
    #  check if less than 0
    t1 = (-b + (np.sqrt(discriminant)))/(2*a)  # uses quadratic formula
    t2 = (-b - (np.sqrt(discriminant)))/(2*a)
    t_flight = max(t1, t2)
    return t_flight

#Gets range of projectile
def getRange (v0_x, t_flight):
    return v0_x*t_flight

#Gets maximum height of projectile
def maxHeight (v0_y, y0, g):
    y_max = y0 + (v0_y**2)/(2*g)
    return y_max

#Gets height of a projectile at given point
def getHeight (y0, v0_y, g, t):
    height = y0 + (v0_y*t) -(.5*g*t**2)
    return height

#Gets impact velocity of projectile
def impactVelo (v0_x, v0_y, g, totalTime):
    vfx = v0_x
    vfy = v0_y - (g * totalTime)
    v_impact = np.sqrt(vfx**2+vfy**2)
    return v_impact

def printValues (totalTime, totalRange, y_max, vfinal):
    print(f"Time of flight:", totalTime, "seconds")
    print("Range:", totalRange, "meters")
    print("Max Height of Projectile:", y_max, "meters")
    print("Impact Velocity: ", vfinal, "meters per second")

def projectilePlot (t_points, y_points):
    # Creates plot
    plt.plot(t_points, y_points, marker='o', color='b', linestyle='-')
    # Labels
    plt.xlabel("Time (seconds)")
    plt.ylabel("Height (m)")
    plt.title("Projectile Motion: Height vs Time")
    plt.grid(True)
    plt.show()

#Constants
g = 9.81

#Begins taking user input
v0 = float(input("Enter initial velocity (m/s): "))
theta = float(input("Enter Launch Angle (degrees):"))
y0 = float(input("Enter initial height (m): "))
#converts theta to radians
thetaR = np.radians(theta)

#Break Up Magnitude of v0 into components
v0_x = v0 * np.cos(thetaR)
v0_y = v0 * np.sin(thetaR)

#Calculations/functions
totalTime = t_flight(v0_y, y0, g)
totalRange = getRange(v0_x, totalTime)
y_max = maxHeight (v0_y, y0, g)
vfinal = impactVelo(v0_x, v0_y, g, totalTime)

#prints values
printValues (totalTime, totalRange, y_max, vfinal)

#Creates arrays of time intervals and points of y
t_points = np.linspace(0, totalTime, 25)
y_points = getHeight (y0, v0_y, g, t_points)
#Creates plot
projectilePlot (t_points, y_points)







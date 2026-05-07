import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#Finds time of TOTAL flight
def t_flight (v0_z, y0, g):
    a = -.5*g
    b = v0_z
    c = y0
    discriminant = (b**2) - (4*a*c)
    #  check if less than 0
    t1 = (-b + (np.sqrt(discriminant)))/(2*a)  # uses quadratic formula
    t2 = (-b - (np.sqrt(discriminant)))/(2*a)
    t_flight = max(t1, t2)
    return t_flight

def getRange3d(v0_x, v0_y, t_flight):
    xf = v0_x * t_flight
    yf = v0_y * t_flight
    return np.sqrt(xf**2 + yf**2)

def maxHeight (v0z, z0, g):
    return z0 + (v0_z**2) / (2 * g )

#Gets range of projectile
def getCoords (v0_x, v0_y, v0_z, y0, g, t):
    x = v0_x * t
    y = v0_y * t
    z = y0 + (v0_z * t) - (0.5 * g * t ** 2)
    return x, y, z

#Gets impact velocity of projectile
def impactVelo (v0_x, v0_y, v0_z,  g, totalTime):
    vfx = v0_x
    vfy = v0_y
    vfz = v0_z - (g * totalTime)
    return np.sqrt(vfx ** 2 + vfy ** 2 + vfz ** 2)

#Constants
g = 9.81

#Begins taking user input
v0 = float(input("Enter initial velocity (m/s): "))
theta = float(input("Enter Launch Angle (degrees from horizontal):"))
phi = float(input("Enter Azimuthal Angle (degrees from the x-axis):"))
z0 = float(input("Enter initial height (m): "))

#converts theta to radians
thetaR = np.radians(theta)
phiR = np.radians(phi)

#Break Up Magnitude of v0 into components
v0_z = v0 * np.sin(thetaR)
v0_horiz = v0 * np.cos(thetaR)
v0_x = v0_horiz * np.cos(phiR)
v0_y = v0_horiz * np.sin(phiR)

#Calculations/functions
totalTime = t_flight(v0_z, z0, g)
totalRange = getRange3d(v0_x, v0_y, totalTime)
z_max = maxHeight (v0_z, z0, g)
vfinal = (impactVelo (v0_x, v0_y, v0_z, g, totalTime))

#prints values
print("\n--- Results ---")
print(f"Time of Flight: {totalTime:.2f} seconds")
print(f"Total 3D Range: {totalRange:.2f} meters")
print(f"Maximum Height: {z_max:.2f} meters")
print(f"Impact Velocity:{vfinal:.2f} meters per second")
print("---------------------------------")

#Creates arrays of time intervals and points of y
t_points = np.linspace(0, totalTime, 25)
x_p, y_p, z_p = getCoords(v0_x, v0_y, v0_z, z0, g, t_points)

#Creates plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_p, y_p, z_p, marker='o', color='b')

ax.set_xlabel('X-Distance (m)')
ax.set_ylabel('Y-Distance (m)')
ax.set_zlabel('Z-Height (m)')
plt.title("3D Projectile Trajectory")
plt.show()





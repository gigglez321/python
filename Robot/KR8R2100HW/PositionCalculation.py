from sympy import symbols, Eq, solve, trigsimp, simplify
from sympy import sin
from sympy import cos

from math import pi

from numpy import array as matrix

# from DrawingVectors import theraVar

theta1, theta2, theta3, theta4, theta5, theta6 = symbols("theta1 theta2 theta3 theta4 theta5 theta6")

robMatrix = [[-(((-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*sin(theta4) - 1.0*cos(theta1)*cos(theta4)*cos(theta2 + theta3))*cos(theta5) + (6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1) + 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1.0*sin(theta2 + theta3)*cos(theta1))*sin(theta5))*cos(theta6) + (6.12323399573677e-17*((-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*sin(theta4) - 1.0*cos(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) - 1.0*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) - 6.12323399573677e-17*(6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1) + 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1.0*sin(theta2 + theta3)*cos(theta1))*cos(theta5) + 3.74939945665464e-33*sin(theta1) - 1.0*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 6.12323399573677e-17*sin(theta2 + theta3)*cos(theta1))*sin(theta6),
  1.0*(((-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*sin(theta4) - 1.0*cos(theta1)*cos(theta4)*cos(theta2 + theta3))*cos(theta5) + (6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1) + 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1.0*sin(theta2 + theta3)*cos(theta1))*sin(theta5))*sin(theta6) + 1.0*(6.12323399573677e-17*((-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*sin(theta4) - 1.0*cos(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) - 1.0*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) - 6.12323399573677e-17*(6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1) + 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1.0*sin(theta2 + theta3)*cos(theta1))*cos(theta5) + 3.74939945665464e-33*sin(theta1) - 1.0*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 6.12323399573677e-17*sin(theta2 + theta3)*cos(theta1))*cos(theta6),
  -1.0*((-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*sin(theta4) - 1.0*cos(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) - 6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 1.0*(6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1) + 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1.0*sin(theta2 + theta3)*cos(theta1))*cos(theta5) + 2.29584502165847e-49*sin(theta1) - 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 3.74939945665464e-33*sin(theta2 + theta3)*cos(theta1),
  50*(((-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*sin(theta4) - 1.0*cos(theta1)*cos(theta4)*cos(theta2 + theta3))*cos(theta5) + (6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1) + 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1.0*sin(theta2 + theta3)*cos(theta1))*sin(theta5))*cos(theta6) - 100.0*((-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*sin(theta4) - 1.0*cos(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) - 6.12323399573677e-15*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 100.0*(6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1) + 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1.0*sin(theta2 + theta3)*cos(theta1))*cos(theta5) - 50*(6.12323399573677e-17*((-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*sin(theta4) - 1.0*cos(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) - 1.0*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) - 6.12323399573677e-17*(6.12323399573677e-17*(-1.0*sin(theta1) + 3.06161699786838e-17*sin(-theta1 + theta2 + theta3) + 3.06161699786838e-17*sin(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1) + 6.12323399573677e-17*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1.0*sin(theta2 + theta3)*cos(theta1))*cos(theta5) + 3.74939945665464e-33*sin(theta1) - 1.0*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 6.12323399573677e-17*sin(theta2 + theta3)*cos(theta1))*sin(theta6) - 6.00076931582209e-14*sin(theta1)*sin(theta2) - 2.8421709430404e-14*sin(theta1)*sin(theta2 + theta3) + 6.21508250567282e-14*sin(theta1) - 6.12323399573677e-15*sin(theta4)*cos(theta1)*cos(theta2 + theta3) + 1015.0*sin(theta2 + theta3)*cos(theta1) + 980.0*cos(theta1)*cos(theta2) + 220.0*cos(theta1)*cos(theta2 + theta3) + 160.0*cos(theta1)],
 [-(((1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*sin(theta4) - 1.0*sin(theta1)*cos(theta4)*cos(theta2 + theta3))*cos(theta5) + (6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1.0*sin(theta1)*sin(theta2 + theta3) - 6.12323399573677e-17*cos(theta1))*sin(theta5))*cos(theta6) - (-6.12323399573677e-17*((1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*sin(theta4) - 1.0*sin(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) + 1.0*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*(6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1.0*sin(theta1)*sin(theta2 + theta3) - 6.12323399573677e-17*cos(theta1))*cos(theta5) + 1.0*sin(theta1)*sin(theta4)*cos(theta2 + theta3) - 6.12323399573677e-17*sin(theta1)*sin(theta2 + theta3) + 3.74939945665464e-33*cos(theta1))*sin(theta6),
  1.0*(((1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*sin(theta4) - 1.0*sin(theta1)*cos(theta4)*cos(theta2 + theta3))*cos(theta5) + (6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1.0*sin(theta1)*sin(theta2 + theta3) - 6.12323399573677e-17*cos(theta1))*sin(theta5))*sin(theta6) - 1.0*(-6.12323399573677e-17*((1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*sin(theta4) - 1.0*sin(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) + 1.0*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*(6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1.0*sin(theta1)*sin(theta2 + theta3) - 6.12323399573677e-17*cos(theta1))*cos(theta5) + 1.0*sin(theta1)*sin(theta4)*cos(theta2 + theta3) - 6.12323399573677e-17*sin(theta1)*sin(theta2 + theta3) + 3.74939945665464e-33*cos(theta1))*cos(theta6),
  -1.0*((1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*sin(theta4) - 1.0*sin(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) - 6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 1.0*(6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1.0*sin(theta1)*sin(theta2 + theta3) - 6.12323399573677e-17*cos(theta1))*cos(theta5) - 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 3.74939945665464e-33*sin(theta1)*sin(theta2 + theta3) - 2.29584502165847e-49*cos(theta1),
  50*(((1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*sin(theta4) - 1.0*sin(theta1)*cos(theta4)*cos(theta2 + theta3))*cos(theta5) + (6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1.0*sin(theta1)*sin(theta2 + theta3) - 6.12323399573677e-17*cos(theta1))*sin(theta5))*cos(theta6) - 100.0*((1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*sin(theta4) - 1.0*sin(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) - 6.12323399573677e-15*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 100.0*(6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1.0*sin(theta1)*sin(theta2 + theta3) - 6.12323399573677e-17*cos(theta1))*cos(theta5) + 50*(-6.12323399573677e-17*((1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*sin(theta4) - 1.0*sin(theta1)*cos(theta4)*cos(theta2 + theta3))*sin(theta5) + 1.0*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*(6.12323399573677e-17*(1.0*cos(theta1) + 3.06161699786838e-17*cos(-theta1 + theta2 + theta3) - 3.06161699786838e-17*cos(theta1 + theta2 + theta3))*cos(theta4) + 6.12323399573677e-17*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1.0*sin(theta1)*sin(theta2 + theta3) - 6.12323399573677e-17*cos(theta1))*cos(theta5) + 1.0*sin(theta1)*sin(theta4)*cos(theta2 + theta3) - 6.12323399573677e-17*sin(theta1)*sin(theta2 + theta3) + 3.74939945665464e-33*cos(theta1))*sin(theta6) - 6.12323399573677e-15*sin(theta1)*sin(theta4)*cos(theta2 + theta3) + 1015.0*sin(theta1)*sin(theta2 + theta3) + 980.0*sin(theta1)*cos(theta2) + 160.0*sin(theta1) + 6.00076931582203e-14*sin(theta2)*cos(theta1) - 110.0*sin(-theta1 + theta2 + theta3) + 110.0*sin(theta1 + theta2 + theta3) - 6.21508250567282e-14*cos(theta1)],
 [((6.12323399573677e-17*(cos(theta2 + theta3) + 1)*sin(theta4) + 1.0*sin(theta2 + theta3)*cos(theta4))*cos(theta5) + (3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) + 1.0*cos(theta2 + theta3) - 3.74939945665464e-33)*sin(theta5))*cos(theta6) - (6.12323399573677e-17*(6.12323399573677e-17*(cos(theta2 + theta3) + 1)*sin(theta4) + 1.0*sin(theta2 + theta3)*cos(theta4))*sin(theta5) - 6.12323399573677e-17*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*(3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) + 1.0*cos(theta2 + theta3) - 3.74939945665464e-33)*cos(theta5) + 1.0*sin(theta4)*sin(theta2 + theta3) + 6.12323399573677e-17*cos(theta2 + theta3) - 2.29584502165847e-49)*sin(theta6),
  -1.0*((6.12323399573677e-17*(cos(theta2 + theta3) + 1)*sin(theta4) + 1.0*sin(theta2 + theta3)*cos(theta4))*cos(theta5) + (3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) + 1.0*cos(theta2 + theta3) - 3.74939945665464e-33)*sin(theta5))*sin(theta6) - 1.0*(6.12323399573677e-17*(6.12323399573677e-17*(cos(theta2 + theta3) + 1)*sin(theta4) + 1.0*sin(theta2 + theta3)*cos(theta4))*sin(theta5) - 6.12323399573677e-17*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*(3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) + 1.0*cos(theta2 + theta3) - 3.74939945665464e-33)*cos(theta5) + 1.0*sin(theta4)*sin(theta2 + theta3) + 6.12323399573677e-17*cos(theta2 + theta3) - 2.29584502165847e-49)*cos(theta6),
  1.0*(6.12323399573677e-17*(cos(theta2 + theta3) + 1)*sin(theta4) + 1.0*sin(theta2 + theta3)*cos(theta4))*sin(theta5) + 3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 1.0*(3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) + 1.0*cos(theta2 + theta3) - 3.74939945665464e-33)*cos(theta5) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) - 3.74939945665464e-33*cos(theta2 + theta3) + 1.40579962855621e-65,
  -50*((6.12323399573677e-17*(cos(theta2 + theta3) + 1)*sin(theta4) + 1.0*sin(theta2 + theta3)*cos(theta4))*cos(theta5) + (3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) + 1.0*cos(theta2 + theta3) - 3.74939945665464e-33)*sin(theta5))*cos(theta6) + 100.0*(6.12323399573677e-17*(cos(theta2 + theta3) + 1)*sin(theta4) + 1.0*sin(theta2 + theta3)*cos(theta4))*sin(theta5) + 3.74939945665464e-31*(cos(theta2 + theta3) + 1)*cos(theta4) - 100.0*(3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) + 1.0*cos(theta2 + theta3) - 3.74939945665464e-33)*cos(theta5) + 50*(6.12323399573677e-17*(6.12323399573677e-17*(cos(theta2 + theta3) + 1)*sin(theta4) + 1.0*sin(theta2 + theta3)*cos(theta4))*sin(theta5) - 6.12323399573677e-17*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*(3.74939945665464e-33*(cos(theta2 + theta3) + 1)*cos(theta4) - 6.12323399573677e-17*sin(theta4)*sin(theta2 + theta3) + 1.0*cos(theta2 + theta3) - 3.74939945665464e-33)*cos(theta5) + 1.0*sin(theta4)*sin(theta2 + theta3) + 6.12323399573677e-17*cos(theta2 + theta3) - 2.29584502165847e-49)*sin(theta6) + 980.0*sin(theta2) - 6.12323399573677e-15*sin(theta4)*sin(theta2 + theta3) + 220.0*sin(theta2 + theta3) - 1015.0*cos(theta2 + theta3) + 520.0],
 [0, 0, 0, 1.00000000000000]]


pointTCP = [robMatrix[0][3], robMatrix[1][3], robMatrix[2][3]]

print(f"x:{robMatrix[0][3]} \n")
print(f"x:{robMatrix[1][3]} \n")
print(f"x:{robMatrix[2][3]} \n")
import numpy as np
import math

dM1 = [1,1]
dP1 = [1,1]
dM2 = [-1,1]
dP2 = [-1,1]
dM3 = [-1,-1]
dP3 = [-1,-1]
dM4 = [1,-1]
dP4 = [1,-1]

def DipoleForce(dipoleMoment1, dipolePosition1, dipoleMoment2, dipolePosition2):
    m1 = np.array(dipoleMoment1)
    m2 = np.array(dipoleMoment2)
    R = np.array(dipolePosition2) - np.array(dipolePosition1)
    mag_R = np.sqrt(R.dot(R))
    mu = 4 * math.pi * pow(10,-7)
    coefficient =  (3*mu)/(4*math.pi*pow(mag_R,5))
    first_term = m1.dot(R)*m2
    second_term = m2.dot(R)*m1
    third_term = m1.dot(m2)*R
    fourth_term = R* (5* m1.dot(R) * m2.dot(R))/(pow(mag_R,2))
    return coefficient * (first_term + second_term + third_term - fourth_term)

print(DipoleForce(dM1,dP1,dM2,dP2)+DipoleForce(dM1,dP1,dM3,dP3)+DipoleForce(dM1,dP1,dM4,dP4))

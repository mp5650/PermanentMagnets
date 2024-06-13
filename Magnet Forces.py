import math

# Sets up a list of lists. Each list represents a cross-section of the stellarator and each item in the nested list
# represents the strength of each magnet going counterclockwise around the cross-section
MagnetMatrix = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]

toroidal_resolution = len(MagnetMatrix) # Number of circular cross-sections
toroidal_radius = 10 # radius of the toroid
poloidal_resolution = len(MagnetMatrix[0]) # number of magnets in a circular cross-section
poloidal_radius = 1 # radius of the stellarator cross-section


def MagneticForce(toroidal1_index, poloid1_index, toroidal2_index, poloid2_index):
    magnet1_strength = MagnetMatrix[toroidal1_index][poloid1_index] #gets strengths of magnets from Magnet Vector using thew input indices
    magnet2_strength = MagnetMatrix[toroidal2_index][poloid2_index]
    mu = 12.57 * (10**(-7)) # Permeabiltiy of a vacuum, should replace with permeability of a plasma
    theta1 = (2*math.pi / poloidal_resolution)* poloid1_index
    phi1 = (2*math.pi / toroidal_resolution) * toroidal1_index
    theta2 = (2*math.pi / poloidal_resolution) * poloid2_index
    phi2 = (2*math.pi / toroidal_resolution) * toroidal2_index
    theta= theta2-theta1# Angle around cross section
    phi = phi2-phi1 # Angle around torus
    # redo distances by first defining the position of the magnets and then finding the difference
    position1 = [math.cos(phi1)*(toroidal_radius+(math.cos(theta1)*poloidal_radius)),
                  poloidal_radius * math.sin(theta1),
                  toroidal_radius * math.sin(phi1)]
    position2 = [math.cos(phi2) * (toroidal_radius + (math.cos(theta2) * poloidal_radius)),
                 poloidal_radius * math.sin(theta2),
                 toroidal_radius * math.sin(phi2)]
    distance_x = position2[0]-position1[0]
    distance_y = position2[1]-position1[1]
    distance_z = position2[2]-position1[2]
    distance = math.sqrt(pow(distance_x,2)+pow(distance_y,2)+pow(distance_z,2))
    # Magnet force calculated using F=(u*m1*m2)/(4pi*distance), multiplied by a cos(theta) and cos(phi) terms to account
    # for how magnet orientation affects force (perpendicular magnets apply zero force and parrallel apply max force
    # Returns a list which includes the x,y and z components of force
    return ((mu*magnet1_strength*magnet2_strength)/(4*math.pi*distance))*math.cos(theta)*math.cos(phi)



#The part below produces a matrix of the total net force on each magnet
ForceMatrix = []
for cross_section1 in range(len(MagnetMatrix)):
    ForceMatrix.append([])
    for magnet1 in range(len(MagnetMatrix[cross_section1])):
        force_on_magnet = 0
        for cross_section2 in range(len(MagnetMatrix)):
            for magnet2 in range(len(MagnetMatrix[cross_section2])):
                if cross_section1 != cross_section2:
                    force_on_magnet += MagneticForce(cross_section1,magnet1,cross_section2,magnet2)
                elif cross_section1 == cross_section2 and magnet1 != magnet2:
                    force_on_magnet += MagneticForce(cross_section1, magnet1, cross_section2, magnet2)
        ForceMatrix[cross_section1].append(force_on_magnet)

print(ForceMatrix)



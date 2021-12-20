import math
def gamma(T,atomicMass,u1):
    return (T/(float(atomicMass)*u1))+1
def beta(gamma):
    return math.sqrt(1-(1/(gamma**2)))

atomicMass=input("Enter the Atomic mass : ") #A
Q=input("Enter positive state : ")
q=float(Q)*(1.6e-19) #q is the charge of the particle

kineticEnergy=input("Enter the Kinetic Energy in AMeV : ")

T=float(kineticEnergy)*float(atomicMass) #Kinetic Energy T in MeV

u1=931.494 #MeV/C^2
u2=1.6666e-27 #kg

m0=float(atomicMass)*u2 #in Kg

c=3e8 #speed of light in m/s

gamma=gamma(T,atomicMass,u1)
beta=beta(gamma)
print("gamma = ",gamma)
print("beta = ",beta)

Bp=(gamma*beta*c*m0)/q #B is magnetic Field and p is bending radius

print("Bp = ",Bp," Tesla meter")

import numpy as np
from scipy import optimize

## reactor volume
d = float(input("Enter diameter of the reactor in cm:")) # cm
L = float(input("Enter length of the reactor in cm:")) # cm
V_re = np.pi*(d**2)/4*L # cm3

## conditions
T = float(input("Enter reaction temperature in degree Celcius:")) # degree Celcius
percent_load = float(input("Enter load of water in the reactor (e.g. 0.8 for 80%):"))


V_water_amb = percent_load*V_re # cm3
V_air_amb = (1-percent_load)*V_re # cm3

## molar amount of water and air
MW_water = 18.015 # g/mol
rho_water = 1 # g/cm3 at ambient
n_water_total = V_water_amb*rho_water/MW_water # mol

MW_air = 28.97 # g/mol
rho_air = 0.001225 # g/cm3 at ambient
n_air = V_air_amb*rho_air/MW_air # mol

## vapor pressure of water
# constants
c1 = 73.649
c2 = -7258.2
c3 = -7.3037
c4 = 4.1653E-06
c5 = 2
# P_sat = exp(c1+c2/T+c3lnT+c4T^c5) from Perry's handbook
T_abs = T+273.15 # Kelvin
P_sat = np.exp(c1+c2/T_abs+c3*np.log(T_abs)+c4*T_abs**c5)*1E-05 #bar

## compressed liquid density
# water properties
Tc = 647.14 # Kelvin
Pc = 220.64 # bar
Vc = 55.95 # critical liquid volume, cm3/mol
Zc = 0.229 # critical compressibility factor
omega = 0.344
# reduced temperature
Tr = T_abs/Tc
# constants, correlation for compressed liquid
a0 = -170.335
a1= -28.578
a2 = 124.809
a3 = -55.5393
a4 = 130.01
b0 = 0.164813
b1 = -0.0914427
A = a0+a1*Tr+a2*Tr**3+a3*Tr**6+a4/Tr
B = b0+omega*b1
C = np.exp(1)
D = 1.00578
# saturated liquid volume
Vs = Vc*Zc**(1-Tr)**(2/7)
    
def fun(P):
    # volume of water at reaction temperature
    V_b = Vs*(n_water_total-n_air*P_sat/(P-P_sat))*(A*Pc+C**((D-Tr)**B)*(P-P_sat))/(A*Pc+C*(P-P_sat))
    # volume of air and vapor in gas phase
    V_a = n_air*83.14*T_abs/(P-P_sat)

    return (V_a+V_b)-V_re

sol = optimize.fsolve(fun,x0=P_sat+0.01)
P = sol[0]
print('Reactor pressure becomes {0:.2f} bar after heating.'.format(P))

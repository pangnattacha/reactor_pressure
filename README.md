# Reactor pressure
## Introduction
This is a project to calculate pressure inside a reactor when water inside the reactor is heated and the reactor is completely closed. That is, water and air inside the reactor do not leak out. Vaporization of water takes place during the process. Therefore, the pressure indside the reactor increases over saturated pressure and liquid water is compressed . 

## Problem setting
<img src="https://github.com/pangnattacha/reactor_pressure/blob/master/reactor.png" width="30%" height="30%">

Water is filled in designated percent load (e.g. 80%) of total volume of reactor (V_re). The initial volume of water (V_water) is then equal to 0.8V_re. Assuming that water in air is neglegible, and thus volume of space is volume of the air (V_air = V_re-V_water). Then the reactor is closed and heated to designated temperatures (e.g. 200 degree celcius). Partially, water vaporizes into gas phase, thus volume of liquid water consequently changes. The new volumes of gas phase and water become V_a and V_b, respectively. What is the new pressure in the reactor?

### Libraries used for this problem
- NumPy
- SciPy.Optimize

## Solution
#### At ambient conditions
<img src="https://latex.codecogs.com/gif.latex?%5Crho_%7Bwater%7D"> = 1 g/cm3 </br>
<img src="https://latex.codecogs.com/gif.latex?%5Crho_%7Bair%7D"> = 0.001225 g/cm3 </br>

Calculate molar amount of water and air by </br>
<img src="https://latex.codecogs.com/gif.latex?n%3D%20%5Cfrac%7BV*%5Crho%7D%7Bmolecular%20weight%7D">, mol
#### At reaction temperature
1. Calculate saturated pressure (P_sat) of water at reaction temperature to find equilibrium of water in liquid and gas phases.[1]</br>

    <img src="https://latex.codecogs.com/gif.latex?P_%7Bsat%7D%20%3D%20exp%28C1&plus;C2/T&plus;C3lnT&plus;C4T%5E%7BC5%7D%29">, MPa </br>

2. Calculate saturated volume (V_sat) of water [2]</br>

    <img src="https://latex.codecogs.com/gif.latex?V_%7Bsat%7D%20%3D%20V_cZ_c%5E%7B1-%28T/T_c%29%5E%7B2/7%7D%7D">, cm3/mol

3. Calculate compressed volume using the equation of Chang and Zhao (1990) [2] </br>

    <img src="https://latex.codecogs.com/gif.latex?V%3DV_s%5Cfrac%7BAP_c&plus;C%5E%7B%28D-Tr%29%5EB%7D%28P-P_%7Bsat%7D%29%7D%7BAP_c&plus;C%28P-P_%7Bsat%7D%29%7D">, cm3/mol </br>

    A, B, C and D are the constants of Aalto et al.(1996), which can be found in the [code](https://github.com/pangnattacha/reactor_pressure/blob/master/reactor_pressure.py).

    Then, calculate mole of vapor using [Raoult's law](https://chemistry.tutorvista.com/inorganic-chemistry/raoults-law.html): </br>

    <img src="https://latex.codecogs.com/gif.latex?y_%7Bvapor%7D%3D%5Cfrac%7Bn_%7Bvapor%7D%7D%7Bn_%7Bvapor%7D&plus;n_%7Bair%7D%7D%3D%5Cfrac%7BP_%7Bsat%7D%7D%7BP%7D"></br>
    <img src="https://latex.codecogs.com/gif.latex?n_%7Bvapor%7D%3Dn_%7Bair%7D%5Cfrac%7BP_%7Bsat%7D%7D%7BP-P_%7Bsat%7D%7D">, mol

    where y_vapor is vapor molar fraction in gas phase, n_i is mole of gas i.

    Therefore, mole of water in liquid phase after heating is n_water-n_vap and thus</br>

    V_b = (n_water-n_vapor)*V, cm3

4. Calculate volume of gas phase (V_a) using the [ideal gas law](https://en.wikipedia.org/wiki/Ideal_gas_law):</br>

    PV = nRT, where R is gas constant and T is temperature in Kelvin.</br>

    V_a = n_air*RT/(P-P_sat)
    
5. Solve P that makes V_re = V_a + V_b

## Citations
[1] Don W. Green, Robert H. Perry, McGraw-Hill Professional. (2008). Perry's Chemical Engineers' Handbook, Eighth Edition. VAPOR PRESSURES OF PURE SUBSTANCES, Chapter. </br>
[2] E. Poling, Bruce & M. Prausnitz, John & O'Connell, John. (2000). The Properties of Gases and Liquids. 

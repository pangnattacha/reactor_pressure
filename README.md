# Reactor pressure
## Introduction
This is a project to calculate pressure inside a reactor when water inside the reactor is heated and the reactor is completely closed. That is, water and air inside the reactor do not leak out. Vaporization of water takes place during the process. Therefore, the pressure indside the reactor increases over saturated pressure and liquid water is compressed . 

## Problem setting
<img src="https://github.com/pangnattacha/reactor_pressure/blob/master/reactor.png" width="30%" height="30%">

Water is filled in designated percent load (e.g. 80%) of total volume of reactor (V_re). The initial volume of water (V_water) is then equal to 0.8V_re. Assuming that water in air is neglegible, and thus volume of space is volume of the air (V_air = V_re-V_water). Then the reactor is closed and heated to designated temperatures (e.g. 200 degree celcius). Partially, water vaporizes into gas phase, thus volume of liquid water consequently changes. The new volumes of gas phase and water become V_a and V_b, respectively.

### Libraries used for this problem
- NumPy
- SciPy.Optimize

## Solution
#### At ambient conditions
<img src="https://latex.codecogs.com/gif.latex?%5Crho_%7Bwater%7D"> = 1 g/cm3

<img src="https://latex.codecogs.com/gif.latex?%5Crho_%7Bair%7D"> = 0.001225 g/cm3

Calculate molar amount of water and air by 

<img src="https://latex.codecogs.com/gif.latex?n%3D%20%5Cfrac%7BV*%5Crho%7D%7Bmolecular%20weight%7D">, mol

#### At reaction temperature
1. Calculate P_sat of water at reaction temperature to find equilibrium of water in liquid and gas phases.

<img src="https://latex.codecogs.com/gif.latex?P_%7Bsat%7D%20%3D%20exp%28C1&plus;C2/T&plus;C3lnT&plus;C4T%5E%7BC5%7D%29">

2. Calculate V_sat of water
<img src="https://latex.codecogs.com/gif.latex?V_%7Bsat%7D%20%3D%20V_cZ_c%5E%7B1-%28T/T_c%29%5E%7B2/7%7D%7D">

## Citations
[1] Don W. Green, Robert H. Perry, McGraw-Hill Professional. (2008). Perry's Chemical Engineers' Handbook, Eighth Edition. VAPOR PRESSURES OF PURE SUBSTANCES, Chapter.
[2] E. Poling, Bruce & M. Prausnitz, John & O'Connell, John. (2000). The Properties of Gases and Liquids. 

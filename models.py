# models.py
import numpy as np
from config import *

def calculate_k(T):
    return k_300 * np.exp((E_a / R) * (1/300 - 1/T))

def calculate_Kc(T):
    return Kc_450 * np.exp((-dH_rx / R) * (1/450 - 1/T))

def equilibrium_conversion(T):
    Kc = calculate_Kc(T)
    a = C_A0
    b = -(2 * C_A0 + 1 / Kc)
    c = C_A0
    return (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)

def pfr_adiabatic(V, y):
    X, T = y
    k = calculate_k(T)
    Kc = calculate_Kc(T)
    
    r_A = -k * C_A0**2 * ((1 - X)**2 - X / (C_A0 * Kc))
    
    dX_dV = -r_A / F_A0
    dT_dV = (-r_A * -dH_rx) / (F_A0 * sum_CP)
    
    return [dX_dV, dT_dV]

# Add this function to the bottom of models.py

def pfr_constant_Ta(V, y):
    X, T = y
    k = calculate_k(T)
    Kc = calculate_Kc(T)
    
    # Rate law
    r_A = -k * C_A0**2 * ((1 - X)**2 - X / (C_A0 * Kc))
    
    # Mole and Energy Balances (with heat exchanger term)
    dX_dV = -r_A / F_A0
    dT_dV = (Ua * (T_a - T) + (-r_A * -dH_rx)) / (F_A0 * sum_CP)
    
    return [dX_dV, dT_dV]
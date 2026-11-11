import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# Update the import line to include the new model
from models import pfr_adiabatic, pfr_constant_Ta, equilibrium_conversion

V_span = [0, 10]
V_eval = np.linspace(0, 10, 500)
y0 = [0.0, 300.0]

# Solve Part (a) - Adiabatic
sol_a = solve_ivp(pfr_adiabatic, V_span, y0, t_eval=V_eval, method='Radau')
X_out_a = sol_a.y[0]
T_out_a = sol_a.y[1]
X_eq_a = [equilibrium_conversion(T) for T in T_out_a]

# Solve Part (b) - Constant Coolant Temperature
sol_b = solve_ivp(pfr_constant_Ta, V_span, y0, t_eval=V_eval, method='Radau')
X_out_b = sol_b.y[0]
T_out_b = sol_b.y[1]
X_eq_b = [equilibrium_conversion(T) for T in T_out_b]

# Plotting Both Systems
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Conversion Plot
ax1.plot(V_eval, X_out_a, label='(a) PFR Conv. (Adiabatic)', color='#1f77b4')
ax1.plot(V_eval, X_out_b, label='(b) PFR Conv. (Constant $T_a$)', color='#2ca02c')
ax1.plot(V_eval, X_eq_a, label='(a) $X_{eq}$ (Adiabatic)', color='#1f77b4', linestyle='--')
ax1.plot(V_eval, X_eq_b, label='(b) $X_{eq}$ (Constant $T_a$)', color='#2ca02c', linestyle='--')
ax1.set_xlabel('Volume (dm³)')
ax1.set_ylabel('Conversion')
ax1.set_title('Conversion vs Volume')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Temperature Plot
ax2.plot(V_eval, T_out_a, label='(a) Temp (Adiabatic)', color='#1f77b4')
ax2.plot(V_eval, T_out_b, label='(b) Temp (Constant $T_a$)', color='#2ca02c')
ax2.axhline(450, color='gray', linestyle=':', label='Coolant $T_a$ (450 K)')
ax2.set_xlabel('Volume (dm³)')
ax2.set_ylabel('Temperature (K)')
ax2.set_title('Temperature vs Volume')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
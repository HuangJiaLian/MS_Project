import matplotlib.pyplot as plt 

import matplotlib.pyplot as plt
import numpy as np

# Crystals          AlH3    RbAlH4      Rb5Al3H14   Rb3AlH6      RbH
# RbH(%)            0/4     2/6         10/22       6/10         2/2
# RbH(%)            0       33.33       45.45       60          100
# E_f/atom (eV)     0      -0.145593986 -0.067463493 -0.089290582 0
# rho H2(1/Ang.^3)  0.03205 0.01860     0.02057     0.01709     0.00904

# Data
crystals = ['AlH3', 'RbAlH4', 'Rb5Al3H14', 'Rb3AlH6', 'RbH']
rbh_percent = [0, 33.33, 45.45, 60, 100]
formation_energy = [0, -0.145593986, -0.067463493, -0.089290582, 0]
H2_density = [0.03205, 0.01860, 0.02057, 0.01709, 0.00904]

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.grid(True)
plt.scatter(rbh_percent, formation_energy)
plt.xlabel('Percentage of RbH')
plt.ylabel('Formation energy/atom [eV]')
plt.title('Phase Diagram of Crystals - Formation Energy')
plt.tick_params(direction='in')
for i, crystal in enumerate(crystals):
    plt.text(rbh_percent[i]-1, formation_energy[i], crystal, fontsize=8, ha='right')

plt.subplot(2, 1, 2)
plt.grid(True)
plt.scatter(rbh_percent, H2_density, color='green', marker='s')
plt.xlabel('Percentage of RbH')
plt.ylabel('H2 density [Å$^{-3}$]')
plt.title('Phase Diagram of Crystals - H2 Density')
plt.tick_params(direction='in')
for i, crystal in enumerate(crystals):
    plt.text(rbh_percent[i]-1, H2_density[i], crystal, fontsize=8, ha='right')

plt.tight_layout()
plt.savefig('phasediaRbH.png')
plt.savefig('phasediaRbH.pdf')
plt.show()




import matplotlib.pyplot as plt
import numpy as np

# Crystals          AlH3    RbAlH4      Rb5Al3H14   Rb3AlH6      RbH
# RbH(%)            0/4     2/6         10/22       6/10         2/2
# RbH(%)            0       33.33       45.45       60          100
# E_f/atom (eV)     0      -0.145593986 -0.067463493 -0.089290582 0
# rho H2(1/Ang.^3)  0.03205 0.01860     0.02057     0.01709     0.00904

# Data
crystals = ['AlH$_3$', 'RbAlH$_4$', 'Rb$_5$Al$_3$H$_{14}$', 'Rb$_3$AlH$_6$', 'RbH']
rbh_percent = [0, 33.33, 45.45, 60, 100]
formation_energy = [0, -0.145593986, -0.067463493, -0.089290582, 0]
H2_density = [0.03205, 0.01860, 0.02057, 0.01709, 0.00904]

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.scatter(rbh_percent, formation_energy)
plt.ylabel('E$_\mathrm{form}$/atom [eV]', fontsize=18)
plt.tick_params(direction='in', labelsize=12)
plt.xlim(-5, 112)
plt.ylim(-0.16, 0.03)
for i, crystal in enumerate(crystals):
    plt.text(rbh_percent[i]+8, formation_energy[i]+0.005, crystal, fontsize=16, ha='right', va='bottom')
plt.text(0.03, 0.1, '(a)', fontsize=16, fontweight='bold', transform=plt.gca().transAxes)

plt.subplot(2, 1, 2)
plt.scatter(rbh_percent, H2_density, color='green', marker='s')
plt.xlabel('Percentage of RbH', fontsize=18)
plt.ylabel('H$_2$ density [Å$^{-3}$]', fontsize=18)
plt.tick_params(direction='in', labelsize=12)
plt.xlim(-5, 112)
plt.ylim(0.006, 0.038)
for i, crystal in enumerate(crystals):
    plt.text(rbh_percent[i]+8, H2_density[i]+0.001, crystal, fontsize=16, ha='right', va='bottom')
plt.text(0.03, 0.1, '(b)', fontsize=16, fontweight='bold', transform=plt.gca().transAxes)

plt.tight_layout()
plt.savefig('phasediaRbH.png')
plt.savefig('phasediaRbH.pdf')
plt.show()




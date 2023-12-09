import matplotlib.pyplot as plt
import numpy as np


# This is demostration how we calculate the atomic fraction
# Crystals          AlH3    NaAlH4      Na5Al3H14   Na3AlH6      NaH
# NaH(%)            0/4     2/6         10/22       6/10         2/2
# NaH(%)            0       33.33       45.45       60          100



crystals = ['BH$_3$', 'LiBH$_4$', 'Li$_5$B$_3$H$_{14}$:sod', 'Li$_3$BH$_6:P1$', 'LiH']
atomic_fraction_of_XH = np.array([0, 33.33, 45.45, 60, 100])
# Fomation energy E [(eV)/atom]  
formation_energies =   np.array([[0,   -0.1733778826,  0.2945110488,  0.1313523268,   0],  # Before relaxation
                                 [0,   0,  0,  0.2376843637,   0], 
                                 [0,   0,  0,  0.2493945165,   0]]) # After relaxation 

# The dots need to be connected
convex_hull_idx_list = [[0, 1, 4],
                        [0, 1, 4], 
                        [0, 1, 4]
                        ]

numCrystals = len(crystals)
markers = ['s','v' , 'o', 'D', '^']

plt.figure(figsize=(5.5, 3))
# Plot line y = 0 
plt.axhline(y=0, color='gray', linestyle=':', lw=0.5)
plt.ylabel('E$_\mathrm{form}$ [eV/atom]', fontsize=18)
#plt.tick_params(labelbottom=False)
plt.xlabel('Atomic fraction of LiH [%]', fontsize=18)
plt.ylim(-0.2, 0.4)
# Plot vertical lines at the percentage of 0, 33.33, 45.45, 60, 100
for f in atomic_fraction_of_XH:
    plt.axvline(x=f, color='gray', linestyle='--', lw=0.3)
# Plot convex hull 
plt.plot(atomic_fraction_of_XH[convex_hull_idx_list[0]], formation_energies[0][convex_hull_idx_list[0]], 'black', lw=0.6, linestyle='-')
plt.scatter(atomic_fraction_of_XH, formation_energies[0], marker=markers[0], color='black', label='BH$_3$, LiBH$_4$, Li$_5$B$_3$H$_{14}$, Li$_3$BH$_6$, LiH')
plt.scatter(atomic_fraction_of_XH[3], formation_energies[1][3], marker='+', color='black', label='Li$_3$BH$_6$_R3')
plt.scatter(atomic_fraction_of_XH[3], formation_energies[2][3], marker='X', color='black', label='Li$_3$BH$_6$_sod')
plt.tick_params(direction='in', labelsize=12)
plt.xlim(-15, 115)
plt.tight_layout()
plt.legend(ncol=1, loc='upper left', frameon=False)
plt.savefig('phasediaBH3_LiH.png')
plt.savefig('phasediaBH3_LiH.pdf')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# This is demostration how we calculate the atomic fraction
# Crystals          AlH3    RbAlH4      Rb5Al3H14   Rb3AlH6      RbH
# RbH(%)            0/4     2/6         10/22       6/10         2/2
# RbH(%)            0       33.33       45.45       60          100



crystals = ['AlH$_3$', 'XAlH$_4$', 'X$_5$Al$_3$H$_{14}$', 'X$_3$AlH$_6$', 'XH']
atomic_fraction_of_XH = np.array([0, 33.33, 45.45, 60, 100])
# Fomation energy E [(eV)/atom]   # AlH3  (X)AlH4           (X)5Al3H14        (X)3AlH6       (X)H
formation_energies =   np.array([[0,    0.00940625384,    0.009556500753,  -0.0232288214,   0],  # Li
                                 [0,   -0.06348366911,   -0.0620795669,    -0.05635193381,  0],  # Na
                                 [0,   -0.1253529605,    -0.07825203177,   -0.08740277958,  0],  # K
                                 [0,   -0.145593986,     -0.067463493,     -0.089290582,    0],  # Rb
                                 [0,   -0.1596555026,    -0.05658973646,   -0.1011775038,   0]]) # Cs

# The dots need to be connected
convex_hull_idx_list = [[0, 3, 4],
                        [0, 1, 2, 3, 4], 
                        [0, 1, 3, 4], 
                        [0, 1, 3, 4], 
                        [0, 1, 3, 4]]

numCrystals = len(crystals)
markers = ['s','v' , 'o', 'D', '^']

plt.figure(figsize=(5.5, 8))
for i, X in enumerate(['Li', 'Na', 'K', 'Rb', 'Cs']):
    plt.subplot(5, 1, i+1)
    # Plot line y = 0 
    plt.axhline(y=0, color='gray', linestyle=':', lw=0.5)
    # Plot vertical lines at the percentage of 0, 33.33, 45.45, 60, 100
    for f in atomic_fraction_of_XH:
        plt.axvline(x=f, color='gray', linestyle='--', lw=0.3)
    # Plot convex hull 
    plt.plot(atomic_fraction_of_XH[convex_hull_idx_list[i]], formation_energies[i][convex_hull_idx_list[i]], 'black', lw=0.6)
    
    # Plot each the formation energy for each crystal
    for j in range(numCrystals):
        plt.scatter(atomic_fraction_of_XH[j], formation_energies[i][j], marker=markers[j], color='black', label=crystals[j])
    plt.tick_params(direction='in', labelsize=12)
    plt.xlim(-15, 115)
    plt.ylim(-0.19, 0.06)
    plt.xlabel('Atomic fraction of (X)H [%]', fontsize=18)
    if i ==2:
        plt.ylabel('E$_\mathrm{form}$ [eV/atom]', fontsize=18)
    if i != 4:
        plt.tick_params(labelbottom=False)
        plt.xlabel('')
    # (a) - (e)
    plt.annotate(f'({chr(97+i)})', xy=(0.02, 0.8), xycoords="axes fraction", fontsize=16)
    plt.annotate('X={}'.format(X), xy=(0.02, 0.1), xycoords="axes fraction", fontsize=16)

    # Legend at the top 
    if i == 0:
        plt.legend(ncol=5, columnspacing=0.1, handletextpad=0, loc='upper center', bbox_to_anchor=(0.5, 1.30), fontsize=12, frameon=False)
plt.subplots_adjust(hspace=0.02, wspace=0.01, left=0.15, bottom=0.1, right=0.99, top=0.95)
plt.savefig('phasediagram.png')
plt.savefig('phasediagram.pdf')
plt.show()

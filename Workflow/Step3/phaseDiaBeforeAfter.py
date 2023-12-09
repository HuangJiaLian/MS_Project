import matplotlib.pyplot as plt
import numpy as np


# This is demostration how we calculate the atomic fraction
# Crystals          AlH3    NaAlH4      Na5Al3H14   Na3AlH6      NaH
# NaH(%)            0/4     2/6         10/22       6/10         2/2
# NaH(%)            0       33.33       45.45       60          100



crystals = ['AlH$_3$', 'XAlH$_4$', 'X$_5$Al$_3$H$_{14}$', 'X$_3$AlH$_6$', 'XH']
atomic_fraction_of_XH = np.array([0, 33.33, 45.45, 60, 100])
# Fomation energy E [(eV)/atom]   # AlH3  NaAlH4           Na5Al3H14        Na3AlH6       NaH
formation_energies =   np.array([[0,     -0.06364545,     -0.06178818 ,   -0.05610553 ,   0],  # Before relaxation
                                 [0,    -0.06346385,    -0.06204824 ,     -0.05632537 ,  0]]) # After relaxation 

# The dots need to be connected
convex_hull_idx_list = [[0, 1, 2, 3, 4],
                        [0, 1, 2, 3, 4]]

numCrystals = len(crystals)
markers = ['s','v' , 'o', 'D', '^']

plt.figure(figsize=(5.5, 3))
# Plot line y = 0 
plt.axhline(y=0, color='gray', linestyle=':', lw=0.5)
plt.ylabel('E$_\mathrm{form}$ [eV/atom]', fontsize=18)
plt.tick_params(labelbottom=False)
plt.xlabel('')
for i, X in enumerate(['Pre', 'Post']):
    #plt.subplot(5, 1, i+1)
    # Plot vertical lines at the percentage of 0, 33.33, 45.45, 60, 100
    for f in atomic_fraction_of_XH:
        plt.axvline(x=f, color='gray', linestyle='--', lw=0.3)
    # Plot convex hull 
    plt.plot(atomic_fraction_of_XH[convex_hull_idx_list[i]], formation_energies[i][convex_hull_idx_list[i]], 'black', lw=0.6, linestyle='-' if i == 0 else '--')
    
    # Plot each the formation energy for each crystal
    # for j in range(numCrystals):
    #     plt.scatter(atomic_fraction_of_XH[j], formation_energies[i][j], marker=markers[j], color='blue' if i == 0 else 'red', label=crystals[j])
    plt.scatter(atomic_fraction_of_XH, formation_energies[i], marker=markers[i], color='blue' if i == 0 else 'red', label=X)
    plt.tick_params(direction='in', labelsize=12)
    plt.xlim(-15, 115)
    plt.ylim(-0.19, 0.06)
    plt.xlabel('Atomic fraction of (X)H [%]', fontsize=18)

    # (a) - (e)
    #plt.annotate(f'({chr(97+i)})', xy=(0.02, 0.8), xycoords="axes fraction", fontsize=16)
    #plt.annotate('X={}'.format(X), xy=(0.02, 0.1), xycoords="axes fraction", fontsize=16)

    # Legend at the top 
    # plt.legend(ncol=5, columnspacing=0.1, handletextpad=0, loc='upper center', bbox_to_anchor=(0.5, 1.30), fontsize=12, frameon=False)
# plt.subplots_adjust(hspace=0.02, wspace=0.01, left=0.15, bottom=0.1, right=0.99, top=0.95)
plt.legend(ncol=2, frameon=False)
plt.tight_layout()

plt.savefig('phasediaPrePost.png')
plt.savefig('phasediaPrePost.pdf')
plt.show()

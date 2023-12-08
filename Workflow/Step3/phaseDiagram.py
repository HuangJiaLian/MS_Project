import matplotlib.pyplot as plt
import numpy as np

# This is demostration how we calculate the atomic fraction
# Crystals          AlH3    RbAlH4      Rb5Al3H14   Rb3AlH6      RbH
# RbH(%)            0/4     2/6         10/22       6/10         2/2
# RbH(%)            0       33.33       45.45       60          100



crystals = ['AlH$_3$', 'XAlH$_4$', 'X$_5$Al$_3$H$_{14}$', 'X$_3$AlH$_6$', 'XH']
atomic_fraction_of_XH = [0, 33.33, 45.45, 60, 100]
# Fomation energy E [(eV)/atom]   # AlH3  (X)AlH4           (X)5Al3H14        (X)3AlH6       (X)H
formation_energies =   np.array([[0,    0.00940625384,    0.009556500753,  -0.0232288214,   0],  # Li
                                 [0,   -0.06348366911,   -0.0620795669,    -0.05635193381,  0],  # Na
                                 [0,   -0.1253529605,    -0.07825203177,   -0.08740277958,  0],  # K
                                 [0,   -0.145593986,     -0.067463493,     -0.089290582,    0],  # Rb
                                 [0,   -0.1596555026,    -0.05658973646,   -0.1011775038,   0]]) # Cs




plt.figure(figsize=(5.5, 8))


for i, X in enumerate(['Li', 'Na', 'K', 'Rb', 'Cs']):
    plt.subplot(5, 1, i+1)
    plt.scatter(atomic_fraction_of_XH, formation_energies[i])
    plt.tick_params(direction='in', labelsize=12)
    plt.xlim(-15, 115)
    plt.ylim(-0.19, 0.04)
    plt.xlabel('Atomic fraction of (X)H', fontsize=18)
    if i ==2:
        plt.ylabel('E$_\mathrm{form}$ [eV/atom]', fontsize=18)
    if i != 4:
        plt.tick_params(labelbottom=False)
        plt.xlabel('')
    plt.annotate(f'({chr(97+i)})', xy=(0.02, 0.8), xycoords="axes fraction", fontsize=16)
plt.subplots_adjust(hspace=0.02, wspace=0.01, left=0.15, bottom=0.1, right=0.99, top=0.95)
# plt.savefig('phasediaRbH.png')
# plt.savefig('phasediaRbH.pdf')
plt.show()



# for i, crystal in enumerate(crystals):
#     plt.text(rbh_percent[i]+8, formation_energy[i]+0.005, crystal, fontsize=16, ha='right', va='bottom')
# plt.text(0.03, 0.1, '(a)', fontsize=16, fontweight='bold', transform=plt.gca().transAxes)

# plt.subplot(2, 1, 2)
# plt.scatter(rbh_percent, H2_density, color='green', marker='s')
# plt.xlabel('Percentage of RbH', fontsize=18)
# plt.ylabel('H$_2$ density [Å$^{-3}$]', fontsize=18)
# plt.tick_params(direction='in', labelsize=12)
# plt.xlim(-5, 112)
# plt.ylim(0.006, 0.038)
# for i, crystal in enumerate(crystals):
#     plt.text(rbh_percent[i]+8, H2_density[i]+0.001, crystal, fontsize=16, ha='right', va='bottom')
# plt.text(0.03, 0.1, '(b)', fontsize=16, fontweight='bold', transform=plt.gca().transAxes)



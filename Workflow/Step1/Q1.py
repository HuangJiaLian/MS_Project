from ase.io import read, write

crystals = ['AlH3.cif', 'RbAlH4.cif', 'RbH.cif']

for crystal in crystals:
    atoms = read(crystal)
    print('==========================================')
    print(f'Formula: {atoms.get_chemical_formula()}')
    print(f'Total atoms: {len(atoms)}')

    #print('Degree of freedom:', len(atoms)*3)

    lattice = atoms.get_cell()
    print(f'Lattice parameters: {lattice} Angstrom')

    hydrogen_atoms = [atom for atom in atoms if atom.symbol == 'H']
    pairs_of_hydrogen_atoms = len(hydrogen_atoms) // 2
    volume = atoms.get_volume()
    print(f'Volume: {volume:.2f} cubic Angstrom')
    pairs_per_volume = pairs_of_hydrogen_atoms / volume
    print(f'Pairs of hydrogen atoms per volume: {pairs_per_volume:.3f}')
    
    # Constants for ideal gas law
    R = 8.31446261815324  # m3⋅Pa⋅K−1⋅mol−1
    T = 298.15  # K
    # Convert volume from cubic Angstrom to L
    volume_L = volume * 1e-30
    # Calculate pressure in atm
    N_A = 6.02214076e23  # Avogadro's number, mol^-1
    # Calculate moles of H2
    moles_H2 = pairs_of_hydrogen_atoms / N_A
    # Calculate pressure in atm using ideal gas law
    P = (moles_H2 * R * T / volume_L)*(9.86923*1e-6)
    print(f'H2-pressure in a gas tank: {P:.2f} atm')


from ase.io import read, write
import sys

if len(sys.argv) < 2:
    print("Usage: python log2cif.py QE_log_file")
    sys.exit(1)


qe_out = sys.argv[1]

# Read the last frame from QE output log file
frame = read(qe_out, index=-1, format='espresso-out')
lattice = frame.get_cell().tolist()
print(f'Lattice parameters:\n{lattice}')
print(f'Formula: {frame.get_chemical_formula()}')

total_atoms = len(frame)
print('Number of total atoms: ', total_atoms)

# Get the total energy for the last frame
last_frame_energy = frame.get_total_energy()
print('Total Energy: {} eV'.format(last_frame_energy))
print('Total Energy: {} Ry'.format(last_frame_energy/13.605703976))

hydrogen_atoms = [atom for atom in frame if atom.symbol == 'H']
pairs_of_hydrogen_atoms = len(hydrogen_atoms) / 2.
print('H2 number: {}'.format(pairs_of_hydrogen_atoms))
volume = frame.get_volume()
print(f'Volume: {volume:.2f} cubic Angstrom')

pairs_per_volume = pairs_of_hydrogen_atoms / volume
print(f'Pairs of hydrogen atoms per volume: {pairs_per_volume:.5f}')

write('{}.cif'.format(qe_out), frame)

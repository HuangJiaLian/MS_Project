#Quick tip; if the imports don't work, switch to the python interpreter to 3.11.4 (conda) and run the script from there.
from pymatgen.core import Structure
from pymatgen.io.pwscf import PWInput
from ase.io import read
from pymatgen.io.ase import AseAtomsAdaptor
import pandas as pd
from pymatgen.core.composition import Element, Composition
from pymatgen.core.periodic_table import Specie

def weight_percentage(structure: Structure):
    """
    structure: pymatgen.core.structure.Structure object
    This function calculates the weight percentage of hydrogen in a given structure.
    """
        
    total_mass = 0.0
    Hmass = 0.0
    Number_of_hydrogen = 0
    for atom in structure:
        total_mass += atom.specie.atomic_mass
        if atom.specie.symbol == "H":
            Hmass += atom.specie.atomic_mass
            Number_of_hydrogen += 1
    print(f'Found {Number_of_hydrogen} hydrogen atoms in the structure.')                
    return Hmass/total_mass *100

def get_data(files: list):
    """
    files: list of the respective filepaths of files to be analyzed.
    This function calculates:
        the number of hydrogen pairs per volume in a given structure
        the ideal gas pressure in atmospheres
        the weight percentage of hydrogen in a given structure
        the number of atoms in a given structure
    And returns a pandas DataFrame with the data.
    """
    
    data_list = []
    for file in files:    
        # Load the CIF file
        if file.endswith(".cif"):
            structure = Structure.from_file(file)
        elif file.endswith(".in"):
            # We need to do an extra check for the .in files:
            # Control needs to be in the file, or else it doesn't work:
            with open(file, 'r') as f: qe_input_content = f.read()
            # Check if "CONTROL" is present in the content
            assert "CONTROL" in qe_input_content, f"The file {file} does not contain the keyword 'CONTROL', please give an input file that does have a control section."
            structure_ase = read(file)
            structure = AseAtomsAdaptor.get_structure(structure_ase)
        else:
            print(f"Unsupported file format: {file}")
            break

        print(file)
        wt = weight_percentage(structure)
        print(f"weight percentage: {weight_percentage(structure)}")
        # Get the number of atoms
        num_atoms = len(structure)
        # print(f"Number of atoms: {num_atoms}")

        num_H_atoms = sum(atom.specie.symbol == "H" for atom in structure)

        # print(f"Number of H atoms in the structure: {num_H_atoms}")
        
        # find the total mass of the hydrogen atoms:
        for atom in structure:
            if atom.specie.symbol == "H":
                mass = atom.specie.atomic_mass
                break
        
        unit_cell_volume = structure.volume
        # print(f"Unit cell volume: {unit_cell_volume}")
        # Get number of hydrogen pairs per volume in Angstrom^-3:
        num_H_pairs_per_volume = 0.5 * num_H_atoms / unit_cell_volume
        # print(f"Number of H pairs per volume: {num_H_pairs_per_volume}")

        R = 8.314  # Ideal gas constant (J/(mol·K))
        Na = 6.02214076e23 # Avogadro constant (mol^-1)
        T = 293.15 # Temperature (K) 273.15 + 20
        kb = 1.380649e-23
        # ideal gas pressure (Pa):
        P = R * T * ((num_H_pairs_per_volume * 10**30))/Na # 10**30 to convert from Angstrom^-3 to m^-3
        # print(f"Ideal gas pressure: {P} Pa")
        # pressure in atmospheres:
        P_atm = P * 9.86923e-6
        # print(f"Ideal gas pressure: {P_atm} atm")
        # shorten filename to remove folder name
        data_list.append([file[16:], num_atoms, num_H_pairs_per_volume, wt, P_atm])
    # Create a pandas DataFrame
    columns = ["Crystal", "# Atoms", "H2 pairs per volume [Å⁻³]", "Weigth percentage [%]", "Pressure [atm]"]
    df = pd.DataFrame(data_list, columns=columns, index=None)
    # Fix indices (so they don't creep up)
    blankIndex=[''] * len(df)
    df.index=blankIndex
    print(df)

# example:
get_data(["Structure_files/KAlH3.cif","Structure_files/K3AlH6.cif",  "Structure_files/KAlH3_ecutwfc_10.in", "Structure_files/AlH3.cif"])

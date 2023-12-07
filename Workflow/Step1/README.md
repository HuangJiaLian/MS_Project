# Scripts to read and manipulate cif, input and output files

1. `Q1.py`

Calculate the basic infomation including crystal formula, atom number, H2 density, and pressure.

2. `replacing.py`

Replace one type of atom to another, and save as new cif file. 

3. Fundamental_data.py

Calculate the basic infomation including crystal formula, atom number, H2 density, and pressure.
For this input files, cif files as well as output files can be used.
Files should be put into 'Structure_files' folder. For now it's coded so that you can just run the script and it will calculate all the output (*.out) files in the folder. If you wish to include ciffiles or input files, you can change the the argument of the get_data() function. Goal of this piece of code: add your vc-relax output files to the folder, run the script, and get a csv file with all the data. Don't work from terminal, if you really want to, change the argument of the get_data(process_all_files()) function to the correct path.

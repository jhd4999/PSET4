
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns

#read in IGS dataset and store as pd dataframe
IGS_df = pd.read_excel('Payne_datasets/Payne_table1_PGP1f.xlsx', header=1, usecols='A:H', nrows=555)

#initialize dictionary containing all X, Y, Z coords of every read of that cell type
# nested dictionary
# PGP1f[cell_id][chr_num]['x', 'y', 'z', 'pos'] where 'x' is array of all x dimensions, and so on
PGP1f = {}
for cell in range(1, 107):
    cell_str = 'cell'+str(cell)
    PGP1f[cell_str] = {}
    for chr in range(1, 25):
        chr_str = 'chr'+str(chr)
        PGP1f[cell_str][chr_str] = {}
        for axis in ['x', 'y', 'z', 'pos']:
            PGP1f[cell_str][chr_str][axis] = []

# go through each row of the IGS_df and assign data to proper place in dictionary
# stores x, y, and z measurements, as well as position on the chromosome, for
#      each chromosome in each cell in the dataset. Ignores reads labeled as chromosome > 24
for i in range(0, len(IGS_df)):
    if int(IGS_df.iloc[i]['cell_id']) < 107 and int(IGS_df.iloc[i]['hg38_chr']) < 25:
        cell_str = 'cell' + str(int(IGS_df.iloc[i]['cell_id']))
        chr_str = 'chr' + str(int(IGS_df.iloc[i]['hg38_chr']))
        PGP1f[cell_str][chr_str]['x'].append(IGS_df.iloc[i]['x_um'])
        PGP1f[cell_str][chr_str]['y'].append(IGS_df.iloc[i]['y_um'])
        PGP1f[cell_str][chr_str]['z'].append(IGS_df.iloc[i]['z_um'])
        PGP1f[cell_str][chr_str]['pos'].append(IGS_df.iloc[i]['hg38_pos'])


# plot cell1 reads in 3D
cm = plt.get_cmap('tab20b')
fig = plt.figure(figsize=(12, 12))
ax = plt.axes(projection='3d')

cell_str = 'cell1'
for chr in range(1,25):
    chr_str = 'chr'+str(chr)
    x_coords = PGP1f[cell_str][chr_str]['x']
    y_coords = PGP1f[cell_str][chr_str]['y']
    z_coords = PGP1f[cell_str][chr_str]['z']
    #scatter3D = ax.scatter3D(x_coords, y_coords, z_coords, marker='o', label=chr_str, color=cm(1.*chr/24))
    line3D = ax.plot(x_coords, y_coords, z_coords, marker='o', label=chr_str, color=cm(1. * chr / 24), linewidth=0.1)
ax.set_xlabel('X Position (um)')
ax.set_ylabel('Y Position (um)')
ax.set_zlabel('Z Position (um)')
ax.set_title('PGP1f Cell 1 In Situ Genome Read Locations')

ax.legend()

plt.show()
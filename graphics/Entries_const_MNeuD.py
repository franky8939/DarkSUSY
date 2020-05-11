# coding=utf-8
# from modules.darkSUSY.classDarkSUSY import *
# from modules.general.F_search import *
from modules.graph.histograms import *
# from IPython.display import clear_output

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import h5py
import os

plt.rc('figure', max_open_warning=0)

# Localization of h5 for all data
directory = 'data/DarkSUSY.+h5'
# Open file *.h5 of data
hf = h5py.File(directory, 'r')

Vect_MNeuL = [10]
Vect_MNeuD = [0.25, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # mass of dark neutrino
Vect_MPhoD = [0.25, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # mass of  dark photon
Vect_TcPhoD = [5, 10, 20, 30, 40, 50, 60]  # values of life time (Tc)
Vect_Card = ["HL", "CMS"]

out_CMS = np.zeros([len(Vect_MNeuL), len(Vect_MNeuD),
                    len(Vect_MPhoD), len(Vect_TcPhoD)], dtype=int)
out_HL = np.zeros([len(Vect_MNeuL), len(Vect_MNeuD),
                   len(Vect_MPhoD), len(Vect_TcPhoD)], dtype=int)
out_relative = np.zeros([len(Vect_MNeuL), len(Vect_MNeuD),
                         len(Vect_MPhoD), len(Vect_TcPhoD)], dtype=int)
out_diff = np.zeros([len(Vect_MNeuL), len(Vect_MNeuD),
                     len(Vect_MPhoD), len(Vect_TcPhoD)], dtype=int)

# print out_CMS

i_MNeuL = -1  # initialise MNeuL
for MNeuL in Vect_MNeuL:
    i_MNeuL += 1  # count MNeuL
    i_MNeuD = -1  # initialise MNeuD
    for MNeuD in Vect_MNeuD:
        i_MNeuD += 1  # count MNeuD
        i_MPhoD = -1  # initialise MPhoD
        for MPhoD in Vect_MPhoD:
            if MNeuD + MPhoD <= MNeuL:  # condition mass equilibrium
                i_MPhoD += 1  # count MPhoD
                i_TcPhoD = -1  # initialise TcPhoD
                for TcPhoD in Vect_TcPhoD:
                    i_TcPhoD += 1  # count TcPhoD
                    for Card in ["HL", "CMS"]:
                        direction = "MNeuL_" + str(MNeuL) + "/MNeuD_" + str(MNeuD) + \
                                    "/MPhoD_" + str(MPhoD) + "/LifeTime/TcPhoD_" + str(TcPhoD) + \
                                    "/Card_" + Card
                        # print direction
                        group = hf.get(direction)
                        # print np.array(group.get('Entries')), type(int(np.array(group.get('Entries'))))
                        if Card is "HL":
                            out_HL[i_MNeuL, i_MNeuD, i_MPhoD, i_TcPhoD] = int(np.array(group.get('Entries')))
                        elif Card is "CMS":
                            out_CMS[i_MNeuL, i_MNeuD, i_MPhoD, i_TcPhoD] = int(np.array(group.get('Entries')))

                    if out_HL[i_MNeuL, i_MNeuD, i_MPhoD, i_TcPhoD] > 0:
                        out_relative[i_MNeuL, i_MNeuD,
                                     i_MPhoD, i_TcPhoD] = (float(out_HL[i_MNeuL, i_MNeuD, i_MPhoD, i_TcPhoD]) -
                                                           float(out_CMS[i_MNeuL, i_MNeuD, i_MPhoD, i_TcPhoD])) / \
                                                          float(out_HL[i_MNeuL, i_MNeuD, i_MPhoD, i_TcPhoD]) * 100
                        out_diff[i_MNeuL, i_MNeuD,
                                 i_MPhoD, i_TcPhoD] = float(out_CMS[i_MNeuL, i_MNeuD, i_MPhoD, i_TcPhoD]) / \
                                                      float(out_HL[i_MNeuL, i_MNeuD, i_MPhoD, i_TcPhoD]) * 100

hf.close()
locals()

# print out_HL
# print out_CMS

# Graphics of all data
def graphics3DHist(x, y, z, position=[1, 1, 1], title=None,
                   x_label=None, y_label=None, z_label=None,
                   zlim=None, figure=None):
    if figure is None:
        plt.rcParams['figure.figsize'] = [20, 100]
        fig = plt.figure()
    else:
        fig = figure
    ax = fig.add_subplot(position[0], position[1], position[2], projection='3d')
    ax.bar3d(x.ravel(), y.ravel(), 0,
             abs(np.gradient(x, axis=0)).ravel(),
             abs(np.gradient(y, axis=1)).ravel(),
             z.ravel(), zsort='average')
    if zlim is None:
        ax.set_zlim(0, np.max(z) * 1.1)
    else:
        ax.set_zlim(0, zlim * 1.1)
    if title is not None:
        ax.set_title(title, y=1.08)
    if x_label is not None:
        ax.set_xlabel(x_label)
    if y_label is not None:
        ax.set_ylabel(y_label)
    if z_label is not None:
        ax.set_zlabel(z_label)
    ax.view_init(20, 125)

    return fig

# Change Vect_MNeuD
x, y = np.meshgrid(Vect_MPhoD, Vect_TcPhoD, sparse=False, indexing='ij')  # MATRIX COMBINED
plt.rcParams['figure.figsize'] = [40, 60]
fig = plt.figure()
print np.max(out_HL)
for i in range(len(Vect_MNeuD)):
    position = [len(Vect_MNeuD), 4, 4 * i + 1]
    print str(position)
    fig = graphics3DHist(x, y, out_HL[0, i, :, :] / 100, position=position,
                         title="Usando Card CMS, para MNeuD (GeV) = "+str(Vect_MNeuD[i]),
                         x_label="MPhoD (GeV)",
                         y_label="TcPhoD (mm)",
                         z_label="EvMuMu (%)",
                         zlim=np.max(out_HL) / 100, figure=fig)

    position = [len(Vect_MNeuD), 4, 4 * i + 2]
    fig = graphics3DHist(x, y, out_CMS[0, i, :, :] / 100, position=position,
                         title="Usando Card HL, para MNeuD (GeV) = "+str(Vect_MNeuD[i]),
                         x_label="MPhoD (GeV)",
                         y_label="TcPhoD (mm)",
                         z_label="EvMuMu (%)",
                         zlim=np.max(out_HL) / 100, figure=fig)
    position = [len(Vect_MNeuD), 4, 4 * i + 3]
    fig = graphics3DHist(x, y, out_relative[0, i, :, :], position=position,
                         title="Comparando Card, para MNeuD (GeV) = "+str(Vect_MNeuD[i]),
                         x_label="MPhoD (GeV)",
                         y_label="TcPhoD (mm)",
                         z_label="Error Relativo Porcentual (%)",
                         zlim=np.max(out_relative), figure=fig)
    position = [len(Vect_MNeuD), 4, 4 * i + 4]
    fig = graphics3DHist(x, y, out_diff[0, i, :, :], position=position,
                         title="Comparando Card, para MNeuD (GeV) = "+str(Vect_MNeuD[i]),
                         x_label="MPhoD (GeV)",
                         y_label="TcPhoD (mm)",
                         z_label="Diferencia Porcentual (%)",
                         zlim=np.max(out_diff), figure=fig)
    # fig.show()

fig.savefig("files_PDF/Event_all_histConst_MNeuD.pdf.pdf")
# fig.show()


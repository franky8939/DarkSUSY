# coding=utf-8
# from modules.darkSUSY.classDarkSUSY import *
# from modules.general.F_search import *
from modules.graph.hist1D import *
# from IPython.display import clear_output

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import h5py
import os

plt.rc('figure', max_open_warning=0)

# Localization of h5 for all data
directory = 'data/DarkSUSY.h5'
# Open file *.h5 of data
hf = h5py.File(directory, 'r')

# Visualizar cambios en los graficos con Tc
Vect_MNeuL = [10]
Vect_MNeuD = [1]  # mass of dark neutrino
Vect_MPhoD = [9]  # mass of  dark photon
Vect_TcPhoD = [10]  # values of life time (Tc)
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
Vect_var = ["T", "PT", "Eta", "Phi", "MassInv", "D0", "DZ", "IsolationVar"]

for var in Vect_var:
    plt.figure()
    plt.grid(True)
    plt.title("Diferencias entre configuraciones para :: " + "\n" + "MNeuL = " + str(Vect_MNeuL[0]) +
              ", MNeuD = " + str(Vect_MNeuD[0]) +
              ", MPhoD = " + str(Vect_MPhoD[0]) +
              ", TcPhoD = " + str(Vect_TcPhoD[0]))
    plt.xlabel('Valores de ' + var)
    plt.ylabel('Frecuencia Normalizada')

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
                        for Card in Vect_Card:
                            direction = "MNeuL_" + str(MNeuL) + "/MNeuD_" + str(MNeuD) + \
                                        "/MPhoD_" + str(MPhoD) + "/LifeTime/TcPhoD_" + str(TcPhoD) + \
                                        "/Card_" + Card
                            # print direction
                            group = hf.get(direction)
                            hf.get

                            out = np.array(group.get(var)).flatten()

                            hist1D(out, bins=50, alpha=0.4, normed=1)
                        plt.legend(["Valores para Card HL", "Valores para Card CMS"])

                        # print np.array(group.get('Entries')), type(int(np.array(group.get('Entries'))))
                        """if Card is "HL":
                            #out_HL_log = np.array(group.get(var)).flatten()
                            #out_HL = out_HL_log[
                            #    (out_HL_log > np.percentile(out_HL_log, 1)) *  # (out_HL_log > 0) *
                            #    (out_HL_log < np.percentile(out_HL_log, 99))]
                            #plt.hist(out_HL)
                        elif Card is "CMS":
                            #out_CMS_log = np.array(group.get(var)).flatten()
                            #out_CMS = out_CMS_log[
                            #    (out_CMS_log > np.percentile(out_CMS_log, 1)) *  # (out_CMS_log > 0) *
                            #    (out_CMS_log < np.percentile(out_CMS_log, 99))]
                            #plt.hist(out_CMS, bins=50, alpha=0.4, normed=1)"""
    plt.savefig("files_PDF/Cambio de " + var + " con Card.pdf")
    plt.savefig("files_PDF/Cambio de " + var + " con Card.png")
    plt.show()

######################
######################

'''# Visualizar cambios en los graficos con Tc
Vect_MNeuL = [10]
Vect_MNeuD = [1]  # mass of dark neutrino
Vect_MPhoD = [9]  # mass of  dark photon
Vect_TcPhoD = [5, 100]  # values of life time (Tc)
Vect_Card = ["HL"]

out_CMS = np.zeros([len(Vect_MNeuL), len(Vect_MNeuD),
                    len(Vect_MPhoD), len(Vect_TcPhoD)], dtype=int)
out_HL = np.zeros([len(Vect_MNeuL), len(Vect_MNeuD),
                   len(Vect_MPhoD), len(Vect_TcPhoD)], dtype=int)

plt.figure()
# print out_CMS
var = "IsolationVar"
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
                    for Card in Vect_Card:
                        direction = "MNeuL_" + str(MNeuL) + "/MNeuD_" + str(MNeuD) + \
                                    "/MPhoD_" + str(MPhoD) + "/LifeTime/TcPhoD_" + str(TcPhoD) + \
                                    "/Card_" + Card
                        # print direction
                        group = hf.get(direction)
                        # print np.array(group.get('Entries')), type(int(np.array(group.get('Entries'))))
                        if Card is "HL":
                            out_HL_log = np.array(group.get(var)).flatten()
                            out_HL = out_HL_log[out_HL_log > 0]
                            plt.hist(out_HL, bins=50, alpha=0.5, normed=1)
                            print 0
                        elif Card is "CMS":
                            out_CMS_log = np.array(group.get(var)).flatten()
                            out_CMS = out_CMS_log[out_CMS_log > 0]
                            plt.hist(out_CMS, bins=50, alpha=0.5, normed=1)
                            print 0

hf.close()

plt.grid(True)
plt.xlabel("Valores de "+var)
plt.ylabel('Frecuencia Normalizada')
# plt.xlim(-4, 4)
# plt.ylim([0, 0.1])
# plt.legend(["ct = 5 mm", "ct = 10 mm","ct = 50 mm"])
plt.savefig("files_PDF/Cambio de " + var + "con Tc.pdf")
plt.savefig("files_PDF/Cambio de " + var + "con Tc.png")
plt.show()
'''

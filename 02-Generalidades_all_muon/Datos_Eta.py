from modules.general.F_search import *
from modules.graph.hist1D import *

import matplotlib.pyplot as plt
import numpy as np
import h5py
import sys
import re

# Create general h5 for all data
INPUT = "/home/franky8939/GITHUP/DarkSUSY-master/data/h5_muon/DarkSUSY.h5"

# Si existe el archivo OUTPUT ACTUALIZARLO #
if os.path.exists(INPUT):
    hf = h5py.File(INPUT, 'r')
else:
    print(" :: Datos de entrada inexistentes:: ")
    sys.exit()

# code to find
# var


Eta_CMS_all = None
Eta_HL_all = None

INPUT_CMS = None
INPUT_HL = None

# prueba
for MNeuL in hf.keys():
    # print(MNeuL)
    MNeuD_all = hf.require_group(MNeuL)
    for MNeuD in MNeuD_all.keys():
        # print(MNeuL + "/" + MNeuD)
        MPhoD_all = hf.require_group(MNeuL + "/" + MNeuD)
        for MPhoD in MPhoD_all.keys():
            # print(MNeuL + "/" + MNeuD + "/" + MPhoD)
            TcPhoD_all = hf.require_group(MNeuL + "/" + MNeuD + "/" + MPhoD)
            for TcPhoD in TcPhoD_all.keys():
                # print(MNeuL + "/" + MNeuD + "/" + MPhoD + "/" + TcPhoD)
                Data_Card = hf.require_group(MNeuL + "/" + MNeuD + "/" + MPhoD + "/" + TcPhoD)
                for Card in Data_Card.keys():
                    # Identifiacion del archivo en Name_of_FileROOT
                    # print(MNeuL + "/" + MNeuD + "/" + MPhoD + "/" + TcPhoD + "/" + Card)
                    FileROOT = hf.require_group(MNeuL + "/" + MNeuD + "/" + MPhoD + "/" + TcPhoD + "/" + Card)
                    if np.array(FileROOT.get("Verification")) is "OFF" or \
                            np.array(FileROOT.get("Mu_Entries")).shape[0] < 100:  # Mal Introducida Data
                        continue

                    name = str(np.array(FileROOT.get("Name_of_FileROOT")))
                    # print(name)
                    Values = Ob_Value(name)
                    INPUT_VAR = [float(Values["MNeuL"]), float(Values["MNeuD"]),
                                 float(Values["MPhoD"]), float(Values["TcPhoD"])]
                    print(INPUT_VAR)

                    # var in the respective root
                    Eta = np.array(FileROOT.get("Eta"))
                    # Eta = np.array(FileROOT.get("Eta"))
                    # Phi = np.array(FileROOT.get("Phi"))
                    # D0 = np.array(FileROOT.get("D0"))
                    # DZ = np.array(FileROOT.get("DZ"))
                    # T = np.array(FileROOT.get("T"))
                    # Charge = np.array(FileROOT.get("Charge"))
                    # MassInv = np.array(FileROOT.get("MassInv"))
                    # InsolationVar = np.array(FileROOT.get("InsolationVar"))
                    diMu_Entries = np.array(FileROOT.get("diMu_Entries"))
                    # Particles = diMu_Entries[:, 1:5]  # position of particles

                    if Eta.shape is ():  # caso cuando no se tienen datos
                        continue

                    if Values["Card"] is "_CMS_":
                        if Eta_CMS_all is None:
                            Eta_CMS_all = Eta.reshape((1, Eta.shape[0] * Eta.shape[1]))
                            Eta_CMS_0 = Eta[diMu_Entries[:, 1:5] == 0]
                            Eta_CMS_1 = Eta[diMu_Entries[:, 1:5] == 1]
                            Eta_CMS_2 = Eta[diMu_Entries[:, 1:5] == 2]
                            Eta_CMS_3 = Eta[diMu_Entries[:, 1:5] == 3]
                            # Eta_CMS_all = Eta
                            # Phi_CMS_all = Phi
                            # D0_CMS_all = D0
                            # DZ_CMS_all = DZ
                            # T_CMS_all = T
                            # Charge_CMS_all = Charge
                            # MassInv_CMS_all = MassInv
                            # InsolationVar_CMS_all = InsolationVar
                        else:
                            Eta_CMS_all = np.hstack((Eta_CMS_all, Eta.reshape((1, Eta.shape[0] * Eta.shape[1]))))
                            Eta_CMS_0 = np.hstack((Eta_CMS_0, Eta[diMu_Entries[:, 1:5] == 0]))
                            Eta_CMS_1 = np.hstack((Eta_CMS_1, Eta[diMu_Entries[:, 1:5] == 1]))
                            Eta_CMS_2 = np.hstack((Eta_CMS_2, Eta[diMu_Entries[:, 1:5] == 2]))
                            Eta_CMS_3 = np.hstack((Eta_CMS_3, Eta[diMu_Entries[:, 1:5] == 3]))
                    elif Values["Card"] is "_HL_":
                        if Eta_HL_all is None:
                            Eta_HL_all = Eta.reshape((1, Eta.shape[0] * Eta.shape[1]))
                            Eta_HL_0 = Eta[diMu_Entries[:, 1:5] == 0]
                            Eta_HL_1 = Eta[diMu_Entries[:, 1:5] == 1]
                            Eta_HL_2 = Eta[diMu_Entries[:, 1:5] == 2]
                            Eta_HL_3 = Eta[diMu_Entries[:, 1:5] == 3]
                        else:
                            Eta_HL_all = np.hstack((Eta_HL_all, Eta.reshape((1, Eta.shape[0] * Eta.shape[1]))))
                            Eta_HL_0 = np.hstack((Eta_HL_0, Eta[diMu_Entries[:, 1:5] == 0]))
                            Eta_HL_1 = np.hstack((Eta_HL_1, Eta[diMu_Entries[:, 1:5] == 1]))
                            Eta_HL_2 = np.hstack((Eta_HL_2, Eta[diMu_Entries[:, 1:5] == 2]))
                            Eta_HL_3 = np.hstack((Eta_HL_3, Eta[diMu_Entries[:, 1:5] == 3]))
                    else:
                        print(":: PROBLEMS :: EXIT ::")

                    # print(Eta)
                    # sys.exit()

hf.close()
# GRAFICAR
plt.rcParams['figure.figsize'] = [20, 4]
fig = plt.figure()
# Xlim = 100
ax = fig.add_subplot(1, 3, 1)
ax.hist(Eta_HL_all.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_CMS_all.T, bins=100, alpha=0.5, normed=True)
ax.legend(["Valores para HL", "Valores para CMS"])
ax.set_xlabel(" Valor de la Pseudorapidez $\eta$")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
ax.set_title(" Todos los Valores")
ax.grid(True)

ax = fig.add_subplot(1, 3, 2)
ax.hist(Eta_CMS_3.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_CMS_2.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_CMS_1.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_CMS_0.T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 1", "Muon 2", "Muon 3", "Muon 4"])
ax.set_xlabel(" Valor de la Pseudorapidez $\eta$")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
ax.set_title(" Valores $\eta$ de los muones " + "\n" + "para la configuracion CMS")
ax.grid(True)

ax = fig.add_subplot(1, 3, 3)
ax.hist(Eta_HL_3.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_HL_2.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_HL_1.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_HL_0.T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 1", "Muon 2", "Muon 3", "Muon 4"])
ax.set_xlabel(" Valor de la Pseudorapidez $\eta$")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
ax.set_title(" Valores $\eta$ de los muones " + "\n" + "para la configuracion HL")
ax.grid(True)

fig.savefig("Datos_Eta_ALL.pdf")
fig.savefig("Datos_Eta_ALL.png")
fig.show()



plt.rcParams['figure.figsize'] = [20, 4]
fig = plt.figure()

ax = fig.add_subplot(1, 4, 1)
ax.hist(Eta_HL_3.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_CMS_3.T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 1 para HL", "Muon 1 para CMS"])
ax.set_xlabel(" Valor de la Pseudorapidez $\eta$")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
# ax.set_title(" Comparacion de Momentos Transversales")
ax.grid(True)

ax = fig.add_subplot(1, 4, 2)
ax.hist(Eta_HL_2.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_CMS_2.T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 2 para HL", "Muon 2 para CMS"])
ax.set_xlabel(" Valor de la Pseudorapidez $\eta$")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
# ax.set_title(" Comparacion de Momentos Transversales")
ax.grid(True)

ax = fig.add_subplot(1, 4, 3)
ax.hist(Eta_HL_1.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_CMS_1.T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 3 para HL", "Muon 3 para CMS"])
ax.set_xlabel(" Valor de la Pseudorapidez $\eta$")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
# ax.set_title(" Comparacion de Momentos Transversales")
ax.grid(True)

ax = fig.add_subplot(1, 4, 4)
ax.hist(Eta_HL_0.T, bins=100, alpha=0.5, normed=True)
ax.hist(Eta_CMS_0.T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 4 para HL", "Muon 4 para CMS"])
ax.set_xlabel(" Valor de la Pseudorapidez $\eta$")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
# ax.set_title(" Comparacion de Momentos Transversales")
ax.grid(True)

fig.savefig("Datos_Eta_for_Mu.pdf")
fig.savefig("Datos_Eta_for_Mu.png")
fig.show()
# hist1D(Eta_CMS_all, Eta_HL_all, bins=50, alpha=0.4, normed=True)

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


IsolationVar_CMS_all = None
IsolationVar_HL_all = None

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
                    IsolationVar = np.array(FileROOT.get("IsolationVar"))
                    # IsolationVar = np.array(FileROOT.get("IsolationVar"))
                    # Phi = np.array(FileROOT.get("Phi"))
                    # IsolationVar = np.array(FileROOT.get("IsolationVar"))
                    # DZ = np.array(FileROOT.get("DZ"))
                    # T = np.array(FileROOT.get("T"))
                    # Charge = np.array(FileROOT.get("Charge"))
                    # MassInv = np.array(FileROOT.get("MassInv"))
                    # InsolationVar = np.array(FileROOT.get("InsolationVar"))
                    diMu_Entries = np.array(FileROOT.get("diMu_Entries"))
                    # Particles = diMu_Entries[:, 1:5]  # position of particles

                    if IsolationVar.shape is ():  # caso cuando no se tienen datos
                        continue

                    if Values["Card"] is "_CMS_":
                        if IsolationVar_CMS_all is None:
                            IsolationVar_CMS_all = IsolationVar.reshape((1, IsolationVar.shape[0] * IsolationVar.shape[1]))
                            IsolationVar_CMS_0 = IsolationVar[diMu_Entries[:, 1:5] == 0]
                            IsolationVar_CMS_1 = IsolationVar[diMu_Entries[:, 1:5] == 1]
                            IsolationVar_CMS_2 = IsolationVar[diMu_Entries[:, 1:5] == 2]
                            IsolationVar_CMS_3 = IsolationVar[diMu_Entries[:, 1:5] == 3]
                            # IsolationVar_CMS_all = IsolationVar
                            # Phi_CMS_all = Phi
                            # IsolationVar_CMS_all = IsolationVar
                            # DZ_CMS_all = DZ
                            # T_CMS_all = T
                            # Charge_CMS_all = Charge
                            # MassInv_CMS_all = MassInv
                            # InsolationVar_CMS_all = InsolationVar
                        else:
                            IsolationVar_CMS_all = np.hstack((IsolationVar_CMS_all, IsolationVar.reshape((1, IsolationVar.shape[0] * IsolationVar.shape[1]))))
                            IsolationVar_CMS_0 = np.hstack((IsolationVar_CMS_0, IsolationVar[diMu_Entries[:, 1:5] == 0]))
                            IsolationVar_CMS_1 = np.hstack((IsolationVar_CMS_1, IsolationVar[diMu_Entries[:, 1:5] == 1]))
                            IsolationVar_CMS_2 = np.hstack((IsolationVar_CMS_2, IsolationVar[diMu_Entries[:, 1:5] == 2]))
                            IsolationVar_CMS_3 = np.hstack((IsolationVar_CMS_3, IsolationVar[diMu_Entries[:, 1:5] == 3]))
                    elif Values["Card"] is "_HL_":
                        if IsolationVar_HL_all is None:
                            IsolationVar_HL_all = IsolationVar.reshape((1, IsolationVar.shape[0] * IsolationVar.shape[1]))
                            IsolationVar_HL_0 = IsolationVar[diMu_Entries[:, 1:5] == 0]
                            IsolationVar_HL_1 = IsolationVar[diMu_Entries[:, 1:5] == 1]
                            IsolationVar_HL_2 = IsolationVar[diMu_Entries[:, 1:5] == 2]
                            IsolationVar_HL_3 = IsolationVar[diMu_Entries[:, 1:5] == 3]
                        else:
                            IsolationVar_HL_all = np.hstack((IsolationVar_HL_all, IsolationVar.reshape((1, IsolationVar.shape[0] * IsolationVar.shape[1]))))
                            IsolationVar_HL_0 = np.hstack((IsolationVar_HL_0, IsolationVar[diMu_Entries[:, 1:5] == 0]))
                            IsolationVar_HL_1 = np.hstack((IsolationVar_HL_1, IsolationVar[diMu_Entries[:, 1:5] == 1]))
                            IsolationVar_HL_2 = np.hstack((IsolationVar_HL_2, IsolationVar[diMu_Entries[:, 1:5] == 2]))
                            IsolationVar_HL_3 = np.hstack((IsolationVar_HL_3, IsolationVar[diMu_Entries[:, 1:5] == 3]))
                    else:
                        print(":: PROBLEMS :: EXIT ::")

                    # print(IsolationVar)
                    # sys.exit()

hf.close()
# GRAFICAR
plt.rcParams['figure.figsize'] = [20, 4]
fig = plt.figure()
lim_min = 0
lim_max = 100
ax = fig.add_subplot(1, 3, 1)
ax.hist(IsolationVar_HL_all[(lim_min < IsolationVar_HL_all)*(IsolationVar_HL_all < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_CMS_all[(lim_min < IsolationVar_CMS_all)*(IsolationVar_CMS_all < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.legend(["Valores para HL", "Valores para CMS"])
ax.set_xlabel(" Parametro de Aislamiento InsolateVar($GeV$)")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
ax.set_title(" Todos los Valores")
ax.grid(True)

ax = fig.add_subplot(1, 3, 2)
ax.hist(IsolationVar_CMS_3[(lim_min < IsolationVar_CMS_3)*(IsolationVar_CMS_3 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_CMS_2[(lim_min < IsolationVar_CMS_2)*(IsolationVar_CMS_2 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_CMS_1[(lim_min < IsolationVar_CMS_1)*(IsolationVar_CMS_1 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_CMS_0[(lim_min < IsolationVar_CMS_0)*(IsolationVar_CMS_0 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 1", "Muon 2", "Muon 3", "Muon 4"])
ax.set_xlabel(" Parametro de Aislamiento InsolateVar($GeV$) ")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
ax.set_title(" Valores IsolationVar de los muones " + "\n" + "para la configuracion CMS")
ax.grid(True)

ax = fig.add_subplot(1, 3, 3)
ax.hist(IsolationVar_HL_3[(lim_min < IsolationVar_HL_3)*(IsolationVar_HL_3 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_HL_2[(lim_min < IsolationVar_HL_2)*(IsolationVar_HL_2 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_HL_1[(lim_min < IsolationVar_HL_1)*(IsolationVar_HL_1 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_HL_0[(lim_min < IsolationVar_HL_0)*(IsolationVar_HL_0 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 1", "Muon 2", "Muon 3", "Muon 4"])
ax.set_xlabel(" Parametro de Aislamiento InsolateVar($GeV$) ")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
ax.set_title(" Valores IsolationVar de los muones " + "\n" + "para la configuracion HL")
ax.grid(True)

fig.savefig("Datos_IsolationVar_ALL.pdf")
fig.savefig("Datos_IsolationVar_ALL.png")
fig.show()



plt.rcParams['figure.figsize'] = [20, 4]
fig = plt.figure()

ax = fig.add_subplot(1, 4, 1)
ax.hist(IsolationVar_HL_3[(lim_min < IsolationVar_HL_3)*(IsolationVar_HL_3 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_CMS_3[(lim_min < IsolationVar_CMS_3)*(IsolationVar_CMS_3 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 1 para HL", "Muon 1 para CMS"])
ax.set_xlabel(" Parametro de Aislamiento InsolateVar($GeV$) ")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
# ax.set_title(" Comparacion de Momentos Transversales")
ax.grid(True)

ax = fig.add_subplot(1, 4, 2)
ax.hist(IsolationVar_HL_2[(lim_min < IsolationVar_HL_2)*(IsolationVar_HL_2 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_CMS_2[(lim_min < IsolationVar_CMS_2)*(IsolationVar_CMS_2 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 2 para HL", "Muon 2 para CMS"])
ax.set_xlabel(" Parametro de Aislamiento InsolateVar($GeV$) ")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
# ax.set_title(" Comparacion de Momentos Transversales")
ax.grid(True)

ax = fig.add_subplot(1, 4, 3)
ax.hist(IsolationVar_HL_1[(lim_min < IsolationVar_HL_1)*(IsolationVar_HL_1 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_CMS_1[(lim_min < IsolationVar_CMS_1)*(IsolationVar_CMS_1 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 3 para HL", "Muon 3 para CMS"])
ax.set_xlabel(" Parametro de Aislamiento InsolateVar($GeV$) ")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
# ax.set_title(" Comparacion de Momentos Transversales")
ax.grid(True)

ax = fig.add_subplot(1, 4, 4)
ax.hist(IsolationVar_HL_0[(lim_min < IsolationVar_HL_0)*(IsolationVar_HL_0 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.hist(IsolationVar_CMS_0[(lim_min < IsolationVar_CMS_0)*(IsolationVar_CMS_0 < lim_max)].T, bins=100, alpha=0.5, normed=True)
ax.legend(["Muon 4 para HL", "Muon 4 para CMS"])
ax.set_xlabel(" Parametro de Aislamiento InsolateVar($GeV$)")
ax.set_ylabel(" Frecuencia Normalizada $f_N$")
# ax.set_title(" Comparacion de Momentos Transversales")
ax.grid(True)

fig.savefig("Datos_IsolationVar_for_Mu.pdf")
fig.savefig("Datos_IsolationVar_for_Mu.png")
fig.show()
# hist1D(IsolationVar_CMS_all, IsolationVar_HL_all, bins=50, alpha=0.4, normed=True)

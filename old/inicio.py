from modules.darkSUSY.classDarkSUSY import *
from modules.general.F_search import *
from modules.graph.histograms import *

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

Delphes_DIR = "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/"  # Directory local of Delphes
ROOT_DIR = "/home/franky8939/PROGRAMAS/root-6.18.02/"  # Directory local of Root
fbash(Delphes_DIR, ROOT_DIR)  # path in bash of Delphes and Root

# CLASE DARKSUSY
DarkFile = DarkSUSY()  # inicializar la clase

# BUSCAR DATA
Event = [10000]
Vect_MNeuL = [10]
Vect_MNeuD = [0.25]
Vect_MPhoD = [0.25]  # [0.25, 1, 2, 3, 4, 5]  # masa de los photons
Vect_TcPhoD = [0.25]  # [0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # valores de Tc
Vect_Card = ["_CMS_", "_HL_"]
# BUSCANDO ARCHIVO DEFAULT
directory = "data/ALL/"
particle = "Muon"
var = "Eta"
for MNeuL in Vect_MNeuL:
    for MNeuD in Vect_MNeuD:
        for MPhoD in Vect_MPhoD:
            for TcPhoD in Vect_TcPhoD:
                for Card in Vect_Card:
                    fileROOT = FindROOT(Event, MNeuL, MNeuD, MPhoD, TcPhoD, directory)
                    if fileROOT is not None:
                        # print(fileROOT)
                        # clear_output()
                        DarkFileCMS = DarkFile  # new
                        DarkFileCMS.Add_File("data/dataD/" + fileROOT)
                        DarkFileCMS.Select_two_dimuon()
                        data = DarkFileCMS.Obtein(var, particle="particle", order=False)

                        plt.hist(data.flatten(),  bins=60, alpha=0.8, normed=1)

plt.grid(True)
plt.savefig("files_PFD/Variable temporal.pdf")
plt.show()


















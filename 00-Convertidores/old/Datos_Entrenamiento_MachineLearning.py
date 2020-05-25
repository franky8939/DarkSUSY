from modules.general.F_search import *
from modules.graph.hist1D import *

import matplotlib.pyplot as plt
import numpy as np
import h5py
import sys
import re

# Create general h5 for all data
INPUT = "/home/franky8939/GITHUP/DarkSUSY-master/data/h5_muon/DarkSUSY.h5"
OUTPUT = "/home/franky8939/GITHUP/DarkSUSY-master/data/h5_muon_histg/DarkSUSY_histg.h5"

# Si existe el archivo OUTPUT ACTUALIZARLO #
if os.path.exists(INPUT):
    hf = h5py.File(INPUT, 'r')
else:
    print(" :: Datos de entrada inexistentes:: ")
    sys.exit()

hf_out = h5py.File(OUTPUT, 'w')
# code to find
# var

steps = 100
div = 50

INPUT_PT_CMS = None
OUTPUT_PT_CMS = None
range_PT_CMS = [0, 100]
size_PT_CMS = (range_PT_CMS[1] - range_PT_CMS[0]) / div
# PT_HL_all = None

INPUT_Eta_CMS = None
OUTPUT_Eta_CMS = None
range_Eta_CMS = [-2.4, 2.4]
size_Eta_CMS = (range_Eta_CMS[1] - range_Eta_CMS[0]) / div
# Eta_HL_all = None

INPUT_Phi_CMS = None
OUTPUT_Phi_CMS = None
range_Phi_CMS = [-3.14, 3.14]
size_Phi_CMS = (range_Phi_CMS[1] - range_Phi_CMS[0]) / div
# Phi_HL_all = None

INPUT_D0_CMS = None
OUTPUT_D0_CMS = None
range_D0_CMS = [-100, 100]
size_D0_CMS = (range_D0_CMS[1] - range_D0_CMS[0]) / div
# D0_HL_all = None

INPUT_DZ_CMS = None
OUTPUT_DZ_CMS = None
range_DZ_CMS = [-100, 100]
size_DZ_CMS = (range_DZ_CMS[1] - range_DZ_CMS[0]) / div
# DZ_HL_all = None

INPUT_T_CMS = None
OUTPUT_T_CMS = None
range_T_CMS = [0, 11*10**(-9)]
size_T_CMS = (range_T_CMS[1] - range_T_CMS[0]) / div

INPUT_IsolationVar_CMS_all = None
OUTPUT_IsolationVar_CMS = None
range_IsolationVar_CMS = [-0.001, 0.25]
size_IsolationVar_CMS = (range_IsolationVar_CMS[1] - range_IsolationVar_CMS[0]) / div

INPUT_MassInv_CMS_all = None
OUTPUT_MassInv_CMS = None
range_MassInv_CMS = [0, 15]
size_MassInv_CMS = (range_MassInv_CMS[1] - range_MassInv_CMS[0]) / div

# Funcion para generar histograma
def histF(inp, sizes, steps, range):
    steps = steps + 1
    cens = np.linspace(range[0], range[1], steps)
    outX = []
    outY = []
    N = len(inp[(inp < np.max(range)) * (inp > np.min(range))])
    for cen in cens:
        if (cen + sizes) > np.max(range):
            sizeC = np.max(range) - cen
            log = (inp > (cen - sizes)) * ((cen + sizeC) > inp)
            val = inp[log]
            outY.append(len(val) / (N * (sizes + sizeC)))
        elif (cen - sizes) < np.min(range):
            sizeC = cen - np.min(range)
            log = (inp < (cen + sizes)) * ((cen - sizeC) < inp)
            val = inp[log]
            outY.append(len(val) / (N * (sizes + sizeC)))
        else:
            sizeC = 0
            log = (inp > (cen - sizes)) * ((cen + sizes) > inp)
            val = inp[log]
            outY.append(len(val) / (N * 2 * sizes))

        # outY.append(len(val)/(N*sizes))
        # print(sizeC)
        outX.append(cen)
    return outX, outY


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
                            np.array(FileROOT.get("Mu_Entries")).shape[0] < 10:  # Mal Introducida Data
                        continue

                    name = str(np.array(FileROOT.get("Name_of_FileROOT")))
                    # print(name)
                    Values = Ob_Value(name)
                    INPUT_VAR = [float(Values["MNeuL"]), float(Values["MNeuD"]),
                                 float(Values["MPhoD"]), float(Values["TcPhoD"])]
                    print(INPUT_VAR)

                    # var in the respective root
                    PT = np.array(FileROOT.get("PT"))
                    Eta = np.array(FileROOT.get("Eta"))
                    Phi = np.array(FileROOT.get("Phi"))
                    D0 = np.array(FileROOT.get("D0"))
                    DZ = np.array(FileROOT.get("DZ"))
                    T = np.array(FileROOT.get("T"))
                    MassInv = np.array(FileROOT.get("MassInv"))
                    IsolationVar = np.array(FileROOT.get("IsolationVar"))
                    diMu_Entries = np.array(FileROOT.get("diMu_Entries"))
                    # Particles = diMu_Entries[:, 1:5]  # position of particles

                    if PT.shape is () or PT.shape[0] < 10:  # caso cuando no se tienen datos o se tiene pocos
                        continue

                    # Generar el archivo histograma
                    PT_X, PT_Y = histF(PT, size_PT_CMS, div * 5, range_PT_CMS)
                    Eta_X, Eta_Y = histF(Eta, size_Eta_CMS, div * 5, range_Eta_CMS)
                    Phi_X, Phi_Y = histF(Phi, size_Phi_CMS, div * 5, range_Phi_CMS)
                    D0_X, D0_Y = histF(D0, size_D0_CMS, div * 5, range_D0_CMS)
                    DZ_X, DZ_Y = histF(DZ, size_DZ_CMS, div * 5, range_DZ_CMS)
                    T_X, T_Y = histF(T, size_T_CMS, div * 5, range_T_CMS)
                    IsolationVar_X, IsolationVar_Y = histF(IsolationVar, size_IsolationVar_CMS, div * 5,
                                                           range_IsolationVar_CMS)
                    MassInv_X, MassInv_Y = histF(MassInv, size_MassInv_CMS, div * 5, range_MassInv_CMS)

                    # Empty Var
                    PT_out = np.zeros((2, len(PT_X)))
                    Eta_out = np.zeros((2, len(Eta_X)))
                    Phi_out = np.zeros((2, len(Phi_X)))
                    D0_out = np.zeros((2, len(D0_X)))
                    DZ_out = np.zeros((2, len(DZ_X)))
                    T_out = np.zeros((2, len(T_X)))
                    IsolationVar_out = np.zeros((2, len(IsolationVar_X)))
                    MassInv_out = np.zeros((2, len(MassInv_X)))

                    # Include Var
                    PT_out[0, :] = PT_X
                    Eta_out[0, :] = Eta_X
                    Phi_out[0, :] = Phi_X
                    D0_out[0, :] = D0_X
                    DZ_out[0, :] = DZ_X
                    T_out[0, :] = T_X
                    IsolationVar_out[0, :] = IsolationVar_X
                    MassInv_out[0, :] = MassInv_X

                    PT_out[1, :] = PT_Y
                    Eta_out[1, :] = Eta_Y
                    Phi_out[1, :] = Phi_Y
                    D0_out[1, :] = D0_Y
                    DZ_out[1, :] = DZ_Y
                    T_out[1, :] = T_Y
                    IsolationVar_out[1, :] = IsolationVar_Y
                    MassInv_out[1, :] = MassInv_Y

                    # Entrar los datos en el archivo h5 de salida
                    local_group = hf_out.require_group(MNeuL + "/" + MNeuD + "/" + MPhoD + "/" + TcPhoD + "/" + Card)
                    local_group.create_dataset(name="PT", data=PT_out)
                    local_group.create_dataset(name="Eta", data=Eta_out)
                    local_group.create_dataset(name="Phi", data=Phi_out)
                    local_group.create_dataset(name="D0", data=D0_out)
                    local_group.create_dataset(name="DZ", data=DZ_out)
                    local_group.create_dataset(name="T", data=T_out)
                    local_group.create_dataset(name="IsolationVar", data=IsolationVar_out)
                    local_group.create_dataset(name="MassInv", data=MassInv_out)
                    local_group.create_dataset(name="Input", data=INPUT_VAR)
                    local_group.create_dataset(name="Entries", data=PT.shape[0])

hf.close()
hf_out.close()

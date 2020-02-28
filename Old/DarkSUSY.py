import sys
import os
#sys.getdefaulencoding()
import ROOT
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats # usar media o desviacion estandar
ROOT.gSystem.Load("/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/libDelphes")
#ROOT.gSystem.Load("/home/franky8939/PROGRAMAS/root-6.18.02/build/lib/libPyROOT")

ROOT.gInterpreter.Declare('#include "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/classes/SortableObject.h"')
ROOT.gROOT.ProcessLine('.include .')
ROOT.gInterpreter.Declare('#include "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/classes/DelphesClasses.h"')
ROOT.gInterpreter.Declare('#include "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/external/ExRootAnalysis/ExRootTreeReader.h"')
#inputFile = "darkphoton_m0p25_ct0mm.root"
inputFile = "darkphoton_5GeV_ctau0.root"
File = ROOT.TChain("Delphes;1")
File.Add(inputFile)


## FUNCTIONS ##sys.getdefaulencoding()
## SELECCIONA LOS POSIBLES DI-MUONES EN DEPENDENCIA DE SU CARGA ##
def di_muon_Charge(entrada, leng):
    salida = []
    for one in range(leng):
        for two in range(one, leng):
            if entrada[one] + entrada[two] == 0:
                salida.append([one, two])
    return salida


## SELECCIONAR EL PAR CON MENOR MASA INVARIANTE
def Select_two_di_muon(entrada, muones, archivo):
    AllDiffInvMass = np.array([])
    AllInvMass = np.array([])
    Alltwo_di_muon = np.array([])
    # COMBINATION OF TWO DI-MUONS
    for one in range(len(entrada)):
        for two in range(one + 1, len(entrada)):
            if entrada[one][0] != entrada[two][0] and entrada[one][0] != entrada[two][1] and \
                    entrada[one][1] != entrada[two][0] and entrada[one][1] != entrada[two][1]:
                mass1 = (muones.At(entrada[one][0]).P4() + muones.At(entrada[one][1]).P4()).M()
                mass2 = (muones.At(entrada[two][0]).P4() + muones.At(entrada[two][1]).P4()).M()
                AllDiffInvMass = np.append(AllDiffInvMass, np.abs(mass1 - mass2))
                two_di_muon = np.array([entrada[one][0], entrada[one][1], entrada[two][0], entrada[two][1]])
                # print(two_di_muon)
                if len(Alltwo_di_muon) == 0:
                    Alltwo_di_muon = two_di_muon
                    AllInvMass = [mass1, mass2]
                else:
                    Alltwo_di_muon = np.vstack([Alltwo_di_muon, two_di_muon])
                    AllInvMass = np.vstack([AllInvMass, [mass1, mass2]])
                    # print(Alltwo_di_muon)

    archivo.write(
        "\n" + "||                                 =======================================                                   ||")
    archivo.write(
        "\n" + "||                                 | All Couple of di-muones for select: |                                   ||")
    archivo.write(
        "\n" + "||                                 =======================================                                   || ")
    for count in range(len(AllInvMass)):
        archivo.write("\n" + "||" + " :: First di-muon: [" + str(Alltwo_di_muon[count][0]) + " , " + str(
            Alltwo_di_muon[count][1]) + "] " +
                      " with M1 : " + '%.2f' % AllInvMass[count][0] +
                      " :: Second di-muon: [" + str(Alltwo_di_muon[count][2]) + " , " + str(
            Alltwo_di_muon[count][3]) + "] " +
                      " with M2 : " + '%.2f' % AllInvMass[count][1] +
                      " :: \u0394 Minv : " + '%.3f' % AllDiffInvMass[count])

    archivo.write(
        "\n" + "||                                 =======================================                                   ||")
    archivo.write(
        "\n" + "||                                 | The Couple of di-muones select is : |                                   ||")
    archivo.write(
        "\n" + "||                                 =======================================                                   ||")
    # MIN OF MASS DIF IN THE VECTOR AllInvMAss
    logic = np.where(np.min(AllDiffInvMass) == AllDiffInvMass)[0][0]  # MATRIX LOGIC
    # print(logic)
    salida = (Alltwo_di_muon[logic])  # TWO DI-MUON WITH > (MASS1-MASS2)
    # print(salida)
    # print( AllInvMass[logic][1] )
    archivo.write("\n" + "||" + " :: First di-muon: [" + str(salida[0]) + " , " + str(salida[1]) + "] " +
                  " with M1 : " + '%.2f' % AllInvMass[logic][0] +
                  " :: Second di-muon: [" + str(salida[2]) + " , " + str(salida[3]) + "] " +
                  " with M2 : " + '%.2f' % AllInvMass[logic][1])  # '''

    return salida


# %%

f = open("LOG OF SELECCION OF TWO MUONS.txt", 'w')  # CREATE TXT FILE TO SAVE THE CHARACTERIZATION PROCESS INFO

ALL_DMuon_ForEvent = []
entries = File.GetEntries()  # Number of Event
for entry in range(100):  # entries):
    Event = File.GetEntry(entry)
    if File.Muon.GetEntries() > 3:  # Number of Muon in the Event
        Nmuon = File.Muon.GetEntries()
        Chargemuon = []
        f.write(
            "\n" + "||===========================================================================================================||")
        f.write(
            "\n" + "||                                 || SUMMARY OF EVENT CHARACTERIZATION ||                                   ||")
        f.write(
            "\n" + "||===========================================================================================================||")
        f.write(
            "\n" + "||                                   EVENT : " + str(entry) + " :: NUMBER OF MUONS : " + str(Nmuon))

        for imuon in range(Nmuon):
            Chargemuon.append(File.GetLeaf("Muon.Charge").GetValue(imuon))
        di_muon = di_muon_Charge(Chargemuon, Nmuon)
        two_di_muon = Select_two_di_muon(di_muon, File.Muon, f)
        # f.write( "\n" + "||=========================================================================================================||")
        # f.write( "\n" + "||                                         || END OF THE EVENT ||                                          ||")
        f.write(
            "\n" + "||===========================================================================================================||")
        ## ALL DI-MUON FOR EVENT
        if len(ALL_DMuon_ForEvent) == 0:
            ALL_DMuon_ForEvent = np.hstack([entry, two_di_muon])
        else:
            aa = np.hstack([entry, two_di_muon])
            ALL_DMuon_ForEvent = np.vstack([ALL_DMuon_ForEvent, aa])

f.close()
#!/usr/bin/env python
# %%

# import ROOT

# import matplotlib.pyplot as plt
import numpy as np


# import statistics as stats # usar media o desviacion estandar

'''ROOT.gSystem.Load("/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/libDelphes")
ROOT.gInterpreter.Declare('#include "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/classes/SortableObject.h"')
ROOT.gROOT.ProcessLine('.include .')
ROOT.gInterpreter.Declare('#include "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/classes/DelphesClasses.h"')
ROOT.gInterpreter.Declare('#include "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/external/ExRootAnalysis/ExRootTreeReader.h"')
'''

# inputFile = "darkphoton_m0p25_ct0mm.root"
inputFile = "darkphoton_5GeV_ctau0.root"
# file = ROOT.TFile(inputFile)
a = np.max([1,2,3,4])
# %%

# inputFile = "darkphoton_5GeV_ctau0.root"
# File = ROOT.TChain("Delphes;1")
print(inputFile)
print(a)

def header():
    print "\n" + "||===========================================================================================================||"
    print "\n" + "||                                 || SUMMARY OF EVENT CHARACTERIZATION ||                                   ||"
    print "\n" + "||===========================================================================================================||"
    print "\n" + "||                                   EVENT : "

header()
'''File.Add(inputFile)
Number = File.GetEntries()
print(Number)
i=18
entry = File.GetEntry(i)
entryFromBranch = File.Muon.GetEntries()
print(entryFromBranch)
#print(File.Muon.At(1))

#%%

muon1 = File.Muon.At(1)
muon2 = File.Muon.At(0)
print((muon1.P4() + muon2.P4()).M())'''

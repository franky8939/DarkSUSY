#!/usr/bin/env python
# %%
# ============================ || BEGIN : MODULES || ============================ #
""" Modules using """
import os
import numpy as np
import sys
import ROOT
Delphes_DIR = "/home/franky8939/PROGRAMAS/MG5_aMC/Delphes/"  # Directory local of Delphes
ROOT_DIR = "/home/franky8939/PROGRAMAS/ROOT/obj"  # Directory local of Root


# ============================ || END   : MODULES || ============================ ##

# ======================== || BEGIN : PATH IN PROYECT || ======================== #
def fbash(Delphes_DIR, ROOT_DIR):
    """
    Cargar path de los directorios ROOT y DELPHES
    This is necesary for import path for the bash because in the Jupyter of Pycharm
    not charge this bash include in the environment and is necessary por import the
    module of the program ROOT CERN
    """
    # not necessary for the moment
    sys.path.extend([Delphes_DIR])
    sys.path.extend([Delphes_DIR + "classes"])
    sys.path.extend([Delphes_DIR + "external"])
    sys.path.extend([Delphes_DIR + "external/ExRootAnalysis"])
    # necessary in the different configuration of installation of ROOT
    sys.path.extend([ROOT_DIR + "lib"])
    sys.path.extend([ROOT_DIR + "root/lib"])
    sys.path.extend([ROOT_DIR + "build/lib"])
    # ======================== || END   : PATH IN PROJECT || ======================== ##
    #import ROOT  # necesario
    # ===================== || BEGIN : PYPATH IN PROJECT || ===================== ##
    """
    
    This is necesary for import the path for the library of ROOT CERN and Delphes  
    """

    ROOT.gInterpreter.AddIncludePath(Delphes_DIR)
    ROOT.gInterpreter.AddIncludePath(Delphes_DIR + "classes")
    ROOT.gInterpreter.AddIncludePath(Delphes_DIR + "external/")
    ROOT.gInterpreter.AddIncludePath(Delphes_DIR + "external/ExRootAnalysis/")
    ROOT.gSystem.Load(Delphes_DIR + "libDelphes")

    ROOT.gInterpreter.Declare('#include "DelphesClasses.h"')
    ROOT.gInterpreter.Declare('#include "ExRootTreeReader.h"')
    ROOT.gInterpreter.Declare('#include "SortableObject.h"')
    ROOT.gInterpreter.Declare('#include "ExRootTask.h"')
    # ===================== || END   : PYTHONPATH IN PROYECT || ===================== ##
    return ROOT


fbash(Delphes_DIR, ROOT_DIR)  # path in bash of Delphes and Root


# ========================== || INCLUDE CLASS DARKSUSY || =========================== ##
class DarkSUSY:
    def __init__(self):
        self._Registro_Name = "DarkSUSY Event Log"  # type: str
        self._Registro_Dir = "Log/"  # type: str
        self.File = None  # Delphes_Referencia
        self.Entries = -1  # type: int
        self.Mu_forEvent = np.array([])  # type: np.ndarray > 0
        #        self.MaxMuon = 4
        self.Mu_DiMu = np.array([])  # type: np.ndarray
        self.Mu_info = "LOG OF SELECCION OF TWO MUONS.txt"  # type: str
        self.Mu_info_log = bool(1)  # type: bool

        # self.Config_Hist2D = Config_Hist2D()                        # type: object

    def Add_File(self, name  # type: str
                 ):
        """
        =========================================================================================================
        | Charge the file type XXX.root output of caracterization of Delphes                                    |
        =========================================================================================================
        | Examples:                                                                                             |
        | output = AddFile(inp) or                                                                            |
        | output = AddFile(inp.root) or                                                                       |
        | output = AddFile(Data/inp.root)                                                                     |
        =========================================================================================================
        | if the File  "(...).root" exist then "output" gets bool value 1, otherwise is 0                       |
        | The True case create the dependencies:                                                                |
        | self.Muon_N  :: Type = Vector[int]    :: This is one vector with the number of Muons in each entries  |
        | self.Entries :: Type = int            :: This is the number of event or entries for my data           |
        | self.File    :: Type = Title Delphes  :: Include the name of the Tree in the File Delphes             |
        =========================================================================================================
        """
        output = bool(1)
        self.File = ROOT.TChain("Delphes;1")

        if isinstance(name, str) or isinstance(name + ".root", str):  # existence of .root file
            if os.path.isfile(name) or os.path.isfile(name + ".root"):
                if name[-5:] == '.root':
                    self.File.Add(name)
                    print("The file " + name + " has been successfully loaded.")
                else:
                    self.File.Add(name + ".root")
                    print("The file " + name + ".root has been successfully loaded.")
            else:
                print("Error: The file " + name + " has not been successfully loaded, inp dir is not exist.")
                output = 0
        else:
            print("Error: The file " + name + " has not been successfully loaded, inp is not string.")
            output = 0
        # Variables needed to work
        self.Entries = self.File.GetEntries()  # Number of entrance
        #        self.Mu_forEvent = np.array([])  # Number of Muons for entrance

        '''for entry in range(self.Entries):
            self.File.GetEntry(entry)
            self.Mu_forEvent = np.append(self.Mu_forEvent, self.File.Muon.GetEntries())'''

        return output

    def Mu_for_Event(self):
        self.MuEvent = np.array([])
        for entry in range(self.Entries):
            self.File.GetEntry(entry)
            self.MuEvent = np.append(self.MuEvent, self.File.Muon.GetEntries())
        # print self.MuEvent
        return self.MuEvent

    def Select_two_dimuon(self):
        # f = open (self.Mu_info,'w') # CREATE TXT FILE TO SAVE THE CHARACTERIZATION PROCESS INFO
        output = []  # type:
        for entry in range(self.Entries):
            self.File.GetEntry(entry)
            if self.File.Muon.GetEntries() > 3:
                Nmuon = self.File.Muon.GetEntries()
                Chargemuon = []
                for imuon in range(Nmuon):
                    Chargemuon.append(self.File.GetLeaf("Muon.Charge").GetValue(imuon))
                # || SELECT THE POSSIBLE DI-MUONES IN DEPENDENCE OF CHARGE ||
                di_muon = []
                for one in range(len(Chargemuon)):
                    for two in range(one, len(Chargemuon)):
                        if Chargemuon[one] + Chargemuon[two] == 0:
                            di_muon.append([one, two])
                # || ** SELECT THE PAIR WITH LOWER MASS ** ||
                AllDiffInvMass = np.array([])  # type: np.ndarray # 1D # Diff of Inv Mass
                AllInvMass = np.array([])  # type: np.ndarray # 2D # Values od Inv Mass
                Alltwo_di_muon = np.array([])  # type: np.ndarray # 1D # All combination of Di-muon
                # || COMBINATION OF TWO DI-MUONS ||
                for one in range(len(di_muon)):
                    for two in range(one + 1, len(di_muon)):
                        #  || Do not share particles ||
                        if di_muon[one][0] != di_muon[two][0] and di_muon[one][0] != di_muon[two][1] and \
                                di_muon[one][1] != di_muon[two][0] and di_muon[one][1] != di_muon[two][1]:

                            mass1 = (self.File.Muon.At(di_muon[one][0]).P4() +
                                     self.File.Muon.At(di_muon[one][1]).P4()).M()  # First  Mass
                            mass2 = (self.File.Muon.At(di_muon[two][0]).P4() +
                                     self.File.Muon.At(di_muon[two][1]).P4()).M()  # Second Mass
                            AllDiffInvMass = np.append(AllDiffInvMass,
                                                       np.abs(mass1 - mass2))  # [ (...) , |M1 - M2|]
                            # Indices di-muon1 (i,j) ; di-muon2 (n,m) -> [ i, j, n, m ]
                            two_di_muon = np.array([di_muon[one][0], di_muon[one][1],
                                                    di_muon[two][0], di_muon[two][1]])
                            if len(Alltwo_di_muon) == 0:
                                Alltwo_di_muon = two_di_muon
                                # print(Alltwo_di_muon)
                                # print(AllInvMass)
                                AllInvMass = np.hstack((AllInvMass, [mass1, mass2]))
                            else:
                                Alltwo_di_muon = np.vstack([Alltwo_di_muon, two_di_muon])
                                AllInvMass = np.vstack([AllInvMass, [mass1, mass2]])
                # MIN OF MASS DIF IN THE VECTOR AllInvMAss
                # print(np.min(AllDiffInvMass))
                # print(AllDiffInvMass)
                if len(AllDiffInvMass) > 0:
                    # print(AllDiffInvMass)
                    # print(np.where(np.min(AllDiffInvMass) == AllDiffInvMass)[0][0])
                    logic = np.min(AllDiffInvMass) == AllDiffInvMass  # MATRIX LOGIC
                    # print(logic)
                    # logic = np.where(np.min(AllDiffInvMass) == AllDiffInvMass)[0][0]  # MATRIX LOGIC
                    # print(logic)
                    DiMuon2 = (Alltwo_di_muon[logic])[0]  # TWO DI-MUON WITH > (MASS1-MASS2)
                    # print(DiMuon2)
                    # ALL DI-MUON FOR EVENT
                    if len(output) == 0:
                        output = np.zeros([1, 5], dtype=int)
                        # output[0, 0] = int(entry)
                        # print("_______")
                        output = [int(entry), int(DiMuon2[0]), int(DiMuon2[1]), int(DiMuon2[2]), int(DiMuon2[3])]
                        # print(str(output))
                        # print(str(DiMuon2))
                        # output[0, 1:] = map(int, DiMuon2)
                        # output = np.hstack([entry, DiMuon2])
                    else:
                        # intg = np.hstack([int(entry), map(int, DiMuon2)])
                        # output = np.vstack([output, intg])
                        intg = [int(entry), int(DiMuon2[0]), int(DiMuon2[1]), int(DiMuon2[2]), int(DiMuon2[3])]
                        output = np.vstack([output, intg])
                        #print(output)

        # f.close()
        # RESUMEN FINAL
        '''print("De los ", self.Entries , " eventos procesados, ", sum(self.Nmuon>3) , " poseen mas de 3 muones y ",
              output.shape[0] , " fueron seleccionados bajo el criterio de minima masa invariante.")'''
        self.Mu_DiMu = output
        return output

    def Obtein(self, var, particle="Muon", order=False):
        # output = np.ndarray([])
        # print var
        if var == "Entries":
            output = self.Entries
        elif var in ["Charge", "T", "PT", "Eta", "Phi", "MassInv", "D0", "ErrorD0", "DZ", "ErrorDZ", "IsolationVar",
                     "SumPt", "SumPtNeutral"]:
            # print(self.Mu_DiMu)
            for i in range(self.Mu_DiMu.shape[0]):
                # print(i)
                if len(self.Mu_DiMu.shape) > 1:
                    self.File.GetEntry(int(self.Mu_DiMu[i, 0]))  # Seleccionar el evento correspondiente
                    # vector con los resultados del evento de cada particula
                    if var == "MassInv":
                        vet = [(self.File.Muon.At(int(self.Mu_DiMu[i, 1])).P4() +
                                self.File.Muon.At(int(self.Mu_DiMu[i, 2])).P4()).M(),  # First  Mass
                               (self.File.Muon.At(int(self.Mu_DiMu[i, 3])).P4() +
                                self.File.Muon.At(int(self.Mu_DiMu[i, 4])).P4()).M()]  # Second Mass
                    else:
                        # print self.File.GetLeaf(particle + "." + var).GetValue(self.Mu_DiMu[i, 1])
                        vet = [self.File.GetLeaf(particle + "." + var).GetValue(int(self.Mu_DiMu[i, 1])),
                               self.File.GetLeaf(particle + "." + var).GetValue(int(self.Mu_DiMu[i, 2])),
                               self.File.GetLeaf(particle + "." + var).GetValue(int(self.Mu_DiMu[i, 3])),
                               self.File.GetLeaf(particle + "." + var).GetValue(int(self.Mu_DiMu[i, 4]))]
                elif len(self.Mu_DiMu.shape) is 1:
                    self.File.GetEntry(int(self.Mu_DiMu[0]))  # Seleccionar el evento correspondiente
                    # vector con los resultados del evento de cada particula
                    if var == "MassInv":
                        vet = [(self.File.Muon.At(int(self.Mu_DiMu[1])).P4() +
                                self.File.Muon.At(int(self.Mu_DiMu[2])).P4()).M(),  # First  Mass
                               (self.File.Muon.At(int(self.Mu_DiMu[3])).P4() +
                                self.File.Muon.At(int(self.Mu_DiMu[4])).P4()).M()]  # Second Mass
                    else:
                        # print self.File.GetLeaf(particle + "." + var).GetValue(self.Mu_DiMu[i, 1])
                        vet = [self.File.GetLeaf(particle + "." + var).GetValue(int(self.Mu_DiMu[1])),
                               self.File.GetLeaf(particle + "." + var).GetValue(int(self.Mu_DiMu[2])),
                               self.File.GetLeaf(particle + "." + var).GetValue(int(self.Mu_DiMu[3])),
                               self.File.GetLeaf(particle + "." + var).GetValue(int(self.Mu_DiMu[4]))]
                else:
                    print(" :: Entries no include :: ")
                    output = None
                    return output

                # print vet
                if order:
                    vet = np.array(vet)
                    vet = vet[vet.argsort()]

                if "output" not in locals():
                    output = np.hstack(vet)
                else:
                    intg = np.hstack(vet)
                    output = np.vstack([output, intg])
                # print output
        else:
            print(" :: var no include :: ")
            output = None

        return output


def FloatFile(name):
    FileROOT = open(name, 'r')
    Reduction_Event = []
    for line in FileROOT:
        try:
            float(line)
            Reduction_Event.append(float(line))
            # print str(line)
        except ValueError:
            continue

    FileROOT.close()
    return Reduction_Event

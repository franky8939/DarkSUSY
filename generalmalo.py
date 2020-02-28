#!/usr/bin/env python
# %%
direct = [
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_0.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_10.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_20.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_30.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_40.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_50.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_60.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_70.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_80.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_90.root",
    "Mu4_darkSUSY_Event_10000_Ma_0.25_Tc_100.root"]
DarkFile0 = DarkSUSY()
DarkFile0.Add_File("datosnew/" + direct[0])
DarkFile0.Select_two_dimuon()
DarkFile10 = DarkSUSY()
DarkFile10.Add_File("datosnew/" + direct[1])
DarkFile10.Select_two_dimuon()
DarkFile20 = DarkSUSY()
DarkFile20.Add_File("datosnew/" + direct[2])
DarkFile20.Select_two_dimuon()
DarkFile30 = DarkSUSY()
DarkFile30.Add_File("datosnew/" + direct[3])
DarkFile30.Select_two_dimuon()
DarkFile40 = DarkSUSY()
DarkFile40.Add_File("datosnew/" + direct[4])
DarkFile40.Select_two_dimuon()
DarkFile50 = DarkSUSY()
DarkFile50.Add_File("datosnew/" + direct[5])
DarkFile50.Select_two_dimuon()
DarkFile60 = DarkSUSY()
DarkFile60.Add_File("datosnew/" + direct[6])
DarkFile60.Select_two_dimuon()
DarkFile70 = DarkSUSY()
DarkFile70.Add_File("datosnew/" + direct[7])
DarkFile70.Select_two_dimuon()
DarkFile80 = DarkSUSY()
DarkFile80.Add_File("datosnew/" + direct[8])
DarkFile80.Select_two_dimuon()
DarkFile90 = DarkSUSY()
DarkFile90.Add_File("datosnew/" + direct[9])
DarkFile90.Select_two_dimuon()
DarkFile100 = DarkSUSY()
DarkFile100.Add_File("datosnew/" + direct[10])
DarkFile100.Select_two_dimuon()

# %%

DarkFile10.Select_two_dimuon()

# %%
PropMuon0 = DarkFile0.Obtein("D0", "Muon", True)
PropMuon10 = DarkFile10.Obtein("D0", "Muon", True)
PropMuon20 = DarkFile20.Obtein("D0", "Muon", True)
PropMuon30 = DarkFile30.Obtein("D0", "Muon", True)
PropMuon40 = DarkFile40.Obtein("D0", "Muon", True)
PropMuon50 = DarkFile50.Obtein("D0", "Muon", True)
PropMuon60 = DarkFile60.Obtein("D0", "Muon", True)
PropMuon70 = DarkFile70.Obtein("D0", "Muon", True)
PropMuon80 = DarkFile80.Obtein("D0", "Muon", True)
PropMuon90 = DarkFile90.Obtein("D0", "Muon", True)
PropMuon100 = DarkFile100.Obtein("D0", "Muon", True)
print PropMuon100

# %%

# dir(config)
# print(PTMuon.reshape(1,PTMuon.shape[0]*PTMuon.shape[1]))
# graph = Graph( PTMuon.reshape(1,PTMuon.shape[0]*PTMuon.shape[1]) )
# print(PTMuon.reshape(1,PTMuon.shape[0]*PTMuon.shape[1]))
# print( dir(config) )
'''hist1D(PropMuon0, PropMuon10, PropMuon20, PropMuon30, PropMuon40, PropMuon50,
       PropMuon60, PropMuon70, PropMuon80, PropMuon90, PropMuon100,
       title="D0",
       xlabel='Rangos',
       ylabel='Frecuencia',
       savefile="Frecuencia D0.pdf",
       start=True,
       type="Pbar",
       legend=["Tc 0", "Tc 20", "Tc 30", "Tc 40", "Tc 50", "Tc 60", "Tc 70", "Tc 80", "Tc 90", "Tc 100"])

hist1D(PropMuon10, PropMuon100,
       title="D0",
       xlabel='Rangos',
       ylabel='Frecuencia',
       savefile="Frecuencia D0.pdf",
       start=True,
       type="bar",
       legend=["ct = 10", "ct = 100"])'''
# graph = Graph( PTMuon )
# graph.__AddProp__("xlabel", 'Momento Angular')
# graph.__AddProp__("xlim",[0,100])
# graph.showGraph()

# %%

# a= "a3"
# print(PTMuon0.reshape(1,PTMuon0.shape[0]*PTMuon0.shape[1]))
# print(PTMuon0.reshape(1,PTMuon0.shape[0]*PTMuon0.shape[1])+1)
# %%
a = {"a1": [1, 2, 3],
     "a2": "hola"
     }
print(a["a1"])
print(a["a2"])



'''
## ============================ || BEGIN : MODULES || ============================ ##
Modules using
import os
#import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
#import statistics as stats # usar media o desviacion estandar
import h5py as h # manipular extensiones
from matplotlib.mathtext import List
import sys
import random
import argparse
import ROOT
## ============================= || BEGIN : MAIN || =============================== ##
def main(dirmad, rootfile):
    darksusy = DarkSUSY()
    darksusy.Add_File(rootfile)
    eventdark = darksusy.Select_two_di_muon()
    print(eventdark)



## ========================= || BEGIN : EXTRAS FUNCTION || ========================= ##
class DarkSUSY:
    def __init__(self):
        self._Registro_Name = "DarkSUSY Event Log"  # type: str
        self._Registro_Dir = "Log/"  # type: str
        self.File = None  # type: Delphes_Referencia
        self.Entries = -1  # type: int
        self.Mu_forEvent = np.array([])  # type: List[float] > 0
        #        self.MaxMuon = 4
        self.Mu_DiMu = np.array([])  # type: ndarray
        self.Mu_info = "Informacion general.txt"  # type: str
        self.Mu_info_log = bool(1)  # type: bool

        self.Config_Hist2D = Config_Hist2D()  # type: object

    def Add_File(self, name):
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
                    print(" :: The file " + name + ".root has been successfully loaded.")
                else:
                    self.File.Add(name + ".root")
                    print(" :: The file " + name + " has been successfully loaded.")
            else:
                print(" :: Error: The file " + name + " has not been successfully loaded, inp dir is not exist.")
                output = 0
        else:
            print(" :: Error: The file " + name + " has not been successfully loaded, inp is not string.")
            output = 0
        # Variables needed to work
        self.Entries = self.File.GetEntries()  # Number of entrance
        self.Mu_forEvent = np.array([])  # Number of Muons for entrance
        porciento = 0
        #print(" :: OBTENGAMOS LOS MUONES POR EVENTOS :: ")
        #for entry in range(self.Entries):
        #    self.File.GetEntry(entry)
        #    self.Mu_forEvent = np.append(self.Mu_forEvent, self.File.Muon.GetEntries())

            #if round(float(entry)/self.Entries*100) > porciento:
            #    print(" :: Porciento de ejecucion : ", str(round(float(entry)/self.Entries*100)))
            #    porciento = round(float(entry)/self.Entries*100)
            #else:
            #    print(str(entry/self.Entries*100), " de  ", str(self.Entries), " donde ", str(entry))
            #    print(" :: Evento : ", str(entry))

        return output

    def Select_two_di_muon(self):

        f = open(self.Mu_info, 'w')  # CREATE TXT FILE TO SAVE THE CHARACTERIZATION PROCESS INFO
        output = []  # type: bool
        porciento = 0
        for entry in range(self.Entries): # type: int

            if round(float(entry)/self.Entries*100) > porciento:
                print(" :: Porciento de ejecucion : ", str(round(float(entry)/self.Entries*100)))
                porciento = round(float(entry)/self.Entries*100)
            #else:
            #    print(" :: Evento : ", str(entry))
            Event = self.File.GetEntry(entry)
            if self.File.Muon.GetEntries() > 3:
                Nmuon = self.File.Muon.GetEntries()
                Chargemuon = []  # carga de los muones, matrix[1 x (3>)]
                for imuon in range(Nmuon):  # elemento muon, type: int
                    Chargemuon.append(self.File.GetLeaf("Muon.Charge").GetValue(imuon))

                # SELECT THE POSSIBLE DI-MUONES IN DEPENDENCE OF CHARGE
                di_muon = []  # pares posibles, matrix[(3>)! x 2], type: int>=0
                for one in range(len(Chargemuon)):
                    for two in range(one, len(Chargemuon)):
                        if Chargemuon[one] + Chargemuon[two] == 0:
                            di_muon.append([one, two])

                # SELECT THE PAIR WITH LOWER MASS, COMBINATION OF TWO DI-MUONS
                AllDiffInvMass = np.array([])  # type: ndarray # 1D # , Diff of Inv Mass
                AllInvMass = np.array([])  # type: ndarray # 2D # Values od Inv Mass
                Alltwo_di_muon = np.array([])  # type: ndarray # 1D # All combination of Di-muon

                for one in range(len(di_muon)):
                    for two in range(one + 1, len(di_muon)):
                        # Do not share particles
                        if di_muon[one][0] != di_muon[two][0] and di_muon[one][0] != di_muon[two][1] and \
                                di_muon[one][1] != di_muon[two][0] and di_muon[one][1] != di_muon[two][1]:

                            mass1 = (self.File.Muon.At(di_muon[one][0]).P4() +
                                     self.File.Muon.At(di_muon[one][1]).P4()).M()  # First  Mass
                            mass2 = (self.File.Muon.At(di_muon[two][0]).P4() +
                                     self.File.Muon.At(di_muon[two][1]).P4()).M()  # Second Mass
                            AllDiffInvMass = np.append(AllDiffInvMass, np.abs(mass1 - mass2))  # [ (...) , |M1 - M2|]
                            # Indices di-muon1 (i,j) ; di-muon2 (n,m) -> [ i, j, n, m ]
                            two_di_muon = np.array([di_muon[one][0], di_muon[one][1],
                                                    di_muon[two][0], di_muon[two][1]])
                            if len(Alltwo_di_muon) == 0:
                                Alltwo_di_muon = two_di_muon
                                AllInvMass = [mass1, mass2]
                            else:
                                Alltwo_di_muon = np.vstack([Alltwo_di_muon, two_di_muon])
                                AllInvMass = np.vstack([AllInvMass, [mass1, mass2]])

                # MIN OF MASS DIF IN THE VECTOR AllInvMAss
                logic = np.where(np.min(AllDiffInvMass) == AllDiffInvMass)[0][0]  # MATRIX LOGIC
                DiMuon2 = (Alltwo_di_muon[logic])  # TWO DI-MUON WITH > (MASS1-MASS2)

                ## ALL DI-MUON FOR EVENT
                if len(output) == 0:
                    output = np.hstack([entry, DiMuon2])
                else:
                    intg = np.hstack([entry, DiMuon2])  # matrix[entrada, 1photon[1muon,2muon], 2photon[1muon, 2muon]]
                    output = np.vstack([output, intg])
        f.close()
        self.Mu_DiMu = output
        return output

    def fhist(self, selfnew, entrada):

        if selfnew.percentil > 0 and selfnew.percentil < 100:
            log1 = np.percentile(entrada, selfnew.percentil) < entrada
            log2 = np.percentile(entrada, 100 - selfnew.percentil) > entrada
            log = log1 * log2
            hist = []
            for i in range(len(entrada)):
                if log[i]:
                    hist.append(entrada[i])
        else:
            hist = entrada
            log = True
        ## GRAF

        if hasattr(selfnew, "bins"):
            if hasattr(selfnew, "xlim"):
                binss = int(round(selfnew.bins * (max(hist) - min(hist)) / (selfnew.xlim[1] - selfnew.xlim[0])))
                # print(binss)
                plt.hist(np.delete(hist, log), bins=binss)
                print(1)
            else:
                plt.hist(np.delete(hist, log), bins=selfnew.bins)
                print(2)
        else:
            plt.hist(np.delete(hist, log), bins=10)
            print(3)

        ## PROP
        if hasattr(selfnew, "xlim"):
            plt.xlim(selfnew.xlim[0], selfnew.xlim[1])
        else:
            plt.xlim(min(hist), max(hist))
        if hasattr(selfnew, "ylim"): plt.ylim(selfnew.ylim[0], selfnew.ylim[1])

        if hasattr(selfnew, "title") and len(selfnew.title) > 0: plt.title(selfnew.title)

        if hasattr(selfnew, "grid"):
            plt.grid(selfnew.grid)
        else:
            plt.grid(True)

        if hasattr(selfnew, "ylabel") and len(selfnew.ylabel) > 0: plt.ylabel(selfnew.ylabel)
        if hasattr(selfnew, "xlabel") and len(selfnew.xlabel) > 0: plt.xlabel(selfnew.xlabel)

        if selfnew.start:
            plt.show()
        else:
            print(" Auto plot is deactivate, change the bool .\"start\" ")
        plt.clf()  # closed
        return 1

    def HistM(self):
        # MASA DE LOS DI-MUONES
        AllMass_of_photon = []
        AllminMass_of_photon = []
        AllmaxMass_of_photon = []
        ALL_DMuon_ForEvent = np.array(self.Mu_DiMu)
        for event_2dark in range(self.Mu_DiMu.shape[0]):  # range( entries  ):
            Event = self.File.GetEntry(ALL_DMuon_ForEvent[event_2dark, 0])
            muones = self.File.Muon
            mass1 = (muones.At(int(ALL_DMuon_ForEvent[event_2dark, 1])).P4() +
                     muones.At(int(ALL_DMuon_ForEvent[event_2dark, 2])).P4()).M()
            mass2 = (muones.At(int(ALL_DMuon_ForEvent[event_2dark, 3])).P4() +
                     muones.At(int(ALL_DMuon_ForEvent[event_2dark, 4])).P4()).M()
            AllMass_of_photon.append(mass1)
            AllMass_of_photon.append(mass2)
            if mass1 > mass2:
                AllminMass_of_photon.append(mass2)
                AllmaxMass_of_photon.append(mass1)
            else:
                AllminMass_of_photon.append(mass1)
                AllmaxMass_of_photon.append(mass2)

        # Histogram of all mass
        self.Config_Hist2D.xlim = [np.percentile(AllMass_of_photon, 1), np.percentile(AllMass_of_photon, 99)]
        # plt.figure(1)
        plt.rcParams['figure.figsize'] = [10, 20]
        plt.subplot(311);
        self.Config_Hist2D.title = 'Mass of all DarkPhoton'
        self.Config_Hist2D.percentil = 2
        self.fhist(self.Config_Hist2D, AllMass_of_photon)

        plt.subplot(312);
        self.title = 'Mass of all Max-DarkPhoton'
        self.percentil = 0
        self.fhist(self.Config_Hist2D, AllmaxMass_of_photon)

        plt.subplot(313);
        self.title = 'Mass of all Min-DarkPhoton'
        self.percentil = 0
        self.fhist(self.Config_Hist2D, AllminMass_of_photon)

    def HistPt(self):
        AllPt_of_photon = []
        All1Pt_of_photon = []
        All2Pt_of_photon = []
        All3Pt_of_photon = []
        All4Pt_of_photon = []
        ALL_DMuon_ForEvent = np.array(self.Mu_DiMu)
        for event_2dark in range(self.Mu_DiMu.shape[0]):  # range( entries  ):
            # print(event_2dark)
            Event = self.File.GetEntry(ALL_DMuon_ForEvent[event_2dark, 0])

            for imuon in range(4):
                AllPt_of_photon.append(self.File.GetLeaf("Muon.PT").GetValue(imuon))
            AllPt_of_photon_event = np.hstack([AllPt_of_photon[-4:-1], AllPt_of_photon[-1]])
            AllPt_of_photon_event = np.sort(AllPt_of_photon_event)
            All1Pt_of_photon.append(AllPt_of_photon_event[0])
            All2Pt_of_photon.append(AllPt_of_photon_event[1])
            All3Pt_of_photon.append(AllPt_of_photon_event[2])
            All4Pt_of_photon.append(AllPt_of_photon_event[3])

        ## HISTOGRAMAS DE TODOS LOS MOMENTOS ANGULARES
        self.xlim = [min(AllPt_of_photon_event), max(AllPt_of_photon_event)]
        # plt.figure(1)
        plt.rcParams['figure.figsize'] = [10, 20]
        plt.subplot(511);
        self.title = 'Momento Transversal de todos los Muones'
        self.fhist(self.Config_Hist2D, AllPt_of_photon)
        self.xlabel = " Momento Transversal"
        self.percentil = 0
        plt.subplot(512);
        self.title = "Momento Transversal de los Muones en la posicion 1"  # 
        self.fhist(self.Config_Hist2D, All1Pt_of_photon)
        plt.subplot(513);
        self.title = "Momento Transversal de los Muones en la posicion 2"  # 
        self.fhist(self.Config_Hist2D, All2Pt_of_photon)
        plt.subplot(514);
        self.title = "Momento Transversal de los Muones en la posicion 3"  # 
        self.fhist(self.Config_Hist2D, All3Pt_of_photon)
        plt.subplot(515);
        self.title = "Momento Transversal de los Muones en la posicion 4"  # 
        #self.fhist(self.Config_Hist2D, All4Pt_of_photon)
        #print(All4Pt_of_photon)

class Config_Hist2D:
    """ Configure Histograms Graphic in 2D"""

    def __init__(self):
        self.grid = True
        self.bins = 50
        self.percentil = 0
        self.ylabel = " Frecuencia "
        self.start = True

    def __AddProp__(self, name, value=None):
        self.__dict__[name] = value


## ========================= || BEGIN : CONDITION OF MAIN || ========================= ##
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-dirmad", type=str, help="Directory of Madgraph 5", default="source/MG5_aMC_v2_6_7")
    parser.add_argument("-rootfile", type=str, help="Name of ROOT Input File")

    args = parser.parse_args()

    if os.path.exists(args.dirmad):
        print(" :: Using Directory of Madgraph 5 : " + args.dirmad)
    else:
        print(" :: Directory of Madgraph 5 incorrect")
    if os.path.exists(args.rootfile):
        print(" :: Using Directory of ROOT : " + args.rootfile)
    else:
        print(" :: Directory of ROOT incorrect")
    ## ============================== || BEGIN : DIR || ============================== ##
    Delphes_DIR = args.dirmad + "/Delphes/"
    ROOT_DIR = "/home/franky8939/PROGRAMAS/root-6.18.02/"
    ## ======================== || BEGIN : PATH IN PROYECT || ======================== ##
    """ 
    This is necesary for import path for the bash because in the Jupyter of Pycharm 
    not charge this bash include in the environment and is necessary por import the 
    module of the program ROOT CERN 
    """
    # not necesary for the moment
    sys.path.extend([Delphes_DIR])
    sys.path.extend([Delphes_DIR + "classes"])
    sys.path.extend([Delphes_DIR + "external"])
    sys.path.extend([Delphes_DIR + "external/ExRootAnalysis"])
    # necesary in the different configuration of installation of ROOT
    sys.path.extend([ROOT_DIR + "lib"])
    sys.path.extend([ROOT_DIR + "root/lib"])
    sys.path.extend([ROOT_DIR + "build/lib"])
    ## ===================== || BEGIN : PYTHONPATH IN PROYECT || ===================== ##
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

    # CORRER MAIN ANTERIOREMENTE DEFINIDO
    main(args.dirmad, args.rootfile)
'''















# ============================ || BEGIN : MODULES || ============================ #
''' Modules using '''
import os
# import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
# import statistics as stats # usar media o desviacion estandar
import h5py as h  # manipular extensiones
import re
import sys
import ROOT

# ============================ || END   : MODULES || ============================ ##

# ======================== || BEGIN : PATH IN PROYECT || ======================== #
from numpy.core.records import ndarray

""" 
This is necesary for import path for the bash because in the Jupyter of Pycharm 
not charge this bash include in the environment and is necessary por import the 
module of the program ROOT CERN 
"""


def fbash(Delphes_DIR, ROOT_DIR):
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

    import ROOT  #

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


# ========================== || INCLUDE GENERAL CLASS OBJECT || =========================== ##
class fObject:
    """ Configure of object general for Graphic """

    def __init__(self, **kwargs):
        # basic options
        self.grid = True  # "Default, bool que describe is el grafico tendra la propiedad grid o no"
        self.percentil = 0  # Default, float, en el rango 0<x<100, corta la informacion correspondiente
        self.type = "bar"
        self.zlabel = " Frecuencia "
        self.bins = 30
        self.start = False
        self.sizeBarra = .8  # porciento del tama;o de la barra del histograma con respecto al total
        # include todas las entradas respectivas
        for name, value in kwargs.items():
            self.__dict__[name] = value
        # declaraciones especificas

    def __AddProp__(self, name, value=None):
        """
        :param name: declara el nombre la la nueva variable a incluir
        :param value: optional, declara el valor de la nueva variable a incluir
        :return: no tiene
        """
        self.__dict__[name] = value


# ========================== || INCLUDE CLASS DARKSUSY || =========================== ##
class DarkSUSY:
    def __init__(self):
        self._Registro_Name = "DarkSUSY Event Log"  # type: str
        self._Registro_Dir = "Log/"  # type: str
        self.File = None  # type: Delphes_Referencia
        self.Entries = -1  # type: int
        self.Mu_forEvent = np.array([])  # type: List[float] > 0
        #        self.MaxMuon = 4
        self.Mu_DiMu = np.array([])  # type: ndarray
        self.Mu_info = "LOG OF SELECCION OF TWO MUONS.txt"  # type: str
        self.Mu_info_log = bool(1)  # type: bool

        # self.Config_Hist2D = Config_Hist2D()                        # type: object

    def _Add_File(self, name  # type: str
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
                    print("The file " + name + ".root has been successfully loaded.")
                else:
                    self.File.Add(name + ".root")
                    print("The file " + name + " has been successfully loaded.")
            else:
                print("Error: The file " + name + " has not been successfully loaded, inp dir is not exist.")
                output = 0
        else:
            print("Error: The file " + name + " has not been successfully loaded, inp is not string.")
            output = 0
        # Variables needed to work
        self.Entries = self.File.GetEntries()  # Number of entrance
        self.Mu_forEvent = np.array([])  # Number of Muons for entrance

        for entry in range(self.Entries):
            self.File.GetEntry(entry)
            self.Mu_forEvent = np.append(self.Mu_forEvent, self.File.Muon.GetEntries())

        return output

    def Select_two_dimuon(self):
        # f = open (self.Mu_info,'w') # CREATE TXT FILE TO SAVE THE CHARACTERIZATION PROCESS INFO
        output = []  # type:
        for entry in range(self.Entries):
            Event = self.File.GetEntry(entry)
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
                AllDiffInvMass = np.array([])  # type: ndarray # 1D # Diff of Inv Mass
                AllInvMass = np.array([])  # type: ndarray # 2D # Values od Inv Mass
                Alltwo_di_muon = np.array([])  # type: ndarray # 1D # All combination of Di-muon
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
                                #print(Alltwo_di_muon)
                                #print(AllInvMass)
                                AllInvMass = np.hstack((AllInvMass, [mass1, mass2]))
                            else:
                                Alltwo_di_muon = np.vstack([Alltwo_di_muon, two_di_muon])
                                AllInvMass = np.vstack([AllInvMass, [mass1, mass2]])
                # MIN OF MASS DIF IN THE VECTOR AllInvMAss
                logic = np.where(np.min(AllDiffInvMass) == AllDiffInvMass)[0][0]  # MATRIX LOGIC
                # print(logic)
                DiMuon2 = (Alltwo_di_muon[logic])  # TWO DI-MUON WITH > (MASS1-MASS2)
                ## ALL DI-MUON FOR EVENT
                if len(output) == 0:
                    output = np.hstack([entry, DiMuon2])
                else:
                    intg = np.hstack([entry, DiMuon2])
                    output = np.vstack([output, intg])
        # f.close()
        ## RESUMEN FINAL
        '''print("De los ", self.Entries , " eventos procesados, ", sum(self.Nmuon>3) , " poseen mas de 3 muones y ",
              output.shape[0] , " fueron seleccionados bajo el criterio de minima masa invariante.")'''
        self.Mu_DiMu = output
        return output

    def _Obtein(self, var, particle="Muon", order=False):
        output = []
        if var == "Entries":
            output = self.Entries
        elif var == "Charge" or var == "T" or var == "PT" or var == "Eta" or var == "Phi" or var == "MassInv" or var == "D0" or var == "Dz":
            for i in range(self.Mu_DiMu.shape[0]):
                self.File.GetEntry(self.Mu_DiMu[i, 0])  # Seleccionar el evento correspondiente
                # vector con los resultados del evento de cada particula
                if var == "MassInv":
                    vect = [(self.File.Muon.At(self.Mu_DiMu[i, 1]).P4() +
                             self.File.Muon.At(self.Mu_DiMu[i, 2]).P4()).M(),  # First  Mass
                            (self.File.Muon.At(self.Mu_DiMu[i, 3]).P4() +
                             self.File.Muon.At(self.Mu_DiMu[i, 4]).P4()).M()]  # Second Mass
                else:
                    vect = [self.File.GetLeaf(particle + "." + var).GetValue(self.Mu_DiMu[i, 1]),
                            self.File.GetLeaf(particle + "." + var).GetValue(self.Mu_DiMu[i, 2]),
                            self.File.GetLeaf(particle + "." + var).GetValue(self.Mu_DiMu[i, 3]),
                            self.File.GetLeaf(particle + "." + var).GetValue(self.Mu_DiMu[i, 4])]
                if order:
                    vect = np.array(vect)
                    vect = vect[vect.argsort()]

                if len(output) == 0:
                    output = np.hstack(vect)
                else:
                    intg = np.hstack(vect)
                    output = np.vstack([output, intg])
        else:
            output = -1

        return output

## ========================== || INCLUDE DEF HIST || =========================== ##

def hist1D(*argv,  # type:ndarray
           **kwargs):
    # Definir el tipo de grafico y otros basicos necesarios
    for name, value in kwargs.items():  # se busca valor
        # type si existe
        if name is "type":  # type of graphic
            ty = value
        # incluir conf si existe en el entorno de trabajo
        if name is "conf":
            conf = value
        # donde salvar archivo
        if name is "savefile":
            savefile = value
        if name is "bins":
            bins = value
        if name is "start":  # verificar que se grafica show() o no
            start = value
        if name is "sizeBarra" and 0 < value < 1:
            sizeBarra = value  # tama;o de la barra
        if name is "legend":
            legend = value

    if "conf" in locals():
        print "00"
        if "ty" not in locals():
            if hasattr(conf, "type"):
                ty = conf.type
            else:
                print "0"
                ty = "Pbar"  # basico histograma pero solo puntos
        if "bins" not in locals():
            if hasattr(conf, "bins"):
                bins = conf.bins
            else:
                bins = 30  # basico histograma pero solo puntos
        if "start" not in locals():
            if hasattr(conf, "start"):
                start = conf.start
            else:
                start = False
        if "sizeBarra" not in locals():
            if hasattr(conf, "sizeBarra"):
                sizeBarra = conf.sizeBarra
            else:
                sizeBarra = .9
    else:
        if "ty" not in locals():
            print "1"
            ty = "Pbar"  # basico histograma pero solo puntos
        if "bins" not in locals():
            bins = 30  # basico histograma pero solo puntos
        if "start" not in locals():
            start = conf.start
        if "sizeBarra" not in locals():
            sizeBarra = conf.sizeBarra

    print ty
    # Graficar
    if ty is "bar":
        count = 0
        for inp in argv:
            # print "count"
            hist, bn = np.histogram(inp, bins=bins)  # **si esta en la declaracion inicial
            width = sizeBarra * (bn[1] - bn[0])  # tama;o de la barra
            center = (bn[:-1] + bn[1:]) / 2
            plt.bar(center, hist/( np.sum(hist)* (bn[1] - bn[0]) ), align='center', width=width)  # graphic
    if ty is "Pbar":
        for inp in argv:
            # print "count"
            hist, bn = np.histogram(inp, bins=bins)
            width = sizeBarra * (bn[1] - bn[0])  # tama;o de la barra
            center = (bn[:-1] + bn[1:]) / 2
            plt.plot(center, hist/( np.sum(hist)* (bn[1] - bn[0]) ))  # **si esta en la declaracion inicial

    # propiedades en 'conf'
    if "conf" in locals():
        for name in dir(conf):
            if name in dir(plt) and (name.find("_") != 0):  # comparar con la clase plt
                # print(plt.__dict__[name])
                try:
                    # print("0" + name)
                    plt.__dict__[name](conf.__dict__[name])
                except:
                    print(" ERROR al cargar " + name + " en conf")
    # propiedades en 'kwargs'
    # print kwargs
    # print locals()
    for name, value in kwargs.items():
        if name in dir(plt):  # comparar con la clase plt
            try:
                plt.__dict__[name](value)
            except:
                print(" ERROR al cargar " + name + " en kwargs")
    if "legend" in locals():
        plt.legend(legend)
    # plt.xlabel('Smarts')
    # plt.ylabel('Probability')
    if "savefile" in locals():
        plt.savefig(savefile)
    # print start
    if "start" in locals():  # se declaro como entrada entonces
        if start:
            plt.show()
    else:
        if "conf" in locals() and hasattr(conf, "start") and conf.start:
            plt.show()


'''def hist1D(inp,  # type: ndarray
           conf=None,
           **kwargs):
    # print(locals())
    # print(inp)
    # print(dir(conf))
    if inp.shape[0] == 1:
        inp = inp.T
    # plt.hist(inp)
    # print kwargs.items()
    # # hist
    for name, value in kwargs.items():  # se busca valor
        if name is "bins":
            hist, bn = np.histogram(inp, bins=value)  # **si esta en la declaracion inicial
        if name is "savefile":
            savefile = value
        if name is "start":  # verificar que se grafica show() o no
            start = value
            if conf in locals() and hasattr(conf, "start"):
                conf.start = start

    if 'hist' not in locals():
        if "conf" in locals() and hasattr(conf, "bins"):
            hist, bn = np.histogram(inp, bins=conf.bins)  # *si esta en conf
        else:
            hist, bn = np.histogram(inp, bins=30)  # Basic
    # # propiedades
    for name, value in kwargs.items():  # se busca valor
        if name is "sizeBarra" and 0 < value < 1:
            width = value * (bn[1] - bn[0])  # tama;o de la barra

    if 'width' not in locals():
        if "conf" in locals() and hasattr(conf, "sizeBarra"):
            width = conf.sizeBarra * (bn[1] - bn[0])  # tama;o de la barra
        else:
            width = 0.9 * (bn[1] - bn[0])  # tama;o de la barra
    # # center of bar
    center = (bn[:-1] + bn[1:]) / 2
    # # graficar
    plt.bar(center, hist, align='center', width=width)  # graphic
    # propiedades en 'conf'
    if "conf" in locals():
        for name in dir(conf):
            if name in dir(plt) and (name.find("_") != 0):  # comparar con la clase plt
                # print(plt.__dict__[name])
                try:
                    # print("0" + name)
                    plt.__dict__[name](conf.__dict__[name])
                except:
                    print(" ERROR al cargar " + name + " en conf")
    # propiedades en 'kwargs'
    # print kwargs
    # print locals()
    for name, value in kwargs.items():
        if name in dir(plt):  # comparar con la clase plt
            try:
                plt.__dict__[name](value)
            except:
                print(" ERROR al cargar " + name + " en kwargs")

    # plt.xlabel('Smarts')
    # plt.ylabel('Probability')
    if "savefile" in locals():
        plt.savefig(savefile)
    if ("start" in locals()):  # se declaro como entrada entonces
        if start:
            plt.show()
    else:
        if "conf" in locals() and hasattr(conf, "start") and conf.start:
            plt.show()
    # print(dir(plt))
    # plt.clf() # closed'''

### EN RECONSTRUCCION ###



class Graph:
    """ Configure of object general for Graphic """

    def __init__(self, X = None, Y = None, Z = None, **kwargs):
        # basic options
        self.plt = None
        #self.grid = True  # "Default, bool que describe is el grafico tendra la propiedad grid o no"
        self.percentil = 5  # Default, float, en el rango 0<x<100, corta la informacion correspondiente
        self.type = None
        #self.ylabel = " Frecuencia "
        self.bins = 30
        self.start = False
        # include todas las entradas respectivas
        for name, value in kwargs.items():
            self.__dict__[name] = value

        if Z is not None or Y is not None or X is not None:
            self.__input__(X, Y, Z)  # va a la respectiva funcion

    def __AddProp__(self, name, value=None):
        """
        :param name: declara el nombre la la nueva variable a incluir
        :param value: optional, declara el valor de la nueva variable a incluir
        :return: no tiene
        """
        self.__dict__[name] = value

    def __input__(self, X = None, Y = None, Z=None):
        if  X is None and Y is None and Z is None:
            print(" :: Ninguna entrada Valida, no graficos posibles :: ")
        else:
            if (X is None and Y is None) and Z is not None:
                inp=Z
                print(" :: Entrada unica, declaracion como eje Z :: ")
            elif X is None and Z is None and Y is not None:
                inp=Y
                print(" :: Entrada unica, declaracion como eje Y :: ")
            elif Z is None and Y is None and X is not None:
                inp=X
                print(" :: Entrada unica, declaracion como eje X :: ")
            elif Z is not None and Y is not None and X is not None:
                inp = "xyz"
                print(" :: Entrada de los 3 ejes ::")
            else:
                inp = None
                print(" :: Entrada de datos invalida ::")
            #print(inp)
            if inp is not None:
                if inp == "xyz":
                    print(" :: Entrada de todos los datos X, Y y Z para tratar::")
                else:
                    print(" :: Entrada unica, se procesaran los datos:: ")
                    if inp.shape[0]==1 or inp.shape[1]==1:
                        if inp.shape[0]==1:
                            inp = inp.T
                        print(" :: Datos con forma de vector ::")
                        # cortar datos si estan considerados en config.percentil
                        #print self.percentil
                        if hasattr(self, "percentil") and \
                                0 < self.percentil < 50:
                            # solo los datos en el rago especifico
                            log1 = np.percentile(inp, self.percentil) < inp
                            log2 = np.percentile(inp, 100 - self.percentil) > inp
                            log = log1*log2
                        else:
                            # todos los datos
                            log = True
                        #  Show Graph
                        #print log1
                        #print log1*1
                        #print np.max(np.delete(inp, log))
                        plt.hist( inp[log] )
                    else:
                        print(" :: Datos con mas de una dimension, multiples graficos a tratar ::")
                        plt.rcParams['figure.figsize'] = [10, 20]  # Grafico General
                        # PRIMERO - NUMERO DE LINEAS GRAFICO
                        for i in range(inp.shape[1]+1):
                            print("grafico" + str(i))
                            plt.subplot(str(inp.shape[1]+1) + "1"+ str(i+1))
                            if i==0:
                                inpnew = inp.reshape(1,inp.shape[0]*inp.shape[1])
                            else:
                                inpnew = inp[:,i-1]
                            if inpnew.shape[0]==1:
                                inpnew = inpnew.T
                            if hasattr(self, "percentil") and \
                                    0 < self.percentil < 50:
                                # solo los datos en el rago especifico
                                log1 = np.percentile(inpnew, self.percentil) < inpnew
                                log2 = np.percentile(inpnew, 100 - self.percentil) > inpnew
                                log = log1*log2
                            else:
                                # todos los datos
                                log = True
                            plt.hist( inpnew[log] )

                # guardar grafico
                self.plt = plt
                if self.start:
                    print(self.start)
                    self.showGraph()

        return self  # sacar el grafico para elegir que hacer con el
    def showGraph(self):
        self.start = True
        # Propiedades
        for name in dir(self):
            #print("===")
            #print(name)
            #print(name.find("_"))
            if name in dir(self.plt) and (name.find("__") != 0):
                print(self.plt.__dict__[name])
                self.plt.__dict__[name](self.__dict__[name])

        if self.plt != None:
            self.plt.show()
        else:
            print(" :: No se ha introducido datos correctos para graficar, use __input__::")
        self.start = False
        return 0




    ''''''
    '''if inp.shape[1] > 1:
        for i in range(inp.shape[1]):

    else:
        # si existe la propiedad percentil y esta esta entre 0 y 100

        if hasattr(config, "percentil") and config.percentil > 0 and config.percentil < 100:
            # solo los datos en el rago especifico
            log1 = np.percentile(inp[:, i], config.percentil) < inp[:, i]
            log2 = np.percentile(inp[:, i], 100 - config.percentil) > inp[:, i]
            log = log1 * log2
            hist0 = []
            for j in range(len(inp)):
                if log[j]:
                    hist0.append(inp[j])
        else:
            # todos los datos
            hist0 = inp[:, i]
            log = True
        if i == 0:
            hist = np.delete(hist0, log)
        else:
            print(hist.shape)
            print(hist0.shape)
            hist = np.concatenate((hist0, np.delete(hist0, log).T), axis=1)'''

    # print(hist)
    ## propiedades extras inclusivas
    '''if  hasattr(config, "bins") : 
        if hasattr(config, "xlim") :
            binss=int(round(config.bins*(max(hist)- min(hist))/(config.xlim[1]- config.xlim[0])))
            #print(binss)
            plt.hist(np.delete(hist, log), bins= binss)
            print(1)
        else:
            plt.hist(np.delete(hist, log), bins= config.bins)
            print(2)
    else:
        plt.hist(np.delete(hist, log), bins= 10)          
        print(3)

    ## PROP
    if    hasattr(config, "xlim"): plt.xlim(config.xlim[0],config.xlim[1] )
    else: plt.xlim( min(hist), max(hist) )
    if    hasattr(config, "ylim"): plt.ylim(config.ylim[0],config.ylim[1] )

    if    hasattr(config, "title") and len(config.title)>0: plt.title(config.title)

    if    hasattr(config, "grid"): plt.grid(config.grid)
    else: plt.grid(True)

    if    hasattr(config, "ylabel") and len(config.ylabel)>0 : plt.ylabel(config.ylabel)
    if    hasattr(config, "xlabel") and len(config.xlabel)>0 : plt.xlabel(config.xlabel)

    if    config.start: plt.show()
    else: print(" Auto plot is deactivate, change the bool .\"start\" ")
    # plt.clf() # closed
    return 1'''

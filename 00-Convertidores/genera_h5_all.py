from modules.darkSUSY.classDarkSUSY import *
from modules.general.F_search import *

from IPython.display import clear_output
import numpy as np
import h5py
import os

Delphes_DIR = "/home/franky8939/PROGRAMAS/MG5_aMC/Delphes/"  # Directory local of Delphes
ROOT_DIR = "/home/franky8939/PROGRAMAS/ROOT/"  # Directory local of Root
fbash(Delphes_DIR, ROOT_DIR)  # path in bash of Delphes and Root

# CLASS DARKSUSY
DarkFile = DarkSUSY()  # initialize the DarkSUSY class

# Create general h5 for all data
OUTPUT = '/home/franky8939/GITHUP/DarkSUSY-master/data/h5_muon_all/DarkSUSY_all_NMuon.h5'
FILES_INPUT = "/media/franky8939/10FE09E910FE09E9/datos_investigacion_grandes/"

# Si existe el archivo OUTPUT ACTUALIZARLO #
if os.path.exists(OUTPUT):
    hf = h5py.File(OUTPUT, 'a')
else:
    hf = h5py.File(OUTPUT, 'w')  # create h5py

for files_root in os.listdir(FILES_INPUT):
    if ".root" in files_root:  # THE FILE IS *.root
        for i in [1]:

            try:
                # Identificar la posicion en *.h5
                var = Ob_Value(files_root)
                name_local_group = "MNeuL_" + var["MNeuL"] + "/MNeuD_" + var["MNeuD"] + "/MPhoD_" + var["MPhoD"] + \
                                   "/TcPhoD_" + var["TcPhoD"] + "/" + var["Card"]

                if var["Card"] is "_HL2_":
                    break
                if np.array(hf.get(name_local_group + "/Verification")) == "ON":
                    print(" :: INFO OF FILE " + files_root + " EXIST, CONTINUE WITH THE NEXT")
                    # continue
                    break

                hf.require_group(name_local_group)  # requerirlo para que lo cree si no existe
                del hf[name_local_group]  # borrar siempre para actualizarlo
                local_group = hf.require_group(name_local_group)  # volverlo a crear
                # local_group.require_dataset(name="Name_of_FileROOT", data=files_root)  # Number of Mu for Event
                local_group.create_dataset(name="Name_of_FileROOT", data=files_root)  # Number of Mu for Event
                local_group.create_dataset(name="Verification", data="OFF")

                # Variables
                DarkFileTemp = DarkFile  # new
                DarkFileTemp.Add_File(FILES_INPUT + files_root)  # Add File
                NMu = DarkFileTemp.Mu_for_Event()
                local_group.create_dataset(name='Entries', data=DarkFileTemp.Entries,
                                           dtype=int)  # Number of Event
                local_group.create_dataset(name='Mu_Entries', data=NMu,
                                           dtype=int)  # Number of Mu for Event
                # print(" :: Finalizo correctamente :: ")
                del local_group["Verification"]  # borrar siempre para actualizarlo
                local_group.create_dataset(name="Verification", data="ON")
                # break
                # sys.exit()
            except:
                print(" :: FILE WITH PROBLEMS :: " + files_root)
                # sys.exit()

hf.close()

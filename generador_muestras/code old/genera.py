import os
import shutil
# import subprocess
import random
# import sys
import argparse


#  FUNCION PARA CAMBIAR UNA LINEA DE UN ARCHIVO POR OTRA #
def modificarLinea(archivo, buscar, reemplazar):
    with open(archivo, "r") as f:
        lines = (line.rstrip() for line in f)
        altered_lines = [reemplazar if line == buscar else line for line in lines]

    with open(archivo, "w") as f:
        f.write('\n'.join(altered_lines) + '\n')


# eventos = 10 # numero de eventos a generar
def main(eventos, MassPhoton, fileName, dirmad, modo):
    DirProg = os.getcwd()  # Conocer la direccion actual


    for num in MassPhoton:
        #num = MassPhoton[i]
        print("Masa del photon usada sera : " + str(num))
        #quit() # parada de la ejecucion
        # ====================== #
        # || COPY MG5 PROGRAM || #
        # ====================== #
        if modo:
            NumberOfProcess = str(random.randint(0, 10000))  # NAME OF PROCESS
            os.system("mkdir temp/Process_" + NumberOfProcess)  # CREAR CARPETA
            print(" :: Se crea la carpeta : temp/Process_" + NumberOfProcess + " ::")
            shutil.copytree(dirmad, "/temp/Process_" + NumberOfProcess + "/MG5_aMC")
            print(" :: Se copio mg5 correctamente en la carpeta : temp/Process_" + NumberOfProcess + " :: ")
            DirMadgraph = DirProg + "/temp/Process_" + NumberOfProcess + "/MG5_aMC"
        else:
            DirMadgraph = dirmad

        # ==================== #
        # || COPY MSSMD_UFO || #
        # ==================== #
        # Go to the folder MG5_aMC_vXXX/models. Copy the UFO model there in to folder MSSMD_UFO:
        if os.path.exists(DirMadgraph + "/models/MSSMD_UFO"):  # Verificar la existencia del archivo
            shutil.rmtree(DirMadgraph + "/models/MSSMD_UFO")  # Borrar el archivo con contenido
            print(" :: Se borro archivo MSSMD_UFO :: ")
        else:
            print(" :: No se encontro archivo MSSMD_UFO :: ")
        shutil.copytree(DirProg + "/source/MSSMD_UFO", DirMadgraph + "/models/MSSMD_UFO")  # Copiar la info
        print(" :: Se copio el archivo MSSMD_UFO :: ")
        # ====================== #
        # || Mass Dark Photon || #
        # ====================== #
        # Go to the folder MSSMD_UFO and execute .py:
        os.chdir(DirMadgraph + "/models/MSSMD_UFO")  # Posicionarse en el lugar
        os.system("python write_param_card.py")  # Execute el programa
        os.chdir(DirProg)  # Posicionarse en la posicion inicial
        # Change the mass of dark photon4
        modificarLinea(DirMadgraph + "/models/MSSMD_UFO/param_card.dat",
                       "  3000022 2.500000e-01 # MAD", "  3000022 " + str(num) + " # MAD ")

        # ======================== #
        # || COPY proc_card.dat || #
        # ======================== #
        # Remove the default proc_card.dat in the MG5_aMC_vXXX directory
        if os.path.exists(DirMadgraph + "/proc_card.dat"):
            os.remove(DirMadgraph + "/proc_card.dat")
            print(" :: proc_card.dat fue borrado :: ")
        else:
            print(" :: proc_card.dat no existe en el directorio :: ")

        # Copy the following proc_card.dat there:
        shutil.copy(DirProg + "/source/proc_card.dat", DirMadgraph)
        print(" :: Se copio correctamente el archivo proc_card.dat :: ")

        # =================== #
        # || Generar MSSMD || #
        # =================== #
        # Run ./bin/mg5_aMC proc_card.dat and generate the folder called MSSMD.
        # MADGRAPH5 PATH
        if modo:
            print(" :: Dir base : " + DirProg)
            os.environ["MADGRAPH5_N"] = DirMadgraph  # base
            os.environ["Delphes_N"] = os.environ["Delphes"] + os.environ["MADGRAPH5_N"] + "/Delphes"  # base
            os.environ["ExRoot_N"] = os.environ["Delphes"] + "/external" + ":" + \
                                     os.environ["Delphes"] + "/external/ExRootAnalysis" + ":" + \
                                     os.environ["Delphes"] + "/classes" + ":"
            os.environ["Pythia8_N"] = os.environ["MADGRAPH5_N"] + "/HEPTools/pythia8"
            os.environ["Heptools_N"] = os.environ["MADGRAPH5_N"] + "/HEPTools"
            os.environ["lhapdf6"] = os.environ["Heptools_N"] + "/lhapdf6"
            os.environ["PATH"] = os.environ["PATH"] + ":" + \
                                 os.environ["MADGRAPH5_N"] + "/bin" + ":" + \
                                 os.environ["ExRoot_N"] + ":" + \
                                 os.environ["ExRoot_N"] + "/bin" + ":" + \
                                 os.environ["Pythia8_N"] + "/bin" + ":" + \
                                 os.environ["lhapdf6"] + "/bin" + ":" + \
                                 os.environ["Heptools_N"] + "/bin" + ":"
            os.environ["LD_LIBRARY_PATH"] = os.environ["LD_LIBRARY_PATH"] + ":" + \
                                            os.environ["ExRoot_N"] + ":" + \
                                            os.environ["ExRoot_N"] + "/lib" + ":" + \
                                            os.environ["Pythia8_N"] + "/lib" + ":" + \
                                            os.environ["lhapdf6"] + "/lib" + ":" + \
                                            os.environ["Heptools_N"] + "/lib" + ":"
            os.environ["DYLD_LIBRARY_PATH"] = os.environ["DYLD_LIBRARY_PATH"] + ":" + \
                                              os.environ["ExRoot_N"] + ":"
            os.environ["ROOT_INCLUDE_PATH"] = os.environ["ROOT_INCLUDE_PATH"] + ":" + \
                                              os.environ["ExRoot_N"] + ":"
            os.environ["PYTHONPATH"] = os.environ["PYTHONPATH"] + ":" + \
                                              os.environ["ExRoot_N"] + ":"

        os.chdir(DirMadgraph)  # Posicionarse en el lugar
        os.system("./bin/mg5_aMC proc_card.dat")  # EXECUTE
        os.chdir(DirProg)
        print(" :: Generada la carpeta MSSMD :: ")

        # ================== #
        # || Copy madspin || #
        # ================== #
        # Copy the madspin card to the Cards directory /MadGraph5/MG5_aMC_vXXX/MSSMD/Cards
        shutil.copy(DirProg + "/source/madspin_card.dat", DirMadgraph + "/MSSMD/Cards")
        print(" :: Se copio el archivo madspin_card.dat ::")

        # ===================== #
        # || Change Run_card || #
        # ===================== #
        # Copiar el archivo Run_card en el lugar correspondiente
        shutil.copy(DirProg + "/source/run_card.dat", DirMadgraph + "/MSSMD/Cards")
        # realizar el cambio correspondiente en el archivo run_card
        modificarLinea(DirMadgraph + "/MSSMD/Cards/run_card.dat",
                       "  10000 = nevents ! Number of unweighted events requested",
                       "  " + str(
                           eventos) + "  = nevents ! Number of unweighted events requested ")  # cambiar el numero de eventos
        print(" :: Se cambio la Run_card :: ")

        # ======================= #
        # || Activar el Shower || #
        # ======================= #
        if os.path.exists(DirMadgraph + "/MSSMD/Cards/pythia8_card.dat"):
            os.remove(DirMadgraph + "/MSSMD/Cards/pythia8_card.dat")
            print(" :: pythia8_card.dat fue borrado para su sustitucion:: ")
        else:
            print(" :: pythia8_card.dat no existe en el directorio :: ")
        shutil.copy(DirMadgraph + "/MSSMD/Cards/pythia8_card_default.dat",
                    DirMadgraph + "/MSSMD/Cards/pythia8_card.dat")  # SE ACTIVA Pythia8
        print(" :: pythia8_card.dat a sido copiado correctamente en el directorio :: ")

        # ======================== #
        # || Activar el Delphes || #
        # ======================== #
        if os.path.exists(DirMadgraph + "/MSSMD/Cards/delphes_card.dat"):
            os.remove(DirMadgraph + "/MSSMD/Cards/delphes_card.dat")
            print(" :: delphes_card.dat fue borrado para su sustitucion:: ")
        else:
            print(" :: delphes_card.dat no existe en el directorio :: ")
        shutil.copy(DirMadgraph + "/MSSMD/Cards/delphes_card_CMS.dat",
                    DirMadgraph + "/MSSMD/Cards/delphes_card.dat")  # SE ACTIVA DELPHES
        print(" :: delphes_card.dat a sido copiado correctamente en el directorio :: ")

        # ================== #
        # || Genera datos || #
        # ================== #
        print(" :: Comienzo de la generacion de datos :: ")
        os.chdir(DirMadgraph + "/MSSMD")  # Posicionarse en el lugar
        os.system("./bin/generate_events ")

        # =================== #
        # || Guardar datos || #
        # =================== #
        print(" :: Guardando datos :: ")
        DirOutput = DirProg + "/output/DarkSUSY_MassPhoton_" + str(num) + \
                    "_Event_" + str(eventos) + "_Default"
        if os.path.exists(DirOutput):
            shutil.rmtree(DirOutput)
            print(" :: Se Borro la direccion : " + DirOutput)
        else:
            print(" :: No existe la direccion de guardado")

        #os.system("mkdir " + DirOutput)  # CREAR CARPETA
        shutil.copytree(DirMadgraph + "/MSSMD/Events/", DirOutput)  # Copiar la info
        print(" :: Salvados con exito, proxima corrida pues :: ")
        os.chdir(DirProg)  # posicion inicial de new

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-event", type=int, help="Number of Event", default=100)
    parser.add_argument("-mphoton", help="Mass of the Photon", default=None)
    parser.add_argument("-tcphoton", help="Mass of the Photon", default=None)
    parser.add_argument("-dirmad", type=str, help="Directory of Madgraph 5", default="source/MG5_aMC_v2_6_7")
    parser.add_argument("-filename", type=str, help="Name of Output File", default="darkSUSY")
    parser.add_argument("-modo", type=bool,
                        help=" 0 o False : Trabajar en el directorio de Madgraph; 1 o True Trabajar en directorio nuevo",
                        default=False)

    args = parser.parse_args()
    #print(args.modo)
    if args.event == 100:
        print(" :: Using default Event : 100")
    else:
        print(" :: Using Event : " + str(args.event))
    if args.mphoton == None:
        args.mphoton = [.25, .6, .7, .8, .9, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(" :: Using default Photon Mass Default")
    else:
        print(" :: Using Photon Mass : " + str(args.mphoton))
    if args.tcphoton == None:
        args.mphoton = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        print(" :: Using default Photon Tc Default")
    else:
        print(" :: Using Photon Tc : " + str(args.mphoton))

    if args.filename == "darkSUSY":
        print(" :: Using default File Name : darkSUSY")
    else:
        print(" :: Using File Name : " + args.filename)
    #print("masa" +  str(args.mphoton[1]))

    if os.path.exists(args.dirmad):
        print(" :: Using Directory of Madgraph 5 : " + args.dirmad)
        print(" :: Masa que se usara en todo el proceso : ", args.mphoton)
        main(args.event, args.mphoton, args.filename, args.dirmad, args.modo)
    else:
        print(" :: Directory of Madgraph 5 incorrect, using Default")

        if args.modo:
            print(" :: Modo 1 no es posible ya que directorio Madgraph incorrecto, using Default 0")
            args.modo = 0

        if os.path.exists(os.getcwd() + "/source/MG5_aMC_v2_6_7"):
            print(" :: Using default Directory of Madgraph 5 : in source/MG5_aMC_v2_6_7")
            main(args.event, args.mphoton, args.filename, os.getcwd() + "/source/MG5_aMC_v2_6_7", args.modo)
        else:
            print(" :: No Directory of Madgraph 5 is using, stop programs :: ")



import os
import shutil
import subprocess
import random


##  PROGRAMA A USAR  ##
#MG5_DIR = "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7"
#MG5_DIR = "/LUSTRE/home/fmsanchez/MG5_aMC_v2_6_6" # CLUSTER
##  GUARDAR RESULTADOS  ##
#MG5_DIR_out = "/home/franky8939/DatosDarkSUSY"
#MG5_DIR_out = "/LUSTRE/home/fmsanchez/DatosDarkSUSY" # CLUSTER
##  DONDE ESTA EL EJECUTABLE  ##
#MG5_DIR_prog = "/home/franky8939/PycharmProjects/GDarkSUSY"
MG5_DIR_prog = "/LUSTRE/home/fmsanchez/EXE" # CLUSTER


##  FUNCIONES  ##
#dirActual = os.getcwd()
def modificarLinea(archivo, buscar, reemplazar):
    with open(archivo, "r") as f:
        lines = (line.rstrip() for line in f)
        altered_lines = [reemplazar if line == buscar else line for line in lines]

    with open(archivo, "w") as f:
        f.write('\n'.join(altered_lines) + '\n')

eventos = 10 # numero de eventos a generar

for num in range(1,10):
    # ====================== #
    # || COPY MG5 PROGRAM || #
    # ====================== #
    NumberOfProcess =  str(random.randint(0, 10000))  # NAME OF PROCESS
    os.system("tar - xvf source/mg5_aMC.tar - C temp/Process_" + NumberOfProcess)  # DESCOMPRIMIR mg5

    # Go to the folder MG5_aMC_vXXX/models. Copy the UFO model there in to folder MSSMD_UFO:
    if os.path.exists(MG5_DIR + "/models/MSSMD_UFO"):  # Verificar la existencia del archivo
        shutil.rmtree(MG5_DIR + "/models/MSSMD_UFO")   # Borrar el archivo con contenido
        print("Se borro archivo MSSMD_UFO")
    shutil.copytree(MG5_DIR_prog + "/Recursos/MSSMD_UFO", MG5_DIR + "/models/MSSMD_UFO") # copiar la info


    # Go to the folder MSSMD_UFO and execute .py:
    os.chdir(MG5_DIR + "/models/MSSMD_UFO/") # posicionarse en el directorio
    os.system("python write_param_card.py") # Execute

    # Change the mass of dark photon4
    #num = 10
    modificarLinea("param_card.dat", "  3000022 2.500000e-01 # MAD", "  3000022 " + str(num) + " # MAD ")

    # Remove the default proc_card.dat in the MG5_aMC_vXXX directory
    if os.path.exists(MG5_DIR + "/proc_card.dat"):
        os.remove(MG5_DIR + "/proc_card.dat")
        print("proc_card.dat existe en el directorio" + MG5_DIR + " y fue borrado")
    else:
        print("proc_card.dat no existe en el directorio " + MG5_DIR)
    # Copy the following proc_card.dat there:

    shutil.copy(MG5_DIR_prog + "/Recursos/proc_card.dat" , MG5_DIR)
    print("Se copio correctamente el archivo proc_card.dat en la carpeta correspondiente")

    # Run ./bin/mg5_aMC proc_card.dat and generate the folder called MSSMD.
    os.chdir(MG5_DIR) # posicionarse en el directorio
    os.system("./bin/mg5_aMC proc_card.dat")

    # Copy the madspin card to the Cards directory /MadGraph5/MG5_aMC_vXXX/MSSMD/Cards
    shutil.copy(MG5_DIR_prog + "/Recursos/madspin_card.dat" , MG5_DIR + "/MSSMD/Cards")

    # Copiar el archivo Run_card en el lugar correspondiente
    shutil.copy(MG5_DIR_prog + "/Recursos/run_card.dat", MG5_DIR + "/MSSMD/Cards")
    # realizar el cambio correspondiente en el archivo run_card

    modificarLinea(MG5_DIR + "/MSSMD/Cards/run_card.dat", "  10000 = nevents ! Number of unweighted events requested",
                   "  " + str(eventos) + "  = nevents ! Number of unweighted events requested ")# cambiar el numero de eventos

    # Generar los datos
    os.chdir(MG5_DIR + "/MSSMD") # posicionarse en el directorio

    # Remove previous instance of RunWeb
    subprocess.call(['rm', 'RunWeb'])
    subprocess.call(['./bin/generate_events', '-f', '--laststep=delphes'])

    if not os.path.exists(MG5_DIR_prog + "/DatosGenerados"):
        os.system("mkdir " + MG5_DIR_prog + "/DatosGenerados")  # genera la carpeta de info

    if not os.path.exists(MG5_DIR_prog + "/DatosGenerados/DarkSUSY_MMu_" + str(num) + "_Event_" + str(eventos)):
        os.system("mkdir " + MG5_DIR_prog + "/DatosGenerados/DarkSUSY_MMu_" + str(num) + "_Event_" + str(eventos)) # genera la carpeta de resultados
    # copia la informacion a la carpeta respectiva
    shutil.move(MG5_DIR + "/MSSMD/Event/", MG5_DIR_prog + "/DatosGenerados/DarkSUSY_MMu_" + str(num) + "_Event_" + str(eventos))

    #os.mkdir(MG5_DIR_prog + "/DatosGenerados/)


#os.system("./bin/generate_events")
#subprocess.call("./bin/generate_events << 'detector=Delphes' ", shell=True)
#ret.communicate(inp=" 0 ")
#p = subprocess.Popen(returned_value, stdin=subprocess.PIPE, shell=True)

#os.system("./bin/generate_events")
#os.system("shower = Pythia8")
#os.system("detector = Delphes")
#os.system("madspin = ON")















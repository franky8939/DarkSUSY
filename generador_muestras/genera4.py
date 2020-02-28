from mod_configuration import *


 eventos = 10 # numero de eventos a generar
def main(eventos, MassPhoton, TcPhoton, fileName, dirmad, modo):
    DirProg = os.getcwd()  # Conocer la direccion actual

    # # COPY MG5 PROGRAM # #
    if modo:
        NumberOfProcess = str(random.randint(0, 10000))  # NAME OF PROCESS
        os.system("mkdir temp/Process_" + NumberOfProcess)  # CREAR CARPETA
        print(" :: Se crea la carpeta : temp/Process_" + NumberOfProcess + " ::")
        shutil.copytree(dirmad, "/temp/Process_" + NumberOfProcess + "/MG5_aMC")
        print(" :: Se copio mg5 correctamente en la carpeta : temp/Process_" + NumberOfProcess + " :: ")
        DirMadgraph = DirProg + "/temp/Process_" + NumberOfProcess + "/MG5_aMC"
    else:
        DirMadgraph = dirmad

    # #  BARRER MASA DE PHOTONS  # #
    for num in MassPhoton:
        # num = MassPhoton[i]
        print(" :: Masa del photon usada sera : " + str(num))

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

        # ====================== #
        # || Desactiva Shower || #
        # ====================== #
        if os.path.exists(DirMadgraph + "/MSSMD/Cards/pythia8_card.dat"):
            os.remove(DirMadgraph + "/MSSMD/Cards/pythia8_card.dat")
            print(" :: pythia8_card.dat fue borrado para su sustitucion:: ")
        else:
            print(" :: pythia8_card.dat no existe en el directorio :: ")
        # shutil.copy(DirMadgraph + "/MSSMD/Cards/pythia8_card_default.dat",
        #            DirMadgraph + "/MSSMD/Cards/pythia8_card.dat")  # SE ACTIVA Pythia8
        # print(" :: pythia8_card.dat a sido copiado correctamente en el directorio :: ")

        # ======================= #
        # || Desactiva Delphes || #
        # ======================= #
        if os.path.exists(DirMadgraph + "/MSSMD/Cards/delphes_card.dat"):
            os.remove(DirMadgraph + "/MSSMD/Cards/delphes_card.dat")
            print(" :: delphes_card.dat fue borrado para su sustitucion:: ")
        else:
            print(" :: delphes_card.dat no existe en el directorio :: ")
        # shutil.copy(DirMadgraph + "/MSSMD/Cards/delphes_card_CMS.dat",
        #            DirMadgraph + "/MSSMD/Cards/delphes_card.dat")  # SE ACTIVA DELPHES
        # print(" :: delphes_card.dat a sido copiado correctamente en el directorio :: ")

        # #  Guardar  *.lhe  # #
        print(" :: Guardando datos .lhe :: ")
        # /output/Events_### (si no existe crealo)
        if os.path.exists(DirProg + "/output/Events_" + str(eventos)):
            print(" :: Directorio : /output/Events_" + str(eventos) + " existe :: ")
        else:
            print(" :: Directorio : /output/Events_" + str(eventos) + " no existe :: ")
            os.system("mkdir " +
                      DirProg + "/output/Events_" + str(eventos))  # crea carpeta
            print(" :: Directorio : /output/Events_" + str(eventos) + " fue creado :: ")

        # /output/Events_$$$/Mphohon_$$$ (si no existe crealo)
        if os.path.exists(DirProg + "/output/Events_" + str(eventos) + "/Mphohon_" + str(num)):
            print(" :: Directorio : /output/Events_" + str(eventos) + "/Mphohon_" +
                  str(num) + " existe :: ")
            # shutil.rmtree(DirProg + "/output/Events_" + str(eventos) + "/Mphohon_" + str(num))  # borra
            # print(" :: Directorio : /output/Events_" + str(eventos) + "/Mphohon_" +
            #      str(num) + " fue borrado :: ")
        else:
            print(" :: Directorio : /output/Events_" + str(eventos) + "/Mphohon_" +
                  str(num) + " no existe :: ")
            os.system("mkdir " +
                      DirProg + "/output/Events_" + str(eventos) + "/Mphohon_" + str(num))  # crea carpeta Mphohon_###
            print(" :: Directorio : /output/Events_" + str(eventos) + "/Mphohon_" +
                  str(num) + " fue creado :: ")
        DirOutput = DirProg + "/output/Events_" + str(eventos) + "/Mphohon_" + str(num)  # carpeta de salida
        os.system("mkdir " + DirOutput + "/Roots_Mu_min4")  # carpeta de salida de los root con (3 Mu) <

        # /output/Events_$$$/Mphohon_$$$/default_lhe (si no existe crealo)
        if os.path.exists(DirOutput + "/default_lhe"):
            print(" :: Directorio : /output/Events_" + str(eventos) + "/Mphohon_" +
                  str(num) + "/default_lhe  existe :: ")
            # shutil.rmtree(DirOutput + "/default_lhe")  # borra
            # print(" :: Directorio : /output/Events_" + str(eventos) + "/Mphohon_" +
            #      str(num) + "/default_lhe  fue borrado :: ")
            # print("  ::: 111 :::")
        else:
            # print("  ::: 222 :::")
            print(" :: Directorio : /output/Events_" + str(eventos) + "/Mphohon_" +
                  str(num) + "/default_lhe  no existe :: ")
            os.system("mkdir " + DirOutput + "/default_lhe")  # crea carpeta /default_lhe_###
            print(" :: Directorio : /output/Events_" + str(eventos) + "/Mphohon_" +
                  str(num) + "/default_lhe  fue creado :: ")

        # # Genera datos si no existen claro # #
        if os.path.exists(DirOutput + "/default_lhe/run_01_decayed_1"):
            print(" :: Datos *.lhe existentes :: ")
        else:
            print(" :: Archivo *.lhe no encontrado, comienzo de la generacion de datos :: ")
            os.chdir(DirMadgraph + "/MSSMD")  # Posicionarse en el lugar
            os.system("./bin/generate_events <<< 0 <<< 0 ")  # genera solo el .lhe
            # copy *.lhe to /output/Events_$$$/Mphohon_$$$/default_lhe
            if os.path.exists(DirOutput + "/default_lhe"):
                shutil.rmtree(DirOutput + "/default_lhe")  # borrar directorio
            shutil.copytree(DirMadgraph + "/MSSMD/Events", DirOutput + "/default_lhe")  # Copiar la info
            print(" :: Resultados de la simulacion para la obtencion del *.lhe relocalizado y guardados :: ")
            # shutil.copy(DirMadgraph + "/MSSMD/Events/run_01_decayed_1/unweighted_events.lhe.gz",
            #           )  # guarda *.lhe

            # os.chdir(DirOutput + "/default_lhe")    # se posiciona en la carpeta
            # os.system("gzip -d unweighted_events.lhe.gz")  # descomprime

        # # Activa Shower # #
        shutil.copy(DirMadgraph + "/MSSMD/Cards/pythia8_card_default.dat",
                    DirMadgraph + "/MSSMD/Cards/pythia8_card.dat")  # SE ACTIVA Pythia8
        print(" :: pythia8_card.dat a sido copiado correctamente en el directorio :: ")

        # # Activa Delphes # #
        shutil.copy(DirProg + "/source/delphes_card_HL.dat",
                    DirMadgraph + "/MSSMD/Cards/delphes_card.dat")  # SE ACTIVA DELPHES
        print(" :: delphes_card.dat a sido copiado correctamente en el directorio :: ")


        if os.path.exists(DirOutput + "/default_lhe/run_01_decayed_1/unweighted_events.lhe.gz"):
            os.system("gzip -d " + DirOutput + "/default_lhe/run_01_decayed_1/unweighted_events.lhe.gz")  # descomprime
            print(" :: descomprimir unweighted_events.lhe.gz en la posicion de guardado :: ")
        # quit()
        # # Ciclos de cambio de tiempo de vida, generacion de los archivos root
        for tc in TcPhoton:
            if not os.path.exists(DirOutput +
                                  "ROOT_Event_" + str(eventos) + "_Ma_" + str(num) + "_Tc_" + str(tc) + ".root"):

                # #  Preparando Madgraph de previos calculos # #
                shutil.rmtree(DirMadgraph + "/MSSMD/Events")  # borrar resultados
                print(" :: borrar resultados de directorio : ", DirMadgraph + "/MSSMD/Events")

                # os.system("mkdir " + DirMadgraph + "/MSSMD/Events/")  # crea carpeta
                # print(" :: Crea carpeta : " + DirMadgraph + "/MSSMD/Events/")

                shutil.copytree(DirOutput + "/default_lhe/", DirMadgraph + "/MSSMD/Events")  # copia archivo
                print(" :: Se crea el directorio Event y se copia la informacion ahi :: ")

                # os.chdir(DirMadgraph + "/MSSMD/Events/run_01_decayed_1")  # se posiciona en la carpeta
                # os.chdir(DirOutput + "/default_lhe/run_01_decayed_1")  # se posiciona en la carpeta

                lifetime(tc,  input=DirOutput + "/default_lhe/run_01_decayed_1/unweighted_events.lhe",
                         output=DirMadgraph + "/MSSMD/Events/run_01_decayed_1/unweighted_events.lhe")  # cambia life time
                print(" :: Se cambio el life time por : " + str(tc))
                #quit()
                os.system("gzip -1 " + DirMadgraph + "/MSSMD/Events/run_01_decayed_1/unweighted_events.lhe")  # comprime
                print(" :: Se comprimio unweighted_events.lhe.gz en la carpeta Eventos de Madgraph :: ")

                os.chdir(DirMadgraph + "/MSSMD")  # Posicionarse en el lugar
                os.system("./bin/madevent pythia8 run_01_decayed_1 <<< 0")  # genera solo el .lhe
                print(" :: Se genera el archivo *.lhe :: ")

                # #  Encuentra archivo *.root creado  # #
                outROOT = []
                for i in os.listdir(DirMadgraph + "/MSSMD/Events/run_01_decayed_1/"):
                    if i.find(".root") != -1:
                        outROOT = i

                NameOutput = "darkHLSUSY_Event_" + str(eventos) + "_Ma_" + str(num) + "_Tc_" + str(tc)
                if os.path.exists(DirMadgraph + "/MSSMD/Events/run_01_decayed_1/" + outROOT):
                    os.rename(DirMadgraph + "/MSSMD/Events/run_01_decayed_1/" + outROOT,
                              DirMadgraph + "/MSSMD/Events/run_01_decayed_1/" + NameOutput + ".root")  # rename

                shutil.copy(DirMadgraph + "/MSSMD/Events/run_01_decayed_1/" + NameOutput + ".root",
                            DirOutput)
                print(" :: Se copia el archivo root a su localidad de guardado :: ")

                # Convertir el root y seleccionar solo los eventos con 4 muones o mas
                os.chdir(DirProg)  # se posiciona en el lugar
                command = 'root -l SelectDark3.C\'("' + \
                          DirOutput + '/' + NameOutput + '.root" , "' + \
                          DirOutput + '/Roots_Mu_min4/Mu4_' + NameOutput + '.root" , "' + \
                          DirOutput + '/Roots_Mu_min4/LOG_Mu4_' + NameOutput + '.txt")\' <<< 0'
                print(" :: Se ejecutara el comando en la terminal : " + command)
                os.system(command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-event", type=int, help="Number of Event", default=100)
    parser.add_argument("-mDNeu", help="Mass of the Dark Neutralino", default=1)
    parser.add_argument("-mLNeu", help="Mass of the Lightest Neutalino", default=10)
    parser.add_argument("-mphoton", help="Mass of the Photon", default=None)
    parser.add_argument("-tcphoton", help="Mass of the Photon", default=None)
    parser.add_argument("-dirmad", type=str, help="Directory of Madgraph 5", default="source/MG5_aMC_v2_6_7")
    parser.add_argument("-modo", type=bool,
                        help=" 0 o False : Trabajar en el directorio de Madgraph; 1 o True Trabajar en directorio nuevo",
                        default=False)
    parser.add_argument("-Card", type=str, help="Card of Delphes using in the simulation ", default="CMS")

    args = parser.parse_args()
    # print(args.modo)
    if args.event == 100:
        print(" :: Using default Event : 100")
    else:
        print(" :: Using Event : " + str(args.event))
    if args.mphoton == None:
        args.mphoton = [.25, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(" :: Using default Photon Mass Default")
    if args.tcphoton == None:
        args.tcphoton = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        print(" :: Using default Photon Tc Default")

    if os.path.exists(args.dirmad):
        print(" :: Using Directory of Madgraph 5 : " + args.dirmad)
        #main(args.event, args.mphoton, args.tcphoton, args.filename, args.dirmad, args.modo)
    else:
        print(" :: Directory of Madgraph 5 incorrect, using Default")
        quit()
    print args.tcphoton

# %%
# ============================== || BEGIN : DIR || ============================== ##
import re
from codex.classDarkSUSY import *
# from codex.histograms import *
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm


Delphes_DIR = "/home/franky8939/PROGRAMAS/MG5_aMC_v2_6_7/Delphes/"
ROOT_DIR = "/home/franky8939/PROGRAMAS/root-6.18.02/"
ROOT = fbash(Delphes_DIR, ROOT_DIR)  # path in bash

'''
""" Characterize the data """
MPho = [.25, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # masa de los photons
TcPho = [0.0000001, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000]  # valores de Tc
Event = 10000  # event
# code find data in name
""" Identifier the file and the protocols """
ROOTs = []
for i in os.listdir("datosnew/"):
    # print i
    if (i.find(".root") != -1) and (i.find("Mu4_darkSUSY_") != -1):
        print i
        ROOTs.append([i, re.search(V_event, i).group(0), re.search(V_mass, i).group(0), re.search(V_tc, i).group(0)])
        # print(i) #ROOTs = i
        #print(str(re.search(V_event, i).group()))
        #print(str(re.search(V_mass, i).group()))
        #print(str(re.search(V_tc, i).group()))
        #print("ot" in ".root")
print(ROOTs)
'''
# %%
MPho = [.25, 1, 2, 3, 4, 5]  #, 6, 7, 8, 9]  # masa de los photons
TcPho = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # valores de Tc

X, Y = np.meshgrid(MPho, TcPho, sparse=False, indexing='ij')  # MATRIX COMBINADA
Z = np.zeros(X.shape)
print X
print Y
V_event = r"(?<=(_Event_))([\d\.]+)"
V_mass = r"(?<=(_Ma_))([\d|\.]+)"
V_tc = r"(?<=(_Tc_))([\d|\.]+)"
# CLASE DARKSUSY
DarkFile = DarkSUSY()  # inicializar la clase
# Grafico 3d
# BUSCANDO ARCHIVO
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        # localizar el archivo respectivo
        finalfileROOT = None
        for fileROOT in os.listdir("data/"):
            #print X[i, j], Y[i, j], fileROOT
            if (fileROOT.find(".root") != -1) and (fileROOT.find("Mu4_darkSUSY_") != -1):  # verificar que seas
                Mass0 = X[i, j]
                Mass1 = re.search(V_mass, fileROOT).group(0)
                Tc0 = Y[i, j]
                Tc1 = re.search(V_tc, fileROOT).group(0)
                Event0 = 10000
                Event1 = re.search(V_event, fileROOT).group(0)
                if float(Event0) == float(Event1) and float(Mass0) == float(Mass1) and float(Tc0) == float(Tc1):
                    finalfileROOT = fileROOT
                    print("El archivo fue encontrado: " + fileROOT)
                    DarkFile.Add_File("data/" + fileROOT)
                    #DarkFile.Select_two_dimuon()
                    Z[i, j] = DarkFile.Entries
                    break
                #else:
                #    print("Archivo root correspondiente no encontrado")
        if finalfileROOT == None:
            print X[i, j], Y[i, j], " File correspondiente no fue encontrado"
            quit()
        #print i, j
        #print j

print Z
# %%
#plt.rcParams['figure.figsize'] = [20, 5]
fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.plot_surface(X, Y, Z, cmap='copper',
#                       linewidth=0, antialiased=False)
#ax.plot_trisurf(X, Y, Z, linewidth=0.2, antialiased=True)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_wireframe(X, Y, Z)
#ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
#ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
#ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
#ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
ax.view_init(45, 135)
ax.bar3d(X.ravel(), Y.ravel(), 0, .5, .5,  Z.ravel(), zsort='average')
plt.title(' Analisis de frecuencias 3D ')
plt.show()
# %%
ax




import numpy as np
import pylab as pl # SE TARDA
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

# graficar
def Graf(X, Y, Z, xy = None, xyz = None, xlabel=None , ylabel=None, zlabel=None, fig=None):

    #plt.rcParams['figure.figsize'] = [20, 12]
    if fig is None:
        fig = pl.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(X, Y, Z,  cmap='bone')
    if xlabel is not None :
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if zlabel is not None:
        ax.set_zlabel(zlabel)

    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.colors.coolwarm, linewidth=0, antialiased=False)
    ax.set_zlim(0, np.max(Z))

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    if xy and xyz is not None:
        ax.view_init(xy, xyz)
        #print("rota")

    fig.colorbar(surf, shrink=0.55, aspect=5)
    plt.show()

##########################
# Muon tracking efficiency
##########################
fig = pl.figure(1)

pt_v = np.linspace(0, 5000,100)
eta_v = np.linspace(0, 3.14, 100)
pt_mesh, eta_mesh = np.meshgrid(pt_v, eta_v)
Mu_track = (pt_mesh <= 0.1) * 0.00 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 0.1) * (pt_mesh <= 1.0) * 0.75 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 1.0) * (pt_mesh <= 1.0e3) * 0.99 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 1.0e3) * (0.99*np.exp(0.5 - pt_mesh*5.0e-4)) + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 0.1) * (pt_mesh <= 1.0) * 0.70 + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 1.0) * (pt_mesh <= 1.0e3) * 0.98 + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 1.0e3) * (0.98*np.exp(0.5 - pt_mesh*5.0e-4)) + \
           (abs(eta_mesh) > 2.5) * 0.00
#print(Mu_track)
# pl.figure()
pl.subplot(131)
Graf(eta_mesh, pt_mesh, Mu_track, xy=20, xyz=45,
     xlabel= "Eta Angle", ylabel="Transversal moment", zlabel="Muon tracking efficiency", fig=fig)

pl.subplot(132)
Graf(eta_mesh, pt_mesh, Mu_track, xy=20, xyz=135,
     xlabel= "Eta Angle", ylabel="Transversal moment", zlabel="Muon tracking efficiency")

# DIAGRAMA 1
pt_v = np.linspace(0, 5, 100)
eta_v = np.linspace(0, 3.14, 100)
pt_mesh, eta_mesh = np.meshgrid(pt_v, eta_v)
Mu_track = (pt_mesh <= 0.1) * 0.00 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 0.1) * (pt_mesh <= 1.0) * 0.75 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 1.0) * (pt_mesh <= 1.0e3) * 0.99 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 1.0e3) * (0.99*np.exp(0.5 - pt_mesh*5.0e-4)) + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 0.1) * (pt_mesh <= 1.0) * 0.70 + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 1.0) * (pt_mesh <= 1.0e3) * 0.98 + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 1.0e3) * (0.98*np.exp(0.5 - pt_mesh*5.0e-4)) + \
           (abs(eta_mesh) > 2.5) * 0.00

fig = pl.figure()
ax=pl.imshow(Mu_track,
             cmap='copper',
             extent=[np.min(pt_v), np.max(pt_v), np.max(eta_v), np.min(eta_v)],
             aspect='auto')
pl.ylabel('Eta Angle')
pl.xlabel("Transversal moment")
pl.title("Muon tracking efficiency", fontsize=15)
pl.colorbar(shrink=0.95)
pl.text(.35, .75, '0.75', color="blue", fontsize=15)
pl.text(2.5, .75, '0.99', color="blue", fontsize=15)
pl.text(.35, 2, '0.70', color="blue", fontsize=15)
pl.text(2.5, 2, '0.98', color="blue", fontsize=15)
pl.text(2.5, 2.8, '0', color="gray", fontsize=15)
pl.show()

# DIAGRAMA 2
pt_v = np.linspace(0, 5000, 100)
eta_v = np.linspace(0, 3.14, 100)
pt_mesh, eta_mesh = np.meshgrid(pt_v, eta_v)
Mu_track = (pt_mesh <= 0.1) * 0.00 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 0.1) * (pt_mesh <= 1.0) * 0.75 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 1.0) * (pt_mesh <= 1.0e3) * 0.99 + \
           (abs(eta_mesh) <= 1.5) * (pt_mesh > 1.0e3) * (0.99*np.exp(0.5 - pt_mesh*5.0e-4)) + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 0.1) * (pt_mesh <= 1.0) * 0.70 + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 1.0) * (pt_mesh <= 1.0e3) * 0.98 + \
           (abs(eta_mesh) > 1.5) * (abs(eta_mesh) <= 2.5) * (pt_mesh > 1.0e3) * (0.98*np.exp(0.5 - pt_mesh*5.0e-4)) + \
           (abs(eta_mesh) > 2.5) * 0.00

fig = pl.figure()
ax=pl.imshow(Mu_track,
             cmap='copper',
             extent=[np.min(pt_v), np.max(pt_v), np.max(eta_v), np.min(eta_v)],
             aspect='auto')
pl.ylabel('Eta Angle')
pl.xlabel("Transversal moment")
pl.title("Muon tracking efficiency", fontsize=15)
pl.colorbar(shrink=0.95)
pl.text(400, .75, '0.99', color="blue", fontsize=15)
pl.text(400, 2, '0.98', color="blue", fontsize=15)
pl.text(1700, .75, r'$0.99*e^{[0.5 - \dfrac{5~P_t}{10^4}]}$', color="blue", fontsize=15)
pl.text(1700, 2, r'$0.98*e^{[0.5 - \dfrac{5~P_t}{10^4}]}$', color="blue", fontsize=15)
pl.text(2400, 2.8, '0', color="gray", fontsize=15)
pl.show()


###############################
# Momentum resolution for muons
###############################
pt_v = np.linspace(0.1, 1000,100)
eta_v = np.linspace(0, 3.14,100)
pt_mesh, eta_mesh = np.meshgrid(pt_v, eta_v)
Mu_resl = (abs(eta_mesh) <= 0.5)*(pt_mesh > 0.1)*np.sqrt(0.01**2 + pt_mesh**2*1.0e-4**2) + \
          (abs(eta_mesh) > 0.5)*(abs(eta_mesh) <= 1.5)*(pt_mesh > 0.1)*np.sqrt(0.015**2 + pt_mesh**2*1.5e-4**2) + \
          (abs(eta_mesh) > 1.5)*(abs(eta_mesh) <= 2.5)*(pt_mesh > 0.1)*np.sqrt(0.025**2 + pt_mesh**2*3.5e-4**2)

#print(Mu_resl)

Graf(eta_mesh, pt_mesh, Mu_resl, xy=20, xyz=-120,
     xlabel= "Eta Angle", ylabel="Transversal moment", zlabel="Momentum resolution for muons")
Graf(eta_mesh, pt_mesh, Mu_resl, xy=20, xyz=-45,
     xlabel= "Eta Angle", ylabel="Transversal moment", zlabel="Momentum resolution for muons")

# DIAGRAMA 1
fig = pl.figure()
#pl.contourf(eta_mesh,pt_mesh,Mu_resl,100, alpha=.75, cmap='pink')
ax=pl.imshow(Mu_resl,
             cmap='copper',
             extent=[np.min(pt_v), np.max(pt_v), np.max(eta_v), np.min(eta_v)],
             aspect='auto')
pl.ylabel('Eta Angle')
pl.xlabel("Transversal moment")
pl.title("Momentum resolution for muons", fontsize=15)
pl.colorbar(shrink=0.95)
pl.text(300, .27, r'$\sqrt{0.010^2 +10^{-10} ~ P_t^2}$', color="blue", fontsize=15)
pl.text(300, 1.2, r'$\sqrt{0.015^2 + 15^{-10} ~ P_t^2}$', color="blue", fontsize=15)
pl.text(300, 2.2, r'$\sqrt{0.025^2 + 25^{-10} ~ P_t^2}$', color="blue", fontsize=15)
pl.text(500, 2.9, '0', color="gray", fontsize=15)
pl.show()



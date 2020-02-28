#!/usr/bin/env python
# %%
# ============================ || BEGIN : MODULES || ============================ #
''' Modules using '''
import matplotlib.pyplot as plt
import numpy as np
# ============================ || END   : MODULES || ============================ ##

def hist1D(*argv,
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
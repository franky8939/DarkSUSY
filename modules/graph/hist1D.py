#!/usr/bin/env python
# %%
# ============================ || BEGIN : MODULES || ============================ #
''' Modules using '''
import matplotlib.pyplot as plt
import numpy as np


# ============================ || BEGIN : FUNCTION || ============================ ##
def hist1D(*args,
           **kwargs
           ):
    percentil = 0
    bins = 100
    alpha = 0.5
    for name, value in kwargs.items():  # se busca valor
        # donde salvar archivo
        if name is "savefile":
            savefile = value
        if name is "bins":
            bins = value
        if name is "alpha":
            alpha = value
        if name is "percentil":
            percentil = value

    # Graficar
    data_input = {}  # np.array([])  # dict(type=np.array)
    data_cut = {}  # np.array([])  # dict(type=np.array)
    count = 0
    dmax = np.array([])
    dmin = np.array([])
    for vector in args:
        # print vector
        count += 1
        data_input[count] = vector
        # if percentil > 0:
        data_cut[count] = vector[(vector >= np.percentile(vector, percentil)) *
                                 (vector <= np.percentile(vector, 100 - percentil))]
        # else:
        #    data_cut[count] = vector[True]
        # print data_cut[count]
        dmax = np.hstack((dmax, [np.max(data_cut[count])]))
        dmin = np.hstack((dmin, [np.min(data_cut[count])]))

    dmax = max(dmax)
    dmin = min(dmin)
    # obtener centroides
    # print dmin, dmax, (dmax-dmin)/bins
    interval = np.arange(dmin, dmax + (dmax - dmin) / bins, (dmax - dmin) / bins)
    centro_interval = interval[:-1] + (dmax - dmin) / bins / 2

    # Obtener frecuencias
    for var in data_cut:
        # print "-----"
        # print data_cut[var]
        centro_frecuencia = np.zeros(len(centro_interval))
        for i in range(len(centro_frecuencia)):
            centro_frecuencia[i] = np.sum((data_cut[var] >= interval[i]) *
                                          (data_cut[var] <= interval[i + 1]))
        normaliza = sum(centro_frecuencia) * (dmax - dmin)

        # Graficar correspondientemente
        plt.bar(centro_interval, centro_frecuencia / normaliza,
                align='center',
                width=(dmax - dmin) / bins,
                alpha=alpha)

    for name, value in kwargs.items():
        if name in dir(plt):  # comparar con la clase plt
            try:
                plt.__dict__[name](value)
            except:
                print(" :: ERROR IN kwargs:: " + name)

    return plt


# dataX = np.random.rand(1, 10)

# data, data2 = hist1D(np.random.rand(1, 409), np.random.rand(1, 400)+.3)

'''            type="bar",
           bins=20,
           alpha=0.5,
           start=False,
           sizeBarra=.9,
           normed=1,
           fig=None,
           legend=None,
           savefile=None
           
    hist, bn = np.histogram(args, bins=bins)
    width = sizeBarra * (bn[1] - bn[0])  # tama;o de la barra
    center = (bn[:-1] + bn[1:]) / 2

    if type is "bar":
        plt.bar(center, hist / (np.sum(hist) * (bn[1] - bn[0])), align='center', width=width)  # graphic
    elif type is "Pbar":
        plt.plot(center, hist / (np.sum(hist) * (bn[1] - bn[0])))  # **si esta en la declaracion inicial

    # propiedades en 'conf'
    for name, value in kwargs.items():
        if name in dir(plt):  # comparar con la clase plt
            try:
                plt.__dict__[name](value)
            except:
                print(" :: ERROR IN kwargs:: " + name)'''

'''    if "legend" in locals():
        plt.legend(legend)
    # plt.xlabel('Smarts')
    # plt.ylabel('Probability')
    if "savefile" in locals():
        plt.savefig(savefile)
    # print start
    if kwargs["start"] in locals():  # se declaro como entrada entonces
        if start:
            plt.show()
    else:
        if "conf" in locals() and hasattr(args, "start") and conf.start:
            plt.show()'''

#!/usr/bin/env python
# %%
# ============================ || BEGIN : MODULES || ============================ #
''' Modules using '''
import re
import os


def isname(inp, *argv):
    """
    Buscar un archivo, return bool
    """
    out = []
    for name in argv:
        log = inp in name
        out.append(log)
    return out


def Ob_Value(inp, *argv):
    out = {}  # initializer dictionary
    if len(argv) == 0:
        V_Event = r"(?<=(_Event_))([\d\.]+)"
        Event = None
        try:
            Event = re.search(V_Event, inp).group()
        except ValueError:
            # handle ValueError exception
            pass

        V_MNeuL = r"(?<=(_MNeuL_))([\d\.]+)"
        MNeuL = None
        try:
            MNeuL = re.search(V_MNeuL, inp).group()
        except ValueError:
            # handle ValueError exception
            pass

        V_MNeuD = r"(?<=(_MNeuD_))([\d\.]+)"
        MNeuD = None
        try:
            MNeuD = re.search(V_MNeuD, inp).group()
        except ValueError:
            # handle ValueError exception
            pass

        V_MPhoD = r"(?<=(_MPhoD_))([\d\.]+)"
        MPhoD = None
        try:
            MPhoD = re.search(V_MPhoD, inp).group()
        except ValueError:
            # handle ValueError exception
            pass

        V_TcPhoD = r"(?<=(_TcPhoD_))([\d\.]+)"
        TcPhoD = None
        try:
            TcPhoD = re.search(V_TcPhoD, inp).group()
        except ValueError:
            # handle ValueError exception
            pass

        if "_CMS_" in inp:
            Card = "_CMS_"
        elif "_HL_" in inp:
            Card = "_HL_"
        elif "_HL2_" in inp:
            Card = "_HL2_"
        else:
            Card = None

        if "log" in inp.lower():
            includeLOG = True
        else:
            includeLOG = False

        if ".root" in inp.lower():
            includeROOT = True
        else:
            includeROOT = False


        # Include in out
        out["Event"] = Event
        out["Card"] = Card
        out["MNeuL"] = MNeuL
        out["MNeuD"] = MNeuD
        out["MPhoD"] = MPhoD
        out["TcPhoD"] = TcPhoD
        out["includeLOG"] = includeLOG
        out["includeROOT"] = includeROOT
    else:
        for name in argv:
            try:
                out[name] = re.search(name, inp).group()
            except:
                out[name] = None
        # out[""] = re.search(V_mass, fileROOT).group(0)
    # else:
    return out


def FindROOT(Event=None, Card=None, MNeuL=None, MNeuD=None, MPhoD=None, TcPhoD=None, include=None, directory=None):
    # localizar el archivo respectivo
    outfileROOT = None
    if directory is None:
        directory = os.getcwd()  # direction
    outfileROOT = []
    for file in os.listdir(directory):
        # print Event0, Mass0, Tc0, fileROOT
        var = Ob_Value(file)
        log = True
        # print var
        if Event is not None and not float(Event) == float(var["Event"]):
            continue
        if Card is not None and not Card == var["Card"]:
            continue
        if MNeuL is not None and not float(var["MNeuL"]) == float(MNeuL):
            continue
        if MNeuD is not None and not float(var["MNeuD"]) == float(MNeuD):
            continue
        if MPhoD is not None and not float(var["MPhoD"]) == float(MPhoD):
            continue
        if TcPhoD is not None and not float(var["TcPhoD"]) == float(TcPhoD):
            continue
        for text in include:
            #print text, file
            if text not in file:
                log = False
        if log:
            outfileROOT.append(file)
        # else:
        #    print("Archivo root correspondiente no encontrado")
    if outfileROOT is None:
        pass
        #print(Event + " " + MNeuL + " " + MNeuD + " " + MPhoD + " " + TcPhoD +
        #      " :: File correspondiente no fue encontrado ::")
    else:
        #print(" :: File localizado correctamente :: ")
        for fill in outfileROOT:
            pass
            #print(" :: archivo :: " + fill)
        # outfileROOT = None
    return outfileROOT

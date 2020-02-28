#!/usr/bin/env python
# %%
# ============================ || BEGIN : MODULES || ============================ #
''' Modules using '''
import re


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
        V_event = r"(?<=(_Event_))([\d\.]+)"
        Events = None
        try:
            Events = re.search(V_event, inp).group()
        except ValueError:
            # handle ValueError exception
            pass
        V_mass = r"(?<=(_Ma_))([\d|\.]+)"
        MPhoton = None
        try:
            MPhoton = re.search(V_mass, inp).group()
        except ValueError:
            # handle ValueError exception
            pass
        V_tc = r"(?<=(_Tc_))([\d|\.]+)"
        TcPhoton = None
        try:
            TcPhoton = re.search(V_tc, inp).group()
        except ValueError:
            # handle ValueError exception
            pass
        # Include in out
        out["Events"] = Events
        out["MPhoton"] = MPhoton
        out["TcPhoton"] = TcPhoton
    else:
        for name in argv:
            try:
                out[name] = re.search(name, inp).group()
            except:
                out[name] = None
        # out[""] = re.search(V_mass, fileROOT).group(0)
    # else:
    return out


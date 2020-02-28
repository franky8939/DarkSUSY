import os
import shutil
import random
import argparse
import random

#  FUNCION PARA CAMBIAR UNA LINEA DE UN ARCHIVO POR OTRA #
def modificarLinea(archivo, buscar, reemplazar):
    with open(archivo, "r") as f:
        lines = (line.rstrip() for line in f)
        altered_lines = [reemplazar if line == buscar else line for line in lines]

    with open(archivo, "w") as f:
        f.write('\n'.join(altered_lines) + '\n')


def lifetime(ctau_mean_mm, input="unweighted_events.lhe", output="unweighted_events_new.lhe"):
    '''
    function using in replace_lifetime_in_LHE.py
    necesita estar en la carpeta para que funcione
    '''
    # set input file name
    # filename = "unweighted_events.lhe"
    f = open(input, 'r')
    g = open(output, 'w')
    event_begin = False
    event_end = True
    for line in f:
        if line == '<event>\n':
            event_begin = True
            event_end = False
        if line == '</event>\n':
            event_begin = False
            event_end = True
        new_line = ''
        if event_begin == True and event_end == False:
            word_n = 0
            for word in line.split():
                if word == '3000022' or word_n > 0:
                    word_n = word_n + 1
                    if word_n < 13:
                        if word_n == 12:
                            if ctau_mean_mm is not 0:
                                ctau_mm = '%E' % random.expovariate(
                                    1.0 / float(ctau_mean_mm))  # exponential distribution
                                # print "ctau (mm) mean: ", ctau_mean_mm, " actual: ", ctau_mm
                            else:
                                ctau_mm = '%E' % float(0)
                            new_line = new_line + ctau_mm + '   '
                        else:
                            new_line = new_line + word + '   '
                    else:
                        new_line = new_line + word + '\n'
                        word_n = 0
        if new_line == '':
            g.write(line.rstrip('\n') + "\n")
            #print line.rstrip('\n')
        else:
            g.write(new_line.rstrip('\n') + "\n")
            #print new_line.rstrip('\n')
    f.close()
    g.close()

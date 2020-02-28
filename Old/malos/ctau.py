# %%

import random
import argparse

def lifetime(ctau_mean_mm, inp="unweighted_events.lhe", output="unweighted_events0.lhe"):
    '''
    function using in replace_lifetime_in_LHE.py
    necesita estar en la carpeta para que funcione
    '''
    # set inp file name
    # filename = "unweighted_events.lhe"
    f = open(inp, 'r')
    g = open(output, 'w')
    event_begin = False
    event_end = True
    print("entro")
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
                                    1.0 / ctau_mean_mm)  # exponential distribution
                                # print "ctau (mm) mean: ", ctau_mean_mm, " actual: ", ctau_mm
                            else:
                                ctau_mm = '%E' % 0  # exponential distribution
                                # print "ctau (mm) mean: ", ctau_mean_mm, " actual: ", ctau_mm
                            new_line = new_line + ctau_mm + '   '
                        else:
                            new_line = new_line + word + '   '
                    else:
                        new_line = new_line + word + '\n'
                        word_n = 0
        if new_line == '':
            g.write(line.rstrip('\n'))
            print(line.rstrip('\n'))
        else:
            g.write(new_line.rstrip('\n'))
            print(new_line.rstrip('\n'))

    f.close()
    g.close()

# correr el programa
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ctau", type=float, help=" Tiempo de Vida ", default=10)
    parser.add_argument("-file", help=" Input file ", default="unweighted_events.lhe")

    args = parser.parse_args()

    lifetime(args.ctau, args.file)
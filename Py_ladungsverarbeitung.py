import pandas as pd
import numpy as np
import argparse
from pandas import DataFrame as df

def ladungsv(ACF_datei,ausgabe_datei='ladungs.out'):
    with open(ACF_datei, 'r+') as istream:
        la = 689 # la: letztes Atom
        atome_info = []
        for iline,line in enumerate(istream.readlines()):
            atome_info.append(line.strip().split())
        atome_info    = atome_info[2:la+2]
        atome_info_df = df(atome_info, columns=['Na', 'X', 'Y', 'Z',
                                                'Ladung', 'MinAbs', 'AtVol'])
        print (atome_info_df)


    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument("-i", '--input', help='Sys_YAML Datei')
    parser.add_argument("-i", '--input', help='Eingabe Datei')
    parser.add_argument("-o", '--output', help='Ausgabe Datei')
    args = parser.parse_args()
    if args.input:
        ladungsv(args.input)
    elif args.input and args.output:
        ladungsv(args.input,args.output)
    else:
        pass

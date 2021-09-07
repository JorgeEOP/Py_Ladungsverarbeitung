import pandas as pd
import numpy as np
import argparse
from pandas import DataFrame as df

def ladungsv(ACF_datei,ausgabe_datei='ladungs.out'):
    with open(ACF_datei, 'r+') as istream:
        la = 689 # la: letztes Atom
        atome_info = []
        mols_dic   = {'mol_0':[1,144], 'mol_1':[145,257], 'mol_2':[258,la]}
        ladungen   = []
        voll_lad   = 0

        for iline,line in enumerate(istream.readlines()):
            atome_info.append(line.strip().split())
        atome_info    = atome_info[2:la+2]
        atome_info_df = df(atome_info, columns=['Na', 'X', 'Y', 'Z',
                                                'Ladung', 'MinAbs', 'AtVol'])

        lad_spalte = atome_info_df['Ladung']

        for imols,mols in enumerate(mols_dic.items()):
            mol_lad = pd.to_numeric(lad_spalte[ (mols[1])[0]-1:(mols[1])[1] ],
                                    downcast='float')
            ladungen.append(mol_lad.sum())

        CNT_lad = ladungen[0] + ladungen[2]

        for i in range(len(ladungen)):
            voll_lad += ladungen[i]
        print (CNT_lad)
        print (ladungen[1])
        print (voll_lad)


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

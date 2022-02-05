import re
from pandas import DataFrame as df
import pandas as pd

def main(Ladungsdatei, ausgabedatei):
    lines_dic = {}
    with open(Ladungsdatei, 'r+') as istream:
        for iline, line in enumerate(istream.readlines()):
            lines_dic[iline] = line.strip().split()
    nlines = len(lines_dic)

    atom_ladung = []
    atom_nummer = []
    for (key, value) in lines_dic.items():
        if key in [0, 1, nlines, nlines-1, nlines-2, nlines-3, nlines-4]:
            pass
        else:
            atom_nummer.append(int(value[0]))
            atom_ladung.append(float(value[4]))
    
    with open(ausgabedatei, 'r+') as istream2:
        for iline2,line2 in enumerate(istream2.readlines()):
            if re.search(' MODULE QUICKSTEP:  ATOMIC COORDINATES IN angstrom',
                         line2):
                l2suchen = iline2 + 5
            else:
                pass

    atom_name_ausgabe   = []
    atom_nummer_ausgabe = []
    atom_ladung_ausgabe = []
    with open(ausgabedatei, 'r+') as istream3:
        for i in range(l2suchen - 1):
            istream3, next(istream3)
        for line3 in range(l2suchen, l2suchen + len(atom_ladung)):
            line_ausgabe_list = istream3.readline().strip().split()
           
            atom_name_ausgabe.append(line_ausgabe_list[2])
            atom_nummer_ausgabe.append(int(line_ausgabe_list[0]))
            atom_ladung_ausgabe.append(float(line_ausgabe_list[7]))

    netto_ladung = []
    for ilad in range(len(atom_nummer)):
        netto_ladung.append(atom_ladung_ausgabe[ilad] - atom_ladung[ilad])

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    ladung_data = df()
    ladung_data['Name'] = atom_name_ausgabe
    ladung_data['Pseudo Ladung'] = atom_ladung_ausgabe
    ladung_data['Bader Ladung'] = atom_ladung
    ladung_data['Netto Ladung'] = netto_ladung
    #print(ladung_data)
    #print(ladung_data.shape[0])

    ladung_gros_p50 = ladung_data[ladung_data['Netto Ladung'] >= 0.5]
    #ladung_gros_w50 = ladung_data[ladung_data['Netto Ladung'] < 0.5]
    print (ladung_gros_p50)
    print (ladung_gros_p50.shape[0])

if __name__ == '__main__':
    datei2verarbeiten = 'ACF.dat'
    ausgabedatei      = 'out.out'
    main(datei2verarbeiten, ausgabedatei)

import csv
import os

if __name__ == "__main__":
    dirpath = os.path.split(os.path.realpath(__file__))[0]

    with open(os.path.join(dirpath, 'units.csv'), 'r', encoding='utf-8') as f:
        content = f.read()
        clist = [content][0]

    lenclist = len(clist)
    i = 320
    while i < lenclist:
        if clist[i] == '\n' and clist[i - 1] != ';' and clist[i - 2] != ';':
            clisttemp = clist[:i] + clist[i + 1:]
            clist = clisttemp[:]
            lenclist = len(clist)
        else:
            i = i + 1
    
    with open(os.path.join(dirpath, 'units_originchange.csv'), 'w', encoding='utf-8') as f:
        f.write(clist)



    unitrow = []
    with open(os.path.join(dirpath, 'units_originchange.csv'), newline='', encoding='utf-8') as f: 
        cr = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in cr:
            unitrow.append(row)

    for i in range(len(unitrow) - 3):
        if unitrow[i][0].endswith('_shop"') and unitrow[i + 1][0].endswith('_0"') and unitrow[i + 2][0].endswith('_1"') and unitrow[i + 3][0].endswith('_2"'):
            unitrow[i + 2][1] = unitrow[i][1]
            unitrow[i + 3][1] = unitrow[i][1]

            unitrow[i][10] = unitrow[i][10]
            unitrow[i + 2][10] = unitrow[i][10]
            unitrow[i + 3][10] = unitrow[i][10]

    unitrowmod = []
    for i in range(len(unitrow)):
        unitrowmod.append(';'.join(unitrow[i]))
    
    with open(os.path.join(dirpath, 'units_mod.csv'), 'w', encoding='utf-8') as fw:
        for i in range(len(unitrowmod)):
            fw.write(unitrowmod[i] + '\n')

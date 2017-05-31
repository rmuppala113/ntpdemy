from xlrd import open_workbook
wb = open_workbook('cDot-lif.xls')
data = wb.sheet_by_index(0)
numrows = data.nrows
numcols = data.ncols
for row in range(numrows):
    for col in range(numcols):
        mylist = [data.cell_value(row, col)]
        print(mylist)





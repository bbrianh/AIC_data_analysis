import os

_DIR_CHEAT = 'cheat_sheet'
_PATH_OUTPUT_CSV = 'analysis.csv'

_sheets = os.listdir(_DIR_CHEAT)
data = []
accuracy = []

for _sheet in _sheets:
    acc = float(_sheet.strip('.csv'))/100
    accuracy.append(acc)

    _PATH = os.path.join(_DIR_CHEAT, _sheet)
    f = open(_PATH, 'r')
    f_line = f.readlines()
    f.close
    f_line = f_line[0].split(',')

    for i in range(len(f_line)):
        f_line[i] = int(f_line[i].strip())
    data.append(f_line)

header = ''

for i in range(len(_sheets)):
  model_no = i+1
  model_name = 'model' + str(model_no) + ','
  header += model_name
header = header[:-1]
header += '\n'

f = open(_PATH_OUTPUT_CSV, "w")
f.write(header)

# print(data[0][1])

for j in range(len(data[0])):
    line = ''
    for k in range(len(data)):
        data_str = '%d,' % ( data[k][j] )
        line += data_str
    line = line[:-1]
    line += '\n'
    f.write(line)

acc_line = ''
for i in range(len(accuracy)):
    acc_str = '%.4f,' %(accuracy[i])
    acc_line += str(acc_str)

acc_line = acc_line[:-1]
acc_line += '\n'
f.write(acc_line)

f.close()

print('FINISHED')





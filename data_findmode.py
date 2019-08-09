import os
import numpy as np
from scipy import stats

_DIR_CHEAT = 'cheat_sheet'
_PATH_mode = 'mode.txt'

_sheets = os.listdir(_DIR_CHEAT)
data = []

for _sheet in _sheets:
 _PATH = os.path.join(_DIR_CHEAT, _sheet)
 f = open(_PATH, 'r')
 f_line = f.readlines()
 f.close
 f_line = f_line[0].split(',')

 for i in range(len(f_line)):
   f_line[i] = int(f_line[i].strip())

 data.append(f_line)
 data = data[:-1]

data = np.array(data)
m = stats.mode(data)
mode = np.array(m.mode).tolist()

# np.savetxt("mode.csv", mode, delimiter=",")
f_mode = open(_PATH_mode,'w')
f_mode.write(str(mode[0]))
f_mode.close()





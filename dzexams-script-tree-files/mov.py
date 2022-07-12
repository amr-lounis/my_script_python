from pathlib import Path
import os 

mypath = './dzexams/'
pathOut = './new/'

p = Path(mypath)
for i in p.glob('**/*'):
    if(i.name[-3:]== 'pdf') :
      try:
         # print(pathOut+i.name)
         os.replace(str(i), pathOut+i.name)
      except:
         print("Error:",i,' < - > ',pathOut)   
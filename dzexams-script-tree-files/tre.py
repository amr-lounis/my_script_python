import os 
import re
    
def treeDir(_inPath):
    _lisrInDir= os.listdir(_inPath)
    
    for f in _lisrInDir:
        f_s= f.split('-')
        
        if ( (f[-3:]== 'pdf') & (len(f_s) == 6 ) ):    
            # example 1am => am1
            sp = f_s[1]
            result = re.match('^[012345]', sp)
            if result:
              sp = sp[1:]+sp[0]
            # if exicet correction move to new dir correction
            _dir = ""
            result = re.match('^....1', f_s[4])
            if result:
              _dir = "correction/"
            # if exicet not correction move to new dir year
            result = re.match('^....0', f_s[4])
            if result:
              year = f_s[4][:-1]
              _dir = year +'/'
            # crete path to move
            _outPath = \
            f_s[0]+'/'+\
            sp    +'/'+\
            f_s[3]+'/'+\
            f_s[2]+'/'+\
            _dir
            
            # if not ecist path create the path
            if not os.path.exists(_outPath):
                os.makedirs(_outPath)
            
            try:
              os.replace(_inPath + f, _outPath + f)
              print(_outPath + f)
            except:
              print("Error:",_inPath,' < - > ',_outPath)      
              
treeDir('./sujets2018/') 
treeDir('./sujets2019/') 
treeDir('./sujets2020/') 
treeDir('./sujets2021/') 
  

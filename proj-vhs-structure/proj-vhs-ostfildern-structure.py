from pathlib import Path
import  shutil
import os


L1_vhs =                      './VHS-Ostfildern'
L2_vhs_edv =                  './VHS-Ostfildern/EDV/'
L3_vhs_edv_pp =               './VHS-Ostfildern/EDV/PP/'
L3_vhs_edv_msoffice =         './VHS-Ostfildern/EDV/MS-Office/'
L3_vhs_edv_python =           './VHS-Ostfildern/EDV/Python/'
L2_vhs_sprachen =             './VHS-Ostfildern/SPRACHEN/'
L3_vhs_sprachen_deutsch =     './VHS-Ostfildern/SPRACHEN/Deutsch-Integration/'
L3_vhs_sprachen_italianisch = './VHS-Ostfildern/SPRACHEN/Italianisch/'
L3_vhs_sprachen_spanisch =    './VHS-Ostfildern/SPRACHEN/Spanisch/'
L3_vhs_sprachen_englisch =    './VHS-Ostfildern/SPRACHEN/Englisch/'
L2_vhs_k =                    './VHS-Ostfildern/KINDER/'
L3_vhs_k_robotik =            './VHS-Ostfildern/KINDER/Robotik-Einfuehrung/'
L3_vhs_k_naehen  =            './VHS-Ostfildern/KINDER/Naehen/'


os.makedirs(os.path.dirname(L1_vhs), exist_ok=True)

#VHS/EDV
os.makedirs(os.path.dirname(L2_vhs_edv), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_edv_pp), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_edv_msoffice), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_edv_python), exist_ok=True)

#VHS/SPRACHEN
os.makedirs(os.path.dirname(L2_vhs_sprachen), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_sprachen_deutsch), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_sprachen_italianisch), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_sprachen_spanisch), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_sprachen_englisch), exist_ok=True)


#VHS/KINDER
os.makedirs(os.path.dirname(L2_vhs_k), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_k_robotik), exist_ok=True)
os.makedirs(os.path.dirname(L3_vhs_k_naehen), exist_ok=True)



#Copying index.html under VHS Directory
src = './index.html'
dst = L1_vhs + '/index.html'
shutil.copy(src, dst)





import re
import xml.etree.ElementTree as ET
from random import randint

# Parse the SVG file
svg_file = "/Users/sbinger/Projects/FAIRDO/type-system/TypeSystem3.svg"

# Read the file content
try:
    with open(svg_file, 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    print(f"Error reading SVG file: {e}")
    exit(1)

root = ET.fromstring(content)

#level0 = root.find('.//g[@data-cell-id="0"]')
level1 = root.find('.//g[@data-cell-id="1"]')
handles = {}

#all_types = []
#tmp = []
#for elemens in root.findall('.//{http://www.w3.org/2000/svg}g/{http://www.w3.org/2000/svg}g/{http://www.w3.org/2000/svg}g/{http://www.w3.org/2000/svg}g/{http://www.w3.org/2000/svg}g/{http://www.w3.org/2000/svg}g/{http://www.w3.org/2000/svg}g/{http://www.w3.org/2000/svg}g//'):
#    if elemens.text != None and 'text' in elemens.tag:
#        if elemens.text == '0.FDO/Type':
#            all_types.append(tmp)
#            tmp = [] 
#        tmp.append(elemens.text)   
#for test in all_types:
#    print(len(test))

for level0 in root:
    if level0.tag=="{http://www.w3.org/2000/svg}g":
        for level1 in level0:
            for level2 in level1:
                for level3 in level2:
                    #print(level3.tag, level3.attrib)
                    count=0
                    for level4 in level3:
                        if "data-cell-id" in level4.attrib:
                            count = count+1
                    if count>0: # and 'zZ' in level3.attrib['data-cell-id']:
                        #print(level3.tag, level3.attrib)
                        #print(level3.attrib['data-cell-id'])
                        #print('#####################')
                        for level4 in level3:
                            for level5 in level4:
                                if "data-cell-id" in level5.attrib:
                                    for level6 in level5:
                                        if level6.attrib=={}: 
                                            for level7 in level6:
                                                for level8 in level7:
                                                    for level9 in level8:
                                                        if 'foreignObject' in level9.tag:
                                                            for level10 in level9:
                                                                for level11 in level10:      
                                                                    for level12 in level11:
                                                                        # As names can appear more than once use random extension
                                                                        handles[tmpvar][level12.text+'_r'+str(randint(0,9999))]='0'                                                                                                                                                    
                                elif level5.attrib=={}:
                                    for level5a in level5: 
                                        for level5b in level5a: 
                                            if 'text' in level5b.tag:
                                                tmpvar = level5b.text 
                                                handles[level5b.text]={}
                                                #print('----'+level5b.text+'-----')

handles_sorted={}
for elem in handles:
    mlist = list(handles[elem])
    leng = int(len(mlist)/2)
    handles_sorted[elem.split('_r')[0]]=[]
    for i in range(leng):
#        handles_sorted[elem.split('_r')[0]][mlist[i]]=mlist[leng+i].split('_r')[0] 
        handles_sorted[elem.split('_r')[0]].append({mlist[i].split('_r')[0] : mlist[leng+i].split('_r')[0] })


import json
with open('type-system-v2.json', 'w') as f:
    json.dump(handles_sorted, f)

### Manuel fixes

name_of_pubkey='21T11993_USER1-pub.bin'
admin_key='300:111111111111:12345/hdl1'

with open('type-system.batch', 'w') as f:
    f.write('AUTHENTICATE PUBKEY:300:0.NA/21.T11.9993\n')
    f.write('admpriv_21.T11.9993.bin\n')
    f.write('\n')
    for elem in handles_sorted:
        f.write('CREATE '+ elem + '\n')
        f.write('100 HS_ADMIN 86400 1110 ADMIN 300:111111111111:12345/hdl1\n')
        f.write('300 HS_PUBKEY 86400 1110 FILE '+name_of_pubkey+'\n')
        count=1
        for kv in handles_sorted[elem].keys():
            f.write(str(count)+' ' + kv+ ' 86400 1110 UTF8 ' + handles_sorted[elem][kv]+'\n')
            count = count+1
        f.write('\n')



#for i in range(len(handles['0.FDO/Type'])):
 

#handles_sorted['0.FDO/Type'] = 
#print(type(root))
#print(type(content))

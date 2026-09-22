import json
import sys

name_of_pubkey='/Users/sbinger/Projects/ePIC/Prefix_Administration/21.T11970/admpriv.bin'
admin_key='300:111111111111:0.NA/21.T11970'

# Default values

input_json = 'type-system.json'
action = 'CREATE'

if len(sys.argv) == 2: 
    input_json = sys.argv[1]
elif len(sys.argv) == 1: 
    print('Usage: python create_handle_batch.py <filename.json> <action>')
    print('Usage: Using default: type-system.json and action can be CREATE or MODIFY')
elif len(sys.argv) == 3:
    input_json = sys.argv[1]
    action = sys.argv[2]
else:
    print('WARING: Too many parameters!')

output = input_json.split('.')[0]+'.batch'
print('Output: '+output)
print('Action: '+action)
# Commments
# - Need to replace all 0.FDO with the prefix used

# Config #####################################
prefix = '21.T11970'
admin_handle = '0.NA/21.T11970'
admin_index = '300:'
##############################################

with open(input_json, 'r') as f:
    handles_sorted = json.load(f)

with open(output, 'w') as f:
    f.write('AUTHENTICATE PUBKEY:'+admin_index+':'+admin_handle+'\n')
    f.write(name_of_pubkey+'\n')
    f.write('\n')
    for elem in handles_sorted:
        f.write(action+' '+ elem.replace('0.FDO',prefix) + '\n')
        f.write('100 HS_ADMIN 86400 1110 ADMIN '+admin_index+':111111111111:'+admin_handle+'\n')
        count=1
        for kv in handles_sorted[elem]:
            key,value = list(kv.items())[0]
            f.write(str(count)+' ' + key.replace('0.FDO',prefix)+ ' 86400 1110 UTF8 ' + value.replace('0.FDO',prefix)+'\n')
            count = count+1
        f.write('\n')

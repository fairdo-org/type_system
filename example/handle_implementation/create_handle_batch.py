import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Default values
name_of_privkey = str(os.getenv('NAME_OF_PRIVKEY'))
admin_key = str(os.getenv('ADMIN_KEY')) # for batch authorization
prefix = str(os.getenv('PREFIX')) # for HS_ADMIN value
admin_handle = str(os.getenv('ADMIN_HANDLE'))  # for HS_ADMIN value
admin_index = str(os.getenv('ADMIN_INDEX'))  # for HS_ADMIN value


if len(sys.argv) == 4:
    input_json = sys.argv[1]
    output = sys.argv[2]
    action = sys.argv[3]
else:
    print('WARNING: Usage is ')
    print(' python create_handle_batch.py <input.json> <output> <action>')
    quit()

with open(input_json, 'r') as f:
    handles_sorted = json.load(f)

with open(output, 'w') as f:
    f.write('AUTHENTICATE PUBKEY:'+admin_index+':'+admin_handle+'\n')
    f.write(name_of_privkey+'\n')
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

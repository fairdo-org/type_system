import json

with open('type-system.json', 'r') as f:
    ts = json.load(f)

with open('type-system-overview.md','w') as f:
    f.write('```mermaid\n')
    f.write('erDiagram\n')
    for elem in ts:
        f.write('  ' + elem.replace('0.FDO/','O.FDO-') + '{')
        for att in ts[elem]:
            key = list(att.keys())[0].replace('0.FDO/','O.FDO-')
            val = list(att.values())[0].replace('0.FDO/','O.FDO-')

            f.write('    ' + key + ' `')
            maxl = 40
            if len(val)>maxl:
                valarr = val.split(' ')
                count = 0 
                text = ''
                for term in valarr:
                    count=count+len(term)
                    text=text+term + ' '
                    if count>maxl:
                        f.write(text + '\n')
                        count=0
                        text=''
                if len(text)>0:
                    f.write(text)
                f.write('`\n')
            else: 
                f.write( val + '`\n')
        f.write('}\n')
    # find relations
    option = 2
    if option == 1:
        for elem1 in ts:
            ent1 = elem1.replace('0.FDO/','O.FDO-')
            for elem2 in ts:
                if elem1 != elem2:
                    found = False
                    for att in ts[elem2]:
                        if list(att.keys())[0].strip() == elem1 and not found:
                            ent2 = elem2.replace('0.FDO/','O.FDO-')
                            f.write(ent1 + ' ||--|| '+ ent2 + ' : ref \n')
                            found = True
    elif option == 2:
        links = []
        for elem1 in ts:
            ent1 = elem1.replace('0.FDO/','O.FDO-')
            for att in ts[elem1]:
                ent2 = list(att.keys())[0].strip().replace('0.FDO/','O.FDO-')
                link = ent1 + ' ||--|| '+ ent2 + ' : requires \n'
                links.append(link)
        # remove duplicates
        links = list(set(links))
        for link in links:
            f.write(link)



    #CUSTOMER ||--o{ ORDER : places
    #ORDER ||--|{ ORDER_ITEM : contains
    #PRODUCT ||--o{ ORDER_ITEM : includes
    #CUSTOMER {
    #    string id
    #    string name
    #    string email
    #}
    #ORDER {
    #    string id
    #    date orderDate
    #    string status
    #}
    #PRODUCT {
    #    string id
    #    string name
    #    float price
    #}
    #ORDER_ITEM {
    #    int quantity
    #    float price
    #})
    f.write('```')
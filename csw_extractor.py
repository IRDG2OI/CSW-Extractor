#!/usr/bin/python3
# Enter server URL here :
csw_server = 'http://g2oi-dev2022.univ.run:8060/geonetwork/srv/eng/csw'
# Keywords to search
csw_req = ''

from owslib.csw import CatalogueServiceWeb
from owslib.fes import PropertyIsEqualTo, PropertyIsLike, BBox
import csv

print('CSW Server :', csw_server)
print('CSW Request:', csw_req)


csw = CatalogueServiceWeb(csw_server)

# Catalog info
print("Type of Catalog:", csw.identification.type)
print("Properties of Catalog:", [op.name for op in csw.operations])
csw.getdomain('GetRecords.resultType')

# Query
all_query = PropertyIsEqualTo('csw:AnyText', csw_req)
csw.getrecords2(constraints=[all_query], maxrecords=10)
csw.results
csw.getrecords2(constraints=[all_query], maxrecords=csw.results['matches'])
result = csw.results
print("Found:", result['matches'], "metadata(s)" "--||-- Filtered:", result['returned'])

# Writing to CSV
data = []
tit = "Title:"
data.append(tit)
    
with open('Titre_Fiches.csv', 'w', newline='\n') as f:
    writer = csv.writer(f, delimiter=';')
    for rec in csw.records:
        meta_title = csw.records[rec].title
        data.append(meta_title)
    writer.writerows(data)

# Format bad data
search_text = ";"
replace_text = ""
with open(r'Titre_Fiches.csv', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

with open(r'Titre_Fiches.csv', 'w') as file:
    file.write(data)
    
print("Finished")
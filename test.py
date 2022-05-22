from conexionDB import *
from Query import *

# x = RegistroDatos()
#
# for i in x.get_column_names('country'):
#     print(i[0])

q = Query()
q.append_parameters('p.Region')
q.append_parameters('p.Population')
q.append_parameters('p.IndepYear')

q.append_tables('country as p')


name_p = 'colombia'
name_p = str("'" + name_p + "'")
if name_p != '\'\'':
    q.append_wheres("p.name like {}".format(name_p))

print(q.get_query())

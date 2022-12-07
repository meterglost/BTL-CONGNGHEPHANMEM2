from .database import Database

if Database.dbInstance is None:
    print('Database not connected!')

import argon2

ph = argon2.PasswordHasher()

try:
    Database.dbInstance.drop_database('uwc')
except:
    pass
Database.dbInstance['uwc']['user'].insert_many([
    { 'username': 'bo1', 'password': ph.hash('123456@bo1'), 'role': 'BackOfficer', 'lang': 'vi_vn'},
    { 'username': 'bo2', 'password': ph.hash('123456@bo2'), 'role': 'BackOfficer', 'lang': 'en_us'},
])

print('Migrate finished!')

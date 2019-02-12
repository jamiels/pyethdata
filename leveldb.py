# Jamiel Sheikh - jamiel@chainhaus.com

# pip install plyvel 

import plyvel


### Connect and pull all keys in LevelDB - Good luck getting this to work on Windows
db = plyvel.DB('/geth/chaindata/000016.ldb',create_if_missing=False)

for k,v in db:
    print(k,":",v)
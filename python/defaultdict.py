# defaultdict 사용법

# value를 기준으로 group by를 할려고 할때
# http://stackoverflow.com/questions/3749512/python-group-by

from collections import defaultdict


input = [
          ('11013331', 'KAT'), 
          ('9085267',  'NOT'), 
          ('5238761',  'ETH'), 
          ('5349618',  'ETH'), 
          ('11788544', 'NOT'), 
          ('962142',   'ETH'), 
          ('7795297',  'ETH'), 
          ('7341464',  'ETH'), 
          ('9843236',  'KAT'), 
          ('5594916',  'ETH'), 
          ('1550003',  'ETH')
]
result = defaultdict(list)

for key, value in input:
    result[value].append(key)


print(
    [
        {'type':key, 'items':value} 
        for key,value 
        in result.items()
    ]
)

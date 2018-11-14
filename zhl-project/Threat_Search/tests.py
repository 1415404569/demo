import re

data = ['4d90e3a14ebb282bcdf3095e377c8d26', #32
        '357463713179797a6579386b61666471316e6d76',  #40
        'd66e45dc52cb2fd6babc1f04d3dd5345d1d6facda6b482f16e16fcaec3523aff',  #64
        'https://www.baidu.com',
        '8.8.8.8',
        'topsec.com.cn',
        ]
if len(data[0]) == 32:
    re_data = re.findall('[a-z0-9]{32}',data[0])
    print(re_data)
if len(data[1]) == 40:
    re_data = re.findall('[a-z0-9]{40}',data[1])
    print(re_data)
if len(data[2]) == 64:
    re_data = re.findall('[a-z0-9]{64}', data[2])
    print(re_data)

if data[3].split('https'):
    print(data[3].split('https'))



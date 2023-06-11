# made by mrcheeze

import json

for dtype,gamedatas in json.load(open('GameDataList.Product.110.json'))['RootNode']['Data'].items():
    if dtype == 'Struct':
        for gamedata in gamedatas:
            for value in gamedata['DefaultValue']:
                if 'ValueText' in value:
                    if not 'HashText' in value:
                        print(value['ValueText'].rsplit('.',1)[1])
                    if not 'HashText' in gamedata:
                        print(value['ValueText'].rsplit('.',1)[0])
                if 'HashText' in gamedata and 'HashText' in value:
                    if not 'ValueText' in value:
                        print(gamedata['HashText']+'.'+value['HashText'])
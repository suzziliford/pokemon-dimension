def find_types(self, name):
        z = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        y = z.json()
        # print({y['types'][0]})
        bug = [b for doodies, b in y.items()  if doodies == 'types']
        print(bug)
        for yups in bug:
            print(yups)
            for pups in yups:
                print (pups)  
                for vets, jets in pups.items():
                    if vets == 'type':
                        print(jets)
                        print(jets['url'])

import re


def generate_dom_to_classes(dom: {}):
    print(f'This is a DOM:\t{dom}')
    

def extract_packages(massive):
    zoo = {}
    for line in massive:
        match_package = re.search(r'\* (.+)', line)
        if match_package:
            zoo.update({match_package.group(1): []})

        match_class = re.search(r'^[^*#].+', line)
        if match_class:
            qu = zoo.get(list(zoo.keys())[-1])
            qu.append(match_class[0])
            print(f'lines of classes:\t{qu}')

    print()
    # print(f'values:\t{list(zoo.values())}')
    # print(f'keys:\t{list(zoo.keys())}')
    print(f'resulted DOM:\t{zoo}')

    generate_dom_to_classes(zoo)


with open('pat.pat', 'r') as f:
    lines = f.readlines()
    print('-----------------------------------------------')
    print(f'file-data:\n{lines}')
    print('-----------------------------------------------')
    # по идее скан по пакаджам идет.

extract_packages(lines)

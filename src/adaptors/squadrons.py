import json

# import src.adaptors.joystick_diagram_interface as jdi
#
# class Squadrons_Parser(jdi.JDinterface):
#     def __init__(self, path, easy_modes=True):
#         jdi.JDinterface.__init__(self)
#         self.path = path
#         self.remove_easy_modes = easy_modes
#         self.__easy_mode = '_easy'
#         self.base_directory = self.__validateBaseDirectory()
#         self.valid_profiles = self.__validateProfiles()
#         self.joystick_listing = {}

def findDeviceLeafs(mapping_dict, device_id, res):
    nodes = mapping_dict.keys()
    for node in nodes:
        subnodes = mapping_dict[node].values()
        for subnode in subnodes:
            if isinstance(subnode, dict):
                findDeviceLeafs(subnode, device_id, res=res)
            else:
                print(node)

# https://stackoverflow.com/a/11570745
def paths(tree, cur=()):
    if not tree or not isinstance(tree, dict):
        yield cur+(tree,)
    else:
        for n, s in tree.items():
            for path in paths(s, cur+(n,)):
                yield path

# Mashup of a couple stackoverflow responses
# https://stackoverflow.com/a/29652561
# https://stackoverflow.com/a/31998950
def gen_dict_extract(key, value, var, path):
    if not path:
        path = []
    if hasattr(var,'items'):
        for k, v in var.items():
            if k == key and v == value:
                yield path
            if isinstance(v, dict):
                local_path = path[:]
                local_path.append(k)
                for result in gen_dict_extract(key, value, v, local_path):
                    yield result

def parseFile():
    path='D:/RDT2/SWS/joystick-diagrams/ProfileOptions_profile_synced_wildfire'
    newdata = ''
    with open (path, "r") as f:
        data = f.read()
        newdata = data.splitlines()

    result = dict()
    for line in newdata:
        val = line.split(' ')[1]
        line = line.split(' ')[0]

        leaf = result
        for item in line.split('.')[:-1]:
            if item not in leaf.keys():
                leaf[item] = dict()
            leaf = leaf[item]

        leaf[line.split('.')[-1]] = val

    # with open(path + ".json", "w") as outfile:
    #     json.dump(result, outfile, indent=4)

    #findDeviceLeafs(result, 1)

    return result


if __name__ == '__main__':
    profiles = parseFile()
    for x in gen_dict_extract('deviceid', '0', profiles['GstKeyBinding']['IncomStarshipInputConcepts'], None):
        print(x)
        # ToDo: Utilize this code to take a list an get the remaining dictionary keys
        #       https://stackoverflow.com/questions/39818669/dynamically-accessing-nested-dictionary-keys

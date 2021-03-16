import json
import math

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


def gen_dict_extract_value(key, value, var, path):
    if not path:
        path = []
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key and v == value:
                yield path
            if isinstance(v, dict):
                local_path = path[:]
                local_path.append(k)
                for result in gen_dict_extract_value(key, value, v, local_path):
                    yield result


def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                yield from gen_dict_extract(key, v)


def parseFile():
    path = 'D:/RDT2/SWS/joystick-diagrams/ProfileOptions_profile_synced_brunas'
    newdata = ''
    with open(path, "r") as f:
        data = f.read()
        newdata = data.splitlines()

    result = dict()
    for line in newdata:
        val = line.split(' ', 1)[1]
        line = line.split(' ')[0]

        leaf = result
        for item in line.split('.')[:-1]:
            if item not in leaf.keys():
                leaf[item] = dict()
            leaf = leaf[item]

        leaf[line.split('.')[-1]] = val

    result['GstInput']['JoystickDevice0'] = 'To Be Determined Device'

    # with open(path + ".json", "w") as outfile:
    #     json.dump(result, outfile, indent=4)

    #findDeviceLeafs(result, 1)

    return result


def translate_button_id(button_id, unmapped_button):
    # Axis: X-Axis: 8/10
    # Y-Axis: 9/11
    # Axis 26 is unmapped Axis indicator
    #
    # Buttons
    # UNKNOWN = 1-13
    # (hunch is 2-5, 8-11 are skipped because those are also axis values or maybe reserved for controllers)
    #
    # Slider0 = 14/15
    # Slider1 = 16/17
    # UNKNOWN = 18-21
    # Button 1-18 = 22-39
    # Z-Axis = 40/41
    # Rx = 42/43
    # Ry = 44/45
    # Rz = 46/47
    # POV1 48-51
    # POV2 52-55
    # POV3 56-59
    # POV4 60-63
    # Button 19-127 = 64-173
    # Button 174 is unmapped button indicator

    if button_id <= 13 or button_id >= unmapped_button or (button_id >= 18 and button_id <= 21):
        return "unknown"
    if button_id == 14:
        return "Slider-0-positive"
    if button_id == 15:
        return "Slider-0-negative"
    if button_id == 16:
        return "Slider-1-positive"
    if button_id == 17:
        return "Slider-1-negative"
    if 22 <= button_id <= 39:
        return "Button-" + str(button_id - 21)
    if 64 <= button_id <= 173:
        return "Button-" + str(button_id - 45)
    if button_id == 40:
        return "Z-Axis-positive"
    if button_id == 41:
        return "Z-Axis-negative"
    if button_id == 42:
        return "Rx-Axis-positive"
    if button_id == 43:
        return "Rx-Axis-negative"
    if button_id == 44:
        return "Ry-Axis-positive"
    if button_id == 45:
        return "Ry-Axis-negative"
    if button_id == 46:
        return "Rz-Axis-positive"
    if button_id == 47:
        return "Rz-Axis-negative"
    if 48 <= button_id <= 63:
        pov_num = math.floor((button_id-48) / 4) + 1
        dir_num = button_id % 4
        if dir_num == 0:
            direction = 'up'
        elif dir_num == 1:
            direction = 'down'
        elif dir_num == 2:
            direction = 'left'
        else:
            direction = 'right'

        return "POV" + str(pov_num) + '-' + direction


if __name__ == '__main__':
    profiles = parseFile()
    buttons = dict()
    axis = dict()
    if int(profiles['GstKeyBinding']['InputDataVersion']) < 4:
        unmapped_button = 86
        unmapped_axis = 26
    else:
        unmapped_button = 174
        unmapped_axis = 26

    device_ids = sorted(set(gen_dict_extract('deviceid',
                                      profiles['GstKeyBinding']['IncomStarshipInputConcepts'])))

    for i in device_ids:
        button_list = list()
        axis_list = list()
        print("********************************************")
        print("DEVICE", str(i) + ": ", profiles['GstInput']['JoystickDevice' + str(int(i)+1)])
        print("********************************************")
        for x in gen_dict_extract_value('deviceid', str(i), profiles['GstKeyBinding']['IncomStarshipInputConcepts'], None):
            ret = profiles['GstKeyBinding']['IncomStarshipInputConcepts']
            for k in x:
                ret = ret[k]

            if ret['button'] != str(unmapped_button):
                print(x[0] + '-' + x[1], translate_button_id(int(ret['button']), unmapped_button))
                button_list.append(int(ret['button']))
            elif ret['axis'] != str(unmapped_axis):
                print(x[0] + '-' + x[1], "Axis-" + ret['axis'])
                axis_list.append(int(ret['axis']))

        buttons[str(i)] = button_list
        axis[str(i)] = axis_list

    print("********************************************")
    print("Buttons")
    print("********************************************")

    for x in buttons:
        buttons[x].sort()
        print("Device: " + x + " " + buttons[x].__str__())

    print("********************************************")
    print("Axis")
    print("********************************************")
    for x in axis:
        axis[x].sort()
        print("Device: " + x + " " + axis[x].__str__())

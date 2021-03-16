import json
import math
import keyboard_scancodes

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
    path = 'D:/RDT2/SWS/joystick-diagrams/ProfileOptions_profile_synced_wildfire_2021-03-15'
    print(path)
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


def translate_keyboard_id(key_id):
    val = keyboard_scancodes.LOOKUP[key_id]['leaf'][1]
    return "KEY_" + val


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
        return "UNKNOWN"
    if button_id == 14:
        return "AXIS_SLIDER_0_P"
    if button_id == 15:
        return "AXIS_SLIDER_0_N"
    if button_id == 16:
        return "AXIS_SLIDER_1_P"
    if button_id == 17:
        return "AXIS_SLIDER_1_N"
    if 22 <= button_id <= 39:
        return "BUTTON_" + str(button_id - 21)
    if 64 <= button_id <= 173:
        return "BUTTON_" + str(button_id - 45)
    if button_id == 40:
        return "AXIS_Z_P"
    if button_id == 41:
        return "AXIS_Z_N"
    if button_id == 42:
        return "AXIS_RX_P"
    if button_id == 43:
        return "AXIS_RX_N"
    if button_id == 44:
        return "AXIS_RY_P"
    if button_id == 45:
        return "AXIS_RY_N"
    if button_id == 46:
        return "AXIS_RZ_P"
    if button_id == 47:
        return "AXIS_RZ_N"
    if 48 <= button_id <= 63:
        pov_num = math.floor((button_id-48) / 4) + 1
        dir_num = button_id % 4
        if dir_num == 0:
            direction = 'U'
        elif dir_num == 1:
            direction = 'D'
        elif dir_num == 2:
            direction = 'L'
        else:
            direction = 'R'

        return "POV_" + str(pov_num) + '_' + direction


def translate_axis_id(axis_id, unmapped_axis):
    # TODO: Validate Axis, ensure invert is not set
    #       Also see what issues invert can cause
    if axis_id >= unmapped_axis:
        return "AXIS_UNKNOWN"
    elif axis_id == 8:
        return "AXIS_X_P"
    elif axis_id == 10:
        return "AXIS_X_N"
    elif axis_id == 9:
        return "AXIS_Y_N"
    elif axis_id == 11:
        return "AXIS_Y_P"
    else:
        return "AXIS_" + str(axis_id)


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

    for device_id in device_ids:
        button_list = list()
        axis_list = list()
        print("********************************************")
        print("DEVICE", device_id + ": ", profiles['GstInput']['JoystickDevice' + str(int(device_id)+1)])
        print("********************************************")
        for x in gen_dict_extract_value('deviceid', device_id,
                                        profiles['GstKeyBinding']['IncomStarshipInputConcepts'], None):
            ret = profiles['GstKeyBinding']['IncomStarshipInputConcepts']
            for k in x:
                ret = ret[k]

            if ret['button'] != str(unmapped_button):
                if device_id == '-1':
                    if ret['button'] == '0':
                        print(x[0] + '-' + x[1], 'KEY_UNKNOWN')
                    else:
                        print(x[0] + '-' + x[1], translate_keyboard_id(int(ret['button'])))
                else:
                    print(x[0] + '-' + x[1], translate_button_id(int(ret['button']), unmapped_button))
                button_list.append(int(ret['button']))
            elif ret['axis'] != str(unmapped_axis):
                if device_id == '-1':
                    print(x[0] + '-' + x[1], "TBD Axis: " + ret['axis'])
                else:
                    print(x[0] + '-' + x[1], translate_axis_id(int(ret['axis']), unmapped_axis))
                axis_list.append(int(ret['axis']))

        buttons[device_id] = button_list
        axis[device_id] = axis_list

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

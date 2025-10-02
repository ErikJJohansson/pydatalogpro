from pycomm3 import LogixDriver
from sys import argv
import argparse
import DATALOG
from itertools import product


def generate_datalog_tags(template, groupname, shortcut, tag):

    # Replace placeholders
    result = template.replace("GROUPNAME", groupname).replace("SHORTCUTTAG", shortcut + tag)

    return result


def get_aoi_tag_instances(plc, tag_type):
    """
    function returns list of tag names matching struct type
    """
    #return tag_list

    tag_list = []

    for tag, _def in plc.tags.items():
        if _def['data_type_name'] == tag_type and not(_def['alias']):
            if _def['dim'] > 0:
                tag_list = tag_list + get_dim_list(tag,_def['dimensions'])
            else:
                tag_list.append(tag)

    return tag_list

def get_dim_list(base_tag, dim_list):
    '''
    function takes a list which has the array size and turns it into a list with all iterations
    '''
    # remove 0's
    filtered_list = list(filter(lambda num: num != 0, dim_list))

    temp = []

    for indices in product(*[range(dim) for dim in filtered_list]):
        temp.append(base_tag + ''.join(f'[{i}]' for i in indices))

    return temp

def main():

    # will be replaced with PLC name
    default_deviceshortcut = ''
    default_groupname = ''

    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Python-based PlantPAX Data Log Pro tool',
        epilog='This tool works on both Windows and Mac.')
    
    # Add command-line arguments
    parser.add_argument('commpath', help='Path to PLC')
    parser.add_argument('taggroup', nargs='?', default=default_groupname,help='Group to store tags in')
    parser.add_argument('deviceshortcut', nargs='?', default=default_deviceshortcut,help='Shortcut in FTView')


    # parse arguments
    args = parser.parse_args()

    # Access the parsed arguments
    commpath = args.commpath
    taggroup = args.taggroup
    device_shortcut = args.deviceshortcut

    # open connection to PLC

    plc = LogixDriver(commpath, init_tags=True,init_program_tags=True)

    print('Connecting to PLC.')
    try:
        plc.open()
        plc_name = plc.get_plc_name()

        print('Connected to ' + plc_name + ' PLC at ' + commpath)
    except:
        print('Unable to connect to PLC at ' + commpath)
        exit()

    # if the shortcut was left blank, create it and spit out a default message
    if device_shortcut == '':
        device_shortcut = '/DATA::[' + plc_name + ']'

        print('No FTView device shortcut specified. Using PLC name. Path is: ' + device_shortcut)


    print("Creating CSV of tags.")

    filename = plc_name + '_DataLogProTags.csv'
    # Write to file
    with open(filename, 'w') as file:
        file.write(DATALOG.DATALOG_TEMPLATE)

        # loop through AOIs
        for aoi_type in DATALOG.DATALOG_LIST:
            aoi_instance_list = get_aoi_tag_instances(plc, aoi_type)

            for aoi_instance in aoi_instance_list:
                file.write(generate_datalog_tags(DATALOG.DATALOG_DEFINITIONS[aoi_type],taggroup,device_shortcut,aoi_instance))




    plc.close()

    print('Done!')


if __name__ == "__main__":
    main()
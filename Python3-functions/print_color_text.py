# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_color_warning(msg,obj=''):
    print(bcolors.WARNING + str(msg) + str(obj) + bcolors.ENDC)

def print_color_ok(msg, obj=''):
    print(bcolors.OKGREEN + str(msg) + str(obj) + bcolors.ENDC)


print_color_warning('hello',[1,2,3])

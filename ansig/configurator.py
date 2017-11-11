from configparser import SafeConfigParser, DuplicateSectionError
from os import path

DEFAULTS = {
    'regions': 'all',
    'regions_exclude': '',
}


class ConfigParser(SafeConfigParser):
    ''' Custom configuration parser '''

    def __init__(self, filename=None):
        super(ConfigParser, self).__init__(DEFAULTS)

        if filename and path.isfile(filename):
            self.read(filename)

        try:
            self.add_section('aws')
        except DuplicateSectionError:
            pass

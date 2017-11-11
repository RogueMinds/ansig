from json import dumps
from os import environ
from sys import stdout

from ansig.configurator import ConfigParser


class Generator(object):
    ''' Dynamic inventory generator for Ansible '''

    def __init__(self, filename=None):
        self.config = ConfigParser(filename)
        self.session = self._configure_session()
        self.regions = self._configure_regions()

    @property
    def _default_inventory(self):
        return {'all': {'hosts': [], 'vars': {}}, '_meta': {'hostvars': {}}}

    def _configure_session(self):
        pass

    def _configure_regions(self):
        regions = []

        configured_regions = self.config.get('aws', 'regions').split(',')
        if 'all' in configured_regions:
            excluded_regions = self.config.get('aws', 'regions_exclude')
            for region_info in []:
                if region_info.name not in excluded_regions:
                    regions.append(region_info.name)
        elif 'auto' in configured_regions:
            reg = environ.get('AWS_REGION', environ.get('AWS_DEFAULT_REGION'))
            if reg:
                regions.append(reg)
        else:
            regions = [reg.strip() for reg in configured_regions]

        return regions

    def generate_host_list(self):
        ''' Generates a list of available hosts and their metadata '''

        inventory = self._default_inventory
        inventory.update({
            'all': {
                'hosts': ['ansible-test.ops.bliminternal.com']
            },
            'webservers': {
                'hosts': ['ansible-test.ops.bliminternal.com']
            }
        })

        stdout.write(dumps(inventory, indent=2))

    def generate_host_info(self, host):
        ''' Generates all the metadata for a specific host '''

        inventory = {}

        stdout.write(dumps(inventory, indent=2))

    def generate_debug_info(self, filename=None):
        ''' Generates debugging information '''

        try:
            pipe = open(filename, 'w')
        except IOError:
            pipe = stdout

        pipe.write('regions\n')
        for region in self.regions:
            pipe.write('==> {0}\n'.format(region))

        pipe.write('configuration\n')
        for key, value in self.config.items('aws'):
            pipe.write('==> {0}: {1}\n'.format(key, value))

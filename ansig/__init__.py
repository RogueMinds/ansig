from argparse import ArgumentParser
from os import environ

from ansig.generator import Generator

__version__ = '0.2.0'


def load(filename=None):
    ''' Dynamic inventory generator loader function '''

    parser = ArgumentParser(
        version=u'%(prog)s ' + __version__,
        description=u'Dynamic inventory generator for Ansible.')
    parser.add_argument(
        '--list', action='store_true', dest='list',
        help='generates a list of available hosts and their metadata')
    parser.add_argument(
        '--host', action='store', dest='host',
        help='generates all the metadata for a specific host')
    parser.add_argument(
        '--debug', action='store_true', dest='log_file',
        default=environ.get('ANSIG_DEBUG'),
        help='enable debugging to file')
    args = parser.parse_args()

    generator = Generator(filename)
    if args.list:
        generator.generate_host_list()
    elif args.host:
        generator.generate_host_info(args.host)
    if args.log_file:
        generator.generate_debug_info(args.log_file)

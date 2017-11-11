import unittest
from os import path

from ansig.configurator import ConfigParser


class TestConfigParser(unittest.TestCase):
    def setUp(self):
        self.rootdir = path.abspath(path.dirname(path.dirname(__file__)))

    def test_default_values(self):
        config = ConfigParser()
        self.assertEquals(
            config.get('aws', 'regions'), u'all')

    def test_custom_values(self):
        filename = path.join(self.rootdir, 'contrib/ansig/config.ini')
        config = ConfigParser(filename=filename)
        self.assertEquals(
            config.get('aws', 'regions'), u'us-east-1')

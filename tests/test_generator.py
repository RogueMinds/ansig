import unittest
from os import path

from ansig.generator import Generator


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.rootdir = path.abspath(path.dirname(path.dirname(__file__)))

    def test_default_generator(self):
        generator = Generator()
        self.assertEquals(
            generator.regions, [])

    def test_configured_generator(self):
        filename = path.join(self.rootdir, 'contrib/ansig/config.ini')
        generator = Generator(filename=filename)
        self.assertEquals(
            generator.regions, [u'us-east-1'])

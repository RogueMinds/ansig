import unittest
import ansig


class TestMain(unittest.TestCase):
    def test_version_semver(self):
        self.assertRegexpMatches(
            ansig.__version__, r'^(?:(\d+)\.)?(?:(\d+)\.)?(\*|\d+)$')

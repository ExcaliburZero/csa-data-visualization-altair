"""
This module contains a test for ensuring that the plot weboage can be generated.
"""
import unittest

from csadatavis.__main__ import main

class ScriptTests(unittest.TestCase):

    def test_script(self) -> None:
        """
        Runs the plot generation script to makesurethat it does not crash due
        to thrown exceptions.
        """
        main()


#-*- coding: utf-8 -*-
import os
import test_NoseXUnitLite

import nosexunitlite.tools as ntools
import nosexunitlite.excepts as nexcepts

class TestFileName(test_NoseXUnitLite.PluginTestCase):
    
    def setUpCase(self):
        content = """
class TestFileName(object):
    def test(self): yield self._test_body, '/toto.\\tata.tutu.bug'
    def _test_body(self, path): pass
"""
        test = test_NoseXUnitLite.Module('test_file_name', content)
        test.save(self.source)
        self.suitepath = self.source
        self.setUpCore(self.core_target, self.source)

    def test(self):
        self.assertWasSuccessful()
        self.assertExists(os.path.join(self.core_target, 'TEST-test_file_name.xml'))

if __name__=="__main__":
    test_NoseXUnitLite.main()


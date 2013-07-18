#-*- coding: utf-8 -*-
import os
import test_NoseXUnitLite

import nosexunitlite.tools as ntools

class TestSaveLoad(test_NoseXUnitLite.TestCase):
    
    def test_sanity(self):
        content = """hello
        how are you ?
        """
        path = os.path.join(self.work, 'foo.dat')
        ntools.save(content, path)
        found = ntools.load(path)
        self.assertEquals(content, found)

if __name__=="__main__":
    test_NoseXUnitLite.main()

#-*- coding: utf-8 -*-
import os
import test_NoseXUnitLite

import nosexunitlite.tools as ntools
import nosexunitlite.excepts as nexcepts

class TestClean(test_NoseXUnitLite.TestCase):
    
    def test_no_option(self):
        test_NoseXUnitLite.File('foo.py').save(self.source)
        ntools.clean(self.source)
        self.assertEquals([], os.listdir(self.source))

    def test_prefix_check(self):
        test_NoseXUnitLite.File('TEST-foo.py').save(self.source)
        ntools.clean(self.source, prefix='TEST-')
        self.assertEquals([], os.listdir(self.source))

    def test_prefix_no_check(self):
        test_NoseXUnitLite.File('foo.py').save(self.source)
        ntools.clean(self.source, prefix='TEST-')
        self.assertEquals(['foo.py', ], os.listdir(self.source))

    def test_ext_check(self):
        test_NoseXUnitLite.File('foo.py').save(self.source)
        ntools.clean(self.source, ext='py')
        self.assertEquals([], os.listdir(self.source))

    def test_ext_no_check(self):
        test_NoseXUnitLite.File('foo.py').save(self.source)
        ntools.clean(self.source, ext='dat')
        self.assertEquals(['foo.py', ], os.listdir(self.source))
        
    def test_all(self):
        test_NoseXUnitLite.File('TEST-foo_1.py').save(self.source)
        test_NoseXUnitLite.File('TEST-foo_2.dat').save(self.source)
        test_NoseXUnitLite.File('foo_3.py').save(self.source)
        test_NoseXUnitLite.File('foo_4.dat').save(self.source)
        ntools.clean(self.source, prefix='TEST-', ext='dat')
        self.assertSet(['TEST-foo_1.py', 'foo_3.py', 'foo_4.dat', ], os.listdir(self.source))

if __name__=="__main__":
    test_NoseXUnitLite.main()

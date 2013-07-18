#-*- coding: utf-8 -*-
import os
import test_NoseXUnitLite

import nosexunitlite.tools as ntools

class TestPackages(test_NoseXUnitLite.TestCase):
    
    def test_package(self):
        p = test_NoseXUnitLite.Package('foo').save(self.source)
        expected = {'foo': p.path(), }
        self.assertEquals(expected, ntools.packages(self.source, search=False, exclude=[]))
        
    def test_module(self):
        m = test_NoseXUnitLite.Module('foo').save(self.source)
        expected = {'foo': m.path(), }
        self.assertEquals(expected, ntools.packages(self.source, search=False, exclude=[]))

    def test_package_module(self):
        p = test_NoseXUnitLite.Package('foo_1')
        m = test_NoseXUnitLite.Module('foo_2')
        p.append(m)
        p.save(self.source)
        expected = {p.full(): p.path(),
                    m.full(): m.path(), }
        self.assertEquals(expected, ntools.packages(self.source, search=True, exclude=[]))

    def test_search(self):
        f = test_NoseXUnitLite.Folder('folder')
        m = test_NoseXUnitLite.Module('foo')
        f.append(m)
        f.save(self.source)
        expected = {m.desc(): m.path(), }
        self.assertEquals(expected, ntools.packages(self.source, search=True, exclude=[]))

    def test_no_search(self):
        f = test_NoseXUnitLite.Folder('folder')
        m = test_NoseXUnitLite.Module('foo')
        f.append(m)
        f.save(self.source)
        self.assertEquals({}, ntools.packages(self.source, search=False, exclude=[]))

    def test_exclude(self):
        f = test_NoseXUnitLite.Folder('CVS')
        m = test_NoseXUnitLite.Module('foo')
        f.append(m)
        f.save(self.source)
        self.assertEquals({}, ntools.packages(self.source, search=True, exclude=['CVS', ]))
    
    def test_double(self):
        f = test_NoseXUnitLite.Folder('folder')
        m_1 = test_NoseXUnitLite.Module('foo')
        f.append(m_1)
        f.save(self.source)
        m_2 = test_NoseXUnitLite.Module('foo').save(self.source)
        expected = {m_2.desc(): m_2.path(), }
        self.assertEquals(expected, ntools.packages(self.source, search=True, exclude=[]))      
    
if __name__=="__main__":
    test_NoseXUnitLite.main()

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:08:53 2019

@author: kuifenhu
"""

class A():  # deriving from 'object' declares A as a 'new-style-class'
    def foo(self):
        print( "foo")
    def test(self):
        self.a=B()
        self.a.foo()

class B(A):
    def foo(self):
        super(B, self).foo()   # calls 'A.foo()'
A1=A()
A2=B()
A2.foo
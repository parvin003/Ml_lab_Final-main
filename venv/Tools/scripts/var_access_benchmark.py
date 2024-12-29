from collections import deque, namedtuple
from timeit import Timer

trials = [None] * 500
steps_per_trial = 25

class A(object):
    def m(self):
        pass

class B(object):
    __slots__ = 'x'
    def __init__(self, x):
        self.x = x

class C(object):
    def __init__(self, x):
        self.x = x

def read_local(trials=trials):
    v_local = 1
    for t in trials:
        v_local; v_local; v_local; v_local; v_local
        v_local; v_local; v_local; v_local; v_local
        v_local; v_local; v_local; v_local; v_local
        v_local; v_local; v_local; v_local; v_local
        v_local; v_local; v_local; v_local; v_local

def make_nonlocal_reader():
    v_nonlocal = 1
    def inner(trials=trials):
        for t in trials:
            nonlocal v_nonlocal
            v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal
            v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal
            v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal
            v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal
            v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal; v_nonlocal
    inner.__name__ = 'read_nonlocal'
    return inner

read_nonlocal = make_nonlocal_reader()

v_global = 1
def read_global(trials=trials):
    for t in trials:
        v_global; v_global; v_global; v_global; v_global
        v_global; v_global; v_global; v_global; v_global
        v_global; v_global; v_global; v_global; v_global
        v_global; v_global; v_global; v_global; v_global
        v_global; v_global; v_global; v_global; v_global

def read_builtin(trials=trials):
    for t in trials:
        oct; oct; oct; oct; oct
        oct; oct; oct; oct; oct
        oct; oct; oct; oct; oct
        oct; oct; oct; oct; oct
        oct; oct; oct; oct; oct

def read_classvar_from_class(trials=trials, A=A):
    A.x = 1
    for t in trials:
        A.x; A.x; A.x; A.x; A.x
        A.x; A.x; A.x; A.x; A.x
        A.x; A.x; A.x; A.x; A.x
        A.x; A.x; A.x; A.x; A.x
        A.x; A.x; A.x; A.x; A.x

def read_classvar_from_instance(trials=trials, A=A):
    A.x = 1
    a = A()
    for t in trials:
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x

def read_instancevar(trials=trials, a=C(1)):
    for t in trials:
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x

def read_instancevar_slots(trials=trials, a=B(1)):
    for t in trials:
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x

def read_namedtuple(trials=trials, D=namedtuple('D', ['x'])):
    a = D(1)
    for t in trials:
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x

def read_boundmethod(trials=trials, a=A()):
    for t in trials:
        a.m; a.m; a.m; a.m; a.m
        a.m; a.m; a.m; a.m; a.m
        a.m; a.m; a.m; a.m; a.m
        a.m; a.m; a.m; a.m; a.m
        a.m; a.m; a.m; a.m; a.m

def write_local(trials=trials):
    v_local = 1
    for t in trials:
        v_local = 1; v_local = 1; v_local = 1; v_local = 1; v_local = 1
        v_local = 1; v_local = 1; v_local = 1; v_local = 1; v_local = 1
        v_local = 1; v_local = 1; v_local = 1; v_local = 1; v_local = 1
        v_local = 1; v_local = 1; v_local = 1; v_local = 1; v_local = 1
        v_local = 1; v_local = 1; v_local = 1; v_local = 1; v_local = 1

def make_nonlocal_writer():
    v_nonlocal = 1
    def inner(trials=trials):
        nonlocal v_nonlocal
        for t in trials:
            v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1
            v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1
            v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1
            v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1
            v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1; v_nonlocal = 1
    inner.__name__ = 'write_nonlocal'
    return inner

write_nonlocal = make_nonlocal_writer()

def write_global(trials=trials):
    global v_global
    for t in trials:
        v_global = 1; v_global = 1; v_global = 1; v_global = 1; v_global = 1
        v_global = 1; v_global = 1; v_global = 1; v_global = 1; v_global = 1
        v_global = 1; v_global = 1; v_global = 1; v_global = 1; v_global = 1
        v_global = 1; v_global = 1; v_global = 1; v_global = 1; v_global = 1
        v_global = 1; v_global = 1; v_global = 1; v_global = 1; v_global = 1

def write_classvar(trials=trials, A=A):
    for t in trials:
        A.x = 1; A.x = 1; A.x = 1; A.x = 1; A.x = 1
        A.x = 1; A.x = 1; A.x = 1; A.x = 1; A.x = 1
        A.x = 1; A.x = 1; A.x = 1; A.x = 1; A.x = 1
        A.x = 1; A.x = 1; A.x = 1; A.x = 1; A.x = 1
        A.x = 1; A.x = 1; A.x = 1; A.x = 1; A.x = 1

def write_instancevar(trials=trials, a=C(1)):
    for t in trials:
        a.x = 1; a.x = 1; a.x = 1; a.x = 1; a.x = 1
        a.x = 1; a.x = 1; a.x = 1; a.x = 1; a.x
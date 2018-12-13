from test import world


def d(f):
    def warp():
        f()
        print("hello")
    return warp


@d
def world1():
    world()

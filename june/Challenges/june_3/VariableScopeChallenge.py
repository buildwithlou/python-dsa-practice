x = "global"


def outer():
    x = "enclosing"

    def inner():
        nonlocal x
        x = "modified by inner"
        print("inner: ", x)

    inner()

    print("outer:", x)


x = " modified by outer"
outer()
print("module:", x)

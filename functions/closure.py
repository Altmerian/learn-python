def closure(msg):

    def inner():
        msg2 = 'World'
        print(msg, msg2)

        print(locals())
        print(globals())

    return inner


f = closure("Hello")

f()

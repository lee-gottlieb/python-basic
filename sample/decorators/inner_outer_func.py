def outer():
    def inner():
        print("Inner function")
    return inner

# style 1
# outer()

# style 2
func = outer()
func()



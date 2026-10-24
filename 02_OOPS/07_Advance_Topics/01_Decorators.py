def extragreeting(func):
    def wrapper():
        print("Good Morning")
        func()
    return wrapper


@extragreeting
def greeting():
    print("Hey How are you?")


greeting()

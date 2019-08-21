class MusicPlayer(object):

    """ Use a class attribute "instance" to record whether the system has created a new object,
    if the system has create a object, then return the first object's address in order to singleton
    model. if not, assign this object's address to this class attribute.

    Use other class attribute "judgement" and use if statement to judge whether the system has excess the init method, if system had
    invoked this method
    """

    instance = None
    judgement = False

    # Notice: There are another method to achieve this function
    # def __init__(self):
    # if MusicPlayer.judgement:
    #    return
    # MusicPlayer.judgement = True
    # print("已经创建了该对象")

    def __init__(self):
        if not MusicPlayer.judgement:
            print("已经创建了该对象")
            MusicPlayer.judgement = True

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance





music1 = MusicPlayer()
music2 = MusicPlayer()

print(music1)
print(music2)
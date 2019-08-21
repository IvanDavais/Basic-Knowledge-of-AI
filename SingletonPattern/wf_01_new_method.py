class MusicPlayer(object):

    def __init__(self):
        print("初始化音乐播放对象！")

    def __new__(cls, *args, **kwargs):
        print("看看会不会调用这句话！")
        instance = super().__new__(cls)
        return instance


my_music = MusicPlayer()
print(my_music)
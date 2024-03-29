class Video:
    def __init__(self):
        self.name = None

    def create(self, name):
        self.name = name

    def play(self):
        print(f'Playing video {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        return cls.videos[video_indx].play()


v1 = Video()
v2 = Video()
v1.create("Python_1")
v2.create("Python_2")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)

class Video:
    def __init__(self, name):
        self.name = name

    def create(self, name):
        self.name = name

    def play(self):
        print(f'воспроизведение видео {self.name}')


class YouTube:
    @classmethod
    def add_video(cls, video):
        cls.video = video


    @classmethod
    def play(cls, video_indx):
        print ((()))



v1 = Video()
v1.create("Python")

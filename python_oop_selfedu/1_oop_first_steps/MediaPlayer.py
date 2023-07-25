# https://stepik.org/lesson/701974/step/5?unit=702075

class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Playing {self.filename.capitalize()}")


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play()
media2.play()
class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if app.name not in [x.name for x in self.apps]:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self, name='Вконтакте'):
        self.name = str(name)


class AppYouTube:
    def __init__(self, name='YouTube', memory_max=1024):
        self.name = str(name)
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, name='Phone', phone_list=[]):
        self.name = str(name)
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)

class AppStore:

    def __init__(self):
        self.apps = {}

    def add_application(self, app):
        self.apps[id(app)] = app

    def remove_application(self, app):
        self.apps.pop(id(app))

    def block_application(self, app):
        self.apps[id(app)].blocked = True

    def total_apps(self):
        return len(self.apps)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked



class RenderList:
    def __init__(self, type_list='ul'):
        if type_list == 'ol':
            self.type_list = type_list
        else:
            self.type_list = 'ul'

    def __call__(self, lst, *args, **kwargs):
        list_items = ['<li>' + item + '</li>' for item in lst]
        html = f'<{self.type_list}>\n' + '\n'.join(list_items) + f'\n</{self.type_list}>'
        return html


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
def say_name(name):
    def say_goodbye():
        print("Don't say me goodbye, " + name + "!")

    return say_goodbye


f_1 = say_name('Name_1')
f_2 = say_name('Name_2')
f_1()
f_2()
#!/usr/bin/env python3
'''command line interface'''


class Command:
    def __init__(self, prompt=">", intro="", command_list={}, logout=""):
        self.prompt = prompt
        self.intro = intro
        self.command_list = command_list
        self.logout = logout
        self.spawn()

    def spawn(self):
        print(self.intro)

    def do(self):
        line = input(self.prompt)
        ''' string.split will be soon replaced by regex '''
        try:
            (command, args) = line.split(" ", 1)
        except:
            command = line
            args = None
        if command in self.command_list:
            self.command_list[command](args)
            return True
        elif command == "quit":
            self.quit()
        else:
            print("Command not found")
            return True

    def quit(self):
        print(self.logout)
        return False

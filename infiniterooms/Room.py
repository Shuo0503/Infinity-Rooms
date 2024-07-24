class Room:
    def __init__(self, name):
        self.name = str(name)
        self.situation = False
        self.next = None
        self.previous = None

    def room_info(self):
        flag_string = "Flag" if self.situation == True else "No flag"
        return self.name + ", " + flag_string

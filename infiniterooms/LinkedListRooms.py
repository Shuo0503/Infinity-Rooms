from Room import Room


class LinkedListRooms:
    def __init__(self, n):
        previous_room = None
        self._first_room = None

        for i in range(n):
            r = Room(i+1)
            if previous_room != None:
                previous_room.next = r

            previous_room = r
            if self._first_room == None:
                self._first_room = r

        choice = int(input("Please choose a room from 1-" + str(n) + '\n'))
        self.current_room = self._first_room  # rooms[int(choice) - 1]

    def look(self):
        self.current_room.room_info()

    def move_next_room(self):
        if self.current_room.next != None:
            self.current_room = self.current_room.next
        else:
            print('You are in the last room')

    def move_previous_room(self):
        room = self._first_room
        if self.current_room == self._first_room:
            print("You're in the first room.")
            return
        while room != None:
            if room.next == self.current_room:
                self.current_room = room
                break
            room = room.next

    def flag_current_room(self):
        self.current_room.situation = not self.current_room.situation

    def print_all_flagged_rooms(self):
        room = self._first_room
        while room != None:
            if room.situation:
                room.room_info()
            room = room.next

    def set_room(self, room_name):
        room = self._first_room
        while room != None:
            if room.name == room_name:
                self.current_room = room
                break
            room = room.next

    def flip_all_flags(self):
        room = self._first_room
        while room != None:
            room.situation = not room.situation
            room = room.next
        print('All flags had been flapped.')

    def delete_room(self, room_name):
        room = self._first_room
        room_before = None
        while room != None:
            if room.name == room_name:
                room_before.next = room.next
                print(str(int(room_name)) + "room is deleted\n")
                return
            room_before = room
            room = room.next
        print("Can't find that room.")

    def print_first_flagged_room(self):
        room = self._first_room
        while room != None:
            if room.situation:
                room.room_info()
                break
            room = room.next

    def print_last_flagged_room(self):
        room = self._first_room
        last_flagged_room = None
        while room != None:
            if room.situation:
                last_flagged_room = room
            room = room.next

        if last_flagged_room is None:
            print("No room has been found.")
            return
        last_flagged_room.room_info()

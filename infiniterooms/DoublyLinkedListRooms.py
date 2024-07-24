from Room import Room


class DoublyLinkedListRooms:
    def __init__(self, n):
        # rooms = []
        previous_room = None
        self._first_room = None

        self._last_room = None
        # create array for rooms
        # for 1 ... n, add room to array
        r = None
        for i in range(n):
            r = Room(i + 1)
            if previous_room is not None:
                previous_room.next = r
                r.previous = previous_room
            # rooms.append(r)
            previous_room = r
            if self._first_room is None:
                self._first_room = r

        self._last_room = r

        choice = int(input("Please choose a room from 1-" + str(n) + '\n'))
        self.current_room = self._first_room  # rooms [int(choice) - 1]

    def look(self):
        return self.current_room.room_info()


    def move_next_room(self):
        if self.current_room.next is not None:
            self.current_room = self.current_room.next
        else:
            print('You are in the last room')

    def move_previous_room(self):
        if self.current_room.previous is not None:
            self.current_room = self.current_room.previous
        else:
            print('You are in the first room')

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
                return
            room = room.next

        print("Room not found")

    def flip_all_flags(self):
        room = self._first_room
        while room != None:
            room.situation = not room.situation
            room = room.next
        print('All flags had been flapped.')

    def delete_room(self, room_name):
        if self.current_room.name == room_name:
            print("You are in this room, cannot delete it.")
            return
        room = self._first_room
        while room != None:
            if room.name == room_name:
                room.previous.next = room.next
                room.next.previous = room.previous
                print(str(int(room_name)) + "room is deleted\n")
                return
            room = room.next
        print("Can't find that room.")

    def print_first_flagged_room(self):
        room = self._first_room
        while room != None:
            if room.situation:
                room.room_info()
                return
            room = room.next
        print("No room has been flagged.")

    def print_last_flagged_room(self):
        room = self._last_room
        while room != None:
            if room.situation:
                room.room_info()
                return
            room = room.previous
        print("No room has been flagged.")

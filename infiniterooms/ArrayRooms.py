from Room import Room


class ArrayRooms:
    def __init__(self, n):
        self.rooms = []
        # create array for rooms
        # for 1 ... n, add room to array
        for i in range(n):
            r = Room(i + 1)
            self.rooms.append(r)

        self.current_room_number = int(input("Please choose a room from 1-" + str(n) + '\n'))
        self.current_room = self.rooms[self.current_room_number - 1]

    def look(self):
        self.current_room.room_info()

    def move_next_room(self):
        if self.current_room_number < len(self.rooms)-2:
            self.current_room_number = self.current_room_number + 1
            self.current_room = self.rooms[self.current_room_number - 1]
        else:
            print('You are in the last room')

    def move_previous_room(self):
        if self.current_room_number >= 2:
            self.current_room_number = self.current_room_number - 1
            self.current_room = self.rooms[self.current_room_number - 1]
        else:
            print('You are in the first room')

    def flag_current_room(self):
        self.current_room.situation = not self.current_room.situation

    def print_all_flagged_rooms(self):
        for room in self.rooms:
            if room.situation:
                room.room_info()

    def set_room(self, room_number):
        for room in self.rooms:
            if room.name == room_number:
                self.current_room = room

    def flip_all_flags(self):
        for k in self.rooms:
            k.situation = not k.situation
        print("All rooms had been flipped.\n")

    def delete_room(self, room_name):
        if self.current_room.name == room_name:
            print("You are in this room, cannot delete it.")
            return

        for idx, room in enumerate(self.rooms):
            if room.name == room_name:
                self.rooms.pop(idx)
                print(str(room.name) + "room has deleted\n")
                return

        print("This room cannot be found.")

    def print_first_flagged_room(self):
        for j in self.rooms:
            if j.situation:
                j.room_info()
                break

    def print_last_flagged_room(self):
        j = len(self.rooms) - 1
        while j >= 0:
            r = self.rooms[j]
            j = j - 1
            if r.situation:
                r.room_info()
                break

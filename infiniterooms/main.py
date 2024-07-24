from ArrayRooms import ArrayRooms
from DoublyLinkedListRooms import DoublyLinkedListRooms
from LinkedListRooms import LinkedListRooms

n = 1000
# room_controller = ArrayRooms(n)
# room_controller = LinkedListRooms(n)
room_controller = DoublyLinkedListRooms(n)


def print_commands():
    print('''If you want to Look, press 1.
If you want to Go_next, press 2.
If you want to Go_back, press 3.
If you want to Flag, press 4.
If you want to check all flagged room, press 5.
If you want to go to a specific room, press 6.
If you want to flip all flags, press 7.
If you want to delete a room, press 8.
If you want to Quit, press 9.
If you want to print first flagged room, press 10.
If you want to print last flagged room, press 11.
If you need help, input 'help'.
''')


def get_input():
    input_string = input('Please choose your command\n').lower()
    # print(input_string)
    return input_string

print_commands()



# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Assignment 12")
# Set geometry (widthxheight)
root.geometry('350x200')

# all widgets will be here
# adding a label to the root window

lbl = Label(root, text = room_controller.look())
lbl.grid()

# function to display text when button is clicked
def clicked_backward():
    room_controller.move_previous_room()
    lbl.configure(text = room_controller.look())

# button widget with red color text inside
previous_button = Button(root, text = "move forward", fg = "red", command = clicked_backward)
# set Button grid
previous_button.grid(column = 0, row = 1)


def clicked_next():
    room_controller.move_next_room()
    lbl.configure(text = room_controller.look())

# button widget with red color text inside
next_button = Button(root, text = "move next",
             fg = "red", command = clicked_next)
# set Button grid
next_button.grid(column = 1, row = 1)

# Execute Tkinter
root.mainloop()

# while True:
    # command = get_input()
    #
    # if command == '1':
    #     room_controller.look()
    # elif command == '2':
    #     room_controller.move_next_room()
    #     room_controller.look()
    # elif command == '3':
    #     room_controller.move_previous_room()
    #     room_controller.look()
    # elif command == '4':
    #     room_controller.flag_current_room()
    #     room_controller.look()
    # elif command == '5':
    #     room_controller.print_all_flagged_rooms()
    # elif command == '6':
    #     s_room = input('Please input the room you want go:\n')
    #     room_controller.set_room(s_room)
    #     room_controller.look()
    # elif command == '7':
    #     room_controller.flip_all_flags()
    # elif command == '8':
    #     d_room = input('Please input the room you want delete:\n')
    #     room_controller.delete_room(d_room)
    # elif command == '9' or command == 'quit':
    #     quit()
    # elif command == "10":
    #     room_controller.print_first_flagged_room()
    # elif command == "11":
    #     room_controller.print_last_flagged_room()
    # elif command == "help":
    #     print_commands()
    # else:
    #     print("Sorry,I don't understand")#
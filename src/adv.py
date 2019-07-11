from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


player = Player("Will", room['outside'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# def print_room(room):
#     current_room = player.current_room
#     print(f"\n-------------------------------")
#     print(f"{room.title}")
#     print(f"\n  {room.description}\n")

# current_room = player.current_room
# print_room(current_room)

# while True:
#     # Print the current room title and description
#     current_room = player.current_room
#     # Wait for user input
#     cmd = input("-> ")
#     #parse user inputs (n, s, e, w, q)
#     if cmd == "n":
#         if current_room.n_to is not None:
#             player.current_room = current_room.n_to
#             print_room(player.current_room)
#         else:
#             print("You cannot go that way")
#     elif cmd == "s":
#         if current_room.s_to is not None:
#             player.current_room = current_room.s_to
#             print_room(player.current_room)
#         else:
#             print("You cannot go that way")
#     elif cmd == "w":
#         if current_room.w_to is not None:
#             player.current_room = current_room.w_to
#             print_room(player.current_room)
#         else:
#             print("You cannot go that way")
#     elif cmd == "e":
#         if current_room.e_to is not None:
#             player.current_room = current_room.e_to
#             print_room(player.current_room)
#         else:
#             print("You cannot go that way")
#     elif cmd == "q":
#         print("Goodbye")
#         break
#     else:
#         print("Not a valid command")
#     # If input is valid, move the player and loop



rock = Item("Rock", "This is a rock.")
pencil = Item("Pencil", "this is a Pencil.")
sandwich = Item("Sandwich", "This is a delicious sandwich")

player = Player("Brady", room['outside'])


current_room = player.current_room

print(current_room)

valid_directions = ["n", "s", "e", "w"]

while True:
    # Wait for user input
    cmd = input("-> ")
    # Parse user inputs (n, s, e, w, q)
    if cmd in valid_directions:
        # If input is valid, move the player and loop
        player.travel(cmd)
    elif cmd == "q":
        print("Goodbye!")
        exit()
    else:
        print("I did not recognize that command")

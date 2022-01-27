# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ron")
define g = Character("You", color="#ffffff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene small_apartment_kitchen_night

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ron guy

    # These display lines of dialogue.

    "It was a normal evening for Ron. He had just had his daily 5 hour long League of Legend gaming session."

    init python:
        import os
     
        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            player = os.environ.get(name)

    "Hello there, [player]."

    r "WHO ARE YOU??!?!"

    g "I am god>><<<><>> OooHhoooo."

    r "Here's a {glitch=1.1}{color=#0f0}{b}Glitch{/b}{/color} Tag wooohoo{/glitch}"

    scene black bg
    with Dissolve(.5)

    pause 5

    scene small_apartment_kitchen_night
    show ron guy
    with Dissolve(.5)
 

    # This ends the game.

    return

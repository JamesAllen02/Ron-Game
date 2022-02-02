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

    scene ron_room:
            zoom 1.65

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ron guy

    python:
        size = ["obese", "chunky", "tubby", "normal", "anoreksia", "thin", "muscular"]


    # These display lines of dialogue.

    "You see a dark room. In the corner, there's a [size[1]] shadow sitting in the corner on a chair."
    "Ron is sitting by his desk. He is currently playing League of Legends."

    "Choose dialogue"

    menu:

        "Hello, Ron.":
            jump choice1_1

        "":
            jump choice1_2

        "Hey, could you tell me what's going on?":
            jump choice1_3


    label choice1_1:

        $ menu_flag = True

        "Ron stops playing. He wasn't wearing a headset and is wondering where the sound came from."
        r "Hello? Who said that?"

        jump choices_done

    label choice1_2:

        $ menu_flag = False

        "Ron stops playing. He wasn't wearing a headset and is wondering where the sound came from."
        r ""

        jump choices_done

    label choice1_3:

        $ menu_flag = False

        "Ron stops playing. He wasn't wearing a headset and is wondering where the sound came from."
        "He looks around, confused, trying to "
        r "Umm, hello? "

        jump choices_done

    label choices_done:

        ""








    menu:

        "":
            jump choice2_yes

        "":
            jump choice2_no

    label choice2_yes:

        $ menu_flag = True

        #"Ron kutter av seg armen og Begynner å skrike som en galning. Men spilleren får muligheten til å klikke på armen hans med musepilen så den regenererer."

        ""


        jump choice2_done

    label choice2_no:

        $ menu_flag = False

        ""

        jump choice2_done

    label choice2_done:

    r ""

    menu:

        "":
            jump choice3_yes

        "":
            jump choice3_no

    label choice3_yes:

        $ menu_flag = True

    r   ""

    jump choice3_done

    label choice3_no:

        $ menu_flag = False

    r   ""

    jump choice3_done

    label choice3_done:


    ""

        # ... the game continues here.







    menu:

        "":
            jump choice4_yes

        "":
            jump choice4_no

    label choice4_yes:

        $ menu_flag = True

    r   ""

    jump choice4_done

    label choice4_no:

        $ menu_flag = False

    r   ""


    jump choice4_done

    label choice4_done:

    ""




    menu:

        "":
            jump choice5_vase

        "":
            jump choice5_dog

    label choice5_vase:

        $ menu_flag = True

    r   ""


    jump choice5_done

    label choice5_dog:

        $ menu_flag = False

    r   ""

    jump choice5_done

    label choice5_done:

    menu:

        "Female":
            jump choice6_1

        "Male":
            jump choice6_2

        "Neither":
            jump choice6_3



    label choice6_1:

        $ menu_flag = True

        python:
            playerGender = "Female"
        r ""

        jump choices_done6

    label choice6_2:

        $ menu_flag = False

        python:
            playerGender = "Male"
        r ""

        jump choices_done6

    label choice6_3:

        $ menu_flag = False

        python:
            playerGender = "Neither"

        g ""
        r ""

        jump choices_done6

    label choices_done6:


        r   ""

        menu:

            "":
                jump choice7_one

            "":
                jump choice7_two

    label choice7_one:

        $ menu_flag = True

        r   ""
        r   ""
        r   ""



    jump choice7_done

    label choice7_two:

        $ menu_flag = False

        r   ""
        r   ""
        r   ""
        r   ""
        r   ""
        r   ""



    ""


    menu:

        "":
            jump choice8_one

        "":
            jump choice8_two

        "":
            jump choice8_three



    label choice8_one:

        $ menu_flag = True

        r   ""


    jump choice8_done

    label choice8_two:

        $ menu_flag = False

        r   ""

        ""

        jump choice10_done

    label choice8_three:

        $ menu_flag = False

        r   ""

        ""

        jump choice10_done

    label choice8_done:

        menu:

            "":
                jump choice9_one

            "":
                jump choice9_two


    label choice9_one:

        $ menu_flag = True

        r   ""

        ""

    jump choice9_done

    label choice9_two:

        $ menu_flag = False

        r   ""

        ""

        jump choice9_done

    label choice10_done:
    label choice9_done:

        ""

return

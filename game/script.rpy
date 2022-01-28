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

    menu:

        "Good day Ron!":
            jump choice1_1

        "Hi Ron!":
            jump choice1_2

        "What the fuck is up Ron?":
            jump choice1_3
                
                

    label choice1_1:

        $ menu_flag = True

        r "What the fuck?"

        jump choices_done

    label choice1_2:

        $ menu_flag = False

        r "What the fuck?"

        jump choices_done

    label choice1_3:

        $ menu_flag = False

        r "What the fuck?"

        jump choices_done

    label choices_done:
        
        "Ron går bort til døra, han åpner."

        r "Hello?"

        g "RON!!"

        r "OUAAAAA, shut up! Am i high? Am i dreaming?"

        r "If im dreaming im probably gonna wake up if i kut my arm off, haha motherfuckers."








    menu:

        "Haha! Do it you pussy!":
            jump choice2_yes

        "No! Dont do it! This is not a dream!":
            jump choice2_no

    label choice2_yes:

        $ menu_flag = True

        "Ron kutter av seg armen og Begynner å skrike som en galning. Men spilleren får muligheten til å klikke på armen hans med musepilen så den regenererer."

        jump choice2_done

    label choice2_no:

        $ menu_flag = False

        "Ron legger vekk kniven, Men er fortsatt i sjokk"

        jump choice2_done

    label choice2_done:

    r "This cant be! Who are you? Am i crazy?"





 
    menu:

        "Yeah! You fucking lunatic!":
            jump choice3_yes

        "No! I am god!":
            jump choice3_no

    label choice3_yes:

        $ menu_flag = True

    r   "I knew it! I knew i was loosing my mind! HAHA!" 
    r   "No wait" 
    r   "crazy people doesnt know they are crazy do they?"
    r   "Ive never heard of anybody sayin “The voice in mye head is telling me i am crazy!" 
    r   "And if i knew i was crazy! I wouldnt be crazy!" 
    r   "But who are you then?"
    r   "You must be, you are God!"

    jump choice3_done

    label choice3_no:

        $ menu_flag = False

    r   "I knew it!" 
    r   "Actually i didnt" 
    r   "but"
    r   "now I know" 
    r   "you are fucking God!" 
    r   "Sorry"
    r   "no more swearing"
    r   "Fuck"

    jump choice3_done

    label choice3_done:

    "ron jubler"

    r "But does that mean. Am i the mesiah? Am i the motherfucking new mesiah of the 21st century?"

        # ... the game continues here.






 
    menu:

        "Ehm, yeah! Sure, The messia! Fuck yeah!":
            jump choice4_yes

        "No you are just Ron!":
            jump choice4_no

    label choice4_yes:

        $ menu_flag = True

    r   "Fuck yeah!" 
    r   "Im gonna turn so much water in to wine!" 
    r   "Im gonna run on that fucking water!"
    r   "And proooobably" 
    r   "loose my virginity" 
    r   "No more porn for Ron"
    r   "HAHA!"
    r   "But lets not get to haisty."

    jump choice4_done

    label choice4_no:

        $ menu_flag = False

    r   "Thats exactly what God would say to the messia!" 
    r   "“blah blah, first and foremost you are a human blah blah”" 
    r   "Yeeess dude!"


    jump choice4_done

    label choice4_done:

    "Ron stopper opp og tenker."
    r   "What does a Messiah do exactly?" 
    r   "Do i have to get nailed to wood and get tortured and shit? " 
    r   "Because im not really feeling all of that you know!"
    r   "But im suuper down with all of that magic and shit!" 
    r   "By the way" 
    r   "my mom told me not to trust strangers and shit"
    r   "and you know"
    r   "i’ve never really been a praying type of guy"

    r   "So i’ve never really spoken to you." 
    r   "So i was just wondering if you could give me some type of sign" 
    r   "just so i know im not crazy and stuff."




    menu:

        "Spilleren kan trykke på en vase så den faller ned og knuser.":
            jump choice5_vase

        "Spillern kan trykke på hunden til Ron som sitter i hjørnet så den dør.":
            jump choice5_dog

    label choice5_vase:

        $ menu_flag = True

    r   "What the fuck man?" 
    r   "Thats my favorite vase!" 
    r   "Yeah yeah"
    r   "i guess you’re real anyways." 


    jump choice5_done

    label choice5_dog:

        $ menu_flag = False

    r   "Whoooahh" 
    r   "cool!" 
    r   "Haha!"
    r   "You killed my dog man! "
    r   "Good for him!"
    r   "Now he’s probably up in heavan with you"
    r   "sitting on your lap or some shit!"
    r   "You’re a nice guy god"
    r   "Or girl"
    r   "or whatever"
    r   "What are you by the way?"



    jump choice5_done

    label choice5_done:

    "ferdig"

return







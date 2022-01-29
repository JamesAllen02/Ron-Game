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
        
        "Ron walks over to the door and opens it."

        r "Hello?"

        g "RON!!"

        r "OUAAAAA, shut up! Am I high? Am I dreaming?"

        r "If I'm dreaming, I'm probably gonna wake up if I cut my arm off."
        r "Haha motherfuckers!"








    menu:

        "Haha! Do it you pussy!":
            jump choice2_yes

        "No! Don't do it! This is not a dream!":
            jump choice2_no

    label choice2_yes:

        $ menu_flag = True

        #"Ron kutter av seg armen og Begynner å skrike som en galning. Men spilleren får muligheten til å klikke på armen hans med musepilen så den regenererer."
        
        "Ron cuts of his arm."

        "He starts to scream like a lunatic."

        "Click on his arm to regenerate it.."

        "OR"

        "Don't"


        jump choice2_done

    label choice2_no:

        $ menu_flag = False

        "Ron puts the knife away, but is still in shock."

        jump choice2_done

    label choice2_done:

    r "This can't be! Who are you? Am I crazy?"

    menu:

        "Yeah, you fucking lunatic!":
            jump choice3_yes

        "No. I am god!":
            jump choice3_no

    label choice3_yes:

        $ menu_flag = True

    r   "I knew it! I knew I was loosing my mind! HAHA!" 
    r   "No, wait.." 
    r   "Crazy people doesn't know they are crazy do they?"
    r   "I've never heard of anybody sayin' “The voice in my head is telling me I am crazy!" 
    r   "And if I knew I was crazy, I wouldn't be crazy!" 
    r   "But who are you, then?"
    r   "You must be... you are God!"

    jump choice3_done

    label choice3_no:

        $ menu_flag = False

    r   "I knew it!" 
    r   "Actually, I didnt." 
    r   "But..."
    r   "Now I know." 
    r   "You are fucking God!" 
    r   "Sorry..."
    r   "No more swearing."
    r   "Fuck."

    jump choice3_done

    label choice3_done:


    "Ron cheers."

    r "But does that mean... am I the messiah? Am I the motherfucking new messiah of the 21st century?"

        # ... the game continues here.






 
    menu:

        "Ehm, yeah! Sure, The messiah! Fuck yeah!":
            jump choice4_yes

        "No, you are just Ron!":
            jump choice4_no

    label choice4_yes:

        $ menu_flag = True

    r   "Fuck yeah!" 
    r   "I'm gonna turn so much water into wine!" 
    r   "I'm gonna run on the fucking water!"
    r   "And proooobably" 
    r   "lose my virginity!"
    r   "No more porn for Ron!"
    r   "HAHA!"
    r   "But let's not get too hasty."

    jump choice4_done

    label choice4_no:

        $ menu_flag = False

    r   "Thats exactly what God would say to the messiah!" 
    r   "“Blah blah, first and foremost you are a human, blah blah.”" 
    r   "Yeeess, dude!"


    jump choice4_done

    label choice4_done:

    "Ron suddenly stops and starts to think out loud."
    r   "What does a Messiah do, exactly?" 
    r   "Do I have to get nailed to wood and get tortured and shit? " 
    r   "Because I'm not really feeling all of that, you know!"
    r   "But I'm suuper down with all of that magic and shit!" 
    r   "By the way.." 
    r   "My mom told me not to trust strangers and shit,"
    r   "and you know.."
    r   "I’ve never really been a praying type of guy"
    r   "So I’ve never really spoken to you." 
    r   "So I was just wondering if you could give me some type of sign." 
    r   "Just so I know that I'm not crazy and stuff."




    menu:

        "Destroy a vase":
            jump choice5_vase

        "Kill the dog":
            jump choice5_dog

    label choice5_vase:

        $ menu_flag = True

    r   "What the fuck, man?" 
    r   "Thats my favorite vase!" 
    r   "Yeah, yeah"
    r   "I guess you’re real anyways." 
    r   "By the way, are you a girl or a boy or something like that?"


    jump choice5_done

    label choice5_dog:

        $ menu_flag = False

    r   "Whoooahh" 
    r   "Cool!" 
    r   "Haha!"
    r   "You killed my dog, man!"
    r   "Good for him!"
    r   "Now he’s probably up in heaven with you,"
    r   "sitting on your lap or some shit!"
    r   "You’re a nice guy, God"
    r   "Or girl"
    r   "or whatever"
    r   "What are you by the way?"



    jump choice5_done

    label choice5_done:

    menu:

        "Are you a gurrrrrl?":
            jump choice6_1

        "Are you a boiiiii?":
            jump choice6_2

        "Are you something else?":
            jump choice6_3
                
                

    label choice6_1:

        $ menu_flag = True

        python:
            playerGender = "girl"

        jump choices_done6

    label choice6_2:

        $ menu_flag = False

        python:
            playerGender = "boy"

        jump choices_done6

    label choice6_3:

        $ menu_flag = False

        python:
            playerGender = "Alien"

        jump choices_done6

    label choices_done6:
        
        r "Oh, so you're a [playerGender]"

return
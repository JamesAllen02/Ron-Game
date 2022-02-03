# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ron")
define g = Character("You", color="#ffffff")

image ron body dark = im.MatrixColor(
    "ron body.png", 
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))

image ron body mad dark = im.MatrixColor(
    "ron body mad.png", 
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))

image ron smile dark = im.MatrixColor(
    "ron smile.png", 
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene ron_room_dark:
        zoom 0.67
            
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    python:
        size = ["obese", "chunky", "tubby", "normal", "anoreksia", "thin", "muscular"]

    python:
        name = renpy.input("What is your name? \n", length=32)
        name = name.strip()
    
        if not name:
            name = "Sebastian"


        g = Character(name, color="#ffffff")



    # These display lines of dialogue.

    "You see a dark room. In the corner, there's a [size[1]] shadow sitting in the corner on a chair."
    "Ron is sitting by his desk. He is currently playing League of Legends."

    
    menu choice0:

        "Choose dialogue"
        "Hello, Ron.":
            jump choice1_1

        "Say nothing.":
            jump choice1_2

        "Hey, could you tell me what's going on?":
            jump choice1_3
                

    label choice1_1:

        $ menu_flag = True

        "Ron stops playing. He wasn't wearing a headset and is now wondering where the sound came from." 

        
        r "Hello? Who said that?"

        jump choices_done

    label choice1_2:

        "Ron continues to play his game."

        jump choice0



    label choice1_3:

        $ menu_flag = False

        "Ron stops playing. He wasn't wearing a headset and is now wondering where the sound came from."
        "He looks around, confused, trying to locate the source of the sound."
        r "Umm, hello! Did someone say something?"

        jump choices_done

    label choices_done:

        "Ron stands up."

        show ron body dark:
            xpos 0.4
            ypos 0.2
            zoom 0.35
        with Dissolve(.3)
            
            


        r "Seriously, who said that? Come out!"


    menu:

        "It was me.":
            jump choice2_yes

        "Say nothing":
            jump choice2_no

    label choice2_yes:

        $ menu_flag = True

        #"Ron kutter av seg armen og Begynner å skrike som en galning. Men spilleren får muligheten til å klikke på armen hans med musepilen så den regenererer."
        show ron body mad dark:
            xpos 0.4
            ypos 0.2
            zoom 0.35

        r "Who are you? And where are you?"

        menu:

            "[name]":
                jump choice2_11
            "God":
                jump choice2_12
            "Your worst nightmare.":
                jump choice2_13

        label choice2_11:
            r "Uh-- ok. Why can't I see you? And why can I hear you in my head?! Are you some kind of telepathic being?"
            show ron smile dark:
                xpos 0.4
                ypos 0.2
                zoom 0.35
            r "No, that's not real... I must be tired. I should probably go to bed early today."
            jump choice2_done

        label choice2_12:
            r "What the fuck? No, that can't be real. I must've stayed up too long. I should probably rest for a bit. There's no one here."
            jump choice2_done
        label choice2_13:
            r "That's really fucking creepy. Seriously, come out! I'm armed!"
            "Ron looks desperately around the room, clearly scared and shaken up. He's obviously not wielding any form of weapon."
            scene ron_room_dark:
                zoom 0.67
            show ron body dark:
                xpos 0.4
                ypos 0.2
                zoom 0.35
            pause 0.5
            scene ron_room:
                zoom 0.67
            show ron body:
                xpos 0.4
                ypos 0.2
                zoom 0.35
            pause 0.5
            scene ron_room_dark:
                zoom 0.67
            show ron body dark:
                xpos 0.4
                ypos 0.2
                zoom 0.35
            pause 0.5
            scene ron_room:
                zoom 0.67
            show ron body:
                xpos 0.4
                ypos 0.2
                zoom 0.35
            pause 0.5
            scene ron_room_dark:
                zoom 0.67
            show ron body dark:
                xpos 0.4
                ypos 0.2
                zoom 0.35
            

            
            g "Why do you lie to me, Ron?"
            r "What? How did you know..?"
            menu:
                "{sc=5}{font=FOT-PopJoyStd-B.otf}Punish Ron for his {font=FOT-PopJoyStd-B.otf}disobedience.{/sc}":
                    "Ron died."
                    "Game over."
            return

        jump choice2_done

    label choice2_no:

        $ menu_flag = False

        r "I guess it was nothing... I could've sworn someone said something. Maybe I'm going crazy."
        "Ron puts his headset on and goes back to playing his game."

        menu quietchoice1:

            "Remain quiet":
                jump quietchoice1
            "Say something":
                jump choice2_21
            "Turn the light on":
                jump choice2_22




        jump choice2_done

    label choice2_done:
        hide ron smile dark
        with dissolve(.5)
    "Ron lies down"
    r "Ok, ok, it's probably nothing. I'm just tired, that's all."

    menu:

        "Mess with ron":
            jump choice3_yes

        "Talk to ron":
            jump choice3_no

    label choice3_yes:

        $ menu_flag = True

        menu:
            "What do you do?"
            "Destroy his vase":
                "Ron sits up. He stares frightened towards the now broken vase."
                r "{i}fuck, what was that{/i}"
                #talk some more
                jump choice3_done
            "Change his \"art\"":
                r "Ron sits up and stares frightened towards his poster."
                "Ron whispers to himself"
                r "{i}What the fuck? I must be getting delusional{/i}"
                g "You're not delusional."
                r "Yes.. of course I am. This doesn't make any sense!"
                
                #talk some more

                jump choice3_done


    jump choice3_done

    label choice3_no:

        $ menu_flag = False

    g "Hey, Ron. Ignoring me won't work. I am real."
    r "No, you're not. You're just a figment of my wild imagination!"
    g "How can you be so certain about that?"
    r "I mean.. it just doesn't make any sense. That some kind of telepathic or omnipotent creature tries to contact me."
    r "And now I'm talking to myself... I need to sleep."

    menu:
        "Ron doesn't believe you"
        "Convince him by doing something to his room.":
            jump choice3_yes
        "Keep talking to him.":
            menu realChoice:
                "But I believe I am real. How could I convince you?":
                    r "Look, I don't know! Is there any way you can prove that you're real?"
                    jump choice3_yes
                    #block of code to run
                "Hey, Ron? Are you asleep?":
                    "Ron is pretending he can't hear you."
                    g "Ron?"
                    g "Hey, Roooon! Why are you ignoring me?"
                    r "Leave me alone! You're not real. Please.. just... be quiet."
                    g "Again, if that's what you really believe, then why am I here?"
                    r "What do you mean?"
                    g "If I wasn't real, and just a part of your imagination, then you couldn't realize that, right?"
                    r "I guess... but that means that if I believe in you, then you might not be real!"
                    g "Perhaps, but now you've already proven to be in doubt of it. That must mean something."
                    r "So you're saying that by not believing in you now, then you might be real?"
                    g "Ehh, I guess. It's a bit difficult to follow."
                    "Ron becomes quiet for a while, thinking to himself."
                    "After some time, he sits up, and starts to talk."
                    r "Actually, I completely forgot about this, but I used to have an imaginary friend when I was younger."
                    r "That was when I was really young. I think their name was..."
                    python:
                        import os
                        realName = os.environ.get('username')
                    r "[realName]"
                    r "Is... is that you?"
                    menu:
                        "Yes":
                            r "I knew it. Fuck, and I started to believe you were real."
                            "Ron went to sleep, ignoring anything that you might want to say."
                            #Lys på
                            "The next morning he wakes up, feeling more sane. He continues to play League of Legends, forgetting everything about you."
                            #Fade til svart
                            "Game Over."
                            menu:
                                "Start over":
                                    jump choice0
                                "Back to previous choice":
                                    jump realChoice
                                




    jump choice3_done

    label choice3_done:

    r "Ok... so you're real. You're really like a God."
    r "Jesus, fuck. Sorry, I need to take this in for a second."
    r "Fine, ok, you're real. You're God. You can do stuff."
    r "Wait, so am I like the messiah, then? Why have you chosen me?"

    menu:
        "Yes, you are the messiah":
            r "Yes, I fucking knew it. So am I here to spread your message or something?"
            r "You know what? I'm going to convince everyone that you're real!"
            r "Is that what you want me to do?"
            menu:
                "What do you want Ron to do?"
                "Spread the word of me. Tell everyone that I exist":
                    r "Sure!"
                    r "Umm, how do I do that?"
                    menu:
                        "With violence":
                            "Ron's facial expression immideately changes. He stays quiet for a while."
                            r "Ok. You got it."
                            "Ron opens the door and leaves."
                            "Some times passes."
                            "It's now midnight. Ron enters, covered in blood."
                            r "Hello? Are you here?"
                            g "Yes."
                            r "Oh, thank- you, I guess. I couldn't hear you outside. Anyways-"
                        "With love":
                            "Ron's face lights up."
                            r "Alright. You got it!"

                "No! Don't tell anyone that I exist.":
                    "temp"
                    # This branch can lead to a better life for Ron. He will try to better himself with your choices, as he tries to keep you secret
        "No, I'm just here to check in":
            r "Oh, I guess that makes more sense.. "




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
screen demomenu:
    add "gui/deserto_background.png"
    tag menu
    vbox:
        xalign 0.02
        yalign 0.1
        spacing 20
        imagebutton auto "images/menu/iniciar_%s.png" action ShowMenu("campanha") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        imagebutton auto "images/menu/ajuda_%s.png" action ShowMenu("helpdemo") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        imagebutton auto "images/menu/preferencias_%s.png" action ShowMenu("preferencesdemo") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        imagebutton auto "images/menu/sobre_%s.png" action ShowMenu("about") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        imagebutton auto "images/menu/sair_%s.png" action Quit(confirm=False) activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"











#screen depois de lcicar em load, preferencias e etc...
#imagebutton "images/general_background.png" focus_mask True action ShowMenu("help")    --TESTE Q TALVEZ DE PRA USAR--
screen preferencesdemo():
    add im.Scale("gui/base_deserto.jpg", 1920, 1080)
    tag menu
    hbox:
        xalign 0.97
        yalign 0.6
        spacing 15
        box_wrap True

        if renpy.variant("pc") or renpy.variant("web"):
             vbox:
                 style_prefix "radio"
                 label _("Display")
                 textbutton _("Window") action Preference("display", "window")
                 textbutton _("Fullscreen") action Preference("display", "fullscreen")



        vbox:
            style_prefix "check"
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")
            textbutton _("After Choices") action Preference("after choices", "toggle")
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))




        null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"

            vbox:

                label _("Text Speed")

                bar value Preference("text speed")

                label _("Auto-Forward Time")

                bar value Preference("auto-forward time")



            vbox:

                if config.has_music:
                    label _("Music Volume")

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("Sound Volume")

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    label _("Voice Volume")

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"



            vbox:  #texbutton voltar
                style_prefix "under"
                textbutton _("Voltar") action ShowMenu("demomenu") pos (-1750, 450)

    ##frame do canto
    vbox:
        #style_prefix "gm_nav"
        xalign 0.02
        yalign 0.2
        spacing 10

        textbutton _("Preferencia") action ShowMenu("preferencesdemo")
        textbutton _("Ajuda") action ShowMenu("helpdemo")
        #textbutton _("Save Game") action ShowMenu("save")
        #textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Sobre") action ShowMenu("about")


screen helpdemo:
    add im.Scale("gui/help.png", 1920, 1080)
    tag menu
    default device = "keyboard"
    #style_prefix "help"

    vbox:
        xalign 0.7
        yalign 0.5
        spacing 23

        hbox:
            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")


        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help



    ##frame do canto
    vbox:
        #style_prefix "gm_nav"
        xalign 0.02
        yalign 0.2
        spacing 10
        textbutton _("Preferencia") action ShowMenu("preferencesdemo")
        textbutton _("Ajuda") action ShowMenu("helpdemo")
        #textbutton _("Save Game") action ShowMenu("save")
        #textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Sobre") action ShowMenu("about")

        vbox:  #texbutton voltar
            style_prefix "under"
            textbutton _("Voltar") action ShowMenu("demomenu") pos (-06, 600)

screen campanha:
    add "images/background_prancheta_caps.png"
    add "images/campanha_idle.png" xalign 0.13 yalign 0.11
    #add "images/capitulos_hover.png" xalign 0.14 yalign 0.4
    tag menu
    vbox:
        xalign 0.14
        yalign 0.5
        spacing 150
        imagebutton auto "images/capitulos_%s.png" action ShowMenu("capitulos") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        imagebutton auto "images/voltar_%s.png" action [ Hide ("capitulos"), Show ("demomenu") ] activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"





screen capitulos:
    add "images/forma.png" xalign 0.5 yalign 0.2
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 10
        imagebutton auto "images/comece_%s.png" action Start("start") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

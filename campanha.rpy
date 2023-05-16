screen campanha:
    add "images/background_prancheta_caps.png"
    text"{size=+15} {font=NAPAV.ttf}CAMPANHA{/font}{/size}"xalign 0.1 yalign 0.12
    #add "images/campanha_idle.png" xalign 0.13 yalign 0.11
    #add "images/capitulos_hover.png" xalign 0.14 yalign 0.4
    tag menu
    vbox:
        xalign 0.14
        yalign 0.5
        spacing 150
        textbutton _("{size=+10}Capitulos{/size}")action ShowMenu("capitulos")xpos -40 ypos -30 activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/capitulos_%s.png" action ShowMenu("capitulos") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

        textbutton _("{size=+10}Voltar{/size}")action [ Hide ("capitulos"), Show ("demomenu") ]xpos -20 ypos -30 activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/voltar_%s.png" action [ Hide ("capitulos"), Show ("demomenu") ] activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"



##teste para o pull request q eu n to sabenod fazer ;-;
screen capitulos:
    add "images/forma.png" xalign 0.5 yalign 0.2
    add im.Scale("images/760446.jpg", 360, 260) xalign 0.5 yalign 0.21#imagem do primeiro capitulo
    vbox:
        xalign 0.5
        yalign 0.45
        spacing 10
        textbutton _("{size=+2}Start{/size}")action Start("start")activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"
        #imagebutton auto "images/comece_%s.png" action Start("start") activate_sound "audio/gun_reload_lock_or_click_sound.mp3" hover_sound "audio/zipclick.mp3"

    hbox:
        vbox:
            xpos 1350
            ypos 200
            text"{size=+2}{font=army.ttf}Capitulo 1{/font}{/size}"
            text"O motim"
            #xpos 500 ypos -300

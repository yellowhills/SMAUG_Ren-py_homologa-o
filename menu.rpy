screen demomenu:
    add "gui/deserto_background.png"
    tag menu
    vbox:
        xalign 0.02
        yalign 0.1
        spacing 20
        imagebutton auto "images/menu/iniciar_%s.png" action ShowMenu("campanha")
        imagebutton auto "images/menu/ajuda_%s.png" action ShowMenu("help")
        imagebutton auto "images/menu/preferencias_%s.png" action ShowMenu("preferences")
        imagebutton auto "images/menu/sobre_%s.png" action ShowMenu("about")
        imagebutton auto "images/menu/sair_%s.png" action Quit(confirm=False)

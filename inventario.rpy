define pistola = "fechado" #variavel if

define pistola = "pistol.png"
define moeda = "moeda.png"

label inventario:

    screen inventario:
        frame:
            align (0, 0)#posição
            textbutton "Abrir  "action [Show ("pasta"), Hide ("inventario") ]

    screen pasta:
        add "gui/inventario/inventario1.png"

        modal True



        frame:
            align (0, 0)
            textbutton "Fechar  " action [ Hide ("pasta"), Show ("inventario") ]

        frame:
            align (0, 0.5)
            text ("Pasta")
        add "[objeto1]" xpos 220 ypos 390


#variavel global
init python:
    exercito = ""
    perfil = ""
    rf = 0


#variavel de genero
$G = ""

#variavel de escolhas



define s = Character("Sargento")
define o = Character("Oficial Carolina")

#background idle e hover
image screen_capitulo = "screen_capitulo.png"
image screen_capitulo2 = "screen_capitulo2.png"



image sargento = im.Scale("pngwing.com.png", 513, 785)
image sargentocostas = "pngwing.com (2).png"
image sargentobravo = im.Scale("levibravo.png", 800, 1000)
image oficial = "pngwing.com (1).png"
image bgcity = im.Scale("bg_16__attack_on_titan_tactics__by_maxiuchiha22_dej37qe.png", 1920,1080)
image bgroomsargento  = im.Scale("bg_attack_on_titan_roomsargento.png", 1920, 1080)

#background
image blackgound1 = im.Scale("blackground.jpg", 1920, 1080)
image blackground2 = im.Scale("black-ground.jpg", 1920, 1080)
image war = im.Scale("war.jpg", 1920, 1080)
image war2 = im.Scale("war2.jpg",1920,1080)
image soldado = im.Scale("soldado.png", 1920, 1080)
image cidade_em_chamas = im.Scale("cidade_em_chamas.jpeg", 1920, 1080)
image base_deserto = im.Scale("base deserto.jpg", 1920, 1080)

#cutsceane/gif
image canhao = Movie(size=(1900, 1060), play="canhaoweb.webm")
image fire = Movie(size=(1900, 1060), play="fireweb.webm")

#sons
define audio.war1 = "audio/War_song.mp3"
define audio.cannon = "audio/ship_destroyed.ogg"
define audio.cannon2 = "audio/ship_destroyed_short.ogg"

#menu
image pistola = im.Scale("images/pistol.png", 40, 20)
image moeda = im.Scale("images/moeda.png", 300, 100)

label start:

    call screen capitulos

    call screen inventario

#cena de apresentação da historia
label capitulo1:
    play sound war1 fadein 5.0
    scene blackground2 with fade
    show text "{size=+10}{i}Durante a batalha de Sans Grov’nis, civis escoltados por um esquadrão de 5 homens foram abatidos por fogo de uma equipe de atiradores de precisão." with dissolve
    $renpy.pause(5)
    hide text with dissolve
    pause 0.5
    scene war with fade
    hide blackground2
    show text"{size=+10}{i}Os soldados foram alvejados e, logo após, executados à distância, enquanto um retardatário testemunhava o crime." with dissolve
    $renpy.pause(5)
    hide text with dissolve
    scene soldado with fade
    hide backgorund2
    show text "{size=+10}{i}Sendo a única testemunha, Henry Drovan lhe contará sobre o dia em que perdeu tudo, e você investigará e trará justiça para os moradores da vila e familiares que foram mortos a sangue frio."
    $renpy.pause(8)
    stop sound fadeout 3.0
    scene black
    pause 1.0

    $persistent.cutscene = True
    jump cutscene

#cutscene
label cutscene:
    play sound cannon fadein 1.5
    show canhao with fade
    pause 2.0
    show fire with fade
    hide canhao

    stop sound fadeout 2.0

    pause 1.0
    scene cidade_em_chamas with fade
    show text"{size=+10}{i}A evacuação da vila foi iniciada por conta de ataques de artilharia próximo" at top
    $renpy.pause(5)

    $persistent.teste1 = True

    jump teste1


label teste1:
    $ municao = False
    $incompleto = False


    hide cidade_em_chamas
    s'''
    O que aconteceu la?
    Você se lembra dos detalhes?
    '''
    o "Sim..."

    show cidade_em_chamas with fade

    menu:
        "Seguir as munições":
            $municao = True
            "Não é um bom sinal ter munições no chão por aqui numa hora dessas, é melhor eu ir dar uma olhada"
            jump seguir_municoes
        "Seguir a Foto da garota":    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<OUTRO FINAL
            "INCOMPLETO"


label seguir_municoes:
    hide cidade_em_chamas with fade
    show text "{size=+20}{i}Visitamos uma base proxima para juntar pista" with dissolve
    pause 2.0
    hide text with dissolve
    show base_deserto with fade
    s"O pessoal aqui esta bem tranquilo"
















    s"Aproveitando. você quer uma arma?"
    menu:
        "Sim":
            if pistola == "sim":
                "É bom ter por precaução"
            show pistola:
                im.Scale("images/pistol.png", 300, 200)
                align (0.5, 0)
            $ objeto1 = "pistola"

            show text "{size=+30}Item adicionado ao seu inventario"
            $renpy.pause(0.5)
            hide pistola with dissolve
            hide text with dissolve

    show screen inventario
    s"Se você olhar no canto superior esquerdo verá o icone do seu inventario"
    s"bla bla bla"
    s"bla bla bla"
    s"bla bla bla"







return
#249-gui.rpy
#linha 388 da SCREEN comentada para tirar a barra vertical

#linha 294 da SCREEN, mudado de 0.5 para 0.0
#linha 29 GUI, mudado para a cor BLACK. Linha 36 mudando o hover de "e0e066" para "808080"
#linha 261 GUI, spacing 6 para spacing 1

#linha 329 SCREEN, mudou botão de "Help" para "Ajuda"
#linha 304 SCREEN, mudou botão de "Start" para "Iniciar"
#linha 314 SCREEN, mudou botão de "Preferences" para "preferencias"

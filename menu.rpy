#hover e idle dos capitulos
init python:
    if(persistent.capitulo1 == None):
        persistent.captulo1 = True
    if(persistent.cutscene == None):
        persistent.cutscene = False
    if(persistent.teste1 == None):
        persistent.teste1 = False


#os capitulos depois de iniciar o jogo
screen capitulos:
    add "images/background1.png"
    imagemap:
        ground "images/capitulo idle.png"
        hover "images/capitulo hover.png"

        hotspot(3,280,431,209) action Jump("capitulo1")
        if(persistent.cutscene == True):
            hotspot(596,8,433,206) action Jump("cutscene")
        if(persistent.teste1 == True):
            hotspot(1136,287,447,204) action Jump("teste1")






#texto do menu



return

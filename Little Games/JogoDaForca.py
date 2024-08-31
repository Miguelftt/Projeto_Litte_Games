import pygame
import sys
from random import randint

# Cores
BLACK = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicialização do Pygame
pygame.init()


# Valores constantes
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
LARGURA = 1000
ALTURA = 600

background = pygame.image.load("./assets/backgroundForca.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# Função para renderizar o texto na tela
def render_text(text, x, y, screen, color=BLACK):
    font = pygame.font.Font(None, 30)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))  # Centraliza o texto
    screen.blit(text_surface, text_rect)


def listaPalavras():
    from random import randint

    palavras = {
        1: "Bulbasaur",
        2: "Ivysaur",
        3: "Venusaur",
        4: "Charmander",
        5: "Charmeleon",
        6: "Charizard",
        7: "Squirtle",
        8: "Wartortle",
        9: "Blastoise",
        10: "Caterpie",
        11: "Metapod",
        12: "Butterfree",
        13: "Weedle",
        14: "Kakuna",
        15: "Beedrill",
        16: "Pidgey",
        17: "Pidgeotto",
        18: "Pidgeot",
        19: "Rattata",
        20: "Raticate",
        21: "Spearow",
        22: "Fearow",
        23: "Ekans",
        24: "Arbok",
        25: "Pikachu",
        26: "Raichu",
        27: "Sandshrew",
        28: "Sandslash",
        29: "Nidoran♀",
        30: "Nidorina",
        31: "Nidoqueen",
        32: "Nidoran♂",
        33: "Nidorino",
        34: "Nidoking",
        35: "Clefairy",
        36: "Clefable",
        37: "Vulpix",
        38: "Ninetales",
        39: "Jigglypuff",
        40: "Wigglytuff",
        41: "Zubat",
        42: "Golbat",
        43: "Oddish",
        44: "Gloom",
        45: "Vileplume",
        46: "Paras",
        47: "Parasect",
        48: "Venonat",
        49: "Venomoth",
        50: "Diglett",
        51: "Dugtrio",
        52: "Meowth",
        53: "Persian",
        54: "Psyduck",
        55: "Golduck",
        56: "Mankey",
        57: "Primeape",
        58: "Growlithe",
        59: "Arcanine",
        60: "Poliwag",
        61: "Poliwhirl",
        62: "Poliwrath",
        63: "Abra",
        64: "Kadabra",
        65: "Alakazam",
        66: "Machop",
        67: "Machoke",
        68: "Machamp",
        69: "Bellsprout",
        70: "Weepinbell",
        71: "Victreebel",
        72: "Tentacool",
        73: "Tentacruel",
        74: "Geodude",
        75: "Graveler",
        76: "Golem",
        77: "Ponyta",
        78: "Rapidash",
        79: "Slowpoke",
        80: "Slowbro",
        81: "Magnemite",
        82: "Magneton",
        83: "Farfetch'd",
        84: "Doduo",
        85: "Dodrio",
        86: "Seel",
        87: "Dewgong",
        88: "Grimer",
        89: "Muk",
        90: "Shellder",
        91: "Cloyster",
        92: "Gastly",
        93: "Haunter",
        94: "Gengar",
        95: "Onix",
        96: "Drowzee",
        97: "Hypno",
        98: "Krabby",
        99: "Kingler",
        100: "Voltorb",
        101: "Electrode",
        102: "Exeggcute",
        103: "Exeggutor",
        104: "Cubone",
        105: "Marowak",
        106: "Hitmonlee",
        107: "Hitmonchan",
        108: "Lickitung",
        109: "Koffing",
        110: "Weezing",
        111: "Rhyhorn",
        112: "Rhydon",
        113: "Chansey",
        114: "Tangela",
        115: "Kangaskhan",
        116: "Horsea",
        117: "Seadra",
        118: "Goldeen",
        119: "Seaking",
        120: "Staryu",
        121: "Starmie",
        122: "Mr. Mime",
        123: "Scyther",
        124: "Jynx",
        125: "Electabuzz",
        126: "Magmar",
        127: "Pinsir",
        128: "Tauros",
        129: "Magikarp",
        130: "Gyarados",
        131: "Lapras",
        132: "Ditto",
        133: "Eevee",
        134: "Vaporeon",
        135: "Jolteon",
        136: "Flareon",
        137: "Porygon",
        138: "Omanyte",
        139: "Omastar",
        140: "Kabuto",
        141: "Kabutops",
        142: "Aerodactyl",
        143: "Snorlax",
        144: "Articuno",
        145: "Zapdos",
        146: "Moltres",
        147: "Dratini",
        148: "Dragonair",
        149: "Dragonite",
        150: "Mewtwo",
        151: "Mew",
    }
    return palavras


def gerarPalavra(palavras):
    sorteado = randint(1, len(palavras))
    palavra_escolhida = palavras.get(sorteado)
    return palavra_escolhida.upper()


def verificaChar(char):
    if len(char) == 1 and type(char) == str:
        return True
    else:
        return False


def verificaLetra(letra, palavra):
    if letra in palavra:
        return True
    else:
        return False


def revelaPalavra(letra, p_completa, p_incompleta):
    for x in range(len(p_completa)):
        if letra == p_completa[x]:
            p_incompleta[x] = letra


def escreveListasString(lista, x, y, screen):
    """Renderiza a lista de char formatada"""
    render_text(" ".join(lista), x, y, screen)


def desenhaForca(tela, chances):
    # pygame.draw.rect(tela, branco, (0, 0, LARGURA, ALTURA))
    pygame.draw.line(
        tela, BLACK, (60, 20), ((60, ALTURA - 20)), 8
    )  # linha vertical maior
    pygame.draw.line(
        tela, BLACK, ((57, 20)), (LARGURA / 6, 20), 8
    )  # linha superior horizontal
    pygame.draw.line(
        tela,
        BLACK,
        (LARGURA / 6 - 3, (20 - 3)),
        (LARGURA / 6 - 3, (ALTURA / 10) * 2),
        8,
    )  # linha vertical menor
    pygame.draw.line(
        tela, BLACK, (20, (ALTURA - 20)), (100, (ALTURA - 20)), 8
    )  # linha horizontal menor

    if chances < 10:
        pygame.draw.ellipse(
            tela, BLACK, (LARGURA / 9, ALTURA / 5, 120, 120), 4
        )  # CIRCULO DO ROSTO
    if chances < 9:
        pygame.draw.circle(
            tela, BLACK, (LARGURA / 6 - 20, ALTURA / 4 + 5), 4
        )  # OLHO ESQ
    if chances < 8:
        pygame.draw.circle(
            tela, BLACK, (LARGURA / 6 + 20, ALTURA / 4 + 5), 4
        )  # OLHO DIR
    if chances < 7:

        pygame.draw.arc(
            tela, BLACK, (LARGURA / 7 + 5, ALTURA / 4 + 10, 50, 50), -3, 0, 8
        )  # SORRISO TORTO
    if chances < 6:  # CORPO
        pygame.draw.line(
            tela,
            BLACK,
            (LARGURA / 6 - 3, ALTURA / 3 + 35),
            (LARGURA / 6 - 3, ALTURA / 2 + 60),
            4,
        )
    if chances < 5:  # BRAÇO ESQ
        pygame.draw.line(
            tela,
            BLACK,
            (LARGURA / 6 - 3, ALTURA / 3 + 60),
            (LARGURA / 9 - 3, (ALTURA / 4) * 2 + 50),
            4,
        )
    if chances < 4:  # BRAÇO DIR
        pygame.draw.line(
            tela,
            BLACK,
            (LARGURA / 6 - 3, ALTURA / 3 + 60),
            ((LARGURA / 9) * 2 - 3, (ALTURA / 4) * 2 + 50),
            4,
        )
    if chances < 3:  # PERNA ESQ
        pygame.draw.line(
            tela,
            BLACK,
            (LARGURA / 6 - 3, ALTURA / 2 + 60),
            (LARGURA / 9 - 3, (ALTURA / 3) * 2 + 50),
            4,
        )
    if chances < 2:  # PERNA DIR
        pygame.draw.line(
            tela,
            BLACK,
            (LARGURA / 6 - 3, ALTURA / 2 + 60),
            ((LARGURA / 9) * 2 - 3, (ALTURA / 3) * 2 + 50),
            4,
        )


def JogoDaForca(screen):
    pygame.font.init()
    tentativas = 10
    palavras = listaPalavras()
    palavraEscolhida = list(gerarPalavra(palavras))
    palavraEscura = list("_" * len(palavraEscolhida))
    letras_usadas = []
    flag_teclas = 0
    x_pos = WIDTH // 2  # Posição central horizontal
    y_pos = HEIGHT // 2  # Posição central vertical

    render_text("Palavra vazia: ", x_pos, y_pos - 300, screen)
    escreveListasString(palavraEscura, x_pos, y_pos - 270, screen)
    render_text(
        "Palavra escolhida: " + "".join(palavraEscolhida), x_pos, y_pos - 240, screen
    )

    letras_utilizadas_texto = render_text(
        "Letras utilizadas: ", x_pos, y_pos - 60, screen
    )

    pygame.display.flip()

    while tentativas > 0 and "_" in palavraEscura:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key in [
                    pygame.K_a,
                    pygame.K_b,
                    pygame.K_c,
                    pygame.K_d,
                    pygame.K_e,
                    pygame.K_f,
                    pygame.K_g,
                    pygame.K_h,
                    pygame.K_i,
                    pygame.K_j,
                    pygame.K_k,
                    pygame.K_l,
                    pygame.K_m,
                    pygame.K_n,
                    pygame.K_o,
                    pygame.K_p,
                    pygame.K_q,
                    pygame.K_r,
                    pygame.K_s,
                    pygame.K_t,
                    pygame.K_u,
                    pygame.K_v,
                    pygame.K_w,
                    pygame.K_x,
                    pygame.K_y,
                    pygame.K_z,
                ]:

                    letra_jogador = event.unicode.upper()
                    if verificaChar(letra_jogador):
                        if not (letra_jogador in letras_usadas) and verificaLetra(
                            letra_jogador, palavraEscolhida
                        ):
                            revelaPalavra(
                                letra_jogador, palavraEscolhida, palavraEscura
                            )
                            flag_teclas = 0
                        elif letra_jogador in letras_usadas:
                            flag_teclas = 1
                        else:
                            tentativas = tentativas - 1
                            flag_teclas = 2
                        if letra_jogador not in letras_usadas:
                            letras_usadas.append(letra_jogador)
                    else:
                        render_text("Não é um caractere", x_pos, y_pos - 90, screen)

                # Verifica se a tecla ESC foi pressionada
                elif event.key == pygame.K_ESCAPE:
                    return False  # Retorna ao menu

        pygame.display.update()
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        desenhaForca(screen, tentativas)

        render_text(f"Você tem {tentativas} tentativas", x_pos, y_pos - 210, screen)
        # render_text("Palavra escura: ", x_pos, y_pos - 180, screen)
        escreveListasString(palavraEscura, x_pos, y_pos - 150, screen)

        render_text(
            "Aperte 'ESC' para voltar ao MENU",
            x_pos,
            y_pos + y_pos - y_pos / 2,
            screen,
        )
        # Aqui você pode receber a entrada do usuário diretamente pela tela
        if flag_teclas == 1:
            render_text(
                "***Letra repetida***",
                x_pos,
                y_pos - 120,
                screen,
            )
        elif flag_teclas == 2:
            render_text(
                "***Letra errada***",
                x_pos,
                y_pos - 120,
                screen,
            )
        # Renderiza as letras utilizadas apenas se houver uma alteração
        if len(letras_usadas) != 0:
            letras_utilizadas = " ".join(letras_usadas)
            if letras_utilizadas != letras_utilizadas_texto:
                letras_utilizadas_texto = render_text(
                    "Letras utilizadas: " + letras_utilizadas, x_pos, y_pos - 60, screen
                )
    if tentativas != 0:
        render_text("VOCÊ GANHOU!", x_pos, y_pos - 30, screen)
        render_text(
            "Pressione qualquer tecla para voltar ao menu", x_pos, y_pos, screen
        )
        
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return True
    else:
        render_text("VOCÊ PERDEU!", x_pos, y_pos - 30, screen)
        render_text(
            "Pressione qualquer tecla para voltar ao menu", x_pos, y_pos, screen
        )
        render_text(f"O Pokemon era: ", x_pos, y_pos +70, screen)
        escreveListasString(palavraEscolhida, x_pos, y_pos +100, screen)

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return False
                if tentativas < 1:  # INTERAÇÃO COM ROSTO (FIM DE JOGO)
                    render_text(
                        "X",
                        LARGURA / 6 - 20,
                        ALTURA / 4 + 5,
                        screen,
                    )
                    render_text(
                        "X",
                        LARGURA / 6 + 20,
                        ALTURA / 4 + 5,
                        screen,
                    )
                    pygame.display.update()


# Função principal para executar o jogo da forca
def mainJogoDaForca(screen):
    while True:
        if not JogoDaForca(screen):
            return  # Sair do loop e retornar ao menu


if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    mainJogoDaForca(screen)
    pygame.quit()
    sys.exit()

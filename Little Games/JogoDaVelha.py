import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Valores constantes
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

background = pygame.image.load("./assets/backgroundVelha.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Cores
BLACK = (13, 13, 13)
WHITE = (255, 255, 255)


def render_text(text, x, y, screen, color=WHITE):
    font = pygame.font.Font(None, 48)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def imprimir_tabuleiro(tabuleiro, x_pos, y_pos, screen, cursor_x, cursor_y):
    cell_width = 200  # Largura da célula
    cell_height = 200  # Altura da célula
    line_spacing = 20  # Espaçamento entre as linhas e colunas

    for i, linha in enumerate(tabuleiro):
        for j, cell in enumerate(linha):
            # Calcular a posição x e y da célula atual
            cell_x = x_pos + j * (cell_width + line_spacing)
            cell_y = y_pos + i * (cell_height + line_spacing)

            # Desenhar o retângulo da célula
            pygame.draw.rect(
                screen, WHITE, (cell_x, cell_y, cell_width, cell_height), 3
            )

            # Renderizar o conteúdo da célula (X, O ou espaço em branco)
            render_text(
                cell, cell_x + cell_width // 2, cell_y + cell_height // 2, screen
            )

    # Desenhar o retângulo da célula selecionada
    selected_cell_x = x_pos + cursor_x * (cell_width + line_spacing)
    selected_cell_y = y_pos + cursor_y * (cell_height + line_spacing)
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (selected_cell_x, selected_cell_y, cell_width, cell_height),
        3,
    )


def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(
            tabuleiro[j][i] == jogador for j in range(3)
        ):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(
        tabuleiro[i][2 - i] == jogador for i in range(3)
    ):
        return True

    return False


def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for cell in linha:
            if cell == " ":
                return False  # Tem espaço vazio na matriz
    return True  # Não há espaços


def realizar_jogada(tabuleiro, jogador, linha, coluna):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False


def jogar_com_amigo(screen):
    clock = pygame.time.Clock()

    tabuleiro = [[" "] * 3 for _ in range(3)]
    x_pos = (WIDTH - 3 * 200 - 40) // 2
    y_pos = (HEIGHT - 3 * 200 - 40) // 2
    cursor_x, cursor_y = 0, 0
    jogador_atual = random.choice(["X", "O"])

    while True:
        screen.blit(background, (0, 0))
        imprimir_tabuleiro(tabuleiro, x_pos, y_pos, screen, cursor_x, cursor_y)
        render_text(
            f"Jogador {jogador_atual}, use as setas para mover e Enter para jogar.",
            WIDTH // 2,
            50, #HEIGHT - HEIGHT / 7,
            screen,
        ) 
        render_text(
            f"Aperte 'ESC' para voltar ao MENU",
            WIDTH // 2,
            HEIGHT-50, #HEIGHT - HEIGHT / 10,
            screen,
        )
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Voltar ao menu
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cursor_y = max(0, cursor_y - 1)
                elif event.key == pygame.K_DOWN:
                    cursor_y = min(2, cursor_y + 1)
                elif event.key == pygame.K_LEFT:
                    cursor_x = max(0, cursor_x - 1)
                elif event.key == pygame.K_RIGHT:
                    cursor_x = min(2, cursor_x + 1)
                elif event.key == pygame.K_RETURN:
                    if realizar_jogada(tabuleiro, jogador_atual, cursor_y, cursor_x):
                        if verificar_vitoria(tabuleiro, jogador_atual):
                            screen.blit(background, (0, 0))
                            imprimir_tabuleiro(
                                tabuleiro, x_pos, y_pos, screen, cursor_x, cursor_y
                            )
                            render_text(
                                f"Parabéns! Jogador {jogador_atual} venceu!",
                                WIDTH // 2,
                                HEIGHT-80, #HEIGHT - HEIGHT / 9,
                                screen,
                            )
                            render_text(
                                "Pressione qualquer tecla para voltar ao menu",
                                WIDTH // 2,
                                HEIGHT-50, #HEIGHT - HEIGHT / 6,
                                screen,
                            )
                            pygame.display.update()
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        return False  # Voltar ao menu
                        elif verificar_empate(tabuleiro):
                            screen.fill(BLACK)
                            imprimir_tabuleiro(
                                tabuleiro, x_pos, y_pos, screen, cursor_x, cursor_y
                            )
                            render_text(
                                "Empate!", WIDTH // 2, HEIGHT-80, #HEIGHT - HEIGHT / 9,
                                screen
                            )
                            pygame.display.update()
                            render_text(
                                "Pressione qualquer tecla para voltar ao menu",
                                WIDTH // 2,
                               HEIGHT-50,# HEIGHT - HEIGHT / 6,
                                screen,
                            )
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        return False  # Voltar ao menu
                        jogador_atual = "X" if jogador_atual == "O" else "O"
                elif event.key == pygame.K_ESCAPE:
                    return False  # Voltar ao menu


def mainJogoDaVelha(screen):
    while True:
        if not jogar_com_amigo(screen):
            return  # Sair do loop e retornar ao menu


if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    mainJogoDaVelha(screen)
    pygame.quit()
    sys.exit()

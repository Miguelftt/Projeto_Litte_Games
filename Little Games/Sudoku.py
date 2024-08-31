import pygame
from pygame.locals import *
import random
import sys

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicialização do Pygame
pygame.init()

# Valores constantes
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CELL_SIZE = 60
GRID_SIZE = CELL_SIZE * 9

background = pygame.image.load("./assets/backgroundSudoku.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# Função para sair do jogo
def sair_do_jogo():
    pygame.quit()
    sys.exit()


# Função para criar uma matriz vazia para o Sudoku
def criaSudokuVazio():
    matriz = [[0] * 9 for _ in range(9)]
    return matriz


# Função para desenhar o tabuleiro Sudoku na tela
def desenhaSudoku(screen, tab, selected_cell, verificar=False):
    for i in range(9):
        for j in range(9):
            x = (WIDTH - GRID_SIZE) // 2 + j * CELL_SIZE
            y = (HEIGHT - GRID_SIZE) // 2 + i * CELL_SIZE
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE),1) #Moldura preta
            font = pygame.font.SysFont(None, 40)
            if tab[i][j] != 0:
                text_color = BLACK
                if verificar and not verificaJogada(tab, i, j, tab[i][j]):
                    text_color = RED
                text = font.render(str(tab[i][j]), True, text_color)
                text_rect = text.get_rect(
                    center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2)
                )
                screen.blit(text, text_rect)
            if selected_cell == (i, j):
                pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE), 3)


# Função para renderizar texto na tela
def render_text(text, x, y, screen):
    font = pygame.font.SysFont(None, 40)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# Função para verificar se uma jogada é válida
def verificaJogada(tabuleiro, linha, coluna, numero):
    for x in range(9):
        if tabuleiro[linha][x] == numero and x != coluna:  # Verifica na coluna
            return False
        if tabuleiro[x][coluna] == numero and x != linha:  # Verifica na linha
            return False
    lin_inicio = (linha // 3) * 3
    col_inicio = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tabuleiro[lin_inicio + i][col_inicio + j] == numero and (
                lin_inicio + i != linha or col_inicio + j != coluna
            ):
                return False
    return True


# Função para resolver o Sudoku
def resolveSudoku(tabuleiro):
    linha = coluna = 0
    sem_numero = False

    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                sem_numero = True
                break

        if sem_numero:
            break

    if not (sem_numero):
        return True

    for num in range(1, 10):
        if verificaJogada(tabuleiro, linha, coluna, num):
            tabuleiro[linha][coluna] = num

            if resolveSudoku(tabuleiro):
                return True

            tabuleiro[linha][coluna] = 0
    # escreveSudoku(tabuleiro)
    # print("=========================")
    return False

def geradorDeSudoku(sudoku_gerado):
    sem_solucao = True
    # sudoku_gerado = criaSudokuVazio()
    
    parada = random.randint(15,20)
    contador = 0
    while(sem_solucao):
        print("numero gerado: ", parada)
        for x in range(0,9):
            for y in range(0,9):
                sudoku_gerado[x][y] = 0
        print("entrou aq======================")
        contador = 0
        while(contador < parada):
            numero = random.randint(1,9)
            linha = random.randint(0,8)
            coluna = random.randint(0,8)
            if(verificaJogada(sudoku_gerado,linha, coluna, numero)):
                contador +=1
                sudoku_gerado[linha][coluna] = numero
            print(contador)
        if(resolveSudoku(sudoku_gerado)):
            sem_solucao = False

        print("NÃOOOOOCriouuuuuuuuuuuu")
    return sudoku_gerado

# Função para gerar um Sudoku parcialmente preenchido
def geraSudokuInicial():
    sudoku = criaSudokuVazio()
    # sudoku = geradorDeSudoku(sudoku)
    resolveSudoku(sudoku)

    # Remover alguns números do tabuleiro para criar o Sudoku parcialmente preenchido
    for _ in range(40):  # Número de células a serem removidas
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        sudoku[linha][coluna] = 0

    return sudoku


# Função principal do jogo Sudoku
def jogoSudoku(screen):
    sudoku = geraSudokuInicial()
    selected_cell = None
    verificar = False
    resolved = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Retorna ao menu quando a tecla Esc é pressionada
                elif event.key == pygame.K_v:  # Tecla 'v' para verificar os números
                    verificar = True
                elif event.key == pygame.K_r:  # Tecla 'r' para resolver o Sudoku
                    resolveSudoku(sudoku)
                    resolved = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = (y - (HEIGHT - GRID_SIZE) // 2) // CELL_SIZE
                col = (x - (WIDTH - GRID_SIZE) // 2) // CELL_SIZE
                if 0 <= row < 9 and 0 <= col < 9:
                    selected_cell = (row, col)

                    # Preenche a célula selecionada com um número (de 1 a 9)
                    if event.button == 1:  # Botão esquerdo do mouse
                        sudoku[row][col] = (
                            sudoku[row][col] + 1
                        ) % 10  # Incrementa o número na célula
                    elif event.button == 3:  # Botão direito do mouse
                        sudoku[row][col] = 0  # Limpa a célula

        # Desenha o tabuleiro Sudoku na tela
        screen.blit(background, (0, 0))
        desenhaSudoku(screen, sudoku, selected_cell, verificar)
        render_text(
            "Aperte 'ESC' para voltar ao MENU",
            WIDTH // 2,
            HEIGHT - HEIGHT / 9,
            screen,
        )
        render_text(
            "Quando completar, digite 'V' para verificar. Para resolver, digite 'R'",
            WIDTH // 2,
            HEIGHT / 7,
            screen,
        )
        if resolved:
            render_text("Sudoku Resolvido!", WIDTH // 2, HEIGHT - HEIGHT / 7, screen)
        pygame.display.flip()  # Atualiza a tela

    pygame.quit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    jogoSudoku(screen)


if __name__ == "__main__":
    main()

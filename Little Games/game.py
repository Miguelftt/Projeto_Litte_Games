import pygame
import sys
import JogoDaForca
import JogoDaVelha
import Sudoku
import Snake

# Valores constantes
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
FPS = 60

# Cores
BLACK = (13, 13, 13)


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Little Games")
        self.clock = pygame.time.Clock()
        self.button_width = 350
        self.button_height = 150
        self.button_x = (WIDTH - self.button_width) // 2
        self.button_y = (HEIGHT - self.button_height) // 2
        self.load_assets()

    def load_assets(self):
        try:
            self.imagem = pygame.image.load("./assets/backgroundMenu.png")
            self.tittle = pygame.image.load("./assets/tittle.png")
            self.button_forca = pygame.image.load("./assets/forcaButton.png")
            self.button_sudoku = pygame.image.load("./assets/buttonSudoku.png")
            self.button_snake = pygame.image.load("./assets/buttonSnake.png")
            self.button_velha = pygame.image.load("./assets/buttonVelha.png")

            self.button_width, self.button_height = self.button_forca.get_size()

            self.imagem = pygame.transform.scale(self.imagem, (WIDTH, HEIGHT))
            self.tittle = pygame.transform.scale(self.tittle, (900, 350))
            self.button_forca = pygame.transform.scale(
                self.button_forca, (self.button_width, self.button_height)
            )
            self.button_sudoku = pygame.transform.scale(
                self.button_sudoku, (self.button_width, self.button_height)
            )
            self.button_snake = pygame.transform.scale(
                self.button_snake, (self.button_width, self.button_height)
            )
            self.button_velha = pygame.transform.scale(
                self.button_velha, (self.button_width, self.button_height)
            )
        except pygame.error:
            print("Erro ao carregar imagem.")
            pygame.quit()
            sys.exit()

    def render_main_screen(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.imagem, (0, 0))
        self.screen.blit(
            self.tittle,
            (
                (self.button_x * 1.65) - self.button_x,
                (self.button_y * 1.4) - self.button_y,
            ),
        )
        self.screen.blit(
            self.button_forca, (WIDTH / 1.85, self.button_y + self.button_height * 1.2)
        )
        self.screen.blit(
            self.button_sudoku, (WIDTH / 1.85, self.button_y + self.button_height * 2.8)
        )
        self.screen.blit(
            self.button_snake, (WIDTH / 3.3, self.button_y + self.button_height * 1.2)
        )
        self.screen.blit(
            self.button_velha, (WIDTH / 3.3, self.button_y + self.button_height * 2.8)
        )
        pygame.display.flip()

    def start_game_of_forca(self):
        JogoDaForca.JogoDaForca(self.screen)
        self.render_main_screen()

    def start_game_of_velha(self):
        JogoDaVelha.mainJogoDaVelha(self.screen)
        self.render_main_screen()

    def start_game_of_sudoku(self):
        Sudoku.jogoSudoku(self.screen)
        self.render_main_screen()

    def start_game_of_snake(self):
        Snake.start_game_of_snake()  # Chame a função para iniciar o jogo

        # Atualize a tela do menu após o jogo Snake ser encerrado
        self.render_main_screen()


def main():
    menu = Menu()
    running = True

    while running:
        menu.clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Tecla ESC pressionada. Saindo...")
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if (WIDTH / 1.85) <= mouseX <= (WIDTH / 1.85) + menu.button_width and (
                    menu.button_y + menu.button_height * 1.2
                ) <= mouseY <= (
                    menu.button_y + menu.button_height * 1.2
                ) + menu.button_height:
                    print("Botão Forca clicado!")
                    menu.start_game_of_forca()
                elif (WIDTH / 1.85) <= mouseX <= (
                    WIDTH / 1.85
                ) + menu.button_width and (
                    menu.button_y + menu.button_height * 2.8
                ) <= mouseY <= (
                    menu.button_y + menu.button_height * 2.8
                ) + menu.button_height:

                    print("Botão Sudoku clicado!")
                    menu.start_game_of_sudoku()
                elif (WIDTH / 3.3) <= mouseX <= (WIDTH / 3.3) + menu.button_width and (
                    menu.button_y + menu.button_height * 1.2
                ) <= mouseY <= (
                    menu.button_y + menu.button_height * 1.2
                ) + menu.button_height:

                    print("Botão Snake clicado!")
                    menu.start_game_of_snake()
                elif (WIDTH / 3.3) <= mouseX <= (WIDTH / 3.3) + menu.button_width and (
                    menu.button_y + menu.button_height * 2.8
                ) <= mouseY <= (
                    menu.button_y + menu.button_height * 2.8
                ) + menu.button_height:

                    print("Botão Velha clicado!")
                    menu.start_game_of_velha()

        menu.render_main_screen()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

import pygame
import sys
import random
from pygame.math import Vector2

pygame.init()
pygame.mixer.init()

# Valores constantes
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
FPS = 60

# Definição dos diretórios e arquivos de fonte
fonte_press_start = "./assets/PressStart2P-Regular.ttf"

# Definição dos tamanhos de fonte para título e pontuação
tamanho_fonte_titulo = 40
tamanho_fonte_pontuacao = 13

# Carregar as fontes
fonte_titulo = pygame.font.Font(fonte_press_start, tamanho_fonte_titulo)
fonte_pontuacao = pygame.font.Font(fonte_press_start, tamanho_fonte_pontuacao)

# Tamanho de cada célula no grid do jogo e número de células
tamanho_celula = 20
numero_celulas = 20

# Definição do offset para alinhar elementos na tela
OFFSET_X = (WIDTH - (tamanho_celula * numero_celulas)) // 2
OFFSET_Y = (HEIGHT - (tamanho_celula * numero_celulas)) // 2

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Retrô")
clock = pygame.time.Clock()

# Carregar as imagens
surface_comida = pygame.image.load("./assets/food.png")
tela = pygame.image.load("./assets/telaSnake.png")

# Redimensionar a imagem da tela inicial para ocupar toda a tela
tela = pygame.transform.scale(tela, (WIDTH, HEIGHT))

# Pausa para exibir a tela inicial
pygame.time.wait(1000)

# Definição do evento personalizado para atualizar a cobra
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)


# Classe responsável por gerenciar a comida do jogo
class Comida:
    def __init__(self, corpo_cobra):
        # Inicializar a posição da comida
        self.posicao = self.gerar_posicao_aleatoria(corpo_cobra)

    # Método para desenhar a comida na tela
    def desenhar(self):
        rect_comida = pygame.Rect(
            (
                OFFSET_X + self.posicao.x * tamanho_celula,
                OFFSET_Y + self.posicao.y * tamanho_celula,
                tamanho_celula,
                tamanho_celula,
            )
        )
        screen.blit(surface_comida, rect_comida)

    # Gerar uma célula aleatória para a comida
    def gerar_celula_aleatoria(self):
        x = random.randint(0, numero_celulas - 2)
        y = random.randint(0, numero_celulas - 2)
        return Vector2(x, y)

    # Gerar uma posição aleatória para a comida, garantindo que não esteja na cobra
    def gerar_posicao_aleatoria(self, corpo_cobra):
        posicao = self.gerar_celula_aleatoria()
        while posicao in corpo_cobra:
            posicao = self.gerar_celula_aleatoria()
        return posicao


# Função para sair do jogo
def sair_do_jogo():
    pygame.quit()
    sys.exit()


# Classe responsável pela cobra e suas funcionalidades
class Cobra:
    def __init__(self):
        # Inicializar o corpo da cobra, sua direção e a indicação de adicionar um segmento
        self.corpo = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direcao = Vector2(1, 0)
        self.adicionar_segmento = False
        # Carregar os sons
        self.som_moeda = pygame.mixer.Sound("./assets/coin.mp3")
        self.som_batida = pygame.mixer.Sound("./assets/dead.mp3")

    # Método para desenhar a cobra na tela
    def desenhar(self):
        for segmento in self.corpo:
            segmento_rect = (
                OFFSET_X + segmento.x * tamanho_celula,
                OFFSET_Y + segmento.y * tamanho_celula,
                tamanho_celula,
                tamanho_celula,
            )
            pygame.draw.rect(screen, (43, 51, 24), segmento_rect, 10, 3)

    # Atualizar a posição da cobra
    def atualizar(self):
        self.corpo.insert(0, self.corpo[0] + self.direcao)
        if self.adicionar_segmento == True:
            self.adicionar_segmento = False
        else:
            self.corpo = self.corpo[:-1]

    # Reiniciar a cobra
    def reiniciar(self):
        self.corpo = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direcao = Vector2(1, 0)


# Classe responsável pelo gerenciamento do jogo
class Jogo:
    def __init__(self):
        # Inicializar a cobra, a comida, o estado do jogo e a pontuação
        self.cobra = Cobra()
        self.comida = Comida(self.cobra.corpo)
        self.estado = "PARADO"
        self.pontuacao = 0

    # Desenhar elementos na tela
    def desenhar(self):
        self.comida.desenhar()
        self.cobra.desenhar()
        superficie_pontuacao = fonte_pontuacao.render(
            "Pontuação: " + str(self.pontuacao), True, (255, 255, 255)
        )
        screen.blit(superficie_pontuacao, (OFFSET_X, OFFSET_Y - 30))

    # Atualizar o estado do jogo
    def atualizar(self):
        if self.estado == "EXECUTANDO":
            self.cobra.atualizar()
            self.verificar_colisao_com_comida()
            self.verificar_colisao_com_bordas()
            self.verificar_colisao_com_cauda()

    # Verificar colisão da cobra com a comida
    def verificar_colisao_com_comida(self):
        if self.cobra.corpo[0] == self.comida.posicao:
            self.comida.posicao = self.comida.gerar_posicao_aleatoria(self.cobra.corpo)
            self.cobra.adicionar_segmento = True
            self.pontuacao += 1
            self.cobra.som_moeda.play()

    # Verificar colisão da cobra com as bordas da tela
    def verificar_colisao_com_bordas(self):
        if self.cobra.corpo[0].x == numero_celulas or self.cobra.corpo[0].x == -1:
            self.fim_jogo()
        if self.cobra.corpo[0].y == numero_celulas or self.cobra.corpo[0].y == -1:
            self.fim_jogo()

    # Finalizar o jogo
    def fim_jogo(self):
        self.cobra.reiniciar()
        self.comida.posicao = self.comida.gerar_posicao_aleatoria(self.cobra.corpo)
        self.estado = "PARADO"
        self.pontuacao = 0
        self.cobra.som_batida.play()

    # Verificar colisão da cobra com sua própria cauda
    def verificar_colisao_com_cauda(self):
        corpo_sem_cabeca = self.cobra.corpo[1:]
        if self.cobra.corpo[0] in corpo_sem_cabeca:
            self.fim_jogo()


# Função para iniciar o jogo da Snake
def start_game_of_snake():
    # Inicialização do jogo
    jogo = Jogo()

    # Mostrar tela inicial
    mostrar_tela_inicial()
    aguardando_inicio = True
    while aguardando_inicio:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_do_jogo()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    executando = False
                elif event.key == pygame.K_SPACE:
                    aguardando_inicio = False
                    pygame.mixer.music.stop()

    # Loop principal do jogo
    executando = True
    while executando:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == SNAKE_UPDATE:
                jogo.atualizar()
            if event.type == pygame.QUIT:
                executando = False
                sair_do_jogo()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Quando Esc é pressionado, saia do loop do jogo
                    executando = False

                if jogo.estado == "PARADO":
                    jogo.estado = "EXECUTANDO"

                # Controles da cobra
                if event.key == pygame.K_UP and jogo.cobra.direcao != Vector2(0, 1):
                    jogo.cobra.direcao = Vector2(0, -1)
                if event.key == pygame.K_DOWN and jogo.cobra.direcao != Vector2(0, -1):
                    jogo.cobra.direcao = Vector2(0, 1)
                if event.key == pygame.K_LEFT and jogo.cobra.direcao != Vector2(1, 0):
                    jogo.cobra.direcao = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and jogo.cobra.direcao != Vector2(-1, 0):
                    jogo.cobra.direcao = Vector2(1, 0)

        # Desenhar elementos na tela
        screen.fill((175, 215, 70))
        pygame.draw.rect(
            screen,
            (43, 51, 24),
            (
                OFFSET_X - 5,
                OFFSET_Y - 5,
                tamanho_celula * numero_celulas + 10,
                tamanho_celula * numero_celulas + 10,
            ),
            5,
        )
        jogo.desenhar()

        superficie_titulo = fonte_titulo.render("Snake Retro", True, (43, 51, 24))
        voltar = fonte_pontuacao.render(
            "Aperte 'ESC' para voltar para o MENU", True, (0, 0, 0)
        )

        screen.blit(superficie_titulo, (OFFSET_X - 5, HEIGHT / 7))
        screen.blit(voltar, (OFFSET_X - 5, HEIGHT - HEIGHT / 7))

        pygame.display.update()
        clock.tick(FPS)


# Função para mostrar a tela inicial
def mostrar_tela_inicial():
    try:
        # Carregar e reproduzir a música de fundo
        pygame.mixer.music.load("./assets/inicio.mp3")
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print("Erro ao carregar ou reproduzir a música:", e)

    # Desenhar elementos na tela
    screen.blit(tela, (0, 0))
    texto_titulo = fonte_titulo.render("Press ESPACE to start", True, (255, 255, 255))
    texto_x = (screen.get_width() - texto_titulo.get_width()) // 2
    texto_y = screen.get_height() - texto_titulo.get_height() - 20
    screen.blit(texto_titulo, (texto_x, texto_y))
    pygame.display.update()


if __name__ == "__main__":
    start_game_of_snake()

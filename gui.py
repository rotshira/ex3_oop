import pygame
from pygame import display, gfxdraw, RESIZABLE
from src import DiGraph

INF = 999999999
WIDTH, HEIGHT = 1000, 800
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=30, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 10, bold=True)
radius = 15

class gui:

    def __init__(self, graph: DiGraph):
        self.graph = graph
        pygame.init()
        screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        pygame.font.init()
        radius = 15

        while (True):
            # check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            screen.fill(pygame.Color(15, 100, 100))
            self.draw_n(screen)
            self.draw_Edges(screen)

            # refresh screen
            screen.fill(pygame.Color(0, 0, 0))
            # draw nodes

    def draw_n(self, screen):
        for n in self.graph.vertex:
            x = self.my_scale(self.graph.vertex[n][0], x=True)
            y = self.my_scale(self.graph.vertex[n][1], y=True)

            # its just to get a nice antialiased circle
            gfxdraw.filled_circle(screen, int(x), int(y), radius, pygame.Color(64, 80, 174))
            gfxdraw.aacircle(screen, int(x), int(y), radius, pygame.Color(255, 255, 255))

            # draw the node id
            id_srf = FONT.render(str(n), True, pygame.Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)

            # draw edges
    def draw_Edges(self, screen):
            for e in self.graph.edges:
                # find the edge nodes
                src = next(n for n in self.graph.vertex if n == e[0])
                dest = next(n for n in self.graph.vertex if n == e[1])

                # scaled positions
                src_x = self.my_scale(self.graph.vertex[src][0], x=True)
                src_y = self.my_scale(self.graph.vertex[src][1], y=True)
                dest_x = self.my_scale(self.graph.vertex[dest][0], x=True)
                dest_y = self.my_scale(self.graph.vertex[dest][1], y=True)

                # draw the line
                pygame.draw.line(screen, pygame.Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y))
                # pygame.draw.polygon(screen, pygame.Color(61, 72, 126), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
            # update screen changes
            display.update()

            # refresh rate
            clock.tick(60)

            # a function of the algorithm of dijkstra

    def scaleX(self, data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimensions
        """
        abs1 = abs(max_data - min_data)
        scaleX = screen.get_width() / abs1
        return ((data) * (max_screen - min_screen) * scaleX) % screen.get_width() + min_screen

        # scale the point[Y] to be seen in the graph

    def scaleY(self, data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimensions
        """
        abs1 = abs(max_data - min_data)
        scaleY = screen.get_height() / abs1
        return ((data) * (max_screen - min_screen) * scaleY) % screen.get_height() + min_screen

        # scale the point to be seen in the graph



    def my_scale(self, data, x=False, y=False):
        # get data proportions
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0
        for i in range(0, len(self.graph.vertex) - 1):
            x = self.graph.vertex[i][0]
            min_x = min(self.graph.vertex[i + 1][0], x)
        for i in range(0, len(self.graph.vertex) - 1):
            y = self.graph.vertex[i][1]
            min_y = min(self.graph.vertex[i + 1][1], y)
        for i in range(0, len(self.graph.vertex) - 1):
            x1 = self.graph.vertex[i][0]
            max_x = max(self.graph.vertex[i + 1][0], x1)
        for i in range(0, len(self.graph.vertex) - 1):
            y1 = self.graph.vertex[i][1]
            max_y = max(self.graph.vertex[i + 1][1], y1)
        if x:
            return self.scaleY(data, 10, screen.get_width() - 55, min_y, max_y)
        if y:
            return self.scaleX(data, 40, screen.get_height() - 40, min_x, max_x)


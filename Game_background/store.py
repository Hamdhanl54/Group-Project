WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

START_BUTTON_HEIGHT = 50
START_BUTTON_WIDTH = 200
START_BUTTON_COLOR = GRAY
START_BUTTON_HOVER_COLOR = (150, 150, 150)
START_BUTTON_TEXT_COLOR = BLACK
START_BUTTON_FONT_SIZE = 30


        def create_text(text, color, font_size):
            font = pygame.font.SysFont('font.ttf', font_size)
            text_surface = font.render(text, True, color)
            return text_surface, text_surface.get_rect()
        
        def create_button(x, y, width, height, color, hover_color, text, text_color, font_size):
            button_rect = pygame.Rect(x, y, width, height)
            text_surface, text_rect = create_text(text, text_color, font_size)
            text_rect.center = button_rect.center
            return button_rect, text_surface, text_rect
        
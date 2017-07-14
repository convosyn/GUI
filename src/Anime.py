import pygame, sys
import pygame.locals

class Anime:

    # a simple animation class for the animation programmers

    def __init__(self, title_of_window = "Demo", width = 640, height = 480, frame_count = 30, scene_func = None):

        pygame.init()
        self.width = width
        self.height = height
        self.DISP_SURF = pygame.display.set_mode((self.width, self.height))
        self.frame_count = frame_count
        self.fps_clock = pygame.time.Clock()
        self.scene_func = scene_func
        pygame.display.set_caption(title_of_window)

    def run(self):

        self.DISP_SURF.fill(pygame.Color(255, 255, 255))
        while True:    
            self.draw_scene(self.get_scene_func())
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.fps_clock.tick(self.frame_count)

    def draw_scene(self, draw_function = None):

        if draw_function != None:
            draw_function()
        else:
            self.default_draw_function()
    
    def default_draw_function(self):
        
        background_color = pygame.Color(254, 255, 204)
        self.DISP_SURF.fill(background_color)
        font_obj = pygame.font.Font("../fonts/Qarmic_sans_Abridged.ttf", 60)
        text_surf_obj_shadow = font_obj.render("Scene Here ...", True, pygame.Color(216, 216, 214))
        text_surf_obj = font_obj.render("Scene Here ...", True, pygame.Color(226, 210, 31))
        font_obj.set_bold(True)
        text_rect_obj_shadow = text_surf_obj_shadow.get_rect()
        text_rect_obj = text_surf_obj.get_rect()
        text_rect_obj_shadow.center = (self.width / 2 + 4, self.height / 2 + 2)
        text_rect_obj.center = (self.width / 2, self.height / 2)
        self.DISP_SURF.blit(text_surf_obj_shadow, text_rect_obj_shadow)
        self.DISP_SURF.blit(text_surf_obj, text_rect_obj)

    def get_scene_func(self):
        return self.scene_func

    def set_scene_func(self, scene_func):
        self.scene_func = scene_func

    def get_scene_surface(self):
        return self.DISP_SURF

    def get_screen_width(self):
        return self.width

    def get_screen_height(self):
        return self.height
import Anime
import pygame
import time

class BallDrop(Anime.Anime):
    
    FLIP_VERTICAL = 0
    FLIP_HORIZONTAL = 1

    def __init__(self):
        Anime.Anime.__init__(self)
        self.background_color = pygame.Color(255, 255, 255)
        self.set_scene_func(self.scene)
        self.ball_coords = (int(self.width/2), int(self.height/2))
        self.ball = Ball(self.get_scene_surface(), self.flip(*self.ball_coords), ball_color= pygame.Color(255, 0, 0), radius = 10)
        self.ground = Ground(self.get_scene_surface(), (10, self.get_screen_height() - 10),(self.get_screen_width()-10, self.get_screen_height()-10), width = 4)
        self.init_time = time.time()
        self.acceleration = -9.8

    def scene(self):

        ball_rect = self.ball.ball_rect()
        ground_rect = self.ground.ground_rect()

        #here instead of detecting the overlap between the ball and the ground
        #the coordinates of the ball center have been increased in y direction
        #by the amount of radius of the ball so that the ball instead of getting merged into the ground 
        #stays some distance up from the ground
        #though it is not a good solution and has to be curbed soon

        ball_rect.center = (ball_rect.center[0], ball_rect.center[1] + self.ball.get_radius())
        if not ball_rect.colliderect(ground_rect):
            self.calculate_ball_position()
            self.ball.set_coords(self.flip(*self.ball_coords))

        self.get_scene_surface().fill(self.background_color)
        self.ground.draw()
        self.ball.draw()

    def calculate_ball_position(self):
        get_current_time = time.time() - self.init_time
        x, y = self.ball_coords
        new_y = y + 0.5 * self.acceleration * (get_current_time ** 2)
        new_x = x
        self.ball_coords = (int(new_x), int(new_y))

    def flip(self, x, y, flip_dir = 0):
        new_x, new_y = x, y

        if flip_dir == BallDrop.FLIP_HORIZONTAL:
            new_x = self.get_screen_width() - x
        if flip_dir == BallDrop.FLIP_VERTICAL:
            new_y = self.get_screen_height() - y
        
        return (new_x, new_y)
                
class Ball:

    def __init__(self, display_surf, coords = (0, 0), radius = 10, ball_color = pygame.Color(180, 239, 91)):
            self.display_surf = display_surf
            self.coords = coords
            self.radius = radius
            self.ball_color = ball_color

    def draw(self):
        pygame.draw.circle(self.display_surf, self.ball_color, self.coords, self.radius)

    def set_coords(self, coords):
        self.coords = coords

    def ball_rect(self):
        ball_rect =  pygame.Rect(self.coords[0] - self.radius, self.coords[1] - self.radius, self.radius * 2, self.radius * 2)
        return ball_rect

    def get_radius(self):
        return self.radius

    def get_coords(self):
        return self.coords

class Ground:
    
    LINE_GROUND = 0
    RECTANGLE_GROUND = 1    # to be implemented
    RANDOM_POP_GROUND = 2   # to be implemented 
    REAL_POP_GROUND = 3     # to be implemented 

    def __init__(self, display_surf,  coords_start, coords_end, type_surface = 0, width = 1):
        self.coords_start = coords_start
        self.coords_end = coords_end
        self.type_surface = type_surface
        self.display_surf = display_surf
        self.width = width

    def draw(self):

        if self.type_surface == Ground.LINE_GROUND:
            ground_color = pygame.Color(27, 175, 22)
            pygame.draw.line(self.display_surf, ground_color, self.coords_start, self.coords_end, self.width)

    def ground_rect(self):

        ground_rect = None

        if self.type_surface == Ground.LINE_GROUND:
            ground_rect = pygame.Rect(self.coords_start[0], self.coords_start[1], self.coords_end[0] - self.coords_start[0], self.width)

        return ground_rect

    def get_coords(self):
        return (self.coords_start, self.coords_end)

gph = BallDrop()
gph.run()
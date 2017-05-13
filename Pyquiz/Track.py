import pygame

class Track:
    def __init__(self, name, song):
        self.name = name
        self.song = song

    def playsound(self):
        sound = pygame.mixer.Sound(self.song)
        clock = pygame.time.Clock()
        sound.play()
        while True:
            clock.tick(1)

    def playsong(self):
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(0)
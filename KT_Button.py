import pygame
from pygame.locals import *

class KT_Button():
    
    BUTTON_PRESSED = "button pressed"
    BUTTON_ON_HOLD = "button pressed and roll away"
    BUTTON_EXIST = "button exist"
    
    
    def __init__(self, screen, cord, upImage, downImage):
        self.screen = screen
        self.cord = cord
        self.upImage = pygame.image.load(upImage)
        self.downImage = pygame.image.load(downImage)

        #retrieve the rect(area) of the button for checking whether it's pressed or hover
        self.rect = self.upImage.get_rect()
        self.rect[0] = self.cord[0]       
        self.rect[1] = self.cord[1]

        self.state = KT_Button.BUTTON_EXIST

    def button_update(self, theEvent):
        if theEvent.type not in (MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION):
            return False

        mouseWithinButton = self.rect.collidepoint(theEvent.pos)

        if self.state == KT_Button.BUTTON_EXIST:
            if theEvent.type == MOUSEBUTTONDOWN and mouseWithinButton:
                self.state = KT_Button.BUTTON_PRESSED

        elif self.state == KT_Button.BUTTON_PRESSED:
            if theEvent.type == MOUSEBUTTONUP and mouseWithinButton:
                self.state = KT_Button.BUTTON_EXIST
                return True

            if (theEvent.type == MOUSEMOTION) and not(mouseWithinButton):
                self.state = KT_Button.BUTTON_ON_HOLD

        elif self.state == KT_Button.BUTTON_ON_HOLD:
            if mouseWithinButton:
                self.state = KT_Button.BUTTON_PRESSED
            elif theEvent.type == MOUSEBUTTONUP:
                self.state = KT_Button.BUTTON_EXIST

        return False

    def draw(self):
        if self.state == KT_Button.BUTTON_PRESSED:
            self.screen.blit(self.downImage,(self.cord))
        else:
            self.screen.blit(self.upImage, (self.cord))


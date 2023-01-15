def menu_main():
    import pygame
    from pygame import mixer
    import Platformer
    import TICTACTOE
    import sys

    # Pygame and pygame mixer need to be intialized first, pygame mixer also needs to be pre-initialized with configurations
    pygame.mixer.pre_init(44100, -16, 2, 512)
    mixer.init()
    pygame.init()

    # Stop all music from the other games and initialize main menu music
    pygame.mixer.music.load("sounds/Monsters Inc Theme.mp3")
    pygame.mixer.music.play(-1, 0.0, 6000)
    pygame.mixer.music.set_volume(0.5)

    # Screen
    width = 800
    height = 500
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame project By Mohamed & Zeeina")

    # define font
    font1 = pygame.font.SysFont("French Script MT", 40)

    # Load images
    bd = pygame.image.load("images/OIP.jfif")
    background = pygame.transform.scale(bd, (width, height))
    start = pygame.image.load("images/start_btn.png")
    exitbutton = pygame.image.load("images/exit_btn.png")
    start = pygame.transform.scale(start, (180,80))
    exitbutton = pygame.transform.scale(exitbutton, (190, 90))

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        window.blit(img, (x ,y))

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.clicked = False # prevents output spam when reset button clicked

        def draw(self):
            pressed = False # variable to tell the game loop that reset was pressed

            # get mouse position
            pos = pygame.mouse.get_pos()

            # check mouseover and clicked conditions
            if self.rect.collidepoint(pos): # mouse is considered a point so this tests if button rect collided with it ( mouse over it )
                # the following produces a list with 0s and 1s depending on what has been clicked
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # left mouse button is index 0, clicked = 1
                    pressed = True
                    self.clicked = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
            # draw button
            window.blit(self.image, self.rect)

            return pressed


    # Create buttons
    start_button = Button(width // 2 - 350, height // 2 - 100, start)
    start_button1 = Button(width // 2 + 170, height // 2 - 100, start)
    exit_button = Button(width // 2 - 90, height - 150, exitbutton)


    # menu loop
    run = True
    while run:

        # Drawing objects onto screen
        window.blit(background, (0, 0))
        draw_text("Platformer", font1, (255,255,255), 65, 100)
        draw_text("Tic-tac-toe", font1, (255,255,255), width - 210, 100)

        if exit_button.draw():
            pygame.quit()
            sys.exit()
        if start_button.draw():
            #import Platformer
            Platformer.platformer()
            run = False
        if start_button1.draw():
            #import TICTACTOE
            TICTACTOE.ttt()
            run = False

        # Update display
        pygame.display.update()

        # close event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

menu_main()
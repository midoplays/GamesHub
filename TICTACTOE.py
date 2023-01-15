clicked = False
def ttt():
    import main_menu
    import pygame
    import sys
    pygame.init()  # initializing
    pygame.mixer.music.stop()

    def tictactoe():
        import numpy as np


        c1 = (252, 193, 240)  # line colors
        c2 = (204, 255, 255)
        c3 = (255, 255, 153)
        c4 = (204, 255, 204)

        mouseclick = pygame.mixer.Sound("sounds/mc.wav")  # background music and mouseclick sound
        winningsound = pygame.mixer.Sound("sounds/WSE.wav")
        bgmusic = pygame.mixer.music.load("sounds/bread.wav")
        pygame.mixer.music.play(-1)

        bgc = (255, 255, 255)  # background color
        sch = 600  # screen height
        scw = 600  # screen width
        br = 3  # board rows
        bc = 3  # board cols
        cr = 60  # circle radius
        cw = 15  # circle width
        xw = 25  # X width
        space = 55
        cc = (223, 192, 255)  # O color
        xc = (252, 222, 178)  # X color

        sc = pygame.display.set_mode((scw, sch))  # game window creation
        pygame.display.set_caption(("tic-tac-toe"))  # setting a caption

        # bg= pygame.image.load('C:/Users/zeena/OneDrive/Desktop/img/bg.jpg')

        board = np.zeros((br, bc))

        sc.fill(bgc)
        pygame.draw.line(sc, c1, (190, 20), (190, 580), 10)  # drawing game lines
        pygame.draw.line(sc, c2, (390, 20), (390, 580), 10)  # (screen, color, line coordinates, line width)
        pygame.draw.line(sc, c3, (20, 190), (580, 190), 10)
        pygame.draw.line(sc, c4, (20, 390), (580, 390), 10)

        def XO():
            for row in range(br):
                for col in range(bc):
                    if board[row][col] == 1:
                        pygame.draw.circle(sc, cc, (int(col * 200 + 200 / 2), int(row * 200 + 200 / 2)), cr,
                                           cw)  # surface, color, position , radius , width
                    elif board[row][col] == 2:
                        pygame.draw.line(sc, xc, (col * 200 + space, row * 200 + 200 - space),
                                         (col * 200 + 200 - space, row * 200 + space), xw)
                        pygame.draw.line(sc, xc, (col * 200 + space, row * 200 + space),
                                         (col * 200 + 200 - space, row * 200 + 200 - space), xw)

        def marksquare(row, col, player):  # parameters
            board[row][col] = player

        def avaisquare(row, col):  # checking if the square is checked or not
            return board[row][col] == 0

        def checkwin(player):  # check if the player won
            # VL
            for col in range(bc):
                if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                    vertL(col, player)
                    return True

            # HL
            for row in range(br):
                if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                    horiL(row, player)
                    return True

            # ascL
            if board[2][0] == player and board[1][1] == player and board[0][2] == player:
                ascdiaL(player)
                return True

            # descL
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                desdiaL(player)
                return True

            return False  # if theres no win

        def vertL(col, player):  # draws the vertical winning line
            posX = col * 200 + 100
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (posX, 15), (posX, sch - 15), 15)

        def horiL(row, player):  # draws the horizontal winning line
            posY = row * 200 + 100
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (15, posY), (scw - 15, posY), 15)

        def ascdiaL(player):  # ascending diagonal line
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (15, sch - 15), (scw - 15, 15), 15)

        def desdiaL(player):  # descending diagonal line
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (15, 15), (scw - 15, sch - 15), 15)

        player = 1
        gameover = False
        run = True
        while run == True:  # running the game

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    run = False  # quitting the game

                if i.type == pygame.MOUSEBUTTONDOWN and not gameover:

                    mouseX = i.pos[1]  # x
                    mouseY = i.pos[0]  # y

                    clickR = int(mouseX // 200)
                    clickC = int(mouseY // 200)

                    pygame.mixer.Sound.play(mouseclick)  # mouseclicksound

                    if avaisquare(clickR, clickC):
                        if player == 1:
                            marksquare(clickR, clickC, 1)
                            if checkwin(player):
                                gameover = True
                            player = 2

                        elif player == 2:
                            marksquare(clickR, clickC, 2)
                            if checkwin(player):
                                gameover = True
                            player = 1
                    if gameover == True:
                        pygame.mixer.Sound.play(winningsound)

                    XO()

            pygame.display.update()  # update the display window


                # if i.type == pygame.KEYDOWN:  # if i.key == pygame.K_r:  # restart()

        #pygame.display.update()  # update the display window


    def tictactoe2():
        import numpy as np

        pygame.mixer.init()

        c1 = (252, 193, 240)  # line colors
        c2 = (204, 255, 255)
        c3 = (255, 255, 153)
        c4 = (204, 255, 204)

        mouseclick = pygame.mixer.Sound("sounds/mc.wav")  # background music and mouseclick sound
        winningsound = pygame.mixer.Sound("sounds/WSE.wav")
        bgmusic = pygame.mixer.music.load('sounds/bread.wav')
        pygame.mixer.music.play(-1)

        bgc = (255, 255, 255)  # background color
        sch = 600  # screen height
        scw = 600  # screen width
        br = 5  # board rows
        bc = 5  # board cols
        cr = 35  # circle radius
        cw = 10  # circle width
        xw = 13  # X width
        space = 90
        cc = (223, 192, 255)  # O color
        xc = (252, 222, 178)  # X color

        sc = pygame.display.set_mode((scw, sch))  # game window creation
        pygame.display.set_caption(("tic-tac-toe"))  # setting a caption

        # bg= pygame.image.load('C:/Users/zeena/OneDrive/Desktop/img/bg.jpg')

        board = np.zeros((br, bc))

        sc.fill(bgc)
        pygame.draw.line(sc, c1, (120, 20), (120, 580), 10)  # drawing game lines
        pygame.draw.line(sc, c2, (240, 20), (240, 580), 10)  # (screen, color, line coordinates, line width)
        pygame.draw.line(sc, c3, (20, 120), (580, 120), 10)
        pygame.draw.line(sc, c4, (20, 240), (580, 240), 10)
        pygame.draw.line(sc, c2, (20, 360), (580, 360), 10)
        pygame.draw.line(sc, c4, (360, 20), (360, 575), 10)
        pygame.draw.line(sc, c1, (480, 20), (480, 575), 10)
        pygame.draw.line(sc, c3, (20, 480), (580, 480), 10)

        def XO():
            for row in range(br):
                for col in range(bc):
                    if board[row][col] == 1:
                        pygame.draw.circle(sc, cc, (int(col * 120 + 120 / 2), int(row * 120 + 120 / 2)), cr,
                                           cw)  # surface, color, position , radius , width
                    elif board[row][col] == 2:
                        pygame.draw.line(sc, xc, (col * 120 + space, row * 120 + 120 - space),
                                         (col * 120 + 120 - space, row * 120 + space), xw)
                        pygame.draw.line(sc, xc, (col * 120 + space, row * 120 + space),
                                         (col * 120 + 120 - space, row * 120 + 120 - space), xw)

        def marksquare(row, col, player):  # parameters
            board[row][col] = player

        def avaisquare(row, col):  # checking if the square is checked or not
            return board[row][col] == 0

        def checkwin(player):  # check if the player won
            # VL
            for col in range(bc):
                if board[0][col] == player and board[1][col] == player and board[2][col] == player and board[3][
                    col] == player:
                    vertLT(col, player)
                    return True
            for col in range(bc):
                if board[1][col] == player and board[2][col] == player and board[3][col] == player and board[4][
                    col] == player:
                    vertLB(col, player)
                    return True

            # HL
            for row in range(br):
                if board[row][0] == player and board[row][1] == player and board[row][2] == player and board[row][
                    3] == player:
                    horiLL(row, player)
                    return True
            for row in range(br):
                if board[row][1] == player and board[row][2] == player and board[row][3] == player and board[row][
                    4] == player:
                    horiLR(row, player)
                    return True

            # ascL
            if board[4][0] == player and board[3][1] == player and board[2][2] == player and board[1][3] == player:
                ascdiaLT(player)
                return True
            if board[3][1] == player and board[2][2] == player and board[1][3] == player and board[0][4] == player:
                ascdiaLB(player)
                return True

            if board[3][0] == player and board[2][1] == player and board[1][2] == player and board[0][3] == player:
                topasc(player)
                return True
            if board[4][1] == player and board[3][2] == player and board[2][3] == player and board[1][4] == player:
                bottomasc(player)
                return True

            # descL
            if board[0][0] == player and board[1][1] == player and board[2][2] == player and board[3][3] == player:
                desdiaLT(player)
                return True
            if board[1][1] == player and board[2][2] == player and board[3][3] == player and board[4][4] == player:
                desdiaLB(player)
                return True

            if board[0][1] == player and board[1][2] == player and board[2][3] == player and board[3][4] == player:
                topdes(player)
                return True
            if board[1][0] == player and board[2][1] == player and board[3][2] == player and board[4][3] == player:
                bottomdes(player)
                return True

            return False  # if theres no win

        def vertLT(col, player):  # draws the vertical winning line,  vertical line top
            posX = col * 120 + 60
            if player == 1:
                color = cc
            elif player == 2:
                color = xc
            pygame.draw.line(sc, color, (posX , 15), (posX , sch - 135), 10)

        def vertLB(col, player):  # draws the vertical winning line,  vertical line bottom
            posX = col * 120 + 60
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (posX, 135), (posX, sch - 15), 10)

        def horiLL(row, player):  # draws the horizontal winning line left
            posY = row * 120 + 60
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (15, posY), (scw - 135, posY), 10)

        def horiLR(row, player):  # draws the horizontal winning line right
            posY = row * 120 + 60
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (135, posY), (scw - 15, posY), 10)

        def ascdiaLB(player):  # ascending diagonal line
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (135, 465), (585, 15), 10)

        def ascdiaLT(player):  # ascending diagonal line
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (15, 585), (465, 135), 10)

        def desdiaLT(player):  # descending diagonal line top
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (15, 15), (scw - 135, sch - 135), 10)

        def desdiaLB(player):  # descending diagonal line bottom
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (135, 135), (scw - 15, sch - 15), 10)

        def topasc(player):
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (15, 465), (465, 15), 10)

        def bottomasc(player):
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (135, 585), (585, 135), 10)

        def topdes(player):
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (135, 15), (585, 465), 10)

        def bottomdes(player):
            if player == 1:
                color = cc
            elif player == 2:
                color = xc

            pygame.draw.line(sc, color, (15, 135), (465, 585), 10)

        player = 1
        gameover = False
        run = True

        while run == True:  # running the game

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    run = False  # quitting the game

                if i.type == pygame.MOUSEBUTTONDOWN and not gameover:

                    mouseX = i.pos[1]  # x
                    mouseY = i.pos[0]  # y

                    clickR = int(mouseX // 120)
                    clickC = int(mouseY // 120)

                    pygame.mixer.Sound.play(mouseclick)  # mouseclicksound

                    if avaisquare(clickR, clickC):
                        if player == 1:
                            marksquare(clickR, clickC, 1)
                            if checkwin(player):
                                gameover = True
                            player = 2

                        elif player == 2:
                            marksquare(clickR, clickC, 2)
                            if checkwin(player):
                                gameover = True
                            player = 1
                    if gameover == True:
                        pygame.mixer.Sound.play(winningsound)
                    XO()

            pygame.display.update()  # update the display window






    screen_width = 600
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('main page')

    font = pygame.font.SysFont('Constantia', 30)
    background = (pygame.image.load('images/2.jpg'))
    #define colors

    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)

    #define variable
    clicked = False
    counter = 0

    class button():

        #colors for button and text
        button_col = (252, 193, 240)
        hover_col = (204, 225, 255)
        click_col = (255, 255, 153)
        text_col = (204,0,0)
        width = 220
        height = 90

        def __init__(self, a, b, text):
            self.a = a
            self.b = b
            self.text = text

        def draw_button(self):

            global clicked
            action = False

            #get mouse position
            pos = pygame.mouse.get_pos()

            #create pygame Rect object for the button
            button_rect = pygame.Rect(self.a, self.b, self.width, self.height)

            #check mouseover
            if button_rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    clicked = True
                    pygame.draw.rect(screen, self.click_col, button_rect)
                elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                    clicked = False
                    action = True
                else:
                    pygame.draw.rect(screen, self.hover_col, button_rect)
            else:
                pygame.draw.rect(screen, self.button_col, button_rect)

            #add shading to button
            pygame.draw.line(screen, white, (self.a, self.b), (self.a + self.width, self.b), 4)
            pygame.draw.line(screen, white, (self.a, self.b), (self.a, self.b + self.height), 4)
            pygame.draw.line(screen, black, (self.a, self.b + self.height), (self.a + self.width, self.b + self.height), 4)
            pygame.draw.line(screen, black, (self.a + self.width, self.b), (self.a + self.width, self.b + self.height), 4)

            #add text to button
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            screen.blit(text_img, (self.a + int(self.width / 4) - int(text_len / 4), self.b + 25))
            return action



    x = button(75, 200, 'Tic Tac Toe 3x3')
    y= button(325, 200, 'Tic Tac Toe 5x5')
    z= button(175 ,300 , "Exit")


    run = True
    while run:

        screen.blit(background,(0,0))

        if x.draw_button():
            tictactoe()
            counter = 0
        if y.draw_button():
            tictactoe2()
        if z.draw_button():
            main_menu.menu_main()
            run = False
            sys.exit()

        counterimg = font.render(str(counter), True, red)
        screen.blit(counterimg, (280, 450))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        pygame.display.update()
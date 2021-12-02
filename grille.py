import pygame


width=800
heigth= 800
line_color=(0,0,0)
white=(255,255,250)
black=(0,0,0)
red=()
grid=[]
col=[]
lin=[]

def grille():
    pygame.init()

    screen = pygame.display.set_mode((width, heigth))
    screen.fill(black)
    carre = (0, 0, width/3*2, heigth)
    pygame.draw.rect(screen, white, carre)


    nb_col=7






    pygame.draw.line(carre,line_color,(width/nb_col,0),(width/nb_col,heigth),3)
    pygame.draw.line(carre, line_color,(width/nb_col*2,0),(width/nb_col*2,heigth),3)

    pygame.draw.line(carre,line_color,(0,heigth/nb_col),(400,heigth/nb_col),3)
    pygame.draw.line(carre,line_color,(0,heigth/nb_col*2),(400,heigth/nb_col*2),3)

    running=True

    while running:
        pygame.display.flip()
        for i in range(1, nb_col + 1):
            grid.append(pygame.rect.Rect(i * width / nb_col, 0, 7, heigth))
            col.append(i * width / nb_col)
            grid.append(pygame.rect.Rect(0, i * heigth / nb_col, width, 7))
            lin.append(i * heigth / nb_col)

        for i in range(nb_col):
            print("col", col[i])
            print("line", lin[i])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running= False

if __name__ == "__main__":
    grille()



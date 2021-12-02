import pygame



width=800
heigth= 800
width2=width//3*2
surface=width2*heigth
gris=(60,60,60)
black=(0,0,0)
white=(255,255,255)
grid=[]
col=[]
lin=[]
easy = 7

def grille():
    screen = pygame.display.set_mode((width, heigth))
    screen.fill(black)
    pygame.display.set_caption("Mot Mélee")
    pygame.init()
    carre=(0,0,width2,heigth)
    pygame.draw.rect(screen, gris,carre)





    nb_col=(7)
    for i in range(1, nb_col + 1):
            grid.append(pygame.rect.Rect(i * width2 / nb_col, 0, 3, heigth))
            col.append(i * width2 / nb_col)
            grid.append(pygame.rect.Rect(0, i * heigth / nb_col, width2, 3))
            lin.append(i * heigth / nb_col)

    for i in range(nb_col):
            print("col", col[i])
            print("line", lin[i])




    running=True

    while running:
        pygame.display.flip()
        for trace in range(nb_col):
            pygame.draw.rect(screen, white, grid[2 * trace])
            pygame.draw.rect(screen, white, grid[2 * trace + 1])


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running= False

if __name__ == "__main__":
    grille()



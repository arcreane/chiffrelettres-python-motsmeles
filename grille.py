import pygame



width=800
heigth= 800
width2=width//3*2
surface=width2*heigth
white=(255,255,250)
black=(0,0,0)
red=(255,0,0)
grid=[]
col=[]
lin=[]

def grille():
    screen = pygame.display.set_mode((width, heigth))
    screen.fill(black)
    pygame.display.set_caption("Mot Mélee")
    pygame.init()





    nb_col=7
    for i in range(0, nb_col + 1):
            grid.append(pygame.rect.Rect(i * width2 / nb_col, 0, 7, heigth))
            col.append(i * width2 / nb_col)
            grid.append(pygame.rect.Rect(0, i * heigth / nb_col, width2, 7))
            lin.append(i * heigth / nb_col)

    for i in range(nb_col):
            print("col", col[i])
            print("line", lin[i])




    running=True

    while running:
        pygame.display.flip()
        for trace in range(nb_col):
            pygame.draw.rect(screen, red, grid[2 * trace])
            pygame.draw.rect(screen, red, grid[2 * trace + 1])


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running= False

if __name__ == "__main__":
    grille()



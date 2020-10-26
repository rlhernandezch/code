import sys, pygame
pygame.init()
size = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego BALL")
width, height = 800,600
speed = [1, 1]
white = 255, 255, 255

ball = pygame.image.load("/home/tr011/github/code/code/python/attack/pygame/ball.jpeg")
ballrect = ball.get_rect()
run=True
while run:
    pygame.time.delay(2)
    for event in pygame.event.get():        
        if event.type == pygame.QUIT: run = False
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0]= -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()
pygame.quit()

import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("EX3")
icon = pygame.image.load('2250026_game_gameboy_handheld_nintendo_portable_icon.png')
pygame.display.set_icon(icon)

bg_sound = pygame.mixer.Sound('1min-2021-10-19_-_Funny_Bit_-_www.FesliyanStudios.com.mp3')
bg_sound.play()

#Player
bg_image = pygame.image.load('background.png').convert_alpha()
walk_left = [
pygame.image.load('pl_1.png').convert_alpha(),
pygame.image.load('pl_2.png').convert_alpha(),
pygame.image.load('pl_3.png').convert_alpha(),]
walk_right = [
pygame.image.load('pl_1_right.png').convert_alpha(),
pygame.image.load('pl_2right.png').convert_alpha(),
pygame.image.load('pl_3right.png').convert_alpha(),]


ded = pygame.image.load('ded.png').convert_alpha()

ded_list_in_game = []



player_anim_count = 0
bg_x = 0

player_y = 550
player_speed = 2
player_x = 150

is_jump = False
jump_count = 12
jump = False
follow = False




ded_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ded_timer, 1000)

label = pygame.font.Font('OldMan.ttf', 180)
lose_lable = label.render('YOU LOSE', False, (255, 255, 255))
restart_lable = label.render('PLAY AGAIN', False, (25, 25, 112))
restart_lable_react = restart_lable.get_rect(topright=(1360, 430))


gameplay = True



running = True
while running:

    ((3+ 1600, 0))screen.blit(bg_image, (bg_x, 0))
    screen.blit(bg_image, (bg_x

    if gameplay:

        player_rect = walk_right[0].get_rect(topright=(player_x, player_y))


        if ded_list_in_game:
            for (i, el) in enumerate(ded_list_in_game):
                screen.blit(ded, el)
                el.x -= 3

                if el.x < -10:
                    ded_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))





    #WALK
        if keys[pygame.K_LEFT] and player_x > -5:
            player_x -= player_speed
        elif keys [pygame.K_RIGHT] and player_x < 1520:
            player_x += player_speed
    #JUMP
        if not jump:
            if keys[pygame.K_SPACE]:
                jump = True


        if jump:
            if not follow:
                player_y -= 2
                if player_y == 300: follow = True
            else:
                player_y += 2
                if player_y == 550:
                    follow = False
                    jump = False







        if player_anim_count == 2:
            player_anim_count = 0
        else:
            player_anim_count += 1




        bg_x -= 1
        if bg_x == -1600:
            bg_x = 0
    else:
        screen.fill((135, 206, 235))
        screen.blit(lose_lable, (390, 160))
        screen.blit(restart_lable, restart_lable_react)


        mouse = pygame.mouse.get_pos()
        if restart_lable_react.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ded_list_in_game.clear()


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ded_timer:
            ded_list_in_game.append(ded.get_rect(topright=(1620, 550)))

        clock.tick(60)
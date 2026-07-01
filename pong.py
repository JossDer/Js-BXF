##Télécharger pygame dans le terminal : py -m pip install pygame ##

import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 600
fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

raquette_j1 = pygame.Rect(20, 260, 30, 90)
raquette_j2 = pygame.Rect(870, 260, 30, 90)
balle = pygame.Rect(450, 300, 20, 20)

# =========================
# VITESSE
# =========================
ball_speed = 7
max_ball_speed = 15

ball_dx = random.choice([-ball_speed, ball_speed])
ball_dy = random.choice([-ball_speed, ball_speed])

score_j1 = 0
score_j2 = 0
max_score = 10
gagnant = ""

police = pygame.font.SysFont("Arial", 50)
police_small = pygame.font.SysFont("Arial", 30)

rebond_raquette = pygame.mixer.Sound("Desktop/Coding/269718__michorvath__ping-pong-ball-hit.wav")
rebond_mur = pygame.mixer.Sound("Desktop/Coding/freesound_community-ping-pong-ball-100074.wav")
point = pygame.mixer.Sound("Desktop/Coding/freesound_community-short-success-sound-glockenspiel-treasure-video-game-6346.mp3")

pygame.mixer.music.load("Desktop/Coding/dream-protocol-ping-pong-classic-arcade-game-116818.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

texture_r1 = pygame.image.load("Desktop/Coding/raquette rouge bon.jpg").convert_alpha()
texture_r1 = pygame.transform.scale(texture_r1, (50, 50))

texture_r2 = pygame.image.load("Desktop/Coding/raquette noir.jpg").convert_alpha()
texture_r2 = pygame.transform.scale(texture_r2, (50, 50))

balle_img = pygame.image.load("Desktop/Coding/balle.png").convert_alpha()
balle_img = pygame.transform.scale(balle_img, (balle.width, balle.height))

jeu_actif = True
game_over = False

while jeu_actif:
    clock.tick(60)

    if not game_over:

        fenetre.fill((128, 128, 128))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_actif = False

        touches = pygame.key.get_pressed()

        if touches[pygame.K_z]:
            raquette_j1.y -= 10
        if touches[pygame.K_s]:
            raquette_j1.y += 10

        if touches[pygame.K_UP]:
            raquette_j2.y -= 10
        if touches[pygame.K_DOWN]:
            raquette_j2.y += 10

        raquette_j1.y = max(0, min(HEIGHT - raquette_j1.height, raquette_j1.y))
        raquette_j2.y = max(0, min(HEIGHT - raquette_j2.height, raquette_j2.y))

        balle.x += ball_dx
        balle.y += ball_dy

        # rebond murs
        if balle.top <= 0 or balle.bottom >= HEIGHT:
            ball_dy *= -1
            rebond_mur.play()

        # =========================
        # COLLISION RAQUETTE 1
        # =========================
        if balle.colliderect(raquette_j1):
            ball_dx = abs(ball_dx) + 1
            ball_dy = ball_dy + 1 if ball_dy > 0 else ball_dy - 1

            ball_dx = min(ball_dx, max_ball_speed)
            ball_dy = max(-max_ball_speed, min(ball_dy, max_ball_speed))

            balle.left = raquette_j1.right
            rebond_raquette.play()

        # =========================
        # COLLISION RAQUETTE 2
        # =========================
        if balle.colliderect(raquette_j2):
            ball_dx = -abs(ball_dx) - 1
            ball_dy = ball_dy + 1 if ball_dy > 0 else ball_dy - 1

            ball_dx = max(ball_dx, -max_ball_speed)
            ball_dy = max(-max_ball_speed, min(ball_dy, max_ball_speed))

            balle.right = raquette_j2.left
            rebond_raquette.play()

        # SCORE J1
        if balle.right >= WIDTH:
            score_j1 += 1
            balle.x = WIDTH // 2
            balle.y = HEIGHT // 2

            ball_speed = 7
            ball_dx = -ball_speed
            ball_dy = random.choice([-ball_speed, ball_speed])

            point.play()

        # SCORE J2
        if balle.left <= 0:
            score_j2 += 1
            balle.x = WIDTH // 2
            balle.y = HEIGHT // 2

            ball_speed = 7
            ball_dx = ball_speed
            ball_dy = random.choice([-ball_speed, ball_speed])

            point.play()

        if score_j1 >= max_score:
            game_over = True
            gagnant = "Joueur 1"

        if score_j2 >= max_score:
            game_over = True
            gagnant = "Joueur 2"

        for y in range(0, HEIGHT, 30):
            pygame.draw.rect(fenetre, (255, 255, 255), (WIDTH // 2 - 2, y, 4, 20))

        texture_j1 = pygame.transform.scale(texture_r1, (raquette_j1.width, raquette_j1.height))
        texture_j2 = pygame.transform.scale(texture_r2, (raquette_j2.width, raquette_j2.height))

        fenetre.blit(texture_j1, raquette_j1.topleft)
        fenetre.blit(texture_j2, raquette_j2.topleft)

        fenetre.blit(balle_img, balle.topleft)

        score_text = police.render(f"{score_j1} - {score_j2}", True, (255, 255, 255))
        fenetre.blit(score_text, (WIDTH // 2 - 40, 20))

    else:

        fenetre.fill((128, 128, 128))

        game_over_text = police.render("GAME OVER", True, (255, 80, 80))
        texte = police_small.render(f"{gagnant} a gagné !", True, (255, 255, 255))
        fin = police_small.render("K = quitter", True, (200, 200, 200))

        fenetre.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 200))
        fenetre.blit(texte, (WIDTH // 2 - texte.get_width() // 2, 280))
        fenetre.blit(fin, (WIDTH // 2 - fin.get_width() // 2, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_actif = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    jeu_actif = False

    pygame.display.flip()

pygame.quit()
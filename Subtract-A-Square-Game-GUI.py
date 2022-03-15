# Description : Subtract a square Game
# Author : Seif Yahia
# Version : 3.0
# Date : 5 Mar. 2022

import pygame
from time import sleep
pygame.init()

n_coins = 50
sq_num = [1, 4, 9, 16, 25, 36, 49]

user_move, player = '', "First"

width, height = 800, 600
gameDisplay = pygame.display.set_mode((width, height))
title = pygame.display.set_caption("Subtract a square game!")

pile = pygame.image.load("pile.png")
pile = pygame.transform.scale(pile, (330, 360))
background = pygame.image.load("bkgrnd.jpg")
background = pygame.transform.scale(background, (width, height))

greeting_font = pygame.font.SysFont('calibri', 32, bold=True)
major_font = pygame.font.SysFont('calibri', 26, bold=True)
user_font = pygame.font.SysFont('monospace', 72, bold=True)
end_font = pygame.font.SysFont('calibri', 72, bold=True)

show_box = pygame.Rect(480, 220, 0, 0)
order_box = pygame.Rect(30, 330, 0, 0)
input_box = pygame.Rect(180, 380, 0, 0)


def greeting():
    gameDisplay.blit(
        greeting_font.render(
            "Welcome to subtract a square game!",
            True, 'black'), (150, 30))
    gameDisplay.blit(
        major_font.render(
            "In this game there is a pile of coins that contain 50 coins.",
            True, 'black'), (30, 80))
    gameDisplay.blit(
        major_font.render(
            "Players take turns removing coins from the pile.",
            True, 'black'), (30, 105))
    gameDisplay.blit(
        major_font.render(
            "The player who removes the last coin wins!",
            True, 'black'), (30, 130))
    gameDisplay.blit(
        major_font.render(
            "Good Luck!!", True, 'black'), (30, 155))
    gameDisplay.blit(
        major_font.render(
            player + " player,", True, 'black'), (180, 300))


def change_player():
    global player
    if player == "First":
        player = "Second"
        gameDisplay.blit(major_font.render(player, True, 'black'), (180, 300))
    else:
        player = "First"
        gameDisplay.blit(major_font.render(player, True, 'black'), (180, 300))


def check_input(num):
    global user_move, n_coins
    if int(user_move) in sq_num and n_coins - int(user_move) >= 0:
        n_coins -= num
        user_move = ''
        change_player()


def take_move():
    global user_move, done
    done = False
    order = major_font.render(
        "Enter a square number then press ENTER:", True, 'black')
    gameDisplay.blit(order, (order_box.x, order_box.y))
    text = user_font.render(user_move, True, 'black')

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            pygame.quit()

        if action.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(action.pos):
                done = True
            else:
                done = False

        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_BACKSPACE:
                user_move = user_move[:-1]
            elif action.key == pygame.K_RETURN:
                if user_move != '':
                    check_input(int(user_move))
                else:
                    done = True
            else:
                if action.unicode.isdigit():
                    user_move += action.unicode
                    if text.get_width() > input_box.w - 35:
                        user_move = user_move[:-1]

    pygame.draw.rect(gameDisplay, 'white', input_box, 0, 15)
    input_box.w = max(120, text.get_width()+10)
    input_box.h = max(80, text.get_height())

    if text.get_width() < input_box.w - 35:
        gameDisplay.blit(text, (input_box.x+38, input_box.y))
    else:
        gameDisplay.blit(text, (input_box.x+18, input_box.y))

    pygame.display.update()


def rem_coins():
    show = major_font.render("Remaining coins in the pile:", True, 'black')
    gameDisplay.blit(show, (show_box.x, show_box.y))
    gameDisplay.blit(pile, (460, 230))
    pygame.draw.circle(gameDisplay, (64, 210, 131), (628, 463), 40)
    circle = user_font.render(str(n_coins), True, 'black')

    if n_coins < 10:
        gameDisplay.blit(circle, (605, 422))
    else:
        gameDisplay.blit(circle, (585, 422))


def end_game():
    change_player()
    gameDisplay.blit(background, (0, 0))
    result = end_font.render("Congratulations!! ", True, 'black')
    result2 = end_font.render(f"{player} player has won.", True, 'black')
    thanks = end_font.render("Thank You!", True, 'black')

    gameDisplay.blit(result, (130, 100))
    if player == "First":
        gameDisplay.blit(result2, (90, 200))
    else:
        gameDisplay.blit(result2, (50, 200))
    gameDisplay.blit(thanks, (220, 400))

    pygame.display.update()
    sleep(5)


def play():
    while True:
        gameDisplay.blit(background, (0, 0))
        greeting()
        rem_coins()
        take_move()
        if n_coins == 0:
            end_game()
            break
        pygame.display.update()
        pygame.time.Clock().tick(30)

play()

#!/usr/bin/env python3
## Tic Tac Toe
## 2 player or AI
## Started: 10/06/2020
## Finished: 
## by Arthur Boucard

import pygame
import random
import time
import math
import numpy as np

black = (0, 0, 0)
grey = (122, 122, 122)
light_grey = (212, 212, 212)
white = (255, 255, 255)

def button(window, text, w, x, y, z, color, action_color, mode, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if w + y > mouse[0] > w and x + z > mouse[1] > x:
        pygame.draw.rect(window, action_color, (w, x ,y, z))
        if click[0] == 1 and action != None:
            action(window, mode)
            time.sleep(0.2)
        elif click[0] and mode == 0:
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(window, color, (w, x, y, z))
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    text_surf = font.render(text, True, black)
    text_rect = text_surf.get_rect()
    text_rect.center = ((w + (y / 2)), (x + (z / 2)))
    window.blit(text_surf, text_rect)

def display_board(window, board, player):
    window.fill(white)
    pygame.draw.line(window, black, (0, 50), (600, 50), 2)
    pygame.draw.line(window, black, (200, 50), (200, 650), 2)
    pygame.draw.line(window, black, (400, 50), (400, 650), 2)
    pygame.draw.line(window, black, (0, 250), (600, 250), 2)
    pygame.draw.line(window, black, (0, 450), (600, 450), 2)

    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    if player == 0:
        text_surf = font.render("Turn: Player 1", True, black)
    else:
        text_surf = font.render("Turn: Player 2", True, black)
    text_rect = text_surf.get_rect()
    text_rect.center = ((300, 20))
    window.blit(text_surf, text_rect)

    font = pygame.font.Font(pygame.font.get_default_font(), 115)
    pos_x = 100
    pos_y = 150
    pos_box = 0

    for i in range (9):
        text_surf = font.render(board[pos_box], True, black)
        text_rect = text_surf.get_rect()
        text_rect.center = ((pos_x, pos_y))
        window.blit(text_surf, text_rect)
        pos_x += 200
        pos_box += 1
        if i == 2 or i == 5:
            pos_y += 200
            pos_x = 100


def count_space(board):
    nb = 0
    for i in range(9):
        if board[i] == ' ':
            nb += 1
    return nb

def ai_move(board, depth, maximizer):

    def checkgame(board):
        pos1 = 0
        pos2 = 0
        for i in range(3):
            if board[pos1] == board[pos1 + 1] == board[pos1 + 2]:
                if board[pos1] == 'X':
                    return 1
                elif board[pos1] == 'O':
                    return 2
            pos1 += 3
            if board[pos2] == board[pos2 + 3] == board[pos2 + 6]:
                if board[pos2] == 'X':
                    return 1
                elif board[pos2] == 'O':
                    return 2
            pos2 += 1
        if board[0] == board[4] == board[8]:
            if board[0] == 'X':
                return 1
            elif board[0] == 'O':
                return 2
        if board[2] == board[4] == board[6]:
            if board[2] == 'X':
                return 1
            elif board[2] == 'O':
                return 2
        pos = 0
        for i in range(9):
            if board[pos] == ' ':
                return 0
            pos += 1
        return 3

    # if depth == 0 or checkgame(board) != 0:
        

    return board

def board_event(board, player, mode):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if player == 0:
        char = 'X'
    else:
        char = 'O'
    boxes = [[0, 50, 200, 250],
             [200, 50, 400, 250],
             [400, 50, 600, 250],
             [0, 250, 200, 450],
             [200, 250, 400, 450],
             [400, 250, 600, 450],
             [0, 450, 200, 650],
             [200, 450, 400, 650],
             [400, 450, 600, 650]]

    pos_box = 0
    for i in range(9):
        if boxes[pos_box][2] > mouse[0] > boxes[pos_box][0] and boxes[pos_box][3] > mouse[1] > boxes[pos_box][1]:
            if click[0] == 1 and board[pos_box] == ' ':
                board[pos_box] = char
                if player == 0:
                    player = 1
                else:
                    player  = 0
        pos_box += 1
    return board, player

def test_win(window, board):
    if board[0] == board[1] == board[2] and board[0] != ' ':
        pygame.draw.line(window, black, (20, 150), (580, 150), 10)
        return 1
    if board[3] == board[4] == board[5] and board[3] != ' ':
        pygame.draw.line(window, black, (20, 350), (580, 350), 10)
        return 1
    if board[6] == board[7] == board[8] and board[6] != ' ':
        pygame.draw.line(window, black, (20, 550), (580, 550), 10)
        return 1
    if board[0] == board[3] == board[6] and board[0] != ' ':
        pygame.draw.line(window, black, (100, 70), (100, 630), 10)
        return 1
    if board[1] == board[4] == board[7] and board[1] != ' ':
        pygame.draw.line(window, black, (300, 70), (300, 630), 10)
        return 1
    if board[2] == board[5] == board[8] and board[2] != ' ':
        pygame.draw.line(window, black, (500, 70), (500, 630), 10)
        return 1
    if board[0] == board[4] == board[8] and board[0] != ' ':
        pygame.draw.line(window, black, (20, 70), (580, 630), 10)
        return 1
    if board[2] == board[4] == board[6] and board[2] != ' ':
        pygame.draw.line(window, black, (580, 70), (20, 630), 10)
        return 1
    for i in range(9):
        if board[i] == ' ':
            return 0
    return 2

def disp_win_screen(window, player, mode):
    screen = True
    if player == 0:
        text = "Player 2 won!"
    elif player == 1:
        text = "Player 1 won!"
    else:
        text = "Tied"

    while screen == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(window, white, (0, 0 ,600, 50))
        font = pygame.font.Font(pygame.font.get_default_font(), 40)
        text_surf = font.render(text, True, black)
        text_rect = text_surf.get_rect()
        text_rect.center = ((300, 20))
        window.blit(text_surf, text_rect)
        button(window, "Play Again", 200, 200, 200, 80, grey, light_grey, mode, game_loop)
        button(window, "MENU", 200, 300, 200, 80, grey, light_grey, 3, game_intro)
        button(window, "QUIT", 200, 500, 200, 80, grey, light_grey, 0)
        pygame.display.update()

    

def game_loop(window, mode):
    close = False
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    player = random.randint(0, 1)

    time.sleep(0.5)
    while close is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
        board, player = board_event(board, player, mode)
        display_board(window, board, player)
        if test_win(window, board) == 1:
            pygame.display.update()
            time.sleep(0.2)
            disp_win_screen(window, player, mode)
            break
        elif test_win(window, board) == 2:
            pygame.display.update()
            time.sleep(0.2)
            disp_win_screen(window, 2, mode)
            break
        pygame.display.update()
        if player == 1 and mode == 1:
            player = 1
            time.sleep(0.2)
            board = ai_move(board, count_space(board), True)
            display_board(window, board, player)
            win = test_win(window, board)
            pygame.display.update()
            player = 0
    pygame.quit()
    quit()

def game_intro(window, mode):
    intro = True

    time.sleep(0.1)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)
        font = pygame.font.Font(pygame.font.get_default_font(), 80)
        text_surf = font.render('Tic Tac Toe', True, black)
        text_rect = text_surf.get_rect()
        text_rect.center = ((300, 50))
        window.blit(text_surf, text_rect)
        button(window, "1 Player", 200, 200, 200, 80, grey, light_grey, 1, game_loop)
        button(window, "2 Player", 200, 300, 200, 80, grey, light_grey, 2, game_loop)
        button(window, "QUIT", 200, 500, 200, 80, grey, light_grey, 0)
        pygame.display.update()


def main():
    pygame.init()
    window = pygame.display.set_mode((600, 650))
    pygame.display.set_caption('Tic Tac Toe')

    game_intro(window, 0)


if __name__ == '__main__':
    main()
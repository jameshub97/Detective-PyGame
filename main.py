import pygame, time, random
from pygame.locals import *
import pygame.freetype
import datetime
import sys
import os
from pytmx.util_pygame import load_pygame
import math
import music
from pygame import mixer
import images

mixer.init()
mixer.music.load("music/70scopshowchasingbankrobbers.mp3")
mixer.music.set_volume(0.1)


def blit_all_tiles(window, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            #             tiles[0]...x grid
            #             tiles[1]...y grid
            #             tiles[2]...image data for blitting
            x_pixel = tile[0] * 17 + world_offset[0]
            y_pixel = tile[1] * 17 + world_offset[1]
            window.blit(tile[2], (x_pixel, y_pixel))


def get_tile_properties(tmxdata, x, y, world_offest):
    world_x = x - world_offest[0]
    world_y = y - world_offest[1]
    tile_x = world_x // 16
    tile_y = world_y // 16
    try:
        properties = tmxdata.get_tile_properties(tile_x, tile_y, 0)
    except ValueError:
        properties = {"ground": 0, "interactable": 0, "provides": "", "requires": "", "solid": 0}
    if properties is None:
        properties = {"ground": 0, "interactable": 0, "provides": "", "requires": "", "solid": 0}
    return properties


def callpiggiez(inv):
    myfont = pygame.font.SysFont('couriernew', 30)
    textinv = myfont.render("Ask more further info" + str(inv), False, (255, 0, 0))
    textbloodsplatter = myfont.render('1: Run blood splatter analysis', False, (255, 0, 0))
    print()

    textpones = myfont.render('3: Analyse conviscated phones', False, (255, 0, 0))
    wtf = myfont.render('4: ???', False, (255, 0, 0))
    textsuspect = myfont.render('5: Submit Crime Report', False, (255, 0, 0))
    textclose = myfont.render('X: Close Menu', False, (255, 0, 0))

    end = False

    while not end:
        keyspressed2 = pygame.key.get_pressed()
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if keyspressed2[pygame.K_x]:
                end = True
            if inv[0] == 0 and keyspressed2[pygame.K_1]:
                textbloodsplatter = myfont.render('no available items for analysis', False, (255, 0, 0))
            if inv[0] == 'Axe' and keyspressed2[pygame.K_1]:
                textbloodsplatter = myfont.render('Forensics only show wood particles on axe hmmmm', False, (255, 0, 0))

            if keyspressed2[pygame.K_3]:
                print("hello")
                messages(1)
                end = True
            if keyspressed2[pygame.K_4]:
                mixer.music.play()
            if keyspressed2[pygame.K_5]:
                name()

        window.blit(textbloodsplatter, (10, 90))
        window.blit(textinv, (10, 30))
        window.blit(textbloodsplatter, (10, 90))
        window.blit(textpones, (10, 210))
        window.blit(wtf, (10, 270))
        window.blit(textsuspect, (10, 320))
        window.blit(textclose, (10, 380))

        pygame.display.update()


def crimereport(arr):
    print(arr)
    # LVL 1

    garliclvl1 = "Raw Garlic with bite marks into each cloves. Only a mad man would do this..."
    axelvl1 = "Used and slightly blunted axe. Has an engraving stating *PROPERTY OF PICKLE-P*"
    mintslvl1 = "Super strong mints. Un-opened packet with packaging indicating recent purchase"
    toothpaste = "Toothpaste found under a table. Packet indicates recent purchase, why almost empty then?"

    # LVL 2

    myfont = pygame.font.SysFont('couriernew', 30)
    myfontsmaller = pygame.font.SysFont('couriernew', 16)
    textcaseprofile = myfont.render('CASE PROFILE', False, (255, 0, 0))
    textclose = myfontsmaller.render('X: Close Menu', False, (255, 0, 0))
    textitem1 = myfontsmaller.render('Item1: yet to be found', False, (255, 100, 0))
    textitem2 = myfontsmaller.render('Item2: yet to be found', False, (255, 100, 0))
    textitem3 = myfontsmaller.render('Item3: yet to be found', False, (255, 100, 0))
    textitem4 = myfontsmaller.render('Item4: yet to be found', False, (255, 100, 0))

    if arr[0] == 'Axe':
        textitem1 = myfontsmaller.render(axelvl1, False, (255, 100, 0))
    if arr[1] == 'Mints':
        textitem2 = myfontsmaller.render(mintslvl1, False, (255, 100, 0))
    if arr[2] == 'Toothpaste':
        textitem3 = myfontsmaller.render(toothpaste, False, (255, 100, 0))
    if arr[3] == 'Garlic':
        textitem4 = myfontsmaller.render(garliclvl1, False, (255, 100, 0))

    end = False

    while not end:
        keyspressed2 = pygame.key.get_pressed()
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if keyspressed2[pygame.K_x]:
                end = True

        window.blit(textitem1, (10, 90))
        window.blit(textitem2, (10, 150))
        window.blit(textitem3, (10, 210))
        window.blit(textitem4, (10, 270))
        window.blit(textcaseprofile, (10, 30))
        window.blit(textclose, (10, 380))

        pygame.display.update()


def name():
    window.fill((0, 0, 0))
    name = ""
    font = pygame.font.Font(None, 50)
    subject = []
    myfont = pygame.font.SysFont('couriernew', 30)
    textsuspect = myfont.render('Correct', False, (255, 0, 0))
    textclose = myfont.render('X: Close Menu', False, (255, 0, 0))
    end = False
    while not end:
        for evt in pygame.event.get():
            window.blit(textsuspect, (400, 70))
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                    subject.append(evt.unicode)
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                    subject = subject[:-1]
                    '-'.join(subject)
                    ''.join(subject)
                elif evt.key == K_RETURN:
                    name = ""
                elif evt.key == K_TAB:
                    end = True
            elif evt.type == QUIT:
                end = True

        my_lst_str = ''.join(map(str, subject))
        if my_lst_str == 'sage':
            main(1)
        else:
            window.fill((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))

        rect = block.get_rect()
        rect.center = window.get_rect().center
        window.blit(block, rect)

        pygame.display.flip()


def messages(type):
    #
    myfont = pygame.font.SysFont('couriernew', 30)
    myfontsmaller = pygame.font.SysFont('couriernew', 18)
    textmessage = myfont.render("Relevant messages collected: (add timestamps)", False, (255, 0, 0))
    textcluesegment1 = myfontsmaller.render(
        'Sage: did u no fluoride in toothpaste/h20 causes irreversible genetic mutations?', False, (255, 100, 0))
    textcluesegment2 = myfontsmaller.render('Barry:you better stop texting me...', False, (255, 100, 0))
    textcluesegmentbreaker = myfontsmaller.render('--------------------------------------------', False, (255, 0, 0))

    textcluesegment3 = myfontsmaller.render(
        'Noris: I agree with Sage ur bodybuilding diet make u smell evil.y u lose ur cool?.', False, (255, 100, 0))
    textcluesegment4 = myfontsmaller.render('Flex Wheeler: who you think u speaking 2 & dont need charity donations',
                                            False, (255, 100, 0))
    textcluesegment5 = myfontsmaller.render(
        'Noris: hmmmmm!! what happened to p?. he on the run after what happened?', False, (255, 100, 0))
    textcluesegment6 = myfontsmaller.render('Flex Wheeler: lmao i know how 2 b fresh i have no time for weaklings',
                                            False, (255, 100, 0))
    textclose = myfont.render('X: Close Menu', False, (255, 100, 0))
    texttab = myfont.render('Tab: Back', False, (255, 100, 0))
    end = False

    while not end:
        keyspressed2 = pygame.key.get_pressed()
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if keyspressed2[pygame.K_x]:
                end = True

        window.blit(textmessage, (10, 30))
        window.blit(textcluesegment1, (10, 90))
        window.blit(textcluesegment2, (10, 150))
        window.blit(textcluesegmentbreaker, (10, 210))
        window.blit(textcluesegment3, (10, 270))
        window.blit(textcluesegment4, (10, 330))
        window.blit(textcluesegment5, (10, 390))
        window.blit(textcluesegment6, (10, 450))
        window.blit(textclose, (10, 510))
        window.blit(texttab, (10, 570))
        pygame.display.update()


def start_menu():
    myfont = pygame.font.SysFont('couriernew', 30)
    textsurface = myfont.render('Space: Deploy Special Investigation Unit', False, (255, 0, 0))
    textsurface2 = myfont.render('N: How to play & Dev Notes', False, (255, 0, 0))
    textsurface3 = myfont.render('ESC: Quit', False, (255, 0, 0))
    hide = myfont.render('', False, (255, 0, 0))

    end = False

    while not end:
        keyspressed = pygame.key.get_pressed()
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                end = True
            if keyspressed[pygame.K_SPACE]:
                main(0)
            if keyspressed[pygame.K_ESCAPE]:
                sys.exit()
            if keyspressed[pygame.K_c]:
                textsurface3 = hide
            elif keyspressed[pygame.K_v]:
                textsurface3 = myfont.render('ESC: Quit', False, (255, 0, 0))

        window.blit(textsurface, (10, 30))
        window.blit(textsurface2, (10, 90))
        window.blit(textsurface3, (10, 150))

        pygame.display.update()


def endpage(time, win):
    myfont = pygame.font.SysFont('couriernew', 30)
    winsurface = myfont.render("That's why you're the best detective ;) " + time, False, (255, 0, 0))
    resetsurface = myfont.render('Space: Redeploy Special Investigation Unit', False, (255, 0, 0))
    losssurface = myfont.render("think more like a detective..." + time + " seconds", False, (255, 0, 0))
    end = False

    while not end:
        keyspressed = pygame.key.get_pressed()
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if keyspressed[pygame.K_SPACE]:
                main(2)
            if keyspressed[pygame.K_ESCAPE]:
                sys.exit()
        if win == "won":
            window.blit(winsurface, (10, 30))
        if win == "loss":
            window.blit(losssurface, (10, 30))
        window.blit(resetsurface, (10, 90))
        pygame.display.update()


def main(win):
    '''''GAME VARIABLES'''''
    tmxdata = load_pygame('tiles/lvl1altt.tmx')
    y_ground = window.get_height() - 170
    myfont = pygame.font.SysFont('couriernew', 20)
    textsurface = myfont.render('Space: Pick up Item  C: Crime Report Tab: Utilities: R: Reset Position', False,
                                (255, 0, 0))
    textsurface2 = myfont.render(str([]), False, (255, 0, 0))
    textsurface2 = myfont.render("", False, (255, 0, 0))
    start_ticks = pygame.time.get_ticks()
    quit = False
    x = 800
    y = y_ground
    inv = [0, 0, 0, 0]

    # L
    item1level1 = "Axe"
    item2level1 = "Mints"
    item3level1 = "Toothpaste"
    item4level1 = "Garlic"

    if win == 0:
        item1 = item1level1
        item2 = item2level1
        item3 = item3level1
        item4 = item4level1
    if win == 1:
        pass

    world_offset = [0, 0]
    start_ticks = pygame.time.get_ticks()

    '''''Core  VARIABLES'''''
    while not quit:
        seconds = (pygame.time.get_ticks() - start_ticks) / math.floor(900.0)  # calculate how many seconds
        textsurfacetime = myfont.render(str(round(seconds, 2)), False, (255, 0, 0))
        textineraact = myfont.render("interactable", False, (255, 0, 0))
        window.fill((0, 0, 0))
        # blit_all_tiles(window, tmxdata, world_offset)
        # keyspressed = pygame.key.get_pressed()
        blit_all_tiles(window, tmxdata, world_offset)
        window.blit(textsurface, (0, 0))
        window.blit(textsurface2, (10, 30))
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
        "GAME LOGIC HERE"
        window.blit(textsurfacetime, (400, 70))
        standing_on_plus = get_tile_properties(tmxdata, x + 8, y + 8, world_offset)
        standing_on_minus = get_tile_properties(tmxdata, x - 16, y - 16, world_offset)
        wall_plus = get_tile_properties(tmxdata, x + 2 + 2, y + 2 + 2, world_offset)
        wall_minus = get_tile_properties(tmxdata, x - 2, y - 2, world_offset)
        keyspressed = pygame.key.get_pressed()

        # MENU BUTTONS

        textsurface2 = myfont.render(str(inv), False, (255, 0, 0))
        if keyspressed[pygame.K_TAB]:
            callpiggiez(inv)

        if keyspressed[ord(" ")]:
            print("hello")

        if keyspressed[pygame.K_o]:
            print("inv refresshed")
            inv = [0, 0, 0, 0]

        lefttile = get_tile_properties(tmxdata, x - 30, y - 10, world_offset)
        righttile = get_tile_properties(tmxdata, x - 10 + 4, y - 10, world_offset)
        abovetile = get_tile_properties(tmxdata, x - 32, y - 32 - 8, world_offset)
        belowtile = get_tile_properties(tmxdata, x - 16, y - 10 - 10, world_offset)

        if abovetile['interactable'] == 1 or belowtile['interactable'] == 1 or lefttile['interactable'] == 1 or \
                righttile['interactable'] == 1:
            window.blit(textineraact, (10, 70))
            if keyspressed[ord(" ")]:
                if inv != item1:
                    inv[0] = item1
                print("picked up", item1)
        elif abovetile['interactable'] == 2 or belowtile['interactable'] == 2 or lefttile['interactable'] == 2 or \
                righttile['interactable'] == 2:
            window.blit(textineraact, (10, 70))
            if keyspressed[ord(" ")]:
                if inv != item2:
                    inv[1] = item2
                print("picked up", item2)
        elif abovetile['interactable'] == 3 or belowtile['interactable'] == 3 or lefttile['interactable'] == 3 or \
                righttile['interactable'] == 3:
            window.blit(textineraact, (10, 70))
            if keyspressed[ord(" ")]:
                if inv != item3:
                    inv[2] = item3
                print("picked up", item3)

        elif abovetile['interactable'] == 4 or belowtile['interactable'] == 4 or lefttile['interactable'] == 4 or \
                righttile['interactable'] == 4:
            window.blit(textineraact, (10, 70))
            if keyspressed[ord(" ")]:
                if inv != item4:
                    inv[3] = item4
                print("picked up", item4)

        if keyspressed[pygame.K_c]:
            # feed items into this
            crimereport(inv)

        # if inv != item1:
        #     inv[0]  = item1
        # print("picked up", item1)

        # MOVE BUTTONS

        if keyspressed[ord("a")]:
            if lefttile['ground'] == 1:
                x = x - 16
        if keyspressed[ord("d")]:
            if righttile['ground'] == 1:
                x = x + 16
        if keyspressed[ord("w")]:
            if abovetile['ground'] == 1:
                y = y - 16
        if keyspressed[ord("s")]:
            if belowtile['ground'] == 1:
                y = y + 16

        if y < 0:
            y = 0
        if y > window.get_height():
            y = window.get_height() - 50
        if x < 0:
            x = 0
        if x > window.get_width():
            x = window.get_width() - 50

        if keyspressed[pygame.K_r]:
            x = 800
            y = 600

        if seconds >= 120:
            endpage(str(round(seconds, 2)), "loss")
        if win == 1:
            endpage(str(seconds), "won")
        player = Rect(x, y, 16, 16)
        pygame.draw.rect(window, (6, 0, 255), player)
        pygame.display.update()
        # 25 FPS
        clock.tick(25)


if __name__ == '__main__':
    width, height, = 960, 800
    pygame.font.init()
    pygame.init()

    pygame.mixer.init()
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    start_menu()
    # main()
    pygame.quit()

import csv
import os
import random
import pygame



def main():
    '''
    this function runs the whole program and sets up variables from the graphics files
    along with stats for the characters
    :return:
    '''

    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    pygame.display.set_caption('Cerphance')
    clock = pygame.time.Clock()
    font_title = pygame.font.Font('graphics' + os.sep + 'mangati.ttf', 130)
    font_reg = pygame.font.Font('graphics' + os.sep + 'mangati.ttf', 28)
    font_stats = pygame.font.Font('graphics' + os.sep + 'mangati.ttf', 15)
    game_active = False
    htp_menu = False
    level = 0
    player_encounter = False

    player_stats = {'Health': [10], 'Damage': [10], 'Crit Damage': [10], 'Speed': [10], 'Luck': [10],
                    'Corrosion': [10]}
    player_attacks = {'Basic Attack': [1, 1, 0], 'Health Attack': [0, .8, 1], 'Damage Attack': [0, 1.4, 0],
                      'Crit Attack': [0, .9, 2], 'Speed Attack': [0, .6, 3], 'Luck Attack': [0, .7, 4],
                      'Corrosive Attack': [0, .5, 5]}

    enemy_data = data_get_strand()
    strand_max_hp = enemy_data['Health']
    strand_current_hp = strand_max_hp

    player_max_hp = player_stats['Health'][0]
    player_current_hp = player_max_hp



    background_1 = pygame.image.load('graphics' + os.sep + 'Background_1.png').convert_alpha()
    background_1 = pygame.transform.rotozoom(background_1, 0, .25)

    background_2 = pygame.image.load('graphics' + os.sep + 'Background_2.png').convert_alpha()
    background_2 = pygame.transform.rotozoom(background_2, 0, .45)

    player_model = pygame.image.load('graphics' + os.sep + 'Player.png').convert_alpha()
    player_model = pygame.transform.rotozoom(player_model, 0, 0.75)
    player_model_rect = player_model.get_rect(center=(250, 375))

    strand_model = pygame.image.load('graphics' + os.sep + 'strand_enemy.png').convert_alpha()
    strand_model = pygame.transform.rotozoom(strand_model, 0, 0.3)
    strand_model_rect = strand_model.get_rect(center=(700, 325))

    stats_model = pygame.image.load('graphics' + os.sep + 'stats.png').convert_alpha()
    stats_model = pygame.transform.rotozoom(stats_model, 0, 0.1)
    stats_model_rect = stats_model.get_rect(center=(825, 660))

    title_game = font_title.render("{Cerphance}", False, '#29472c')
    title_game_rect = title_game.get_rect(center=(500, 300))

    text_play = font_reg.render('PLAY', False, 'Green')
    text_play_rect = text_play.get_rect(center=(210, 615))

    text_htp = font_reg.render('How to play', False, 'Green')
    text_htp_rect = text_htp.get_rect(center=(510, 615))

    box_text = font_stats.render('100% DAMAGE', False, 'Green')
    box_text_rect = box_text.get_rect(center = (125, 662.5))


    text_htp_2 = font_reg.render("You'll have one attack to start but when ", False, '#29472c')
    text_htp_2_1 = font_reg.render("you finish the first level you'll gain another ", False, '#29472c')
    text_htp_2_2 = font_reg.render("attack based on the highest stat.", False, '#29472c')
    text_htp_2_3 = font_reg.render("Red number is which stat,", False, '#29472c')
    text_htp_2_4 = font_reg.render("White is how much it will increase.", False, '#29472c')

    text_htp_2_rect = text_htp_2.get_rect(center=(480, 310))
    text_htp_2_1_rect = text_htp_2.get_rect(center=(480, 350))
    text_htp_2_2_rect = text_htp_2.get_rect(center=(480, 390))
    text_htp_2_3_rect = text_htp_2.get_rect(center=(480, 430))
    text_htp_2_4_rect = text_htp_2_4.get_rect(center=(480, 470))

    text_quit = font_reg.render('QUIT', False, 'Green')
    text_quit_rect = text_quit.get_rect(center=(790, 615))



    while True:
        '''
        the whole game runs within this while loop drawing all the designs and texts
        '''
        if game_active:
            '''
            this if statement allows the game to display the play information 
            and the characters
            '''
            screen.blit(background_2, (0, 0))
            pygame.draw.rect(screen, '#29472c', pygame.Rect(0, 575, 1000, 175))
            pygame.draw.rect(screen, 'green', pygame.Rect(700, 575, 20, 175))

            hp_stat = font_stats.render(f'{player_stats['Health'][0]}', False, 'green')
            dmg_stat = font_stats.render(f'{player_stats['Damage'][0]}', False, 'green')
            crt_stat = font_stats.render(f'{player_stats['Crit Damage'][0]}', False, 'green')
            spd_stat = font_stats.render(f'{player_stats['Speed'][0]}', False, 'green')
            lck_stat = font_stats.render(f'{player_stats['Luck'][0]}', False, 'green')
            cor_stat = font_stats.render(f'{player_stats['Corrosion'][0]}', False, 'green')

            hp_stat_rect = hp_stat.get_rect(center=(820, 600))
            dmg_stat_rect = dmg_stat.get_rect(center=(820, 660))
            crt_stat_rect = crt_stat.get_rect(center=(820, 720))
            spd_stat_rect = spd_stat.get_rect(center=(970, 600))
            lck_stat_rect = lck_stat.get_rect(center=(970, 660))
            cor_stat_rect = cor_stat.get_rect(center=(970, 720))


            screen.blit(stats_model, stats_model_rect)
            screen.blit(hp_stat,hp_stat_rect)
            screen.blit(dmg_stat, dmg_stat_rect)
            screen.blit(crt_stat, crt_stat_rect)
            screen.blit(spd_stat, spd_stat_rect)
            screen.blit(lck_stat, lck_stat_rect)
            screen.blit(cor_stat, cor_stat_rect)



            if player_encounter:
                '''
                after the first attack dice numbers will appear
                red is the attribute dice
                white is the amount the attribute will increase by
                green is the enemy's damage on you
                '''
                screen.blit(red_dice,red_dice_rect)
                screen.blit(white_dice,white_dice_rect)
                screen.blit(enemy_dice,enemy_dice_rect)

            if strand_current_hp < 1:
                '''
                this allows you to see that the enemy is no longer alive and you win
                '''
                quit_box = pygame.draw.rect(screen, '#29472c', pygame.Rect(670, 550, 240, 130))
                screen.blit(text_quit, text_quit_rect)
            else:
                screen.blit(strand_model, strand_model_rect)
                pygame.draw.rect(screen, 'red', pygame.Rect(650, 190, strand_max_hp, 20))
                pygame.draw.rect(screen, 'green', pygame.Rect(650, 190, strand_current_hp, 20))

            if player_current_hp < 1:
                '''
                player will disappear after your hp is depleted
                '''
                quit_box = pygame.draw.rect(screen, '#29472c', pygame.Rect(670, 550, 240, 130))
                screen.blit(text_quit, text_quit_rect)
            else:
                screen.blit(player_model, player_model_rect)
                pygame.draw.rect(screen, 'red', pygame.Rect(400, 200, player_max_hp, 20))
                pygame.draw.rect(screen, 'green', pygame.Rect(400, 200, player_current_hp, 20))

            if player_current_hp > 0:
                '''
                player can no longer attack after dying
                '''
                if player_attacks['Basic Attack'][0] == 1:
                    basic_box = pygame.draw.rect(screen, 'Grey', pygame.Rect(25, 600, 200, 125))
                    screen.blit(box_text,box_text_rect)


        else:
            '''
            this is when game is not active and displays the title screen
            '''
            screen.blit(background_1, (-100, 0))  # (x,y,w,h)
            play_box = pygame.draw.rect(screen, '#29472c', pygame.Rect(90, 550, 240, 130))
            htp_box = pygame.draw.rect(screen, '#29472c', pygame.Rect(390, 550, 240, 130))
            quit_box = pygame.draw.rect(screen, '#29472c', pygame.Rect(670, 550, 240, 130))
            screen.blit(title_game, title_game_rect)
            screen.blit(text_play, text_play_rect)
            screen.blit(text_htp, text_htp_rect)
            screen.blit(text_quit, text_quit_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
                '''
                this is the combat of the game which uses two dice 
                one for selecting your attribute and the other for 
                applies itself to the attribute
                after you roll the enemy will roll and attack
                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_attacks['Basic Attack'][0] == 1:
                        if basic_box.collidepoint(event.pos):
                            red_roll = dice_6()
                            white_roll = dice_6()
                            enemy_roll = random.randint(1, enemy_data['Dice'])
                            if red_roll == 1:
                                player_current_hp += white_roll
                                player_max_hp += white_roll
                                player_stats['Health'][0] += white_roll
                            elif red_roll == 2:
                                player_stats['Damage'][0] += white_roll
                            elif red_roll == 3:
                                player_stats['Crit Damage'][0] += white_roll
                            elif red_roll == 4:
                                player_stats['Speed'][0] += white_roll
                            elif red_roll == 5:
                                player_stats['Luck'][0] += white_roll
                            elif red_roll == 6:
                                player_stats['Corrosion'][0] += white_roll

                            strand_current_hp -= player_stats['Damage'][0]
                            if strand_current_hp > 0:
                                player_current_hp -= enemy_roll
                            player_encounter = True

                            red_dice = font_title.render(f'{red_roll}', False, 'red')
                            white_dice = font_title.render(f'{white_roll}', False, 'white')
                            enemy_dice = font_title.render(f'{enemy_roll}', False, 'green')

                            red_dice_rect = red_dice.get_rect(center=(300, 200))
                            white_dice_rect = white_dice.get_rect(center=(500, 200))
                            enemy_dice_rect = enemy_dice.get_rect(center=(400, 400))

            if strand_current_hp < 1 or player_current_hp < 1:
                '''
                this activates the button that allows you to leave to the menu after combat is over
                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_box.collidepoint(event.pos):
                        game_active = False
                        strand_current_hp = strand_max_hp
                        player_stats = {'Health': [10], 'Damage': [10], 'Crit Damage': [10], 'Speed': [10],
                                        'Luck': [10],
                                        'Corrosion': [10]}
                        player_attacks = {'Basic Attack': [1, 1, 0], 'Health Attack': [0, .8, 1],
                                          'Damage Attack': [0, 1.4, 0],
                                          'Crit Attack': [0, .9, 2], 'Speed Attack': [0, .6, 3],
                                          'Luck Attack': [0, .7, 4],
                                          'Corrosive Attack': [0, .5, 5]}
                        player_encounter = False

                        player_max_hp = player_stats['Health'][0]
                        player_current_hp = player_max_hp





            else:
                '''
                the follow allows you to click the buttons for starting, how to play and quiting, respectfully
                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if htp_box.collidepoint(event.pos):
                        if htp_menu:
                            htp_menu = False
                        else:
                            htp_menu = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_box.collidepoint(event.pos):
                        pygame.quit()
                        exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_box.collidepoint(event.pos):
                        game_active = True

        if htp_menu:
            pygame.draw.rect(screen, 'Green', pygame.Rect(100, 200, 800, 300))
            screen.blit(text_htp_2, text_htp_2_rect)
            screen.blit(text_htp_2_1, text_htp_2_1_rect)
            screen.blit(text_htp_2_2, text_htp_2_2_rect)
            screen.blit(text_htp_2_3, text_htp_2_3_rect)
            screen.blit(text_htp_2_4, text_htp_2_4_rect)

        pygame.display.update()
        clock.tick(60)




def data_get_strand() -> dict :
    '''
    sorts the data from data.csv
    :return: dictionary of sorted data
    '''
    data = data_gather()
    return {'Name': data[1][0], 'Dice': int(data[1][1]), 'Health': int(data[1][2])}



def data_gather() -> list:
    '''
    grabs items from data.csv
    :return: list of the data in data.csv
    '''
    with open('data.csv', newline='') as f:
        reader = csv.reader(f)
        return list(reader)


def dice_6() -> int:
    '''
    randomizes between 6 numbers
    :return: int
    '''
    return random.randint(1, 6)

    
    


if __name__ == '__main__':
    main()

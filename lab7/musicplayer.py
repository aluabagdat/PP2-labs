import pygame
import sys
    
    
def main():
    pygame.init()
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Music Player")
    pygame.display.set_icon(pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//musicelements//spotifyicon.png"))
    bg = pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//musicelements//backround.png").convert_alpha()
    
    #пишем кнопки для начального экрана
    myfont = pygame.font.Font("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//musicelements//Roboto-Black.ttf", 60)
    text = myfont.render("ready", False, (193, 196, 192))
    buttom_list = [
        text.get_rect(topleft=(10, 200)),
        text.get_rect(topleft=(10, 300)),
        text.get_rect(topleft=(10, 450)),
        text.get_rect(topleft=(10, 500))
    ]
    
    #photos of the songs
    song_counter = 0
    amount_of_songs = 3
    
    song_image_list = [
        pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//musicelements//basqany.png").convert_alpha(),
        pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//musicelements//asylym.png").convert_alpha(),
        pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//musicelements//severnoe.png").convert_alpha()
    ]
        
    #about sounds
    songs_list = [
        pygame.mixer.Sound("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//music//Ayau, Shiza, M'Dee – basqany ：( [lyric video].mp3"), 
        pygame.mixer.Sound("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//music//Асылым.mp3"),
        pygame.mixer.Sound("C://Users//admin//OneDrive//Рабочий стол//pp2//lab7//music//Иван Дорн - Северное сияние (Full HD).mp3")
    ]


    x = 1
    song_is_play = False
    #использую для пробела, остановить при первом и если еще раз начать песню
    stop_sound = True
    while True:
        #для позиции мышки
        mouse = pygame.mouse.get_pos()
        #стартовый экран
        if not song_is_play:
            screen.blit(bg, (0, 0))
        else:
            screen.blit(song_image_list[song_counter], (0, 0))

        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            #обработка мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                for buttom in buttom_list:
                    if buttom.collidepoint(mouse) and not song_is_play:
                        song_counter = buttom_list.index(buttom)
                        songs_list[song_counter].play()
                        song_is_play = True

            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    song_is_play = False
                    songs_list[song_counter].stop()
                #старт секрет кнопка
                if event.key == pygame.K_q:
                    song_is_play = True
                    songs_list[song_counter].play()
                #смена песен вперед
                if event.key == pygame.K_d:
                    songs_list[song_counter].stop()
                    song_counter += 1
                    
                    #счетчик песен
                    song_counter %= amount_of_songs
                    
                    songs_list[song_counter].play()
                #смена песен назад
                if event.key == pygame.K_a:
                    songs_list[song_counter].stop()
                    
                    if song_counter == 0:
                        song_counter = 2
                    else:
                        song_counter -= 1
                    #тоже чтобы не вышла за грань 
                    song_counter %= amount_of_songs
                    
                    songs_list[song_counter].play()
                #остановить или начать песню 
                if event.key == pygame.K_SPACE:
                    if stop_sound:
                        songs_list[song_counter].stop()
                        stop_sound = False
                    else:
                        songs_list[song_counter].play()
                        stop_sound = True
                                       
main()
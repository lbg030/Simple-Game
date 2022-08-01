import pygame
pygame.init() # 반드시 해줘야 되는 부분

# 화면 크기 
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 480 * 640

background = pygame.image.load("/Users/ibyeong-gwon/Desktop/Git/Simple-Game/Pygame/pygame_basic/pixel.jpg")

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("/Users/ibyeong-gwon/Desktop/Git/Simple-Game/Pygame/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = screen_width / 2 - ( character_width / 2)# 화면 가로의 절반 크기에 해당하는 곳에 위치 ( 가로 )
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 위치 ( 세로 )

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 이벤트 루프
running = True # 게임이 진행중인지 아닌지 확인하는거 = flag
while running :
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 ( 안쓰면 꺼지지 않음 )
            running = False
    
    # screen.fill((0,0,255)) #RGB 형태로 단색 배경을 채우는 코드
    screen.blit(background, (0,0)) # x,y 좌표가 0,0 // 배경 그리기
    
    
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() #게임 화면을 다시 그리기 ! (반드시 계속 호출 되어야 되는 부분)
    

# 파이게임 종료
pygame.quit()
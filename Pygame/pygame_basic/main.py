import pygame
from datafile import *
from pygame.locals import *
#----------------------------------------------------------------#

# 기본 초기화 ( 반드시 해야 할 것들 )
class Game:
    def __init__(self):
        pygame.init() # 반드시 해줘야 되는 부분

        # 화면 크기 
        screen_width = 1280 # 가로
        screen_height = 720 # 세로
        screen = pygame.display.set_mode((screen_width, screen_height))

        #화면 타이틀 설정
        pygame.display.set_caption("Testing Game") #게임 이름

        #FPS

        #--------------------------------------------------------#

        self.camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # 카메라 이동 좌표
        
        self.spriteSheet_player = SpriteSheet('player1.png', 16, 16, 8, 8, 12)      # 플레이어 스프라이트 시트
        
        self.spr_player = {}     # 플레이어 스프라이트 세트
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 8)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [9, 10, 11])

        self.keyLeft = False
        self.keyRight = False

        player_sponOK = True
        player_spon_x = TILE_MAPSIZE[0] // 2 - 1

        # while(player_sponOK):
        #     player_spon_x += 1

        #     if floor_map[player_spon_x] != -1:
        #         player_sponOK = False

        self.player_rect = pygame.Rect((player_spon_x * 8, TILE_MAPSIZE[1] * 4 - 14), (6, 14))  # 플레이어 히트박스
        self.player_movement = [0, 0]            # 플레이어 프레임당 속도
        self.player_vspeed = 0                   # 플레이어 y가속도
        self.player_flytime = 0                  # 공중에 뜬 시간

        self.player_action = 'stay'              # 플레이어 현재 행동
        self.player_frame = 0                    # 플레이어 애니메이션 프레임
        self.player_frameSpeed = 1               # 플레이어 애니메이션 속도(낮을 수록 빠름. max 1)
        self.player_frameTimer = 0
        self.player_flip = False                 # 플레이어 이미지 반전 여부 (False: RIGHT)
        self.player_animationMode = True         # 애니메이션 모드 (False: 반복, True: 한번)
        self.player_walkSoundToggle = False
        self.player_walkSoundTimer = 0

        self.player_attack_timer = 0             # 플레이어 공격 타이머
        self.player_attack_speed = 15            # 플레이어 공격 속도

    def run(self):
        running = True # 게임이 진행중인지 아닌지 확인하는거 = flag


        while running :
            self.screen.fill(BACKGROUND_COLOR)      
            self.camera_scroll[0] += int((self.player_rect.x - self.camera_scroll[0] - WINDOW_SIZE[0] / 8 - 5) / 16)       # 카메라 이동
            self.camera_scroll[1] += int((self.player_rect.y - self.camera_scroll[1] - WINDOW_SIZE[1] / 8 - 2) / 16)

            
            # 2. 이벤트 처리 ( 키보드, 마우스 등 )
            for event in pygame.event.get(): # 어떤 이벤트가 발생하는지
                if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하면 ( 안쓰면 꺼지지 않음 )
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.keyLeft = True
                    if event.key == pygame.K_RIGHT:
                        self.keyRight = True
                    if event.key == pygame.K_UP and self.player_flytime < 6:    # 점프
                        self.player_vspeed = -3.5
                        self.player_flytime += 1
                 
                        self.player_frame, self.player_action, self.player_frameSpeed, self.player_animationMode = change_playerAction(
                            self.player_frame, self.player_action, 'jump', self.player_frameSpeed, 6, self.player_animationMode, False)
                        
            # 3. 게임 캐릭터 위치 정의

            # 4. 충돌 처리
            
            # 5. 화면에 그리기
                  # 화면 초기화
            self.screen.blit(pygame.transform.flip(self.spr_player[self.player_action][self.player_frame], self.player_flip, False)
                               , (self.player_rect.x - self.camera_scroll[0] - 5, self.player_rect.y - self.camera_scroll[1] - 2))      # 플레이어 드로우
            
            pygame.display.update() #게임 화면을 다시 그리기 ! (반드시 계속 호출 되어야 되는 부분)
            
        # 파이게임 종료
        pygame.quit()

game = Game()
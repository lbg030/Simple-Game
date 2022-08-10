# [Python pygame Game] RPG tutorial
# Made by "PrintedLove"
# Referred to DaFluffyPotato's 'Physics - Pygame Tutorial: Making a Platformer'
#-*-coding: utf-8

import pygame, sys, os
from datafile import *
from pygame.locals import *
import pygame.mixer

# 게임 클래스
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        #게임 컨트롤 변수
        pygame.display.set_caption('RPG tutorial')                                      # 창 이름 설정
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        self.screen_scaled = pygame.Surface((WINDOW_SIZE[0] / 4, WINDOW_SIZE[1] / 4))        # 확대한 스크린

        self.camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # 카메라 이동 좌표

        # self.gameScore = 0       # 점수

        # 리소스 불러오기
        self.spriteSheet_player = SpriteSheet('player.png', 16, 16, 8, 8, 12)      # 플레이어 스프라이트 시트
        # self.spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # 공통 오브젝트 스프라이트 시트
        # self.spriteSheet_map1 = SpriteSheet('spriteSheet3.png', 8, 8, 16, 16, 87)         # 지형 1 스프라이트 시트

        self.spr_player = {}     # 플레이어 스프라이트 세트
        self.spr_player['stay'] = createSpriteSet(self.spriteSheet_player, [0])
        self.spr_player['run'] = createSpriteSet(self.spriteSheet_player, 1, 8)
        self.spr_player['jump'] = createSpriteSet(self.spriteSheet_player, [9, 10, 11])

        # self.spr_effect = {}     # 효과 스프라이트 세트
        # self.spr_effect['player_shot'] = createSpriteSet(self.spriteSheet_object, 37, 40)          
        # self.spr_effect['player_shotBoom'] = createSpriteSet(self.spriteSheet_object, 41, 44)

        # self.spr_enemy = {}      # 적 스프라이트 세트
        # self.spr_enemy['slime'] = createSpriteSet(self.spriteSheet_map1, 81, 83)          
        # self.spr_enemy['snake'] = createSpriteSet(self.spriteSheet_map1, 84, 86)

        # self.spr_map_struct = {}     # 구조물 스프라이트 세트
        # self.spr_map_struct['leaf'] = [55, 56]
        # self.spr_map_struct['flower'] = [57, 64]
        # self.spr_map_struct['obj'] = [65, 70]
        # self.spr_map_struct['sign'] = [71, 74]
        # self.spr_map_struct['gravestone'] = [75, 78]
        # self.spr_map_struct['skull'] = [79, 80]

        # self.spr_coin = createSpriteSet(self.spriteSheet_object, [41, 42])    # 코인 스프라이트 세트

        # createMapData()                                 # 맵 데이터 초기화
        # self.mapImage, self.mapImage_front = createMapImage(self.spriteSheet_map1, self.spr_map_struct) # 맵 이미지 생성
        # self.backImage = createBackImage(self.spriteSheet_object)         # 배경 이미지 생성

        # #효과음
        # self.sound_attack = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'attack.wav'))
        # self.sound_coin = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'coin.wav'))
        # self.sound_footstep0 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep0.wav'))
        # self.sound_footstep1 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep1.wav'))
        # self.sound_monster = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'monster.wav'))

        # # 적 생성
        # for i in range(8):
        #     obj_snake = createObject(self.spr_enemy['snake'], (random.randrange(0, 960), 100), 'snake', self)
        #     obj_snake = createObject(self.spr_enemy['slime'], (random.randrange(0, 960), 100), 'slime', self)

        # 플레이어 컨트롤 변수
        self.keyLeft = False
        self.keyRight = False

        player_sponOK = True
        player_spon_x = TILE_MAPSIZE[0] // 2 - 1

        while(player_sponOK):
            player_spon_x += 1

            if floor_map[player_spon_x] != -1:
                player_sponOK = False

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

        # 배경음 실행
        # pygame.mixer.music.load(os.path.join(DIR_SOUND, 'background.wav'))
        # pygame.mixer.music.play(loops = -1)

        # 게임 실행
        self.run()

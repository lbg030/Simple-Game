#-*-coding: utf-8

import pygame, os, random

DIR_PATH = os.path.dirname(__file__)    # 파일 위치
DIR_IMAGE = os.path.join(DIR_PATH, 'image')

# 960 , 640
# -> 192, 32
WINDOW_SIZE = (1280, 720)            # 창 크기
TILE_SIZE = 8                       # 타일 크기
TILE_MAPSIZE = (int(WINDOW_SIZE[0] / 10), int(WINDOW_SIZE[1] / 30))

BACKGROUND_COLOR = (27, 25, 25)

floor_map = [-1] * TILE_MAPSIZE[0]     # 바닥 타일 맵(-1: 없음, 이외: y좌표)

objects = []                # 오브젝트 리스트
enemys = []                 # 적 오브젝트 리스트

# 스프라이트 시트 클래스 
class SpriteSheet:           
    def __init__(self, filename, width, height, max_row, max_col, max_index):
        baseImage = pygame.image.load(os.path.join(DIR_IMAGE, filename)).convert()
        self.spr = []
        self.width = width
        self.height = height

        for i in range(max_index):      # 스프라이트 시트의 각 인덱스에 자른 이미지 저장
            image = pygame.Surface((width, height))
            image.blit(baseImage, (0, 0), 
                       ((i % max_row) * width, (i // max_col) * height, width, height))
            image.set_colorkey((0, 0, 0))
            self.spr.append(image)

# 스프라이트 세트 생성 함수 
def createSpriteSet(spriteSheet, index_list, index_max = None):
    spr = []

    if index_max == None:
        for index in index_list:
            spr.append(spriteSheet.spr[index])
    else:
        for index in range(index_list, index_max + 1):
            spr.append(spriteSheet.spr[index])

    return spr

# 텍스트 드로우 함수
# def draw_text(screen, text, size, color, x, y):
#     gameFont = pygame.font.Font(os.path.join(DIR_FONT, DEFAULT_FONT_NAME), size)
#     text_surface = gameFont.render(text, False, color)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (round(x), round(y))
#     screen.blit(text_surface, text_rect)

# 기본 오브젝트 클래스
class BaseObject:
    def __init__(self, spr, coord, kinds, game):
        self.kinds = kinds
        self.spr = spr
        self.spr_index = 0
        self.game = game
        self.width = spr[0].get_width()
        self.height = spr[0].get_height()
        self.direction = True
        self.vspeed = 0
        self.gravity = 0.2
        self.movement = [0, 0]
        self.collision = {'top' : False, 'bottom' : False, 'right' : False, 'left' : False}
        self.rect = pygame.rect.Rect(coord[0], coord[1], self.width, self.height)
        self.frameSpeed = 0
        self.frameTimer = 0
        self.destroy = False

    def physics(self):
        self.movement[0] = 0
        self.movement[1] = 0

        if self.gravity != 0:
            self.movement[1] += self.vspeed

            self.vspeed += self.gravity
            if self.vspeed > 3:
                self.vspeed = 3

    def physics_after(self):
        self.rect, self.collision = move(self.rect, self.movement)

        if self.collision['bottom']:
            self.vspeed = 0

        if self.rect.y > 400 or self.rect.y  > 400 or self.rect.y  > 400:
            self.destroy = True
    
    def draw(self):
        self.game.screen_scaled.blit(pygame.transform.flip(self.spr[self.spr_index], self.direction, False)
                    , (self.rect.x - self.game.camera_scroll[0], self.rect.y - self.game.camera_scroll[1]))

        if self.kinds == 'enemy' and self.hp < self.hpm:
            pygame.draw.rect(self.game.screen_scaled, (131, 133, 131)
            , [self.rect.x - 1 - self.game.camera_scroll[0], self.rect.y - 5 - self.game.camera_scroll[1], 10, 2])
            pygame.draw.rect(self.game.screen_scaled, (189, 76, 49)
            , [self.rect.x - 1 - self.game.camera_scroll[0], self.rect.y - 5 - self.game.camera_scroll[1], 10 * self.hp / self.hpm, 2])

    def animation(self, mode):
        if mode == 'loop':
            self.frameTimer += 1

            if self.frameTimer >= self.frameSpeed:
                self.frameTimer = 0
                if self.spr_index < len(self.spr) - 1:
                    self.spr_index += 1
                else:
                    self.spr_index = 0

    def destroy_self(self):
        if self.kinds == 'enemy':
            enemys.remove(self)

        objects.remove(self)
        del(self)

# 적 오브젝트 클래스
# class EnemyObject(BaseObject):
#     def __init__(self, spr, coord, kinds, game, types):
#         super().__init__(spr, coord, kinds, game)
#         self.types = types
#         self.actSpeed = 0
#         self.actTimer = 0
#         self.hpm = 0
#         self.hp = 0

#     def events(self):
#         if self.hp < 1:
#             self.destroy = True
#             self.game.sound_monster.play()

#             for i in range(4):
#                 coin = createObject(self.game.spr_coin, (self.rect.x + random.randrange(-3, 4), self.rect.y - 2), 'coin', self.game)
#                 coin.vspeed = random.randrange(-3, 0)
#                 coin.direction = random.choice([True, False])

#         if self.destroy == False:
#             self.physics()

#             if self.types == 'snake':       # 뱀일 경우
#                 self.animation('loop')

#                 if self.direction == False:
#                     if floor_map[self.rect.right // TILE_SIZE] != -1:
#                         self.movement[0] += 1
#                     else:
#                         self.direction = True
#                 else:
#                     if floor_map[self.rect.right // TILE_SIZE - 1] != -1:
#                         self.movement[0] -= 1
#                     else:
#                         self.direction = False
#             elif self.types == 'slime':       # 슬라임일 경우
#                 self.actTimer += 1
#                 self.frameTimer += 1

#                 if self.vspeed >= 0:
#                     if self.frameTimer >= self.frameSpeed:
#                         self.frameTimer = 0
#                         if self.spr_index == 0:
#                             self.spr_index = 1
#                         else:
#                             self.spr_index = 0
#                 else:
#                     self.spr_index = 2

#                 if self.actTimer == self.actSpeed - 35:
#                     self.vspeed = -3
#                 elif self.actTimer > self.actSpeed:
#                     self.actTimer = 0
#                 elif self.actTimer > self.actSpeed - 35:
#                     if self.game.player_rect.x - self.rect.x > 0:
#                         if floor_map[self.rect.right // TILE_SIZE] != -1:
#                             self.direction = False
#                             self.movement[0] += 1
#                     else:
#                         if floor_map[self.rect.right // TILE_SIZE - 1] != -1:
#                             self.direction = True
#                             self.movement[0] -= 1

#             if self.collision['right'] or self.collision['left']:
#                 self.vspeed = -2

# 투사체 오브젝트 클래스
# class EffectObject(BaseObject):
#     def __init__(self, spr, coord, kinds, game, types):
#         super().__init__(spr, coord, kinds, game)
#         self.types = types
#         self.lifetime = 0
#         self.lifeTimer = 0
#         self.damage = 0

#     def events(self):
#         self.physics()
#         self.lifeTimer += 1

#         if self.lifeTimer > self.lifetime:
#             self.destroy = True

#         if self.types == 'player_shot':       # 플레이어 공격일 경우
#             self.animation('loop')

#             if self.direction == False:
#                 self.movement[0] += 3
#             else:
#                 self.movement[0] -= 3

#             if self.collision['right'] or self.collision['left']:
#                 if self.direction:
#                     self.direction = False
#                     self.movement[0] += 4
#                 else:
#                     self.direction = True
#                     self.movement[0] -= 4

#             for enemy in enemys:            # 적과 충돌 계산
#                 if self.destroy == False and enemy.destroy == False and self.rect.colliderect(enemy.rect):
#                     self.destroy = True
#                     enemy.hp -= self.damage

# # 아이템 오브젝트 클래스
# class ItemObject(BaseObject):
#     def __init__(self, spr, coord, kinds, game, types):
#         super().__init__(spr, coord, kinds, game)
#         self.types = types

#     def events(self):
#         self.physics()
#         self.animation('loop')

#         if self.direction == False:
#             self.movement[0] += 1
#         else:
#             self.movement[0] -= 1

#         if self.collision['right'] or self.collision['left']:
#             if self.direction:
#                 self.direction = False
#                 self.movement[0] += 2
#             else:
#                 self.direction = True
#                 self.movement[0] -= 2

#         if self.destroy == False and self.rect.colliderect(self.game.player_rect):
#             self.destroy = True
#             self.game.gameScore += 5
#             self.game.sound_coin.play()


# 오브젝트 생성 함수
# def createObject(spr, coord, types, game):
#     if types == 'snake':
#         obj = EnemyObject(spr, coord, 'enemy', game, types)
#         obj.hpm = 50
#         obj.hp = obj.hpm
#         obj.frameSpeed = 4
#     if types == 'slime':
#         obj = EnemyObject(spr, coord, 'enemy', game, types)
#         obj.hpm = 100
#         obj.hp = obj.hpm
#         obj.frameSpeed = 12
#         obj.actSpeed = 120
#         obj.actTimer = random.randrange(0, 120)
#     if types == 'player_shot':
#         obj = EffectObject(spr, coord, 'effect', game, types)
#         obj.frameSpeed = 10
#         obj.lifetime = 100
#         obj.vspeed = -1
#         obj.damage = 30
#     if types == 'coin':
#         obj = ItemObject(spr, coord, 'item', game, types)
#         obj.frameSpeed = 25

#     objects.append(obj)

#     if obj.kinds == 'enemy':
#         enemys.append(obj)

#     return obj

# 바닥과 충돌 검사 함수
def collision_floor(rect):
    hit_list = []
    col = 0

    for row in floor_map:
        if row != -1:
            floor_rect = pygame.rect.Rect((col * TILE_SIZE, row * TILE_SIZE), (TILE_SIZE, TILE_SIZE * 5))
            if rect.colliderect(floor_rect):
                hit_list.append(floor_rect)
        col += 1

    return hit_list

# 오브젝트 이동 함수
def move(rect, movement):
    collision_types = {'top' : False, 'bottom' : False, 'right' : False, 'left' : False}    # 충돌 타입
    rect.x += movement[0]
    hit_list = collision_floor(rect)

    for tile in hit_list:           # X축 충돌 리스트 갱신
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collision_floor(rect)

    for tile in hit_list:           # Y축 충돌 리스트 갱신
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True

    return rect, collision_types
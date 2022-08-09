import pygame


img = pygame.image.load('Walk_10.png')
img_scale = pygame.transform.scale(img, (100, 70)) # 스케일 변환

pygame.image.save(img_scale, 'newWalk_10.png') 
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("농담곰의 간식먹방")

clock = pygame.time.Clock()

#농담곰의 간식 3가지(먹으면 득점=apple과 동일)
food1_img = pygame.image.load("food1.png")
food1_img = pygame.transform.scale(food1_img, (40, 40))

food2_img = pygame.image.load("food2.png")
food2_img = pygame.transform.scale(food2_img, (40, 40))

food3_img = pygame.image.load("food3.png")
food3_img = pygame.transform.scale(food3_img, (40, 40))

poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 10) # 바닥고정시킴
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        self.rect.clamp_ip(screen.get_rect())


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randint(0, WIDTH - 40)
        self.rect.y = -50 
        self.speed = random.randint(3, 5)

    def update(self):
        self.rect.y += self.speed

        #플레이어가 먹지 못하고 바닥에 떨어지면 제거하는 코드 (gpt)
        if self.rect.top > HEIGHT:
            self.kill()


all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


foods = []


food_spawn_timer = 0
FOOD_SPAWN_INTERVAL = 40  

enemy_spawn_timer = 0
ENEMY_SPAWN_INTERVAL = 20

score = 0
running = True
game_over = False

def spawn_enemy():
    e = Enemy()
    all_sprites.add(e)
    enemy_group.add(e)

#음식 생성 함수.(각 1,2,3번 음식을 랜덤으로 소환하는 코드를 gpt를 통해 작성.)
def spawn_food():
    size = 40
    x = random.randint(0, WIDTH - size)
    y = -size
    vx = 0
    vy = random.randint(3, 5)
    
    choice = random.randint(1, 3)
    
    if choice == 1:
        img = food1_img
        score_val = 1  # 1점
    elif choice == 2:
        img = food2_img
        score_val = 2  # 2점
    else:
        img = food3_img
        score_val = 3  # 3점

    rect = pygame.Rect(x, y, size, size)
    
    foods.append({"rect": rect, "vx": vx, "vy": vy, "img": img, "val": score_val})


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_RETURN:
                game_over = False
                score = 0
                
                player.rect.midbottom = (WIDTH // 2, HEIGHT - 10)

                for e in enemy_group:
                    e.kill()
                
                foods.clear()
                
                food_spawn_timer = 0
                enemy_spawn_timer = 0

    if not game_over:
        all_sprites.update()

        enemy_spawn_timer += 1
        if enemy_spawn_timer >= ENEMY_SPAWN_INTERVAL:
            enemy_spawn_timer = 0
            spawn_enemy()

        
        food_spawn_timer += 1
        if food_spawn_timer >= FOOD_SPAWN_INTERVAL:
            food_spawn_timer = 0
            spawn_food()

        
        new_foods = []
        for food in foods:
            rect = food["rect"]
            rect.x += food["vx"]
            rect.y += food["vy"]

            if rect.top > HEIGHT:
                continue 

            if player.rect.colliderect(rect):
                score += food["val"]  
                continue 

            new_foods.append(food)

        foods = new_foods

        hits = pygame.sprite.spritecollide(player, enemy_group, False)
        if hits:
            print("똥에 맞음! 게임 오버")
            game_over = True

#사진 누끼가 안따져서 티 안나게 흰색으로 배경 바꾸기
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 255, 255), (0, HEIGHT - 60, WIDTH, 60))

    for food in foods:
        screen.blit(food["img"], food["rect"])

    all_sprites.draw(screen)

    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    if game_over:
        over_text = font.render("GAME OVER (Press Enter)", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2
        over_y = (HEIGHT - over_text.get_height()) // 2
        screen.blit(over_text, (over_x, over_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
import random
import sys

pygame.init()  # تشغيل pygame

# تشغيل اللعبة Full Screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

# ألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)

# خطوط
title_font = pygame.font.SysFont(None, 100)   # عنوان كبير
button_font = pygame.font.SysFont(None, 70)   # زرار
number_font = pygame.font.SysFont(None, 60)   # أرقام

GRID_SIZE = 9
CELL_SIZE = HEIGHT // 10   # حجم المربع كبير

# توليد جريد عشوائي
def generate_grid():
    grid = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            # يا إما فاضي يا إما رقم عشوائي
            if random.randint(0, 1) == 1:
                grid[i][j] = random.randint(1, 9)

    return grid

# رسم الشبكة والأرقام
def draw_grid(grid):
    for i in range(10):
        # كل 3 خطوط تخين (شكل سودوكو)
        thickness = 4 if i % 3 == 0 else 1

        pygame.draw.line(screen, BLACK,
                         (0, i * CELL_SIZE),
                         (CELL_SIZE * 9, i * CELL_SIZE),
                         thickness)

        pygame.draw.line(screen, BLACK,
                         (i * CELL_SIZE, 0),
                         (i * CELL_SIZE, CELL_SIZE * 9),
                         thickness)

    # رسم الأرقام
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                num = number_font.render(str(grid[i][j]), True, BLACK)
                screen.blit(num,
                            (j * CELL_SIZE + 20, i * CELL_SIZE + 10))

# شاشة البداية
def welcome_page():
    while True:
        screen.fill(WHITE)

        # العنوان
        title = title_font.render("SUDOKU", True, BLACK)
        screen.blit(title, (WIDTH//2 - 200, HEIGHT//4))

        # زرار start
        button_rect = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 300, 100)
        pygame.draw.rect(screen, BLUE, button_rect)

        text = button_font.render("START", True, WHITE)
        screen.blit(text, (button_rect.x + 60, button_rect.y + 25))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # لو ضغط على الزرار يدخل اللعبة
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

# اللعبة الأساسية
def main():
    grid = generate_grid()  # نجيب أرقام عشوائية

    while True:
        screen.fill(WHITE)

        draw_grid(grid)  # رسم الشبكة

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# تشغيل
welcome_page()
main()
import pygame
import random
import sys

pygame.init()

# شاشة
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

# ألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
GRAY = (200, 200, 200)

# خطوط
title_font = pygame.font.SysFont(None, 100)
button_font = pygame.font.SysFont(None, 60)
number_font = pygame.font.SysFont(None, 50)

# حجم الشبكه
CELL_SIZE = min(WIDTH, HEIGHT) // 12
block_X = (WIDTH - CELL_SIZE * 9) // 2
block_Y = (HEIGHT - CELL_SIZE * 9) // 2

# توليد جريد بسيط
def generate_grid():
    block = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if random.randint(0, 1):
                grid[i][j] = random.randint(1, 9)
    return block

# رسم الشبكه
def draw_block(block, selected):
    # رسم الخلايا
    for i in range(9):
        for j in range(9):
            rect = pygame.Rect(GRID_X + j*CELL_SIZE, GRID_Y + i*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

            if grid[i][j] != 0:
                num = number_font.render(str(grid[i][j]), True, BLACK)
                screen.blit(num, (rect.x + 15, rect.y + 10))
                
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1

        pygame.draw.line(screen, BLACK,
            (bLock_X, block_Y + i * CELL_SIZE),
            (block_X + CELL_SIZE * 9, block_Y + i * CELL_SIZE),
            thickness)

        pygame.draw.line(screen, BLACK,
            (block_X + i * CELL_SIZE, block_Y),
            (block_X + i * CELL_SIZE, block_Y + CELL_SIZE * 9),
            thickness)

    # تحديد الخلية
    if selected:
        r, c = selected
        pygame.draw.rect(screen, BLUE,
            (block_X + c*CELL_SIZE, block_Y + r*CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

# شاشة البداية
def welcome_page():
    while True:
        screen.fill(WHITE)

        title = title_font.render("SUDOKU", True, BLACK)
        screen.blit(title, (WIDTH//2 - 200, HEIGHT//4))

        button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 80)
        pygame.draw.rect(screen, BLUE, button)

        text = button_font.render("START", True, WHITE)
        screen.blit(text, (button.x + 30, button.y + 20))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    return

# اللعبة
def main():
    block = generate_block()
    selected = None

    start_time = pygame.time.get_ticks()

    while True:
        screen.fill(WHITE)

        # Timer
        elapsed = (pygame.time.get_ticks() - start_time) // 1000
        timer_text = number_font.render(f"Time: {elapsed}", True, BLACK)
        screen.blit(timer_text, (50, 50))

        draw_block(block, selected)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # اختيار خلية
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = (x - GRID_X) // CELL_SIZE
                row = (y - GRID_Y) // CELL_SIZE

                if 0 <= row < 9 and 0 <= col < 9:
                    selected = (row, col)

            # إدخال رقم
            if event.type == pygame.KEYDOWN and selected:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    num = event.key - pygame.K_0
                    row, col = selected

                if is_valid(grid, row, col, num):
                    grid[row][col] = num
else:
    print("غلط ❌")

                # مسح الرقم
                if event.key == pygame.K_BACKSPACE:
                    block[selected[0]][selected[1]] = 0
            def is_valid(grid, row, col, num):
    # تحقق من الصف
    for i in range(9):
        if block[row][i] == num:
            return False

    # تحقق من العمود
    for i in range(9):
        if blcok[i][col] == num:
            return False

    # تحقق من المربع 3×3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

# تشغيل
welcome_page()
main()

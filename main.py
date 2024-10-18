import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/шутер.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")

target_width = 100
target_height = 100

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Настройки шрифта
font = pygame.font.SysFont(None, 36)


# Функция для отображения текста
def display_message(message, color, x, y):
    text = font.render(message, True, color)
    screen.blit(text, (x, y))


# Список фраз для успеха
success_messages = [
    "Молодец! Так держать!",
    "Отлично! Продолжай в том же духе!",
    "Ты сделал это! Ты крутой!",
    "Попадание! Ты на пути к победе!",
    "Великолепно! Настоящий снайпер!"
]

# Список фраз для неудачи
failure_messages = [
    "Неудача – путь к успеху! Продолжай!",
    "Ошибки делают нас сильнее! Давай дальше!",
    "Каждая неудача приближает к успеху!",
    "Это не конец, это начало победы!",
    "Не сдался – уже победитель!"
]

# Счётчики удачных и неудачных попыток
success_count = 0
failure_count = 0

running = True
message = ""  # Сообщение, которое будет выводиться на экран
message_color = (0, 0, 0)  # Цвет сообщения (черный по умолчанию)

while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверяем, попал ли игрок в мишень
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Случайная фраза успеха
                message = random.choice(success_messages)
                message_color = (0, 255, 0)  # Зеленый цвет для успеха
                success_count += 1  # Увеличиваем счётчик успехов
            else:
                # Случайная фраза неудачи
                message = random.choice(failure_messages)
                message_color = (255, 0, 0)  # Красный цвет для неудачи
                failure_count += 1  # Увеличиваем счётчик неудач

    # Отображаем мишень
    screen.blit(target_image, (target_x, target_y))

    # Отображаем сообщение
    if message:
        display_message(message, message_color, 10, 10)  # Сообщение в верхнем левом углу

    # Отображаем счёт удачных и неудачных попыток
    display_message(f"Удачных попыток: {success_count}", (0, 255, 0), 10, 50)  # Счёт успехов
    display_message(f"Неудачных попыток: {failure_count}", (255, 0, 0), 10, 90)  # Счёт неудач

    pygame.display.update()

pygame.quit()

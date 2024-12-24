import pygame
import random
from classes import Snake, Apple, GameObject, draw_text, INITIAL_SPEED, CELL_SIZE, MAX_SPEED, SPEED_INCREASE, BACKGROUND_COLOR, TEXT_SIZE, SCREEN, CLOCK


current_speed = INITIAL_SPEED


def main():
    """Основная функция, содержащая игровой цикл."""
    global current_speed
    snake = Snake()
    apple = Apple()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    snake.update_direction((0, -CELL_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.update_direction((0, CELL_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.update_direction((-CELL_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.update_direction((CELL_SIZE, 0))


        snake.move()
        snake.handle_border_collision()

        # Проверка столкновения с яблоком
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
            current_speed = min(current_speed + SPEED_INCREASE, MAX_SPEED)

        # Проверка столкновения с самой собой
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()
            current_speed = INITIAL_SPEED

        # Отрисовка
        SCREEN.fill(BACKGROUND_COLOR)
        snake.draw(SCREEN)
        apple.draw(SCREEN)
        draw_text(f"Length: {snake.length}", TEXT_SIZE, (255, 255, 255),
                  10, 10)
        draw_text(f"Speed: {current_speed}", TEXT_SIZE, (255, 255, 255),
                  10, 30)
        pygame.display.flip()
        CLOCK.tick(current_speed)

    pygame.quit()


if __name__ == "__main__":
    main()
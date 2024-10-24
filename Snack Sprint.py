import pygame as pg
import random as r


def game_over():
    exit("Thanks For Playing")


def plot_snake(snake_body):
    for snake_x, snake_y in snake_body:
        pg.draw.rect(screen, (255, 255, 255, 0.5), [snake_x, snake_y, 20, 20], border_radius=100)


def text_screen(text, tcolor, x, y):
    font = pg.font.SysFont(None, 30)
    text_print = font.render(text, True, tcolor)
    screen.blit(text_print, [x, y])


def run_game():
    pg.init()
    pg.display.set_caption("GAKSHATB")
    pg.display.flip()
    clock = pg.time.Clock()

    flag = True
    dicflag = True

    food_x, food_y = r.randint(0, screen_height), r.randint(0, screen_width)
    food_x, food_y = food_x - (food_x % 20), food_y - (food_y % 20)

    snake_body = []
    snake_len = 20
    snake_x = 100
    snake_y = 100
    score = 0
    fps = 5
    sflag = True

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over()
                elif event.key == pg.K_RIGHT:
                    flag = True
                    dicflag = True
                elif event.key == pg.K_LEFT:
                    flag = True
                    dicflag = False
                elif event.key == pg.K_UP:
                    flag = False
                    dicflag = True
                elif event.key == pg.K_DOWN:
                    flag = False
                    dicflag = False

        if flag:
            if dicflag:
                snake_x = (snake_x + 20) % screen_height
            else:
                snake_x = (snake_x - 20) % screen_height
        else:
            if dicflag:
                snake_y = (snake_y - 20) % screen_width
            else:
                snake_y = (snake_y + 20) % screen_width

        if score % 20 == 19 and sflag:
            sflag = False
            fps += 5

        screen.fill("BLACK")
        # background = pg.image.load("wallpaper.jpg")
        # back_rect = background.get_rect()
        # screen_rect = screen.get_rect()
        # back_rect.midbottom = screen_rect.midbottom
        # screen.blit(background, back_rect)

        pg.draw.rect(screen, (255, 000, 000, 0.5), [food_x, food_y, 20, 20], border_radius=100)

        if abs(snake_x - food_x) == 0 and abs(snake_y - food_y) == 0:
            food_x, food_y = r.randint(0, screen_height), r.randint(0, screen_width)
            food_x, food_y = food_x - (food_x % 20), food_y - (food_y % 20)
            score += 1
            snake_len += 20

        if snake_len == len(snake_body) * 20:
            del snake_body[0]

        head = (snake_x, snake_y)
        if head not in snake_body:
            snake_body.append(head)
        else:
            run_game()
        del head

        text_screen(f"Score: {score}", "Orange", screen_height/2, 20)

        pg.mouse.set_visible(False)

        plot_snake(snake_body)

        pg.display.flip()
        clock.tick(fps)
    pg.quit()
    quit()


if __name__ == "__main__":
    screen_width = 500
    screen_height = 900
    screen = pg.display.set_mode((screen_height, screen_width))
    run_game()

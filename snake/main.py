from turtle import Screen
from snake import Snake
from score import ScoreBoard
import time
from food import Food, SCREEN_WIDTH, SCREEN_HEIGHT


def clean_screen():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.title('Snake')
    screen.listen()
    screen.tracer(0, 0)  # turn off animation i.e. it won't show each turtle moving separately
    return screen


try:
    with open('high_score.txt', 'rb') as f:
        inter = str(f.read(), 'utf-8')
        print('inter:', inter)
        high_score = int(inter)
        print(type(inter))
        print(inter)
except FileNotFoundError:
    high_score = 0

screen = Screen()
new_game = True
while new_game:
    screen = clean_screen()
    screen.update()
    snake1 = Snake(screen)
    score1 = ScoreBoard()
    food1 = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
    play = True
    while play:
        time.sleep(0.1)
        screen.update()
        play = snake1.move()
        high_score = score1.display_score(high_score)
        # Detect collision with food
        if snake1.game_over():
            print('Border broken! You died !')
            score1.display_game_over()
            play = False
            break
        if snake1.head.distance(food1) < 20:
            food1.hideturtle()
            del food1
            print('Good going !')
            snake1.extend_snake()
            print(len(snake1.snake))
            food1 = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
            score1.score += score1.feed_score
        else:
            score1.score += score1.time_score
    with open('high_score.txt', 'wb') as f:
        f.write(bytearray(str(high_score), 'utf-8'))
    wrong_input = True
    while wrong_input:
        replay = screen.textinput('Play Game', 'Would you like to play a new game? Y/N')
        print(replay)
        if replay is None or replay.lower() == 'n':
            print('Thanks for playing !')
            wrong_input = False
            new_game = False
            screen.clearscreen()
            del snake1
            del score1
            del food1
            break
        elif replay.lower() == 'y':
            screen.clearscreen()
            del screen
            del snake1
            del score1
            del food1
            wrong_input = False
        else:
            print('Incorrect input')

print('Tada !')

screen.exitonclick()
del screen

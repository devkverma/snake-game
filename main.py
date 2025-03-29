import curses
import time
import random
from game_over import *

class Game:

    def __init__(self, screen, snake, food):
        self.screen = screen
        self.score = 0
        self.snake = snake
        self.food = food

        height, width = self.screen.getmaxyx()
        self.centerx = width // 2
        self.centery = height // 2

        self.left = self.centerx - 35
        self.right = self.centerx + 35
        self.top = self.centery - 17
        self.bottom = self.centery + 17

        food_x = random.randint(self.left + 1, self.right - 1)
        food_y = random.randint(self.top + 1, self.bottom - 1)

        self.food.coords = [food_x, food_y]

        self.snake.body[0] = [self.centerx,self.centery]

    def play(self):
        self.screen.addstr(1,self.centerx - 15,"Use 'W','S','A','D' to move")
        self.screen.addstr(3,self.centerx - 3, f"Score: {self.score}")


        for i in range(self.left, self.right + 1):
            for j in range(self.top, self.bottom + 1):
                if (i == self.left or j == self.top or i == self.right or j == self.bottom):
                    self.screen.addstr(j,i,'#')

        for segment in self.snake.body:
            self.screen.addstr(segment[1], segment[0], '0')

        self.screen.addstr(self.food.coords[1], self.food.coords[0], '@')        

        self.screen.refresh()

    def gameOver(self):
        
        for _ in range(5):
            self.play()
            self.screen.refresh()
            time.sleep(0.2)
            self.screen.clear()
            self.screen.refresh()
            time.sleep(0.1)
        
        time.sleep(1)
        self.clear_screen_animation()
        self.screen.clear()

        self.screen.addstr(self.centery, self.centerx - 20,"GAME OVER! Press 'P' to play again or any to exit")
        self.screen.nodelay(False)
        key = self.screen.getch()

        if key == ord('p'):
            print(f"Your score: {self.score}")
            main(self.screen)
            
        print(f"Your score: {self.score}")
        

    def clear_screen_animation(self):
        self.screen.clear()
        self.screen.refresh()

        # Simulated game screen content
        height, width = self.screen.getmaxyx()
        
        start_y = height//2 - len(GAME_OVER)//2  # Center vertically
        start_x = width//2 - len(GAME_OVER[0])//2  # Center horizontally

        # Display the game content
        char_positions = []
        for i, line in enumerate(GAME_OVER):
            for j, char in enumerate(line):
                self.screen.addch(start_y + i, start_x + j, char)
                if char != ' ':
                    char_positions.append((start_y + i, start_x + j))  # Store positions

        self.screen.refresh()
        time.sleep(0.5)  
  
        self.screen.clear()
        time.sleep(0.5)  


        

class Snake:

    def __init__(self):
        self.body = [[]]  

    def move(self, direction):

        head_x, head_y, = self.body[0]

        if direction == 'w':
            head_y -= 1

        elif direction == 's':
            head_y += 1
        
        elif direction == 'd':
            head_x += 2

        elif direction == 'a':
            head_x -= 2

        self.body.insert(0, [head_x, head_y])
        self.body.pop()
    
    def eatsFood(self, food):
        food_x, food_y = food.coords
        food_boundary = [(food_x - 1, food_y - 1),
                         (food_x, food_y - 1),
                         (food_x + 1, food_y - 1),
                         (food_x - 1, food_y),
                         (food_x, food_y),
                         (food_x + 1, food_y),
                         (food_x - 1, food_y + 1),
                         (food_x, food_y + 1),
                         (food_x + 1, food_y + 1)]
        
        if tuple(self.body[0]) in food_boundary:
            return True
        return False
    
    def eatsItself(self):

        if self.body[0] in self.body[2:]:
            return True
        return False


class Food:

    def __init__(self):
        self.coords = []

    def setFood(self, left, right, top, bottom, snake):
        while True:
            food_x = random.randint(left + 1, right - 1)
            food_y = random.randint(top + 1, bottom - 1)

            # Ensure food does not spawn on the snake
            if [food_x, food_y] not in snake.body:
                break
        
        self.coords = [food_x, food_y] 
            

def main(stdscr):

    curses.curs_set(0)

    snake = Snake()
    food = Food()
    game = Game(stdscr, snake, food)

    moving = 'd'
    curses.noecho()
    stdscr.nodelay(True)
    while (True):

        snake.move(moving)

        if snake.eatsFood(food):
            food.setFood(game.left, game.right,game.top,game.bottom,snake)
            game.score += 1

            snake.body.append(snake.body[-1][:])

        game.play()

        key = stdscr.getch()

        #Quit game
        if key == ord('q'):
            break

        #Movements
        if key == ord('w') and moving != 's':
            snake.move('w')
            moving = 'w'

        elif key == ord('s') and moving != 'w':
            snake.move('s')
            moving = 's'

        elif key == ord('d') and moving != 'a':
            snake.move('d')
            moving = 'd'

        elif key == ord('a') and moving != 'd':
            snake.move('a')
            moving = 'a'


        snake_x, snake_y = snake.body[0]


        #Out of field
        if snake_x <= game.left or snake_x >= game.right or snake_y <= game.top or snake_y >= game.bottom:
            if snake_x <= game.left:
                snake_x += 2
            elif snake_x >= game.right:
                snake_x -= 2
            if snake_y <= game.top:
                snake_y += 1
            elif snake_y >= game.bottom:
                snake_y -= 1
            
            snake.body[0] = [snake_x, snake_y]
            game.gameOver()
            break

        if snake.eatsItself():
            game.gameOver()
            break

        stdscr.clear()
        time.sleep(0.1)


    stdscr.getch()


curses.wrapper(main)

    
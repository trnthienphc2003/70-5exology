import pygame, random

pygame.init()
bounds = (1920, 1080)
card_scale = 0.2
bg = pygame.transform.scale(pygame.image.load('src/background.png'), bounds)
window = pygame.display
canvas = window.set_mode(bounds)
pygame.display.set_caption("GameUIT Hackathon")

c_small = pygame.image.load('src/card.png')
c_value = [pygame.image.load('src/copper.png'),pygame.image.load('src/aluminium.png'),pygame.image.load('src/iron.png'),pygame.image.load('src/gold.png')]
card_back = pygame.transform.scale_by(c_small, card_scale)

font = pygame.font.Font('src/roboto.ttf', 64)
deck = 40
cnt = [15, 10, 10, 5]
hands_limit = 7
turns = 20
player = 0
text = font.render(f'Deck Count: {deck}', True, (255, 255, 255), (0, 0, 0))
textRect = text.get_rect()
textRect.center = (1000, 1000)

def randomFromDeck():
    global cnt
    return random.choices([0, 1, 2, 3], cnt)[0]

class Button():
    def __init__(self, x_pos, y_pos, bg_color, text_color, text_input):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.bg_color = bg_color
        self.text_color = text_color
        self.text_input = text_input
        self.text = font.render(text_input, True, text_color, bg_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.rect = self.text_rect

    def update(self):
        pygame.draw.rect(canvas, self.bg_color, self.rect)
        canvas.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
            
class ButtonImage():
    def __init__(self, front_img, back_img, x_pos = 0, y_pos = 0, text_input = ''):
        self.front_img = front_img
        self.back_img = back_img
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.front_img.get_rect(topleft=(x_pos,y_pos))
        self.text_input = text_input
        self.text = font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(topleft=(self.x_pos, self.y_pos))

    def update(self, front=False):
        canvas.blit(self.front_img if front else self.back_img, self.rect)
        canvas.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

class Card(ButtonImage):
    def __init__(self, front_img, back_img, x_pos = 0, y_pos = 0, value=-1, name = '', description = ''):
        super().__init__(front_img, back_img, x_pos, y_pos)
        self.name=name
        self.value=value
        self.description=description
        self.hovered = False
    
    def hover(self):
        pass
        # self.y_pos = 1000 - self.rect.height * card_scale
        # self.rect.topleft = (self.x_pos, self.y_pos)
        # self.hovered = True

    def unhover(self):
        pass
        # self.y_pos = 1000
        # self.rect.topleft = (self.x_pos, self.y_pos)
        # self.hovered = False

class Resources(Card):
    def __init__(self, name, description, carbon):
        pass
        

cards = [[], []]
current_card = [0, 0]
dollars = [0, 0]
carbon = [0, 0] 
button = Button(640, 540, (255, 255, 255), (0, 0, 0), 'Draw')
prev_card = [Button(400, 750, (255, 255, 255), (0, 0, 0), '<-'), Button(400, 330, (255, 255, 255), (0, 0, 0), '<-')]
next_card = [Button(600, 750, (255, 255, 255), (0, 0, 0), '->'), Button(600, 330, (255, 255, 255), (0, 0, 0), '->')]

def pushNewCard():
    global deck, player, cnt, card_back
    cur_x = 0
    if deck > 0:
        chosen = randomFromDeck()
        print(chosen)
        cnt[chosen] -= 1
        front_img = pygame.transform.scale_by(c_value[chosen], card_scale)
        card = Card(front_img, card_back, y_pos = 1000, value=chosen)
        cards[player].append(card)
        deck -= 1

def nextTurn():
    global turns, player
    if turns == 0: return
    if player == 1: turns -= 1
    player = 1 - player
    # print(turns, player)

def updatePositionOfDeck():
    global hands_limit, player
    x_scale = 0.04 * 2/3
    y_scale = 0.08 * 2/3
    total_w = sum([card.rect.width * x_scale for card in cards[player][-hands_limit:]])
    cur_x = (bounds[0] - total_w) / 2 + total_w
    cur_y = 1000 if player == 0 else -80
    i = len(cards[player]) - 1
    while i >= 0 and i >= len(cards[player]) - hands_limit:
        card = cards[player][i]
        w = card.rect.width
        cur_y = 1000 - (len(cards[player]) - i - 1) * card.rect.height * y_scale if player == 0 else -80 + (len(cards[player]) - i - 1) * card.rect.height * y_scale
        cards[player][i] = Card(card.front_img, card.back_img, cur_x, cur_y, value=card.value)
        cur_x -= w * x_scale
        print(cur_x, cur_y, card.value)
        i -= 1

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.checkForInput(pygame.mouse.get_pos()): 
                pushNewCard()
                updatePositionOfDeck()
                nextTurn()
            else:
                for i in range(2):
                    if prev_card[i].checkForInput(pygame.mouse.get_pos()):
                        if cards[i]: 
                            current_card[i] = (current_card[i] + len(cards[i]) - 1) % len(cards[i])
                            break
                    elif next_card[i].checkForInput(pygame.mouse.get_pos()):
                        if cards[i]: 
                            current_card[i] = (current_card[i] + 1) % len(cards[i])
                            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pushNewCard()
                updatePositionOfDeck()
                nextTurn()
            elif event.key == pygame.K_LEFT:
                if cards[player]: current_card[player] = (current_card[player] + len(cards[player]) - 1) % len(cards[player])
            elif event.key == pygame.K_RIGHT:
                if cards[player]: current_card[player] = (current_card[player] + 1) % len(cards[player])
        else:
            pass
    
    updatePositionOfDeck()
    canvas.fill((255, 255, 255))
    canvas.blit(bg, (0, 0))
    for i in range(2):
        if cards[i]:
            text = font.render(f'{current_card[i]}', True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (500, 750) if i == 0 else (500, 330)
            canvas.blit(text, textRect)
            preview_card = cards[i][current_card[i]].front_img
            canvas.blit(preview_card, (400, 800) if i == 0 else (400, 0))
        text = font.render(f'Deck: {deck}', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (960, 540)
        canvas.blit(text, textRect)
        for card in reversed(cards[i][-hands_limit:]): card.update()
        button.update()
        if cards[i]:
            prev_card[i].update()
        if cards[i]:
            next_card[i].update()
    window.update()
    pygame.display.update()

pygame.quit()
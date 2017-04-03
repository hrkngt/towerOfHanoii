import pygame
from linkedstack import LinkedStack


pygame.init()

display_width = 1000
display_height = 600

x = display_width
y = display_height

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tower of Hanoi')
clock = pygame.time.Clock()

"""Color collections"""
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
paleGreen = (152, 251, 152)

"""Images"""
standImg = pygame.image.load('stand.png')
oneImg = pygame.image.load('one.png')
twoImg = pygame.image.load('two.png')
threeImg = pygame.image.load('three.png')
fourImg = pygame.image.load('four.png')
fiveImg = pygame.image.load('five.png')


def stand(x, y):
    gameDisplay.blit(standImg, (x, y))


def one(x, y):
    gameDisplay.blit(oneImg, (x, y))


def two(x, y):
    gameDisplay.blit(twoImg, (x, y))


def three(x, y):
    gameDisplay.blit(threeImg, (x, y))


def four(x, y):
    gameDisplay.blit(fourImg, (x, y))


def five(x, y):
    gameDisplay.blit(fiveImg, (x, y))


def movePiece(pStack, nStack):
    pStack.peek()
    nStack.peek()
    if not pStack.isEmpty():
        if nStack.isEmpty():
            nStack.push(pStack.pop())
            return True
        elif pStack.peek() < nStack.peek(): # head of new stack is greater than the moving number
            nStack.push(pStack.pop())
            return True
        elif pStack.peek() > nStack.peek(): # head of new stack is lower than the moving number
            print("can't do that move.")
            return False


def showHold(pStack):
    if pStack is not None:
        font = pygame.font.SysFont("monospace", 25)
        label = font.render("You're holding:", 1, black)
        gameDisplay.blit(label, (30, 105))
        holdingX = 300
        holdingY = 100
        if pStack.peek() == 1:
            one(holdingX, holdingY)
        if pStack.peek() == 2:
            two(holdingX, holdingY)
        if pStack.peek() == 3:
            three(holdingX, holdingY)
        if pStack.peek() == 4:
            four(holdingX, holdingY)
        if pStack.peek() == 5:
            five(holdingX, holdingY)


left = 273
center = 460
right = 645
bottom = 515


def renderPieces(S, pos):
    """Position declaration"""

    space = 45
    for i in range(1, 6):
        if i in S:
            if pos == 0: pos = left
            if pos == 1: pos = center
            if pos == 2: pos = right
            if i == 1: one(pos, bottom - (space * S.getIndex(1)))
            if i == 2: two(pos, bottom - (space * S.getIndex(2)))
            if i == 3: three(pos, bottom - (space * S.getIndex(3)))
            if i == 4: four(pos, bottom - (space * S.getIndex(4)))
            if i == 5: five(pos, bottom - (space * S.getIndex(5)))


"""For clicking detection"""
detector_width = 200
detector_hight = 550
S1 = pygame.Rect(left, 170, detector_width, detector_hight)
S2 = pygame.Rect(center, 170, detector_width, detector_hight)
S3 = pygame.Rect(right, 170, detector_width, detector_hight)


def startScreen():
    font_title = pygame.font.SysFont("monospace", 50)
    font_names = pygame.font.SysFont("monospace", 25)
    label = font_title.render("Tower of Hanoii", 1, black)
    label2 = font_names.render("Click to Start", 1, black)

    crashed = False
    while not crashed:
        gameDisplay.fill(paleGreen)
        gameDisplay.blit(label, (100, 100))
        gameDisplay.blit(label2, (100, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                return  # game starts
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


def mainGame():
    """Generate stacks"""
    Stack1 = LinkedStack()
    Stack2 = LinkedStack()
    Stack3 = LinkedStack()
    for i in range(5, 0, -1):
        Stack1.push(i)

    crashed = False
    pStack = None  # used for movePiece()
    moveCount = 0
    while not crashed:
        gameDisplay.fill(paleGreen)
        stand(x * 0.25, y * 0.3)
        font = pygame.font.SysFont("monospace", 25)
        label = font.render("Moves:" + str(moveCount), 1, black)
        gameDisplay.blit(label, (30, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()

                if S1.collidepoint(point):  # Stack1 is clicked
                    """Clicking Stack one."""
                    if pStack is None:
                        if Stack1.peek() is not None:
                            pStack = Stack1
                    else:
                        nStack = Stack1
                        if movePiece(pStack, nStack):
                            moveCount += 1
                        pStack = None
                elif S2.collidepoint(point):  # Stack2 is clicked
                    """Clicking Stack two."""
                    if pStack is None:
                        if Stack2.peek() is not None:
                            pStack = Stack2
                    else:
                        nStack = Stack2
                        if movePiece(pStack, nStack):
                            moveCount += 1
                        pStack = None
                elif S3.collidepoint(point): #Stack3 is clicked
                    """Clicking Stack three."""
                    if pStack is None:
                        if Stack3.peek() is not None:
                            pStack = Stack3
                    else:
                        nStack = Stack3
                        if movePiece(pStack, nStack):
                            moveCount += 1
                        pStack = None
                else:
                    pStack = None

        renderPieces(Stack1, 0)
        renderPieces(Stack2, 1)
        renderPieces(Stack3, 2)
        showHold(pStack)

        if len(Stack3) == 5:
            showResult(moveCount)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


def showResult(moves):
    font_title = pygame.font.SysFont("monospace", 50)
    font = pygame.font.SysFont("monospace", 25)
    label = font_title.render("Cleared!", 1, black)
    label2 = font.render("Your total move was " + str(moves), 1, black)
    label3 = font.render("Click to replay", 1, black)
    label4 = font.render("Optimal Solution!", 1, black)  # when solving with minimal move
    crashed = False
    while not crashed:
        gameDisplay.fill(paleGreen)
        gameDisplay.blit(label, (100, 100))
        gameDisplay.blit(label2, (100, 200))
        gameDisplay.blit(label3, (100, 300))
        if moves == 31:
            gameDisplay.blit(label4, (100, 250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mainGame()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


startScreen()
mainGame()
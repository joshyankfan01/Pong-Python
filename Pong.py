import pygame

setup = pygame.init()
if setup[1] != 0:
	print('Pygame failed to initialize!')
	quit()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')

leftPaddleX = 25
leftPaddleY = 225

rightPaddleX = 760
rightPaddleY = 225

paddleWidth = 15
paddleHeight = 150

paddleSpeed = 5

ballX = 400
ballY = 300
ballSize = 10

ballSpeedX = -2
ballSpeedY = 2

leftScore = 0
rightScore = 0

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		if leftPaddleY > 0:
			leftPaddleY -= paddleSpeed
	if keys[pygame.K_s]:
		if leftPaddleY + paddleHeight < 600:
			leftPaddleY += paddleSpeed
	if keys[pygame.K_UP]:
		if rightPaddleY > 0:
			rightPaddleY -= paddleSpeed
	if keys[pygame.K_DOWN]:
		if rightPaddleY + paddleHeight < 600:
			rightPaddleY += paddleSpeed


	ballX += ballSpeedX
	ballY += ballSpeedY
	if ballY - ballSize <= 0 or ballY + ballSize >= 600:
		ballSpeedY = -ballSpeedY
		if ballSpeedY < 0:
			ballSpeedY -= 0.5
		else:
			ballSpeedY += 0.5

	if ballX - ballSize <= leftPaddleX + paddleWidth:
		if ballY - ballSize >= leftPaddleY and ballY + ballSize <= leftPaddleY + paddleHeight:
			ballSpeedX = -ballSpeedX
			if ballSpeedX < 0:
				ballSpeedX -= 0.5
			else:
				ballSpeedX += 0.5
	if ballX + ballSize >= rightPaddleX:
		if ballY - ballSize >= rightPaddleY and ballY + ballSize <= rightPaddleY + paddleHeight:
			ballSpeedX = -ballSpeedX
			if ballSpeedX < 0:
				ballSpeedX -= 0.5
			else:
				ballSpeedX += 0.5

	if ballX - ballSize <= 0 or ballX + ballSize >= 800:
		if ballX - ballSize <= 400:
			rightScore += 1
		else:
			leftScore += 1
		ballX = 400
		ballY = 300
		ballSpeedX = -ballSpeedX
		ballSpeedY = -ballSpeedY
		if ballSpeedX < 0:
			ballSpeedX = -2
		else:
			ballSpeedX = 2
		if ballSpeedY < 0:
			ballSpeedY = -2
		else:
			ballSpeedY = 2

	pygame.display.flip()
	pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
	pygame.draw.rect(window, (255, 255, 255), (leftPaddleX, leftPaddleY, paddleWidth, paddleHeight))
	pygame.draw.rect(window, (255, 255, 255), (rightPaddleX, rightPaddleY, paddleWidth, paddleHeight))
	pygame.draw.circle(window, (255, 255, 255), ((int(ballX), int(ballY))), ballSize)
	
	font = pygame.font.SysFont('Arial', 50)
	leftText = font.render(str(leftScore), True, (255, 0, 0))
	rightText = font.render(str(rightScore), True, (255, 0, 0))
	window.blit(leftText, (200, 50))
	window.blit(rightText, (575, 50))

	pygame.time.delay(int(1000/60))
	
pygame.quit()
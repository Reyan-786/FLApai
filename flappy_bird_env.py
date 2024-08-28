import pygame
import numpy as np
from objects import Bird, Pipe, WIDTH, HEIGHT, BLACK, WHITE, PIPE_WIDTH, GAP_SIZE

class FlappyBirdEnv:
    def __init__(self):
        pygame.init()
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.bird = Bird()
        self.pipes = [Pipe()]
        self.score = 0
        return self._get_state()

    def step(self, action):
        if action == 1:  # flap
            self.bird.flap()
        self.bird.update()

        reward = 0
        done = False

        # Update pipes and check for collisions
        for pipe in self.pipes:
            pipe.update()
            if self.bird.rect.colliderect(pipe.rect_top) or self.bird.rect.colliderect(pipe.rect_bottom):
                reward = -100
                done = True
            elif self.bird.rect.y > self.height:
                reward = -100
                done = True
            elif self.bird.rect.x > pipe.x + PIPE_WIDTH and not getattr(pipe, 'passed', False):
                reward = 10
                pipe.passed = True

        # Check if the bird is out of the frame
        if self.bird.rect.y < 0 or self.bird.rect.y > self.height:
            reward = -100
            done = True

        # Add new pipes
        if len(self.pipes) == 0 or self.pipes[-1].x < self.width - 200:
            self.pipes.append(Pipe())

        # Remove off-screen pipes
        self.pipes = [pipe for pipe in self.pipes if pipe.x + PIPE_WIDTH > 0]

        state = self._get_state()
        return state, reward, done

    def _get_state(self):
        return np.array([
            self.bird.y, 
            self.bird.velocity,
            self.pipes[0].rect_top.y,
            self.pipes[0].rect_bottom.y - GAP_SIZE
        ])

    def render(self):
        self.screen.fill(BLACK)
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(30)  # Adjust this to control the frame rate


    def close(self):
        pygame.quit()

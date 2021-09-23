import pyxel
import random


class ParticleSystem:
    count = 0

    def __init__(self, num) -> None:
        self.particles = []
        for i in range(num):
            self.particles.append(Particle())

    def generate(self) -> None:
        for i, p in enumerate(self.particles):
            if p.state == Particle.STATE_NONE:
                self.particles[i].generate(random.uniform(-2, 2),
                                           random.uniform(-2, 2), random.randint(1, 2))
                ParticleSystem.count += 1
                break

    def update(self) -> None:
        for i, p in enumerate(self.particles):
            if p.state == Particle.STATE_ALIVE:
                if self.particles[i].update():
                    self.particles[i].state = Particle.STATE_NONE
                    ParticleSystem.count -= 1

    def draw(self) -> None:
        for i, p in enumerate(self.particles):
            if p.state == Particle.STATE_ALIVE:
                self.particles[i].draw()


class Particle:

    STATE_NONE = 0
    STATE_ALIVE = 1

    def __init__(self) -> None:
        self.state = Particle.STATE_NONE

    def generate(self, vx, vy, size) -> None:
        self.x = pyxel.width / 2
        self.y = pyxel.height / 2

        self.state = Particle.STATE_ALIVE

        self.vx = vx
        self.vy = vy

        self.size = size

    def update(self) -> bool:
        self.vy += 0.3

        self.vx *= 0.95
        self.vy *= 0.95

        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > pyxel.width or self.y < 0 or self.y > pyxel.height:
            return True

        return False

    def draw(self) -> None:
        # pyxel.pset(self.x, self.y, pyxel.frame_count % 16)
        pyxel.rect(self.x, self.y, self.size, self.size, pyxel.frame_count % 16)


class App:
    def __init__(self):
        pyxel.init(160, 120)

        self.p = ParticleSystem(50)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.p.generate()
        self.p.update()

    def draw(self):
        pyxel.cls(0)

        pyxel.text(3, 3, 'count:' + str(ParticleSystem.count), 1)

        self.p.draw()


App()

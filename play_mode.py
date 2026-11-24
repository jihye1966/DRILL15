from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None
balls = []
zombie = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
            return
        boy.handle_event(event)


def init():
    global boy, balls, zombie

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)
    game_world.add_collision_pair('grass:ball', grass, None)

    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)
    for zombie in zombies:
        game_world.add_collision_pair('ball:zombie', zombie, None)
        game_world.add_collision_pair('boy:zombie', boy, zombie)

    balls = [Ball(random.randint(100, 1500), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)
    game_world.add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('grass:ball', None, ball)
        game_world.add_collision_pair('boy:ball', None, ball)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy, balls, zombie
    game_world.clear()
    boy = None
    balls = []
    zombie = None


def update():
    game_world.update()
    game_world.handle_collision()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()

world = [[], [], []]  # 0: background, 1: objects, 2: UI
collision_pairs = {}


def add_oject(o, depth=1):
    world[depth].append(o)


def add_objects(objects, depth=1):
    world[depth].extend(objects)


def add_collision_pair(group, a, b):
    pairs = collision_pairs.setdefault(group, [[], []])
    if a is not None and a not in pairs[0]:
        pairs[0].append(a)
    if b is not None and b not in pairs[1]:
        pairs[1].append(b)


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            return


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    return (left_a <= right_b and right_a >= left_b and
            bottom_a <= top_b and top_a >= bottom_b)


def handle_collision():
    for group, pairs in collision_pairs.items():
        for a in pairs[0][:]:
            for b in pairs[1][:]:
                if a in pairs[0] and b in pairs[1] and collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)


def update():
    for layer in world:
        for o in layer[:]:
            o.update()


def render():
    for layer in world:
        for o in layer[:]:
            o.draw()


def clear():
    for layer in world:
        layer.clear()
    collision_pairs.clear()

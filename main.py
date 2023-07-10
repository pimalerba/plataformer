@namespace
class SpriteKind:
    coin = SpriteKind.create()
    flower = SpriteKind.create()

def on_on_overlap(sprite4, otherSprite2):
    global bee
    sprites.destroy(otherSprite2)
    bee = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 3 . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(bee,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . f f f f . . f f f f f . . . . 
                        . f 5 5 f . . f 5 5 5 f . . . . 
                        . f 5 5 f . . f 5 5 5 f . . . . 
                        . f f 5 f f f f f f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f 5 1 f 1 5 f . . . . . . 
                        . . f 5 5 1 f 1 5 5 f . . . . . 
                        . . f 5 5 1 f 1 5 5 f . . . . . 
                        . . . f 5 1 f 1 5 f . . . . . . 
                        . . . . f f f f f . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f f . . . . . . . 
                        . . . f f f f f f f . . . . . . 
                        . . . f 5 1 f 1 5 f . . . . . . 
                        . . f 5 5 1 f 1 5 5 f . . . . . 
                        . . f 5 5 1 f 1 5 5 f . . . . . 
                        . . . f 5 1 f 1 5 f . . . . . . 
                        . . . . f f f f f . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . f f f f . . f f f f f . . . . 
                        . f 5 5 f . . f 5 5 5 f . . . . 
                        . f 5 5 f . . f 5 5 5 f . . . . 
                        . f f 5 f f f f f f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f 5 1 f 1 5 f . . . . . . 
                        . . f 5 5 1 f 1 5 5 f . . . . . 
                        . . f 5 5 1 f 1 5 5 f . . . . . 
                        . . . f 5 1 f 1 5 f . . . . . . 
                        . . . . f f f f f . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
    bee.set_position(meow.x + 80, meow.y + 80)
    bee.follow(meow)
sprites.on_overlap(SpriteKind.player, SpriteKind.flower, on_on_overlap)

def on_overlap_tile(sprite, location):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def on_on_overlap2(sprite3, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap2)

def on_a_pressed():
    if meow.vy == 0:
        meow.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap3(sprite2, otherSprite3):
    info.change_life_by(-1)
    sprites.destroy(otherSprite3)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_on_overlap3)

def on_overlap_tile2(sprite22, location2):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        portal
    """),
    on_overlap_tile2)

bee: Sprite = None
meow: Sprite = None
flower3 = None
coin3 = None
scene.set_background_color(9)
meow = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . 3 3 3 3 3 3 3 . . . . . 
            . . . . 3 3 3 3 3 3 3 5 f . . . 
            . . . . 5 5 5 5 5 5 5 5 5 . . . 
            . . . . 5 5 5 5 5 5 5 5 5 . . . 
            . . . . . 5 . 5 . 5 . 5 . . . . 
            . . . . . 5 . 5 . 5 . 5 . . . . 
            . . . . . 5 . 5 . 5 . 5 . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(meow, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
meow.ay = 200
scene.camera_follow_sprite(meow)
for value in tiles.get_tiles_by_type(assets.tile("""
    estrela
""")):
    coin2 = sprites.create(assets.image("""
        coin
    """), SpriteKind.coin)
    animation.run_image_animation(coin2,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . e 5 e e e e e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . e 5 e e e e e 5 e . . . 
                        . . . . e 5 e 1 5 5 e 5 e . . . 
                        . . . . e 5 e 5 1 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . e 5 e e e e e 5 e . . . 
                        . . . . e 5 e 1 1 1 e 5 e . . . 
                        . . . . e 5 e 1 1 1 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . e 5 e e e e e 5 e . . . 
                        . . . . e 5 e 1 5 5 e 5 e . . . 
                        . . . . e 5 e 5 1 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . e 5 e e e e e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 e 5 5 5 e 5 e . . . 
                        . . . . e 5 5 5 5 5 5 5 e . . . 
                        . . . . . e e e e e e e . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
    tiles.place_on_tile(coin2, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile0
""")):
    flower2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 6 . 3 3 3 . 6 . . . . . 
                    . . . . 6 6 6 3 6 6 6 . . . . . 
                    . . . . . . . 6 . . . . . . . . 
                    . . . . . . . 7 . 7 7 . . . . . 
                    . . . . . . . 7 7 1 1 7 . . . . 
                    . . . . . . . 7 . 7 7 . . . . . 
                    . . . . . . . 7 . . . . . . . . 
                    . . . . . . . 7 . . . . . . . .
        """),
        SpriteKind.flower)
    tiles.place_on_tile(flower2, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
    """))
info.set_life(3)
if info.life() == 0:
    game.game_over(False)
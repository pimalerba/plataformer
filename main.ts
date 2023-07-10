namespace SpriteKind {
    export const coin = SpriteKind.create()
    export const flower = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.flower, function (sprite4, otherSprite2) {
    sprites.destroy(otherSprite2)
    bee = sprites.create(img`
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
        `, SpriteKind.Enemy)
    animation.runImageAnimation(
    bee,
    [img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    true
    )
    bee.setPosition(meow.x + 80, meow.y + 80)
    bee.follow(meow)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite, location) {
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.coin, function (sprite3, otherSprite) {
    info.changeScoreBy(1)
    sprites.destroy(otherSprite)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (meow.vy == 0) {
        meow.vy = -150
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function (sprite2, otherSprite3) {
    info.changeLifeBy(-1)
    sprites.destroy(otherSprite3)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`portal`, function (sprite22, location2) {
    game.gameOver(true)
})
let bee: Sprite = null
let meow: Sprite = null
let flower3 = null
let coin3 = null
let coin2: Sprite;
let flower2: Sprite;
scene.setBackgroundColor(9)
meow = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(meow, 100, 0)
tiles.setCurrentTilemap(tilemap`level1`)
meow.ay = 200
scene.cameraFollowSprite(meow)
for (let value of tiles.getTilesByType(assets.tile`estrela`)) {
    coin2 = sprites.create(assets.image`coin`, SpriteKind.coin)
    animation.runImageAnimation(
    coin2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    true
    )
    tiles.placeOnTile(coin2, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
}
for (let value2 of tiles.getTilesByType(assets.tile`myTile0`)) {
    flower2 = sprites.create(img`
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
        `, SpriteKind.flower)
    tiles.placeOnTile(flower2, value2)
    tiles.setTileAt(value2, assets.tile`transparency16`)
}
info.setLife(3)
if (info.life() == 0) {
    game.gameOver(false)
}

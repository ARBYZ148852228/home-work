from hitbox import Hitbox

hb1 = Hitbox(x=0, y=100, width=100, height=100)
hb2 = Hitbox(x=100, y=100, width=100, height=100)
hb3 = Hitbox(x=200, y=100, width=100, height=100)


intersection1 = hb1.intersects(hb2)
intersection2 = hb2.intersects(hb3)
intersection3 = hb1.intersects(hb3)
print(intersection1)
print(intersection2)
print(intersection3)
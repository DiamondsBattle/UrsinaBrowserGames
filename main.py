from ursina import *
from browser import timer


def on_click(b):
    global player
    if b.color != color.dark_gray:
        return
    b.color = colors[player]
    b.text = player
    player = 'x' if player == 'o' else 'o'
    game_finished()

def victory():
    t = Text('Victory')
    timer.set_timeout(timeout=3)
    for i in buttons:
        i.color = color.dark_gray
        i.text = ''
    t.text = ''

def game_finished():
    if buttons[0].color == buttons[1].color == buttons[2].color != color.dark_gray: victory()
    if buttons[3].color == buttons[4].color == buttons[5].color != color.dark_gray: victory()
    if buttons[6].color == buttons[7].color == buttons[8].color != color.dark_gray: victory()
    if buttons[0].color == buttons[3].color == buttons[6].color != color.dark_gray: victory()
    if buttons[1].color == buttons[4].color == buttons[7].color != color.dark_gray: victory()
    if buttons[2].color == buttons[5].color == buttons[8].color != color.dark_gray: victory()
    if buttons[0].color == buttons[4].color == buttons[8].color != color.dark_gray: victory()
    if buttons[2].color == buttons[4].color == buttons[6].color != color.dark_gray: victory()
    for i in buttons:
        if i.color == color.dark_gray:
            return
    t = Text('Tie')
    timer.set_timeout(3)
    t.text = 'Resetting'
    timer.set_timeout(2)
    t.text = ''
    for i in buttons:
        i.color = color.dark_gray
        i.text = ''


app = Ursinaa()

camera.fov = 4
camera.position = (1, 1)
player = 'x'
colors = {'x': color.orange,
          'o': color.blue}
buttons = []

for x in range(3):
    for y in range(3):
        b = Button(position=(x, y, 0), color=color.dark_gray)
        buttons.append(b)
        b.on_click = Func(on_click, b)
        player = 'o' if player == 'x' else 'x'


app.run()
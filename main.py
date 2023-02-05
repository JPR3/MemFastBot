import pyautogui
from pynput import mouse, keyboard
from time import sleep

WHITE_IMG = "Images/CardWhite.png"
GRAY_IMG = "Images/GreySample.png"
BACK_IMG = "Images/CardBack.png"
CIRCLE_RED = "Images/RedCircle.png"
CIRCLE_BLU = "Images/BlueCircle.png"
CIRCLE_GRE = "Images/GreenCircle.png"
CIRCLE_PUR = "Images/PurpleCircle.png"
CIRCLE_YEL = "Images/YellowCircle.png"
CIRCLE_GRAY = "Images/GreyCircle.png"
STAR_YEL = "Images/Star.png"
STAR_GRAY = "Images/GreyStar.png"
TRIANGLE_BLU = "Images/BlueTriangle.png"
TRIANGLE_GRAY = "Images/GreyTriangle.png"
SQUARE_GRE = "Images/GreenSquare.png"
SQUARE_GRAY = "Images/GreySquare.png"
CROSS_PUR = "Images/PurpleCross.png"
CROSS_GRAY = "Images/GreyCross.png"
COLOR_SHAPES = [CIRCLE_RED, CIRCLE_BLU, CIRCLE_GRE, CIRCLE_PUR, CIRCLE_YEL, STAR_YEL, TRIANGLE_BLU, SQUARE_GRE, CROSS_PUR]
GRAY_SHAPES = [CIRCLE_GRAY, STAR_GRAY, TRIANGLE_GRAY, SQUARE_GRAY, CROSS_GRAY]
print("Tab into CoolMath and drag from the top left of the game window to the bottom right")
print("Then press space to begin")
# Get window size from user
window_origin = 0
window_region = 0
def wait_for_image(img):
    global window_region
    image = pyautogui.locateOnScreen(img, region=window_region, grayscale=True)
    while image == None:
        image = pyautogui.locateOnScreen(img, region=window_region, grayscale=True)
    return

def on_click(x, y, button, pressed):
    global window_region
    global window_origin
    if pressed:
        window_origin = (x, y)
    else:
        window_region = window_origin + (x - window_origin[0], y - window_origin[1])
        return False
def on_release(key):
    if key == keyboard.Key.space:
        print("Space pressed!")
        return False

with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()

# Wait to begin
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()
#Start

card_positions = []
while(True):
    #Wait until a card white is shown
    wait_for_image(WHITE_IMG)
    card_positions.clear()
    screen_img = pyautogui.screenshot()
    #Search for shapes
    for shape in COLOR_SHAPES:
        card_positions.extend(list(set(pyautogui.locateAll(shape, screen_img, grayscale=False, region=window_region))))
    if(len(card_positions) == 0):
        for shape in GRAY_SHAPES:
            card_positions.extend(list(set(pyautogui.locateAll(shape, screen_img, grayscale=False, region=window_region))))
    
    print(f"Found {len(card_positions)} cards")
    if(len(card_positions) >= 10):
        sleep_time = 0.3 + (0.1 * (len(card_positions) - 10))
        sleep(sleep_time)
    #Click on the cards
    for pos in card_positions:
        pyautogui.leftClick(pos[0], pos[1])
        print(f"Clicking at {pos[0]}, {pos[1]}")
    
    sleep(1)
    

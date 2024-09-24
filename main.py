import mss
import numpy as np
import pyautogui
import keyboard


# Reaction time

REACTION_TARGET_COLOR = [(106, 219, 75),(209, 135, 43)]

def get_pixel_color():
    with mss.mss() as sct:
        # Capture the screen
        monitor = sct.monitors[1] 
        width, height = monitor["width"], monitor["height"]

        # Define the region to capture the center pixel
        center_x, center_y = width // 2, height // 2
        region = {
            "top": center_y,
            "left": center_x,
            "width": 1, 
            "height": 1
        }

        # Capture the pixel at the center of the screen
        screenshot = sct.grab(region)
        
        # Convert the pixel data to an RGB tuple
        img_np = np.array(screenshot)
        pixel_color = img_np[0, 0, :3]  # Get the RGB values of the pixel

        return tuple(pixel_color) 

def reaction_game():
    pixel_color = get_pixel_color()

    # Check if the color matches
    if pixel_color == REACTION_TARGET_COLOR[0] or pixel_color == REACTION_TARGET_COLOR[1]:
        # Click
        pyautogui.click(pyautogui.size()[0] // 2, pyautogui.size()[1] // 2)

# Aim trainer
region = {
    "top": 290,
    "left": 70,
    "width": 1800,
    "height": 510
}
TARGET_COLOR = (149, 195, 232)  

def aim_trainer():
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        img_np = np.array(screenshot)

        for y in range(region["height"]):
            for x in range(region["width"]):
                pixel = img_np[y, x, :3]

                # Compare pixel with color
                if np.all(pixel == TARGET_COLOR):
                    click_x = region["left"] + x
                    click_y = region["top"] + y

                    print(f"Target pixel found at ({click_x}, {click_y}), clicking!")
                    pyautogui.click(click_x, click_y)
                    continue

        print("No target pixel found in the region.")

# Main game loop
def main():
    while True:
        game = input("Choose game (aim/reaction): ").strip().lower()

        if game == "aim":
            while not keyboard.is_pressed('esc'):
                aim_trainer()
        elif game == "reaction":
            while not keyboard.is_pressed('esc'):
                reaction_game()
        else:
            print("Invalid game choice, please choose 'aim' or 'reaction'.")

        if keyboard.is_pressed('esc'):
            print("Escape key pressed. Exiting the program...")
            break

    print("Script has stopped.")

if __name__ == "__main__":
    main()
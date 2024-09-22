import mss
import numpy as np
import pyautogui
import keyboard

TARGET_COLOR = [(106, 219, 75),(209, 135, 43)]

def get_pixel_color_at_center():
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

def check_and_click_if_color_matches():
    pixel_color = get_pixel_color_at_center()

    # Check if the color matches
    if pixel_color == TARGET_COLOR[0] or pixel_color == TARGET_COLOR[1]:
        print(f"Color {pixel_color} matches target. Clicking!")
        # Click
        pyautogui.click(pyautogui.size()[0] // 2, pyautogui.size()[1] // 2)
    else:
        print(f"Color {pixel_color} does not match target.")

def main():
    while True:
        check_and_click_if_color_matches()
        
        if keyboard.is_pressed('esc'):
            print("Escape key pressed. Exiting...")
            break

    print("Script has stopped.")

if __name__ == "__main__":
    main()
from main import AzanBot
import time

# Flag to check if the application has run
hasRun = False

import time
import keyboard


def run():
    global hasRun
    if hasRun != True:
        print("The application is starting...")
        hasRun = True
        AzanBot()  # Run main class
    else:
        print("The application is running!")


if __name__ == "__main__":
    run()
    while True:
        time.sleep(1)
        if keyboard.is_pressed("ctrl+alt+c"):  # check if ctrl+alt+c is pressed
            print("Closing the application...")
            break  # exit the loop to stop the application

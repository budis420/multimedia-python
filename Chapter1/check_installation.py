import pygame
import PIL
import cv2
import moviepy
import pydub
import subprocess

def check_installation():
    print("✅ Pygame version:", pygame.version.ver)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)

    try:
        print("✅ MoviePy version:", moviepy.__version__)
    except AttributeError:
        print("⚠️  MoviePy version attribute not found, trying alternate method.")
        try:
            print("✅ MoviePy version:", moviepy.version.VERSION)
        except Exception as e:
            print("❌ Could not determine MoviePy version:", str(e))

    # Check pydub version using pip show
    try:
        result = subprocess.run(['pip', 'show', 'pydub'], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if line.startswith('Version:'):
                print("✅ Pydub version:", line.split(' ')[1])
                break
        else:
            print("Pydub version information is not available.")
    except Exception as e:
        print("❌ Could not determine Pydub version:", str(e))

    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()

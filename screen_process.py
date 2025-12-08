import pyautogui
from PIL import Image, ImageOps
from pathlib import Path
import time
import zipfile  
import os       

def capture_process_and_zip():
    
    
    desktop_path = Path.home() / "Desktop"
    
    
    image_name = "mirrored_screenshot.jpg"
    image_path = desktop_path / image_name
    

    zip_name = "screenshot_archive.zip"
    zip_path = desktop_path / zip_name

    print("Capturing screenshot in 3 seconds...")
    time.sleep(3)

    try:
        
        screenshot = pyautogui.screenshot()
        print("Screenshot captured.")

        mirrored_image = ImageOps.mirror(screenshot)
        print("Image mirrored.")

        inverted_image = ImageOps.invert(mirrored_image.convert('RGB'))
        bw_image = inverted_image.convert('L')

        
        bw_image.save(image_path, "JPEG", optimize=True, quality=50)
        print(f"Image saved temporarily at: {image_path}")

        

        print("Zipping the file...")
        
        
    
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            

            zipf.write(image_path, arcname=image_name)
            
        print(f"Zip file created at: {zip_path}")

        

        os.remove(image_path) 
        print("Original image file removed (Clean up).")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    capture_process_and_zip()
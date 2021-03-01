# Py-Glasses

Py-Glasses are me trying to use python and openCV to create a sort of smart glasses thing.
This is the varient where i am using object detection to do things. There is another repository wher there is a text overlay as a sort of HUD.


This will mainly be centred around a VR headset (The type you put your phone into) and a Raspberry Pi zero W

Ideas so far:
- Use camera(s) on the front of the headset to relay the live images to a webpage,
- The webpage will display the images in the correct format for the phone to see and use in the headset,
- Information will be added to those images,
- And object detection will be used to point out things like stop signs, other people etc.


- Once this is all working, i will try to encorporate my python vitual assistant into it,
- This will probably be controlled by a ring (or something like it) with a joystick.

***To run object detection:***
```python object_detection_webcam-(yolov3_tiny).py```

in future this and the HUD repo will be intergrated together, with the virtual assistant, and will therfore have a switching mechanism to change form HUD to detection.


# Stuff needed:
- ```pip install -r requirements.txt```
- you will need to create a file called ```.env``` the format of this file is as follows:
```
#.env

HUD_PATH = \\path\\to\\the\\main-HUD\\file\\here\\\main-HUD.py
```
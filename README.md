# Py-Glasses

## This Is Where All The Code Is Kept For My Py-Glasses Project

<br> 

### If you Want To Download This Code Then see The Commands Below:

> #### HUD
> - This is the part that would be running on the VR Goggles (RPi server / Phone)
> - To Get The Code:
> - - `git clone --branch HUD https://CryptoidCoder/Py-Glasses.git`

> #### Detection
> - This is the part that runs object detection
> - To Get The Code:
> - - `git clone --branch Detection https://CryptoidCoder/Py-Glasses.git`

> #### Testing
> - This is the part that has all of my test scripts, and other peoples repos - that I was taking inspiration from
> - To Get The Code:
> - - `git clone --branch Testing https://CryptoidCoder/Py-Glasses.git`

> ### Running:
> - Generally there is a `requirements.txt` file, so run the following command to get all the modules:
> - - `pip install -r requirements.txt`
>
> - you will often have to create `.env` files with api keys etc in them
>
> - There should alwasy be a README.md file that will explain anything else though.


### More About The Project:

- ### Py-Glasses

Py-Glasses are me trying to use python and openCV to create a sort of smart glasses thing.
This is the varient where I am using object detection to do things. There is another repository wher there is a text overlay as a sort of HUD.


This will mainly be centred around a VR headset (The type you put your phone into) and a Raspberry Pi zero W

Ideas so far:
- Use camera(s) on the front of the headset to relay the live images to a webpage,
- The webpage will display the images in the correct format for the phone to see and use in the headset,
- Information will be added to those images,
- And object detection will be used to point out things like stop signs, other people etc.


- Once this is all working, I will try to encorporate my python vitual assistant into it,
- This will probably be controlled by a ring (or something like it) with a joystick.

you will need to download some things in some places, in the branch is a README.md file, it will contain the links to anything you may need to download.

I do not think that there are any requirements.txt files, however there may be, if you are getting import errors, let me know and I can let you know what you need to pip install, otherwise just google the errors.
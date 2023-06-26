# useful-code

This repo contains a bunch of code I like to reuse and want to have easy access to.

# Links

## Create a Python virtual environment

https://gist.github.com/Samuel-Risner/2318e00383ebf54dfc96e7a04e691334

# Folders in this repo

## convert pixel art to svg

Turns images into svgs. This is done pixel by pixel and is then compressed with svgo (https://github.com/svg/svgo).

### How to use:

1. Open the folder in your terminal

2. Install svgo by running:

```shell
npm init
```

3. Create a virtual environment and install the requirements (see the link under "Create a Python virtual environment")

4. Copy the images that you want to convert into the folder "images_to_convert"

5. Run main.py

## pygame windows

A basic template for creating different windows with pygame. Can also resize and enter full-screen.

#!/usr/bin/env python3
from prusacamconfig import PRUSACONNECT_URL, FINGERPRINT, CAMERA_TOKEN
import requests

def push_to_prusaconnect(jpg_image):
    response = requests.put(
        PRUSACONNECT_URL,
        headers={
            "accept": "application/json",
            "content-type": "image/jpg",
            "fingerprint": FINGERPRINT,
            "token": CAMERA_TOKEN,
        },
        data=jpg_image
    )
    if response.status_code != 204:
        print(response.content)
    else:
        print("Success")

import os
if os.uname().sysname == 'Darwin':
    # MacOS
    import imageio as iio
    # import matplotlib.pyplot as plt

    camera = iio.get_reader("<video0>")
    captured_img = camera.get_data(0)
    camera.close()
    captured_jpg = iio.imwrite("<bytes>", captured_img, format=".jpeg")
    push_to_prusaconnect(captured_jpg)
else:
    print("Unsupported")
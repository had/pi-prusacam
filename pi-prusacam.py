#!/usr/bin/env python3
from prusacamconfig import PRUSACONNECT_URL, FINGERPRINT, CAMERA_TOKEN, PRUSACONNECT_TIMEOUT_S
import requests
from requests.exceptions import ConnectionError, Timeout
import os


def push_to_prusaconnect(jpg_image, timeout_s=PRUSACONNECT_TIMEOUT_S):
    try:
        response = requests.put(
            PRUSACONNECT_URL,
            headers={
                "accept": "application/json",
                "content-type": "image/jpg",
                "fingerprint": FINGERPRINT,
                "token": CAMERA_TOKEN,
            },
            data=jpg_image,
            timeout=timeout_s
        )
        if response.status_code != 204:
            print(response.content)
        else:
            print("Success")
    except ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except Timeout as _:
        # The request timed out
        print(f'Timeout error: The request took longer than the timeout value of {timeout_s} seconds.')
    except Exception as e:
        # Handle other possible exceptions
        print(f'An unexpected error occurred: {e}')


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

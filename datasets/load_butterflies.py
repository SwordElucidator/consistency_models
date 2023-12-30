import os

import requests


def load_dataset():
    url = "https://datasets-server.huggingface.co/rows"
    params = {
        "dataset": "huggan/smithsonian_butterflies_subset",
        "config": "default",
        "split": "train",
        "offset": "0",
        "length": "100"
    }

    response = requests.get(url, params=params)
    data = response.json()
    save_dir = "images"  # Directory to save the images
    os.makedirs(save_dir, exist_ok=True)

    for item in data['rows']:
        image_url = item['row']['image']['src']
        image_name = f"{item['row_idx']}.jpg"
        image_path = os.path.join(save_dir, image_name)

        # Download the image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(image_path, "wb") as image_file:
                image_file.write(image_response.content)
            print(f"Downloaded image: {image_name}")
        else:
            print(f"Failed to download image: {image_name}")


if __name__ == '__main__':
    load_dataset()
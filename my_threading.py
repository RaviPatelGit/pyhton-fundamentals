# https://www.youtube.com/watch?v=IEEhzQoKtQU
# Python Threading Tutorial: Run Code Concurrently Using the Threading Module

# https://unsplash.com/photos/735Uz2yMMfQ
# https://unsplash.com/photos/cR7JhspyWqI
# https://unsplash.com/photos/2uAOFkBFpJ0

import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')
#
# for url in img_urls:
#     download_image(url)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')

from DFT import fft2d
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import click
import cv2

@click.command()
@click.argument('img')

def overfreq(img):
    cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    print(type(img))
    fft2 = fft2d(img)
    print(np.abs(fft2))
    h,w = fft2.shape
    print(f'h:{h}, w:{w}')
    fft_plus = np.pad(fft2, ((h//2,h//2), (w//2,w//2)), mode='constant', constant_values=0)
    fig_plus = fft2d(fft_plus, inverse=True)
    print(fig_plus.real)
    plt.imshow(fig_plus.real)
    plt.show()
    cv2.imwrite('overfreq.jpg', fig_plus.real)

if __name__ == '__main__':
    overfreq()
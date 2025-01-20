from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import click
from DFT import fft2d
from STFT import stft





@click.command()
@click.argument('img')
@click.option('--fc', '-f', default=300)
@click.option('--cutoff', '-c', default=200)
def IPM(img:str, fc, cutoff):
    #Only for coloured images
    if type(img) == str:
        fig = imread(img)
        print(fig.shape)
        fig = np.mean(fig, -1)

    
    h, w= fig.shape
    fft=fft2d(fig)
    plt.imshow(fft.real)
    plt.show()
    plt.imshow(fft.imag)
    plt.show()
    vch = np.array([np.arange(w) for i in range(h)])
    vcv = np.array([np.arange(h) for i in range(w)]).T
    vc = vch + vcv
    csin = np.sin(2*np.pi*fc*(vc/h))
    ccos = np.cos(2*np.pi*fc*(vc/h))
    C = csin
    #plt.imshow(np.abs(C))
    #plt.show()
    I = fig*ccos

    Q = fig*csin

    V = I+Q*1j
    c = np.reshape(C, (-1, 1))
    v = np.reshape(V, (-1, 1))
    phi = np.zeros(h*w)
    for i in range(h*w):
        phi[i] = np.abs(np.angle(np.dot(v[i], np.conj(c[i]))))
        if phi[i] < 0:
            phi[i] += 2*np.pi


    phi = np.reshape(phi, (h, w)) 
    #plt.imshow(phi)
    #plt.show()
    print(phi)
    phifft = np.fft.fft(phi[h//2])
    plt.plot(np.arange(w), phifft.real, 'r')
    plt.plot(np.arange(w), phifft.imag, 'b')
    plt.show()

    plt.imshow(phi)
    plt.show()
    #plt.imwrite('IPM.jpg', vm)

    return phi

if __name__ == '__main__':
    IPM()
    
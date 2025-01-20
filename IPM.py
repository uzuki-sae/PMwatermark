from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import click
from DFT import fft2d
from STFT import stft


def rolling(x):
    a=x[1:,1:]
    b=x[:-1,:-1]
    c=x[1:,:-1]
    d=x[:-1,1:]
    return (a+b+c+d)/4


@click.command()
@click.argument('img')
@click.option('--fc', '-f', default=300.0)
@click.option('--cutoff', '-c', default=200)
def IPM(img:str, fc:float, cutoff):
    #Only for coloured images
    if type(img) == str:
        fig = imread(img)
        print(fig.shape)
        fig = np.mean(fig, -1)

    
    h, w= fig.shape
    figfft = np.fft.fft(fig[h//2])
    plt.plot(np.arange(w), figfft.real, 'r', )
    plt.plot(np.arange(w), figfft.imag, 'b')
    plt.xticks(np.arange(0, w, 50))
    plt.show()
    vch = np.array([np.arange(w) for i in range(h)])
    vcv = np.array([np.arange(h) for i in range(w)]).T
    vc = vch + vcv
    csin = np.sin(2*np.pi*fc*(vc/h))
    ccos = np.cos(2*np.pi*fc*(vc/h))

    #plt.imshow(np.abs(C))
    #plt.show()
    I = rolling(rolling(fig*ccos))

    Q = rolling(rolling(fig*csin))

    V = I+Q*1j
    v = np.reshape(V, (-1, 1))
    h, w = V.shape
    phi = np.zeros(h*w)
    for i in range(h*w):
        phi[i] = np.angle(v[i])
        #if phi[i] < 0:
        #    phi[i] += 2*np.pi


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
    
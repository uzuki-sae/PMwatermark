# Import libraries
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import click

#@click.command()
#@click.argument('fig')
#@click.option('--inverse', default=False)
#@click.option('--show', default=True)
def fft2d(fig, inverse=False, show=True):

    if type(fig) == str:
        fig = imread(fig)
        print(fig.shape)
        fig = np.mean(fig, -1)
    else:
        
        print(type(fig))
        pass
    
    #if show:
    #    plt.imshow(fig)
    #    plt.show()

        # Much more efficient to use fft2
    if inverse==False:
        #fft = np.fft.fft(fig, axis=0)
        fft2 = np.fft.fft2(fig)
        if show:
            print(np.abs(fft2))
            fft=np.sum(np.abs(fft2),axis=1)
            x = np.arange(0, len(fft), 1)
            plt.plot(x, np.log(np.abs(fft)))
            #plt.imshow(np.log(np.abs(fft2)))
            #plt.colorbar()
            #plt.show()

            
        return fft2
    else:
        ifft2 = np.fft.ifft2(fig)
        if show:
            plt.imshow(ifft2.real)
            plt.show()
        return ifft2
    
if __name__ == '__main__':
    fft2d()


from DFT import fft2d
import numpy as np
import cv2
import click

@click.command()
@click.argument('img')
@click.option('--fc', '-f', default=300)
@click.option('--beta', '-b', default=np.pi)
def fm(img:str, fc, beta):
    beta=float(beta)
    fig=cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    fig=fig*1/np.max(fig)
    h, w = fig.shape
    vch = np.array([np.arange(w) for i in range(h)])
    vcv = np.array([np.arange(h) for i in range(w)]).T
    vc = vch + vcv
    vm = np.sin(2*np.pi*fc*(vc/h)+beta*fig)*255
    print(vm)
    cv2.namedWindow('after_PM')
    cv2.imshow('after_PM', vm)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('after_PM.jpg', vm)

    

if __name__ == '__main__':
    fm()


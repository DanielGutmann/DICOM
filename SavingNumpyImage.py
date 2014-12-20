from numpy import save, savez

__author__ = 'Agnieszka'


class SavingImageAsNumpy(object):
    def __init__(self, path):
        self.path = path

    def saveImage(self, image, sigma,spacing):
        outfile = file(self.path + str(sigma) + '.npy', 'wb')
        print('file is saving')
        savez(outfile, image=image, sigma=sigma,spacing=spacing)
        outfile.flush()
        outfile.close()
        print('file is saved')

    def saveIndex(self, x, y, sigma):
        outfile = file(self.path +'min_max'+ str(sigma) + '.npy', 'wb')
        print('file is saving')
        savez(outfile, min=x, max=y, sigma=sigma)
        outfile.flush()
        outfile.close()
        print('file is saved')
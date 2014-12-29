__author__ = 'Agnieszka'
from scipy.interpolate import griddata
import numpy as np
from scipy.ndimage import affine_transform, rotate


def rotate_matrix(azimuth, elevation):
    return np.array([[np.cos(azimuth) * np.cos(elevation), -np.sin(azimuth), -np.cos(azimuth) * np.sin(elevation)],
                     [np.sin(azimuth) * np.cos(elevation), np.cos(azimuth), -np.sin(azimuth) * np.sin(elevation)],
                     [np.sin(elevation), 0, np.cos(elevation)]])


def rotation(matrix_size, azimuth, elevation):
    rotate_m = rotate_matrix(azimuth, elevation)
    rotated = []
    pixel = []
    for i in range(-matrix_size, matrix_size + 1, 1):
        for j in range(-matrix_size, matrix_size + 1, 1):
            for z in range(-int(matrix_size / 10), int(matrix_size / 10) + 1, 1):
                pixel.append(np.array([i, j, z]))
                rotated.append(np.dot(np.array([i, j, z]), rotate_m))
    # rotated.append(np.dot(np.array([512, 512, 74]), rotate_m))
    return np.array(rotated), np.array(pixel)


class rotateImage():
    def __init__(self, Image3D):
        self.image3D = Image3D
        self.histogra_size = 8

    def apply(self):
        list_keypoints = self.image3D.keypoints_orientation
        for keypoint in list_keypoints[:-1]:
            azimuth = keypoint[4]
            elevation = keypoint[3]
            keyp = keypoint[0:3]
            self.apply_for_keypoint(azimuth, elevation, 20, keyp)


    def apply_for_keypoint(self, azimuth, elevation, size_of_area, key_point):
        key_point=key_point+20
        area_begin = key_point[0] - size_of_area
        area_end = key_point[0] + size_of_area + 1
        area_begin_y = key_point[1] - size_of_area
        area_end_y = key_point[1] + size_of_area + 1
        area_begin_z = key_point[2] - np.ceil(size_of_area / (self.image3D.spacing[2] / self.image3D.spacing[1]))
        area_end_z = key_point[2] + np.ceil(size_of_area / (self.image3D.spacing[2] / self.image3D.spacing[1])) + 1

        temp_im=np.zeros(np.array([self.image3D.Image3D.shape[0]+40,self.image3D.Image3D.shape[1]+40,self.image3D.Image3D.shape[2]+40]))
        temp_im[20:temp_im.shape[0]-20,20:temp_im.shape[1]-20,20:temp_im.shape[2]-20]=self.image3D.Image3D
        Image3D =temp_im
        Image3D=self.image3D.Image3D#Image3D[area_begin:area_end, area_begin_y:area_end_y, area_begin_z:area_end_z]
        print(Image3D.shape)
        transform = rotate_matrix(azimuth, elevation)
        x = np.array([0, 0, Image3D.shape[2] - 1]).dot(transform.T)
        y = np.array([0, Image3D.shape[1] - 1, 0]).dot(transform.T)
        z = np.array([Image3D.shape[0] - 1, 0, 0]).dot(transform.T)
        spacing = np.array([self.image3D.spacing[0],self.image3D.spacing[1],self.image3D.spacing[2]]).dot(transform.T)
        if(np.abs(spacing)<0.1).sum()>0:

            index=np.abs(spacing)<0.01
            print(spacing)

            spacing[index]=self.image3D.spacing[index]


        s = np.abs(x) + np.abs(y) + np.abs(z)+1
        offset = 0.5 * (np.array([Image3D.shape[0],Image3D.shape[1],Image3D.shape[2]]) - 1) - (0.5 * s).dot(transform)

        print(spacing)
        # hack nearest zastepuje prolemy na brzegach nie do ominiacia jezeli obrocimy wiekszy obszar i wytniemy z niego srodek unikamy problemu
        dst = affine_transform(Image3D, transform.T, order=2, offset=offset, output_shape=s, cval=0 ,
                               output=np.float32)


        return dst, np.abs(spacing)

    def imageInterp(self):
        return griddata(self.grid, self.image3D.get_image3D()[
            self.pixel_index[:, 0], self.pixel_index[:, 1], self.pixel_index[:, 2]]
                        , (self.x, self.y, self.z), method='linear')

        '''
        self.grid, self.pixel_index = rotation(size_of_area, azimuth, elevation)

        x = key_point[0]
        y = key_point[1]
        z = key_point[2]

        step_x = self.image3D.spacing[0]
        step_y = self.image3D.spacing[1]
        step_z = self.image3D.spacing[2]


        self.pixel_index[:, 0] = self.pixel_index[:, 0] + x
        self.pixel_index[:, 1] = self.pixel_index[:, 1] + y
        self.pixel_index[:, 2] = self.pixel_index[:, 2] + z
        #print(np.max(self.grid[:, 0]),np.max(self.grid[:, 1]),np.max(self.grid[:, 2]))
        self.grid[:, 0] = self.grid[:, 0] + x
        self.grid[:, 1] = self.grid[:, 1] + y
        self.grid[:, 2] = self.grid[:, 2] + z
        #self.grid[:, 0] = self.grid[:, 0]
        #self.grid[:, 1] = self.grid[:, 1]
        #self.grid[:, 2] = self.grid[:, 2] *step_z/step_y

        self.x, self.y, self.z = np.mgrid[-255:255, -255:255, -25:25]
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z
        self.x = self.x
        self.y = self.y
        #self.z = self.z *step_z/step_y

        #im = self.imageInterp()

        #print(np.max(self.grid[:, 0]),np.max(self.grid[:, 1]),np.max(self.grid[:, 2]))
        #print(np.min(self.grid[:, 0]),np.min(self.grid[:, 1]),np.min(self.grid[:, 2]))
        if(np.min(self.grid[:, 0])<0):
            s_x=abs(np.max(self.grid[:, 0]))+abs(np.max(self.grid[self.grid[:, 0]<0.0][:,0]))+1
        else: s_x=np.max(self.grid[:, 0])+1
        if(np.min(self.grid[:, 1])<0):
            s_y=abs(np.max(self.grid[:, 1]))+abs(np.max(self.grid[self.grid[:, 1]<0.0][:,1]))+1
        else: s_y=np.max(self.grid[:, 1])+1
        if(np.min(self.grid[:, 2])<0):
            s_z=abs(np.max(self.grid[:, 2]))+abs(np.max(self.grid[self.grid[:, 2]<0.0][:,2]))+1
        else: s_z=np.max(self.grid[:, 2])+1
        print(s_x,s_y,s_z)

        Z=np.zeros((s_x,s_y,s_z))
        for i in range(0,self.pixel_index.shape[0]):
            a=self.grid[i]
            b=self.pixel_index[i]
            Z[self.grid[i, 0], self.grid[i, 1], self.grid[i, 2]]=self.image3D.get_image3D()[self.pixel_index[i, 0], self.pixel_index[i, 1], self.pixel_index[i, 2]]
            if np.sum(a<0)==0:
                if(a[0]<512) and a[1]<512 and a[2]<74 and b[0]<s_x and b[1]<s_y and b[2]<s_z:
                    T[self.pixel_index[i, 0], self.pixel_index[i, 1], self.pixel_index[i, 2]]=self.image3D.get_image3D()[self.grid[i, 0], self.grid[i, 1], self.grid[i, 2]]
        print()
        '''
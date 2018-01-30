from os.path import join as opj, basename
from glob import glob

from PIL import Image
from torch.utils.data import Dataset


class FolderWithImagesAndMasks(Dataset):
    def __init__(self, data_folder, transforms=None):
        self.image_folder_names = glob(opj(data_folder, '*'))
        self.transforms = transforms

    def __len__(self):
        return len(self.image_folder_names)

    def __getitem__(self, index):
        im_path = opj(self.image_folder_names[index], 'images', basename(self.image_folder_names[index]) + '.png')
        im = Image.open(im_path)

        mask_paths = glob(opj(im_path, 'masks', '*.png'))
        masks = []
        for p in mask_paths:
            mask = Image.open(p)
            masks.append(mask)

        if self.transforms:
            im = self.transforms(im)

        return im, masks

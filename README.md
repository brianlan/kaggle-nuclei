# kaggle-nuclei
It's the code for the competetion held on Kaggle - [2018 Data Science Bowl](https://www.kaggle.com/c/data-science-bowl-2018/).

## What does the data look like?
<img src="https://github.com/brianlan/kaggle-nuclei/blob/master/results/kaggle-nuclei-sample-image-1.png" width="400"/><img src="https://github.com/brianlan/kaggle-nuclei/blob/master/results/kaggle-nuclei-sample-image-2.png" width="410"/>

### The trait of this dataset
- Image is stored as png file. It contains 4 channels, i.e. RGBA.
- There're two types of source image data: one is ```brightfield```, the other is ```fluorescence```. The values in the former one's 3 channels are different while the latter one has exactly the same channel values in RGB.
- The numbers of label masks of different images varies, and there's no pixel belonging to more than 1 mask, which means it could be deemed as an Instance Segmentation Task. 

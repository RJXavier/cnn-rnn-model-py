import glob
import os


def labels_to_number(path):

    print(glob.glob(path + '*'))
    for i in glob.glob(path + '*'):
        print(i.split(os.path.sep))
        print(glob.glob(os.path.join(path,'*')))

    
    #classes = [i.split(os.path.sep)[-1] for i in glob.glob(os.path.join(path,'*'))]
    classes = [i.split(os.path.sep)[3] for i in glob.glob(path + '*')]


    classes.sort()

    labels_dict = {}
    for i, label in enumerate(classes):
        labels_dict[label] = i

    return labels_dict



def videos_to_dict(path, labels):

    videos_dict = {}
    for root, dirs, files in os.walk(os.path.relpath(path)):
        for file in files:
            video_name = os.path.join(root, file)
            dir_name = os.path.basename(os.path.dirname(video_name))  # label
            videos_dict[video_name] = labels[dir_name]

    return videos_dict


#classes = [i.split(os.path.sep)[-1] for i in glob.glob(os.path.join(path,'*'))]
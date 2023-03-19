import numpy as np
from pathlib import Path
import os

# MODIFY INPUT/OUTPUT DIR
working_dir = Path(r"./")
npz_dir = working_dir / "desc"
colmap_desc_dir = working_dir / "colmap_desc"
matches_dir = working_dir
img_format = ".JPG"


# MAIN STARTS HERE
matches_dict = {}
pair_files = os.listdir(npz_dir)
for pair in pair_files:
    im1, im2, _ = pair[:-4].split("_", 2)
    im1 = im1 + img_format
    im2 = im2 + img_format
    print(im1, im2)
    matches_matrix = np.empty((0,2))

    npz_file = npz_dir / pair
    npz_file = np.load(npz_file)
    kp_im1 = npz_file['keypoints0']
    kp_im2 = npz_file['keypoints1']
    matches = npz_file['matches']

    with open(colmap_desc_dir / "{}.txt".format(im1), 'w') as colmap_desc1:
        colmap_desc1.write(f"{kp_im1.shape[0]} 128\n")
        for r in range(kp_im1.shape[0]):
            colmap_desc1.write(f"{kp_im1[r,0]} {kp_im1[r,1]} 0.00 0.00\n")
    
    with open(colmap_desc_dir / "{}.txt".format(im2), 'w') as colmap_desc2:
        colmap_desc2.write(f"{kp_im2.shape[0]} 128\n")
        for r in range(kp_im2.shape[0]):
            colmap_desc2.write(f"{kp_im2[r,0]} {kp_im2[r,1]} 0.00 0.00\n")

    for i in range(len(matches)):
        if matches[i] != -1:
            new_matches = np.array([[int(i), int(matches[i])]])
            matches_matrix = np.vstack((matches_matrix, new_matches))
    
    matches_dict[f"{im1} {im2}"] = matches_matrix
    
    
with open(matches_dir / "superglue_matches.txt", 'w') as matches_file:
    for pair in list(matches_dict.keys()):
        matches_file.write(f"{pair}\n")
        
        for r in range(matches_dict[pair].shape[0]):
            if matches_dict[pair][r, 1] != -1:
                matches_file.write(f"{int(matches_dict[pair][r, 0])} {int(matches_dict[pair][r, 1])}\n")
        
        matches_file.write(f"\n\n")
    





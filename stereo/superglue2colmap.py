import numpy as np
from pathlib import Path

# MODIFY INPUT/OUTPUT DIR
im1 = "IMG01.JPG"
im2 = "IMG02.JPG"
working_dir = Path(r"./")
npz_file = working_dir / Path(r"desc/IMG01_IMG02_matches.npz")
colmap_desc_dir = working_dir / Path(r"colmap_desc")
matches_dir = working_dir


# MAIN STARTS HERE
npz_file = np.load(npz_file)
print("npz_file.files\n", npz_file.files)
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

with open(matches_dir / "superglue_matches.txt", 'w') as matches_file:
    matches_file.write(f"{im1} {im2}\n")
    for i in range(len(matches)):
        if matches[i] != -1:
            matches_file.write(f"{i} {matches[i]}\n")
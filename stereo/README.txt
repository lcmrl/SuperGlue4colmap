To obtain SuperPoint keypoints and matches in the COLMAP format:

- From https://github.com/magicleap/SuperGluePretrainedNetwork you can get the SuperGlue matches saved in the .npz format
- Put the npz file in the ./desc directory
- Modify the path to input/output directory in the superglue2colmap.py script
- run python superglue2colmap.py

Now keypoints in the COLMAP format are present in the colmap_desc directory.
The matches from COLMAP are in superglue_matches.txt file.

To import them in COLMAP, open the gui, then:
- File > New project, here you can create a new empty database and select the image folder
- Processing > Feature extraction, go to the Import window, select the path to colmap_desc directory and click on Extract
- Processing > Feature matching, go to the Custom window, select type "Inlier feature matches", then with "Select file" select the superglue_matches.txt file, click to "Run"

If you need to change the interior parameters:
-  Processing > Database management
- Select the Cameras window
- Click on the camera you want to modify, you can set a different camera model, while with double click on params you can manually change the interiors

Finaly: Reconstruction > Start Reconstruction

To see the sparse reconstruction: Render > Render options, change Point min. track lenght equal to 2, then Apply
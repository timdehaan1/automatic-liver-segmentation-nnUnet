print("test")

import os
import nibabel as nib
import numpy as np

input_dir = '/home/rnga/tsdehaan/my-scratch/Data_nnUNet/nnUnet_raw/Dataset001_AAA/imagesU,Ts,4D/'
output_dir = '/home/rnga/tsdehaan/my-scratch/Data_nnUNet/nnUnet_raw/Dataset001_AAA/imagesU,Ts/'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
for filename in os.listdir(input_dir):
    if filename.endswith('.nii') or filename.endswith('.nii.gz'):
        nifti_path = os.path.join(input_dir, filename)
        
        nifti_img = nib.load(nifti_path)
        
        nifti_data = nifti_img.get_fdata()
        print(f"Processing {filename}: original shape {nifti_data.shape}")
        
        if len(nifti_data.shape) == 4:
            
            mean_nifty = np.mean(nifti_data, axis=3)
            
            mean_nifty = nib.Nifti1Image(mean_nifty, nifti_img.affine)
                
            if filename.endswith('.nii.gz'):
                output_filename = filename.replace('.nii.gz', '.nii.gz')
                    
            output_path = os.path.join(output_dir, output_filename)
                
            nib.save(mean_nifty, output_path)
            print(f"3D version saved: {output_path}")
                    
        else:
            print(f"File {filename} is not a 4D file, skipping")
            
            
            
                    
                        
            
            
        
        




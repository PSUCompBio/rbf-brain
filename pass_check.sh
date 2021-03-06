#!/bin/bash

# Add file and the target file size below
repo=rbf-brain-vtk
file=coarse_brain_morphed.vtk
target_file_size=1537589

# Add file 2 and the target file size below
repo2=rbf-brain-inp-creation
file2=coarse_mesh_morphed-v2.inp
target_file_size2=1761823

# Add file 3 and the target file size below
repo3=rbf-vtk-to-vtu-conversion
file3=converted_vtk.vtu
target_file_size3=1977419

# You shoud not have to modify below
#
myfilesize=$(wc -c <"$file")
echo Acutal File Size = "$myfilesize"
echo Target File Size = "$target_file_size"

myfilesize2=$(wc -c <"$file2")
echo Acutal File2 Size = "$myfilesize2"
echo Target File2 Size = "$target_file_size2"

myfilesize3=$(wc -c <"$file3")
echo Acutal File3 Size = "$myfilesize3"
echo Target File3 Size = "$target_file_size3"

if [ $myfilesize -ge $target_file_size ];then
        echo Passed!
        echo "Passed" >> ~/$repo.PASSED
        echo "Acutal File Size = "$myfilesize" " >> ~/$repo.PASSED
        echo "Target File Size = "$target_file_size" " >> ~/$repo.PASSED
else
        echo Failed!
        echo "Failed!" >> ~/$repo.FAILED
        echo "Acutal File Size = "$myfilesize" " >> ~/$repo.FAILED
        echo "Target File Size = "$target_file_size" " >> ~/$repo.FAILED
fi

if [ $myfilesize2 -ge $target_file_size2 ];then
        echo Passed!
        echo "Passed" >> ~/$repo2.PASSED
        echo "Acutal File2 Size = "$myfilesize2" " >> ~/$repo2.PASSED
        echo "Target File2 Size = "$target_file_size2" " >> ~/$repo2.PASSED
else
        echo Failed!
        echo "Failed!" >> ~/$repo2.FAILED
        echo "Acutal File2 Size = "$myfilesize2" " >> ~/$repo2.FAILED
        echo "Target File2 Size = "$target_file_size2" " >> ~/$repo2.FAILED

fi

if [ $myfilesize3 -ge $target_file_size3 ];then
        echo Passed!
        echo "Passed" >> ~/$repo3.PASSED
        echo "Acutal File2 Size = "$myfilesize3" " >> ~/$repo3.PASSED
        echo "Target File2 Size = "$target_file_size3" " >> ~/$repo3.PASSED
else
        echo Failed!
        echo "Failed!" >> ~/$repo3.FAILED
        echo "Acutal File3 Size = "$myfilesize3" " >> ~/$repo3.FAILED
        echo "Target File3 Size = "$target_file_size3" " >> ~/$repo3.FAILED

fi

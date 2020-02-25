#!/bin/bash

# Add file and the target file size below
repo=rbf-brain

# file 1
file1=model.stl
target_file_size1=2090800

# file 2
file2=parameters.prm
target_file_size2=1780

# file 3
file3=coarse_mesh_morphed.vtk
target_file_size3=1403053

# file 4
file4=coarse_mesh_morphed.inp
target_file_size4=1691542

# file 5
file5=centroidtable_coarse.txt
target_file_size5=964983  

# You shoud not have to modify below
#
 myfilesize1=$(wc -c <"$file1")
 echo Acutal File1 Size = "$myfilesize1"
 echo Target File1 Size = "$target_file_size1"
 
 myfilesize2=$(wc -c <"$file2")
 echo Acutal File2 Size = "$myfilesize2"
 echo Target File2 Size = "$target_file_size2"
 
 myfilesize3=$(wc -c <"$file3")
 echo Acutal File3 Size = "$myfilesize3"
 echo Target File3 Size = "$target_file_size3"
 
 myfilesize4=$(wc -c <"$file4")
 echo Acutal File4 Size = "$myfilesize4"
 echo Target File4 Size = "$target_file_size4"
 
 myfilesize5=$(wc -c <"$file5")
 echo Acutal File5 Size = "$myfilesize5"
 echo Target File5 Size = "$target_file_size5"
 
 declare -i myint=0
 # check file 1
 if [ $myfilesize1 -ge $target_file_size1 ];then
         declare -i myint=1
 else
         declare -i myint=0
 fi
 
 # check file 2
 if [ $myfilesize2 -ge $target_file_size2 ];then
         declare -i myint=1
 else
         declare -i myint=0
 fi
 
 # check file 3
 if [ $myfilesize3 -ge $target_file_size3 ];then
         declare -i myint=1
 else
         declare -i myint=0
 fi
 
  # check file 4
 if [ $myfilesize4 -ge $target_file_size4 ];then
         declare -i myint=1
 else
         declare -i myint=0
 fi
 
   # check file 5
 if [ $myfilesize5 -ge $target_file_size5 ];then
         declare -i myint=1
 else
         declare -i myint=0
 fi
 
 if [ $myint -ge 1 ];then
         echo Passed!
         echo "Passed" >> ~/$repo.PASSED
 else
        echo Failed!
         echo "Failed!" >> ~/$repo.FAILED
         echo "Acutal File1 Size = "$myfilesize1" " >> ~/$repo.FAILED
         echo "Target File1 Size = "$target_file_size1" " >> ~/$repo.FAILED
         echo "Acutal File2 Size = "$myfilesize2" " >> ~/$repo.FAILED
         echo "Target File2 Size = "$target_file_size2" " >> ~/$repo.FAILED
         echo "Acutal File3 Size = "$myfilesize3" " >> ~/$repo.FAILED
         echo "Target File3 Size = "$target_file_size3" " >> ~/$repo.FAILED
         echo "Acutal File4 Size = "$myfilesize4" " >> ~/$repo.FAILED
         echo "Target File4 Size = "$target_file_size4" " >> ~/$repo.FAILED
         echo "Acutal File5 Size = "$myfilesize5" " >> ~/$repo.FAILED
         echo "Target File5 Size = "$target_file_size5" " >> ~/$repo.FAILED
 fi

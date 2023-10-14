#!/bin/bash

# Define the target directory where you'll be copying the files to (Hugging Face dataset repository)
target_dir="./huggingface-dataset"

# Initialize an array of file names you want to upload
declare -a files=("releases-data.csv" "processing-commits-flat.csv" "one-forum-data.csv" "libraries-data.csv" "forum-data.csv" "alpha-forum-data.csv" "beta-forum-data.csv" "one-forum-data.csv")

# Loop over the files
for file in "${files[@]}"
do
  # Check if the file exists
  if [[ -f "./$file" ]]; then
    # Get the file size in bytes
    file_size=$(stat -f "%z" "./$file")
    
    # If the file size is greater than 10MB (10 * 1024 * 1024 bytes)
    if [[ $file_size -gt 10485760 ]]; then
      # Zip the large file
      zip "./$file.zip" "./$file"
      
      # Copy the zipped file to the target directory
      cp "./$file.zip" "$target_dir"
      
      # Remove the zipped file from the parent directory
      rm "./$file.zip"
      
      # Change to the child directory and track the zipped file with Git LFS
      cd "$target_dir"
      git lfs track "$file.zip"
      cd -
    else
      # Copy the original file to the target directory
      cp "./$file" "$target_dir"

      # Change to the child directory and track the smaller csv file with Git LFS
      cd "$target_dir"
      git lfs track "$file"
      cd -
    fi
  else
    echo "$file does not exist in this directory."
  fi
done

# Change to the child directory, add .gitattributes and the files to git
cd "$target_dir"
git add .gitattributes
git add .

# Commit the changes in the child repository
git commit -m "Upload data files"
git push

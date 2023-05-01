#!/bin/bash

output_file="$1"
shift
temp_file="temp_concatenated.md"

# Concatenate all input files
echo "" > $temp_file
for file in "$@"
do
    # Get the file's directory
    file_dir=$(dirname "$file")

    # Modify relative links to be relative to the output file
    modified_file=$(mktemp)
    if [ "$file_dir" != "." ]; then
        sed -E "s~(\]\()(\./)?([^/])~\1$file_dir/\3~g" "$file" > "$modified_file"
    else
        cp "$file" "$modified_file"
    fi

    # Add modified file content to the temporary concatenated file
    echo -e "\n<!-- File: $file -->\n" >> $temp_file
    cat "$modified_file" >> $temp_file

    # Remove the modified temporary file
    rm "$modified_file"
done

# Resolve relative links and create the output file
pandoc --standalone --self-contained -t gfm -o "$output_file" "$temp_file"

# Clean up the temporary file
rm $temp_file
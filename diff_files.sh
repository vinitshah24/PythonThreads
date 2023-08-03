#!/bin/bash

# Function to preprocess the Scala files and remove comments and docstrings
preprocess_scala_file() {
    local content
    content=$(cat "$1")

    # Remove block comments (/** ... */)
    content=$(echo "$content" | sed 's:/\*.*\*/::g')

    # Remove line comments (// ...)
    content=$(echo "$content" | sed 's://.*$::g')

    # Remove docstrings (/** ... */)
    content=$(echo "$content" | sed 's:/\*\*.*\*/::g')

    echo "$content"
}

# Function to compare two preprocessed files
compare_files() {
    diff -u <(preprocess_scala_file "$1") <(preprocess_scala_file "$2")
}

# Directory paths
dir1="path_to_directory1"
dir2="path_to_directory2"

# Find corresponding files with the same name in both directories
common_files=$(comm -12 <(cd "$dir1" && ls *.scala | sort) <(cd "$dir2" && ls *.scala | sort))

# Loop through the common files and compare them
for file in $common_files; do
    file1="$dir1/$file"
    file2="$dir2/$file"

    if cmp -s "$file1" "$file2"; then
        echo "$file1 and $file2 are identical."
    else
        echo "Differences between $file1 and $file2:"
        compare_files "$file1" "$file2"
    fi
done

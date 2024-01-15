#!/bin/bash

# Directory where log.csv will be created
log_directory="data"

# Check if the log.csv file already exists in the specified directory
if [ -f "$log_directory/log.csv" ]; then
    read -p "The log.csv file already exists in the '$log_directory' directory. Do you want to (1) destroy and rebuild it, or (2) add to it? Enter 1 or 2: " choice
    case $choice in
    1)
        # Destroy and rebuild the file with UTF-8 encoding
        echo -e "\xEF\xBB\xBF\"Commit Hash\",\"Author Name\",\"Author Email\",\"Author Date\",\"Commit Message\"" >"$log_directory/log.csv"
        echo "The existing log.csv file has been destroyed and rebuilt with UTF-8 encoding."
        ;;
    2)
        # Append to the existing file
        ;;
    *)
        echo "Invalid choice. The existing file will be preserved, and Git log data will not be added."
        exit 1
        ;;
    esac
else
    # Create the header row with UTF-8 encoding in the specified directory
    mkdir -p "$log_directory" # Create the directory if it doesn't exist
    echo -e "\xEF\xBB\xBF\"Commit Hash\",\"Author Name\",\"Author Email\",\"Author Date\",\"Commit Message\"" >"$log_directory/log.csv"
    echo "A new log.csv file with UTF-8 encoding has been created in the '$log_directory' directory."
fi

# Append Git log data to log.csv
git log --date=short --pretty=format:'"%h","%an","%ae","%ad","%s"' >>"$log_directory/log.csv"

echo "Git log data has been written to $log_directory/log.csv"

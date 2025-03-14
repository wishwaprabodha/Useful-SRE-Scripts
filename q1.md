#  Log File Ro­ta­tion Au­tomation

This script provides a simple utility to manage files in a specified directory. It performs two main tasks:

1. **Archive Large Files:**
   Files larger than 100 MB that are not already in ZIP format are compressed into a ZIP archive.
2. **Clean Up Old Archives:**
   ZIP archives that were created over 30 days ago are automatically deleted.

## Features

- **Automatic Archiving:**
  Detects files larger than 100 MB and compresses them.
- **Scheduled Cleanup:**
  Removes ZIP files that are older than 30 days.
- **Easy to Customize:**
  Adjust the target directory, file size limit, or age threshold as needed.

## Prerequisites

- **Python Version:**
  Python 3.x is required.
- **Dependencies:**
  The script uses standard Python libraries:
  - `os`
  - `zipfile`
  - `datetime`

No additional packages are required.

## Usage

1. **Clone or Download the Repository:**

   ```sh
   git clone https://github.com/wishaprabodha/assignment_sre.git
   cd assignment

#
# File containing code to write logs to file
#
#

# Dependencies
import os

# Function to write logs to file
def writeLogs(path, filename, data):
    """Open file at given path and write data into it.

    Keyword arguments:
    path -- string
    filename -- string
    data -- string
    """
    # Check if given path exists
    if not os.path.exists(path):
        # Create directory for given path
        os.makedirs(path)

    # Open file
    file = open(os.path.join(path, filename), "a")
    # Write data to file
    file.write(data)
    # Close file
    file.close()

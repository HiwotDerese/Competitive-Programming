"""
Input:
A list of files in the file system (e.g., files = [{'name': 'file1', 'size': 100, 'extension': '.txt'}, ...]).
Query parameters: name, size, and extension (can be optional or a combination).
Output:
A list of files that match the given parameters.

"""


def filter_files(files, name=None, size=None, extension=None):
    """
    Filters files based on given parameters: name, size, and extension.

    :param files: List of file dictionaries with 'name', 'size', and 'extension'.
    :param name: (Optional) Name of the file to filter by.
    :param size: (Optional) Size of the file to filter by.
    :param extension: (Optional) Extension of the file to filter by.
    :return: List of filtered files.
    """
    # Filter using a list comprehension
    # filtered_files = [
    #     file
    #     for file in files
    #     if (name is None or file["name"] == name)
    #     and (size is None or file["size"] == size)
    #     and (extension is None or file["extension"] == extension)
    # ]

    filtered_files = []

    for file in files:
        print('name, size and extension', name, size, extension)
        if (
            (name is None or file["name"] == name)
            and (size is None or file["size"] == size)
            and (extension is None or file["extension"] == extension)
        ):
            filtered_files.append(file)

    return filtered_files


# Example usage
files = [
    {"name": "file1", "size": 100, "extension": ".txt"},
    {"name": "file2", "size": 200, "extension": ".jpg"},
    {"name": "file3", "size": 100, "extension": ".txt"},
    {"name": "file4", "size": 300, "extension": ".png"},
]

# Query files
result = filter_files(files, size=100, extension=".pdf")
print("Filtered files:", result)

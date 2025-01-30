'''
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.

List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.

void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. 
If the middle directories in the path do not exist, you should create them as well.

void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.

String readContentFromFile(String filePath) Returns the content in the file at filePath.


FileSystem = tree
a/b/c

TreeeNode()
ls = 

Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

'''

# class TreeNode():
#     def __init__(self, value):
#         self.root = value
#         self.children = []
    

# class FileSystem():
#     def __init__(self):
#         TreeNode()


#     def ls(self, path):

    

#     def mkdir(self, path):


#     def addContentToFile(self, filePath, content):



#     def readContentFromFile(self, filePath):










































































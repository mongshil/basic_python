import os


# def search(dirname):
#     try:
#         filenames=os.listdir(dirname)
#         for filename in filenames:
#             full_filename=os.path.join(dirname,filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext=os.path.splitext(full_filename)[-1]
#                 if ext=='.py':
#                     print(full_filename)
#     except Exception:
#         pass

# search("C:\coding")

for (path, dir, files) in os.walk("C:/"):
    for filename in files:
        ext=os.path.splitext(filename)[-1]
        if ext==".py":
            print("%s/%s" %(path,filename))
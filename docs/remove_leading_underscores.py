import os, shutil

curr_vers_dir = 'latest'

dirs = {'_static' : 'static', '_modules' : 'modules',
        '_images' : 'images', '_sources' : 'sources' , '_downloads' : 'downloads'}

for dirpath, subdirs, files in os.walk(curr_vers_dir):
    for d in subdirs:
        if d in dirs.keys():
            shutil.move(os.path.join(dirpath,d),os.path.join(dirpath,dirs[d]))
            
    for f in files:
        if f.lower().endswith('.html'):
            # Read in the file
            with open(os.path.join(dirpath,f), 'r', encoding='utf-8', errors='ignore') as fl:
                filedata = fl.read()

                # Replace the target string
                filedata = filedata.replace(u'_static', u'static')
                filedata = filedata.replace(u'_modules', u'modules')
                filedata = filedata.replace(u'_images', u'images')
                filedata = filedata.replace(u'_sources', u'sources')
                filedata = filedata.replace(u'_downloads', u'downloads')

                # Write the file out again
                with open(os.path.join(dirpath,f), 'w', encoding='utf-8') as fl:
                    fl.write(filedata)

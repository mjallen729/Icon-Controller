import os
import config

settings = config.load()

desktop = os.path.expanduser('~/Desktop')
desktop2 = os.path.join('C:\\Users\\Public\\Desktop')

def is_shortcut(file):
    name, ext = os.path.splitext(file)
    if ext == '.lnk':
        return True
    
    return False

def get_correct_path(file):
    path = os.path.join(desktop, file)
    if os.path.exists(path):
        return path
    
    path = os.path.join(desktop2, file)
    if os.path.exists(path):
        return path

files = os.listdir(desktop)
files += os.listdir(desktop2)

icons_removed = 0
for file in files:
    if settings['shortcut_mandatory'] and not is_shortcut(file):
        continue
    
    file_name, ext = os.path.splitext(file)
    if (file_name in settings['name_blacklist']) or (ext[1:] in settings['extension_blacklist']):
        print(f'{get_correct_path(file)}')
        os.remove(get_correct_path(file))
        icons_removed += 1

print('==============================')
print(f'{icons_removed} icons removed')
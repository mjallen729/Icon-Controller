# Some programs will automatically place a desktop shortcut when they update
# This will delete those annoying icons that keep reappearing
# Compatible with Windows 8 or above

# Type the exact name of the icon (do not include file extensions)
name_blacklist = {
    'Roblox Player',
    'Roblox Studio',
    'iCUE',
    'Bruno'

}

# Do not remove files with these extensions (do not include the .)
extension_blacklist = {
    'pdf',

}

# Only delete the icon if it's a shortcut
shortcut_mandatory = True


def load():
    return {
        'name_blacklist': name_blacklist,
        'extension_blacklist': extension_blacklist,
        'shortcut_mandatory': shortcut_mandatory

    }
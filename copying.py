import shutil, os, time
import keyboard  # using module keyboard
import copy_destination
import drive_name


source_drive = r"E:"
source_path = source_drive + "\\"


def check_for_flash(check_drive):
    USB_name, usb_drive = copy_destination.check_drive(check_drive)
    if USB_name == "COPIED PICS":
        global target
        target = usb_drive + "\\"
        return True
    else:
        return False

## DRIVE SETUP


dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def copy_new_drive():
    folder_name = drive_name.DVD_Name()
    i = 0
    count = ""
    if folder_name == "KODAKCD":
        kodak = True
    else:
        kodak = False
    while(1):
        print(target + folder_name + count)
        if os.path.exists(target + folder_name + count):
            i+= 1   
            count = str(i)
        else:

            dest = str(target + folder_name + count)
            break
    print(folder_name)
    if kodak:
        KODAK_Path = source_path + "PICTURES"
        print(KODAK_Path)
        shutil.copytree(KODAK_Path, dest)
    else:
        shutil.copytree(source_path, dest)
    print("Copy successful")





def print_change(change, result):
    print(change + str(result))

def difference(old, new):
    result = []
    for drive in new:
        if drive not in old:
            result.append(drive)
            change = "New Drive"
            print_change(change, result)
            copy_new_drive()
            old = new
    if not result:
        for drive in old:
            if drive not in new:
                result.append(drive)
                change = "Removed Drive"
                print_change(change,result)
                old = new
    return old

def set_target():
    check_drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    for Drives in check_drives:
        if check_for_flash(Drives):
            return True
    return False

def copy_loop(drives):
    while True:  # making a loop
        check = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        drives = difference(drives, check)
        time.sleep(.5)
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('All done')
            time.sleep(3)
            break  # finishing the loop

drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
if set_target():
    print("Found it")
    copy_loop(drives)
else:
    print("Flash Drive Named COPY PICS not detected")
    
import pathlib
import os
import shutil
import datetime
from time import sleep

root_path = pathlib.Path(__file__).parent.resolve()

backup_options = {
    "paths": {
        "backup": None,
        "saves": None,
        "maps": None,
        "playerdata": None
    }
}

root_options = {
    "paths": {
        "saves": None,
        "maps": None,
        "playerdata": None
    }
}

def check_for_folder(dir):
    print(f"Checking if '{dir}' folder exists...")
    try:
        new_path = backup_options["paths"][dir]
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            print(f"Created: '{new_path}'")
        else:
            print(f"Path already exists: {new_path}")
    except Exception as e:
        print(f"\n[ERROR] Option `dir` name: '{dir}' is invalid. Must be: {backup_options.keys()} ")

def create_timestamp_folder(dir):
    dt = str(datetime.datetime.now())
    formatted_dt = dt.replace("-", "_").replace(":", "_").replace(" ", "_").replace(".", "_")
    new_path = os.path.join(backup_options["paths"][dir], formatted_dt)
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    return new_path

def backup_folder(dir):
    new_path = create_timestamp_folder(dir)
    shutil.copytree(root_options["paths"][dir], new_path, dirs_exist_ok=True)

def get_path_to_dir(dirs, dir, new_path):
    return os.path.join(backup_options["paths"][dir], new_path)

def clean_backups(dir):
    max_num_of_backups = 4
    dirs = next(os.walk(backup_options["paths"][dir]))[1]
    sorted_dirs = []
    for d in dirs:
        sorted_dirs.append(str(d))

    sorted_dirs.sort()
    
    if (len(dirs) > max_num_of_backups):
        diff = len(dirs) - max_num_of_backups
        print(f"Found diff of {diff} folders")
        for i in range(diff):
            print(f"Deleting {sorted_dirs[i]} in {dir} to free space...")
            path_to_backup = get_path_to_dir(sorted_dirs, dir, sorted_dirs[i])
            shutil.rmtree(path_to_backup)            
    
def init():
    backup_options["paths"]["backup"] = os.path.join(root_path, "Backups")
    backup_options["paths"]["saves"] = os.path.join(backup_options["paths"]["backup"], "Saves")
    backup_options["paths"]["maps"] = os.path.join(backup_options["paths"]["backup"], "Maps")
    backup_options["paths"]["playerdata"] = os.path.join(backup_options["paths"]["backup"], "Playerdata")

    root_options["paths"]["saves"] = os.path.join(root_path, "Saves")
    root_options["paths"]["maps"] = os.path.join(root_path, "Maps")
    root_options["paths"]["playerdata"] = os.path.join(root_path, "Playerdata")

    print(f"Identified paths in {root_path}")

    check_for_folder("backup")
    check_for_folder("saves")
    check_for_folder("maps")
    check_for_folder("playerdata")

def backup():
    time_to_save = 3600 # 1 hour
    while (True):
        print("Backing up data...")
        clean_backups("saves")
        clean_backups("maps")
        clean_backups("playerdata")
        
        backup_folder("saves")
        backup_folder("maps")
        backup_folder("playerdata")
        print(f"Done... waiting until {'{:%H:%M:%S}'.format(datetime.datetime.now() + datetime.timedelta(hours=1))} to do another backup\n")
        sleep(time_to_save)

def main():
    print("\n********** Initializing VS Auto Backup **********\n")

    init()

    print("\n********** Finished Init **********\n")
    print("Will back up every 1 hour")

    backup()

if __name__ == '__main__':
    main()
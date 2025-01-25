# An Auto-Backup Utilize for [Vintage Story](https://www.vintagestory.at/)

## How to use

To use, simply copy-paste the `main.py` file into your local VintageStoryData folder and run it using [Python3](https://www.python.org/). This should run in the background while you play your game. If you are not familiar with how to run Python programs, or are hesitant in running a terminal or command prompt, now's the time to learn! Otherwise, use the available `start_backup.sh` and `start_backup.bat` files for your respective system *(Windows users should use the .bat file. Linux users hopefully have enough knowledge to use both Python3 and an .sh file)*

## How it works

This auto-backup utility will create a `Backups` directory in your VintageStoryData folder. Within `Backups`, 3 other directories will be created: `Maps`, `Playerdata`, and `Saves`. Within these folders are time-stamped directories containing the backed up information. An example path would be: `VintageStoryData/Backups/Saves/2025_01_25_12_50_33_814507`. 

To use these backups, simply take these files and copy-paste them back into their main, respective folders. For example, copy the following file `VintageStoryData/Backups/Saves/2025_01_25_12_50_33_814507/myworld.vcdbs` to `VintageStoryData/Saves`. (I may implement an in-code way to do this in the future).

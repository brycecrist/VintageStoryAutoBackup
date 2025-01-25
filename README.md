# An Auto-Backup Utility for [Vintage Story](https://www.vintagestory.at/)
(Tested on both Windows and Linux, requires **[Python 3.xx](https://www.python.org/)**)

## How to use

First download this repository as a zip folder (or clone it if you know how). Then, simply copy-paste the contents of the extracted folder into your local `VintageStoryData` folder. 

To start the utility, run the `main.py` file using [Python3](https://www.python.org/). This utility should run in the background while you play your game. If you are not familiar with how to run Python programs, or are hesitant when it comes to using a terminal or command prompt, feel free to use the available `start_backup.sh` and `start_backup.bat` files for your respective system.

*(Windows users should be able to simply click on the .bat file. Linux users hopefully have enough knowledge to use both Python3 and an .sh file)*

## How it works

This auto-backup utility will create a `Backups` directory in your VintageStoryData folder. Within `Backups`, 3 other directories will be created: `Maps`, `Playerdata`, and `Saves`. Within these folders are time-stamped directories containing the backed up information. An example path would be: `VintageStoryData/Backups/Saves/2025_01_25_12_50_33_814507`. 

To use these backups, simply take these files and copy-paste them back into their main, respective folders. For example, copy the following file `VintageStoryData/Backups/Saves/2025_01_25_12_50_33_814507/myworld.vcdbs` into `VintageStoryData/Saves`. (I may implement an in-code way to do this in the future).

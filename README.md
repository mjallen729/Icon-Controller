# Icon Controller
Some programs will automatically place a desktop shortcut or icon when they update. This script is designed to delete those annoying icons that keep reappearing or to help clean up your desktop.

Compatible with Windows 8 or above.

## Prerequisites
Make sure you have Python 3 installed. Preferably the latest version.

Run the command 'python --version' in cmd to make sure you have it installed and linked to the 'python' command.

## Installation
### Getting the script
1) Download the repo as a zip filed. Extract the folder inside the archive to your desktop or wherever you wish to store it.

### Scheduling automatic execution
#### Creating a new task
1) Open task scheduler. Select Task Scheduler Library on the sidebar.
2) Right click -> create new task.
3) Set the task name and description to whatever you'd like (make it verbose so you can easily find it in the future if needed).

#### Adding triggers
1) Click the triggers tab. Click on new.
2) From the begin the task dropdown, select "on workstation unlock".
3) Ensure that any user is selected and the box at the bottom that says enabled is checked. Click ok.
4) Repeat steps 1-3 for the "at log on" option in the dropdown.
5) You can add any other triggers you'd like, I recommend looking through the dropdown.

#### Setting an action
1) Select the actions tab. Click on new.
2) From the action dropdown, select "start a program".
3) Click browse and navigate to wherever you extracted the repo.
4) Select the run.bat file. This is the executable that runs the python script.

#### Finishing up
1) Select the conditions tab. Look at the section that says "Power". If you are using a laptop, you may wish to uncheck the box that says "Stop if the computer switches to battery power".
2) If you wish to look through the other tabs, do so, but only make changes if you know what you're doing.
3) Click ok to add the new task to task scheduler. Icon Controller will now run whenever you login or unlock your computer.

### Configuration
Open the config.py file to configure the script before it runs. Follow the guides written in the file to adjust each setting to your liking.

## Running
Once you are done setting up you can run a manual test by opening the run.bat file. The command will log each icon deleted and how many in total.

If you wish to pause the automatic close countdown, click anywhere inside the command window. Click esc once ready to resume the countdown, or you can close the window yourself.

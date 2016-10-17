# ClipMenuPython
This is a port of [ClipMenu](https://github.com/flarn2006/ClipMenu) to Python. Instead of running in the system tray, it runs on demand, immediately displaying a dialog. The idea is that you put a shortcut for it in your taskbar yourself, or bind it to a hotkey.

## Instructions
1. Create a file called `clipmenu.txt` containing the list of items that can be copied, one per line. Put it in `~/.config`. You can put it somewhere else or give it a different name if you specify the path on the command line.

2. Save `clipmenu.py` somewhere.

3. *(Optional)* Edit `clipmenu.py` and change the `bottom-padding` to the distance you want between the bottom of the window and the bottom of the screen. Generally this would be the height of your taskbar, but you can specify whatever you want of course.

4. Use your favorite method (shortcut, hotkey, etc.) to create a convenient method of invoking the Python script.

5. *(Optional, KDE only)* To make the window always appear on top, go to System Settings->Window Management->Window Rules and import `always-on-top.kwinrule`.

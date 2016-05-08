"""
Toolkit setup

This file is run on importing anything within this directory.
Its purpose is only to help with the Gamera GUI shell,
and may be omitted if you are not concerned with that.
"""

from gamera import toolkit
import wx
from gamera.toolkits.skeleton import main

# Let's import all our plugins here so that when this toolkit
# is imported using the "Toolkit" menu in the Gamera GUI
# everything works.

from gamera.toolkits.skeleton.plugins import clear

# You can inherit from toolkit.CustomMenu to create a menu
# for your toolkit.  Create a list of menu option in the
# member _items, and a series of callback functions that
# correspond to them.  The name of the callback function
# should be the same as the menu item, prefixed by '_On'
# and with all spaces converted to underscores.
class SkeletonMenu(toolkit.CustomMenu):
    _items = ["Skeleton Toolkit",
              "Skeleton Toolkit 2"]
    def _OnSkeleton_Toolkit(self, event):
        wx.MessageDialog(None, "You clicked on Skeleton Toolkit!").ShowModal()
        main.main()
    def _OnSkeleton_Toolkit_2(self, event):
        wx.MessageDialog(None, "You clicked on Skeleton Toolkit 2!").ShowModal()
        main.main()
skeleton_menu = SkeletonMenu()

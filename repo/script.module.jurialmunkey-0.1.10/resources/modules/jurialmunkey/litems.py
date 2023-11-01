# -*- coding: utf-8 -*-
# Module: default
# Author: jurialmunkey
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

class Container():
    def __init__(self, handle, paramstring, **params):
        self.handle = handle
        self.paramstring = paramstring
        self.params = params

    @staticmethod
    def get_list_item(label='', label2='', path='', offscreen=True, is_folder=True):
        from xbmcgui import ListItem
        return {
            'url': path,
            'listitem': ListItem(label=label, label2=label2, path=path, offscreen=offscreen),
            'isFolder': is_folder
        }

    def add_items(self, items, update_listing=False, plugin_category='', container_content=''):
        import xbmcplugin
        for i in items:
            xbmcplugin.addDirectoryItem(handle=self.handle, **i)
        xbmcplugin.setPluginCategory(self.handle, plugin_category)  # Container.PluginCategory
        xbmcplugin.setContent(self.handle, container_content)  # Container.Content
        xbmcplugin.endOfDirectory(self.handle, updateListing=update_listing)
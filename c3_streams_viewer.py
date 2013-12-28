#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  c3_streams.py
#
#  Copyright 2013  <rei@reixd.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import subprocess
import threading
import wx

THREADS=dict()
VLC_BIN="/usr/bin/cvlc"
VLC_OPTIONS="--volume 50 --scale 0.5 --loop"

STREAMS_URLS = {
    "saal1hq" : "rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal1_native_hq",
    "saal1lq" : "rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal1_native_lq",
    "saal2hq" : "rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal2_native_hq",
    "saal2lq" : "rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal2_native_lq",
    "saal6hq" : "rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal6_native_hq",
    "saal6lq" : "rtmp://rtmp.streaming.media.ccc.de:1935/stream/saal6_native_lq",
    "saalghq" : "rtmp://rtmp.streaming.media.ccc.de:1935/stream/saalg_native_hq",
    "saalglq" : "rtmp://rtmp.streaming.media.ccc.de:1935/stream/saalg_native_lq",
    }

def buttonCalled(evt):
    try:
        print "ButtonCalled", evt

        print evt.GetId()
        print evt.saal
    except Exception as e:
        print e

def openVLC(url):
    p =  "%s %s '%s'" % (VLC_BIN,VLC_OPTIONS,url)
    subprocess.check_output([p],shell=True)

def startVideo(url):
    THREADS[url] = threading.Thread(target=openVLC, args=(url,))
    THREADS[url].daemon = True
    THREADS[url].start()


class C3StreamsWindow(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.button_25 = wx.Button(self, -1, _("Saal1_HQ"))
        self.button_26 = wx.Button(self, -1, _("Saal1_LQ"))
        self.button_27 = wx.Button(self, -1, _("Saal2_HQ"))
        self.button_28 = wx.Button(self, -1, _("Saal2_LQ"))
        self.button_29 = wx.Button(self, -1, _("Saal6_HQ"))
        self.button_30 = wx.Button(self, -1, _("Saal6_LQ"))
        self.button_31 = wx.Button(self, -1, _("SaalG_HQ"))
        self.button_32 = wx.Button(self, -1, _("SaalG_LQ"))
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.handleEvtButtonSaal1HQ, self.button_25)
        self.Bind(wx.EVT_BUTTON, self.handleEvtButtonSaal1LQ, self.button_26)
        self.Bind(wx.EVT_BUTTON, self.handleEvtButtonSaal2HQ, self.button_27)
        self.Bind(wx.EVT_BUTTON, self.handleEvtButtonSaal2LQ, self.button_28)
        self.Bind(wx.EVT_BUTTON, self.handleEvtButtonSaal6HQ, self.button_29)
        self.Bind(wx.EVT_BUTTON, self.handleEvtButtonSaal6LQ, self.button_30)
        self.Bind(wx.EVT_BUTTON, self.handleEvtButtonSaalGHQ, self.button_31)
        self.Bind(wx.EVT_BUTTON, self.handleEvtButtonSaalGLQ, self.button_32)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle(_("C3_Streams_Viewer"))
        self.SetSize((422, 347))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_2.Add(self.button_25, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.button_26, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.button_27, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.button_28, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.button_29, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.button_30, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.button_31, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.button_32, 0, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(self.text_ctrl_1, 0, wx.ALL|wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def handleEvtButtonSaal(self, saal):
        print "Open", saal
        url = STREAMS_URLS[saal]
        startVideo(url)

    def handleEvtButtonSaal1HQ(self, event): # wxGlade: MyFrame1.<event_handler>
        self.handleEvtButtonSaal("saal1hq")
        event.Skip()

    def handleEvtButtonSaal1LQ(self, event): # wxGlade: MyFrame1.<event_handler>
        self.handleEvtButtonSaal("saal1lq")
        event.Skip()

    def handleEvtButtonSaal2HQ(self, event): # wxGlade: MyFrame1.<event_handler>
        self.handleEvtButtonSaal("saal2hq")
        event.Skip()

    def handleEvtButtonSaal2LQ(self, event): # wxGlade: MyFrame1.<event_handler>
        self.handleEvtButtonSaal("saal2lq")
        event.Skip()

    def handleEvtButtonSaal6HQ(self, event): # wxGlade: MyFrame1.<event_handler>
        self.handleEvtButtonSaal("saal6hq")
        event.Skip()

    def handleEvtButtonSaal6LQ(self, event): # wxGlade: MyFrame1.<event_handler>
        self.handleEvtButtonSaal("saal6lq")
        event.Skip()

    def handleEvtButtonSaalGHQ(self, event): # wxGlade: MyFrame1.<event_handler>
        self.handleEvtButtonSaal("saalghq")
        event.Skip()

    def handleEvtButtonSaalGLQ(self, event): # wxGlade: MyFrame1.<event_handler>
        print "Event handler `handleEvtButtonSaalGHQ' not implemented!"
        self.handleEvtButtonSaal("saalglq")
        event.Skip()


if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    C3_Streams = C3StreamsWindow(None, -1, "")
    app.SetTopWindow(C3_Streams)
    C3_Streams.Show()
    app.MainLoop()

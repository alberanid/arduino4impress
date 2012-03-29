#!/usr/bin/env python
"""
This ugly beast reads values in the 0-99 range from a serial port and
shows a slide of an running OpenOffice/LibreOffice presentation accordingly.

Copyright: 2012, Davide Alberani <da@erlug.linux.it>
License: GPLv3
"""

import uno
import time
import serial

SP_DEV = '/dev/ttyACM0'
SP_BAUD = 9600
SLEEP_TIME = 1

# Please run OpenOffice with something like:
# soffice --impress --accept="socket,host=localhost,port=2002;urp;" impress_file.odp
UNO_URL_RESOLVER = "com.sun.star.bridge.UnoUrlResolver"
COMPONENT_CONTEXT = "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext"
DESKTOP = "com.sun.star.frame.Desktop"


def run():
    """Born to rune!"""
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext(UNO_URL_RESOLVER,
            local)
    context = resolver.resolve(COMPONENT_CONTEXT)
    desktop = context.ServiceManager.createInstanceWithContext(DESKTOP,
            context)
    document = desktop.getCurrentComponent()
    presentation = document.Presentation
    controller = presentation.getController()

    currentSlideIdx = controller.getCurrentSlideIndex()
    pages = controller.getCount()

    ser = serial.Serial(SP_DEV, SP_BAUD)

    while True:
        time.sleep(SLEEP_TIME)
        potValue = ser.readline().strip()
        try:
            potValue = int(potValue)
        except (ValueError, TypeError):
            continue
        nextSlideIdx = int(round(potValue * (pages - 1) / 99.))
        if nextSlideIdx == currentSlideIdx:
            continue
        controller.gotoSlideIndex(nextSlideIdx)
        currentSlideIdx = nextSlideIdx


if __name__ == '__main__':
    run()


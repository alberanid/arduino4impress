Arduino 4 Impress
=================

That's a very simple Arduino sketch and python script that can be used
to control an OpenOffice/LibreOffice Impress presentation using an Arduino.
Your slides will still suck, but everyone will have much more fun (of you)!

Beware that this is just a draft, and not a mature project.

Electronic
----------

A potentiometer is used to browse through the slides of an _already running_
presentation.  Five LEDs are used to show the degree of progress along
your presentation.

The circuit diagram is in the arduino4impress\_schema.fzz (you need
http://fritzing.org/ )

Software
--------

The code to be loaded on the Arduino, is in the potentiometer\_percent.ino
sketch.

The Python code to control the slideshow is in arduino4impress\_uno.py

Docs
----

The presentazione\_arduino.odp file contains a very short (Italian)
presentation.

How it works
============

 - wire your Arduino.
 - load the sketch.
 - run OpenOffice/LibreOffice with something like:
   soffice --impress --accept="socket,host=localhost,port=2002;urp;" presentazione\_arduino.odp
 - modify the python script, if needed (e.g.: to change the serial port).
 - run the python script to connect to the presentation.
 - start turning the potentiometer.
 - watch in awe.

Please refer to the code for anything else.
Beware that it will not be accurate for very long slideshows.

Author
======

Davide Alberani <da@erlug.linux.it> (C) 2012
http://www.mimante.net/


License
=======

The code is released under the terms of the GPLv3 license.
The presentation and circuit diagram are covered by a by-sa/3.0
creative commons license.


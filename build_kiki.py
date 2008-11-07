DD = "distroXX" # distro directory

import os, os.path

DD = os.path.join(os.getcwd(), DD)
files = os.listdir(DD)
files = [ os.path.join(DD, filename) for filename in files ]

from kiki import __version__ as version
release = version.split(".")[0]

shortlic = """This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA."""

mail = "project5@wanadoo.nl"
website = "http://come.to/project5"
icq = "84243714"

contact = """Contact info
web: %s
mail/msn: %s
icq: %s""" % (website, mail, icq)


for filename in files:
    try:
        thefile = file(filename, "r")
        text = thefile.read()
        thefile.close()
        replacements = [("$VERSION", version),
                        ("$RELEASE", release),
                        ("$COPYRIGHT", "Copyright (C) 2003, 2004 Project 5"),
                        ("$SHORTLICENCE", shortlic),
                        ("$WEBSITE", website),
                        ("$CONTACTINFO", contact),
                        ("$MAIL", mail),
                        ("$ICQ", icq),
                        ("DEBUGMODE = True", "DEBUGMODE = False")]
        for r in replacements:
            text = text.replace(r[0], r[1])
        thefile = file(filename, "w")
        thefile.write(text)
        thefile.close()
    except:
        pass

####from Reid - http://apple.stackexchange.com/a/4257
#!/usr/bin/python
#
# This script automagically updates a set of wrapper shell scripts in
# ~/bin/mankoffmagic which call Mac apps installed in /Applications.
#
# Inspired by mankoff's shell alias posted on apple.stackexchange.com; see:
# http://apple.stackexchange.com/questions/4240/concisely-starting-mac-os-apps-from-the-command-line/4257#4257
#
# Notes/Bugs:
#
# 1. Does not follow symlinks (aliases?)
#
# 2. Assumes that application names do not contain double-quotes.
#
# 3. Not very smart about finding the actual binary (it guesses). This is
# wrong sometimes, e.g. Firefox. Probably a deeper understanding of the app
# package structure would fix this.

import copy
import glob
import os
import os.path
import re

BINDIR = os.path.expandvars("$HOME/bin/mankoffmagic")
APP_RE = re.compile(r'(.*)\.app$')
STRIP_RE = re.compile(r'[\W_]+')

def main():
   # We aggressively delete everything already in BINDIR, to save the trouble
   # of analyzing what should stay
   for f in glob.glob("%s/*" % BINDIR):
      os.unlink(f)

   # Walk /Applications and create a wrapper shell script for each .app dir
   for (root, dirs, files) in os.walk("/Applications"):
      dirs_real = copy.copy(dirs)  # so we can manipulate dirs while looping
      for d in dirs_real:
         #print "checking %s" % os.path.join(root, d)
         m = APP_RE.search(d)
         if (m is not None):
            #print "Found " + m.group()
            dirs.remove(d)  # no need to recurse into app
            create_script(root, d, m.group(1))

def create_script(path, appdir, appname):
   # remove non-alphanumerics and downcase it
   wrapper = STRIP_RE.sub('', appname).lower()
   wrapper = os.path.join(BINDIR, wrapper)
   fp = open(wrapper, "w")
   # Twiddle the comments in the script depending on whether you want to
   # invoke the binary or use "open" -- the former lets you use any
   # command-line args, while the latter is more Mac-like (app puts itself in
   # the front, etc.)
   fp.write("""
#!/bin/sh
exec "%s/%s/Contents/MacOS/%s" "$@"
#open -a "%s" "$@"
""" % (path, appdir, appname, appname))
   fp.close()
   os.chmod(wrapper, 0700)


if (__name__ == "__main__"):
   main()

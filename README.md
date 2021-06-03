FLACCDA
-------

This is flaccda: CD ripping utilities which add wanted, and remove
unwanted, metadata to FLAC and MP3 files.

`src/` has the executable scripts. `man/` has the Unix manual.  If
using the `makefile`, set `bindir` and `mandir` for defining the
prefix, (e.g. `bindir=/usr/local/ make install`). `DESTDIR` can
also be used.

Community
=========

Join us in channel #sgos, at chat.freenode.net, for free software
discussions, including using and contributing to flaccda.

Ogg Conversion
==============

flaccda exists because of efforts to create both Ogg and MP3
lossy files. Originally, I would use Schilling's cdda2wav like this:

```
cdda2wav -D15,1,0 -Owav -t[tracknumber]+[endingtrack] -B
```

Schilling's cdda2wav also includes paranoia and CDDB capabilities.
Remove `-B` if all tracks are to be in one `.wav` file.

To convert the `.wav` file to Ogg, with metadata, run something like the
following:

```
oggenc [filename.{wav,flac}] -t "Track Name" -a "Artist" -l "Album Name" \
	-d year-mm-dd -N 10 -q 6 -o "filename.ogg"
```

Of course, the easiest way is to use flaccda and convert from FLAC
files with metadata to Ogg Vorbis, using the vorbis-tools
found at <http://www.xiph.org/downloads/>: `oggenc *.flac -q 6`

Is this worth adding as a function to flaccda?

FLACCDA
-------

This is FLACCDA: CD ripping utilities which add wanted, and remove
unwanted, metadata to FLAC and MP3 files.

src/ has the scripts which go into $HOME/bin, /usr/bin,
/usr/local/bin, or /opt/bin.  man/ has the manual which goes in
/usr/share/man/man1 (or /usr/local/share/man/man1,
/opt/share/man/man1).

If using the makefile, set bindir and mandir (or both) for defining
the prefix, (e.g. bindir=/usr/local make install). DESTDIR can also
be used.

Community
=========

Join us in channel #sgos, at chat.freenode.net, for free software
discussions, including using and contributing to flaccda.

Ogg Conversion
==============

FLACCDA exists because of efforts to create both Ogg and MP3
lossy files. Originally, I would use Schilling's cdda2wav like this:

   cdda2wav -D15,1,0 -Owav -t[tracknumber]+[endingtrack] -B

Schilling's cdda2wav also includes paranoia and CDDB capabilities.
Remove -B if all tracks are to be in one wav file.

To convert the wav file to Ogg, with metadata, I would have to run
something like the following:

   oggenc [filename.{wav,flac}] -t "Track Name" -a "Artist" -l "Album Name" \
                         -d year-mm-dd -N 10 -q 6 -o "filename.ogg"

The easiest way, of course, is to use FLACCDA and convert from FLAC
files with metadata to Ogg Vorbis, using the vorbis-tools
found at <http://www.xiph.org/downloads/>:

   oggenc *.flac -q 6

I'd add this as a function to FLACCDA, but the command is so simple that
I don't see the point.

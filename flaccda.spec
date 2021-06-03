# RPM spec file for package flaccda
#
# Copyright 2009 David Egan Evans
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted, provided that the
# above copyright notice and this permission notice appear in all
# copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA
# OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

%define _prefix /opt/%{name}
%define _bindir %{_prefix}/bin
%define _mandir %{_prefix}/man
%define packer %(finger -lp `echo "$USER"` | head -n 1 | cut -d: -f 3)

Name:		flaccda
Summary:	Make FLAC files from CDA
Version:	0.5
Release:	1
License:	ISC
Vendor:		D. E. Evans <sinuhe@gnu.org>
Packager:	%packer
Group:		Applications/Multimedia
Source:		http://deevans.net/hacking/flaccda/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root
# Is this right for Mandriva? RHEL requires EPEL; lame is 3rd party.
#Requires:	flac cdparanoia libcddb lame
Requires:	flac libcddb lame

%description
FLACCDA reads CD Audio Tracks (CDA) and converts the PCM wave data to
Free Lossless Audio Codec (FLAC), or MPEG-1 Audio Layer 3 (MP3), format
adding metadata from CDDB, and renaming the resulting files accordingly.

%prep
echo Building %{name}-%{version}-%{release}
%setup -q -n %{name}-%{version}

%install
%{make_install}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_mandir}/man1/flaccda.1
%{_bindir}/%{name}
%{_bindir}/mp3cda
%{_bindir}/stripmb
/etc/profile.d/%{name}.sh

%changelog
* Sat Feb 23 2013 - D. E. Evans <sinuhe@gnu.org>
- Release 0.5

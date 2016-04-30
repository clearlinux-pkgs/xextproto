#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xextproto
Version  : 7.3.0
Release  : 6
URL      : http://xorg.freedesktop.org/releases/individual/proto/xextproto-7.3.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xextproto-7.3.0.tar.gz
Summary  : XExt extension headers
Group    : Development/Tools
License  : MIT-Opengroup
Requires: xextproto-doc
BuildRequires : libxslt-bin
BuildRequires : xmlto

%description
X Protocol Extensions
Extension names:
DOUBLE-BUFFER
DPMS
Extended-Visual-Information
Generic Event Extension
LBX
MIT-SHM
MIT-SUNDRY-NONSTANDARD
Multi-Buffering
SECURITY
SHAPE
SYNC
TOG-CUP
XC-APPGROUP
XTEST

%package dev
Summary: dev components for the xextproto package.
Group: Development

%description dev
dev components for the xextproto package.


%package doc
Summary: doc components for the xextproto package.
Group: Documentation

%description doc
doc components for the xextproto package.


%prep
%setup -q -n xextproto-7.3.0

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/EVI.h
/usr/include/X11/extensions/EVIproto.h
/usr/include/X11/extensions/ag.h
/usr/include/X11/extensions/agproto.h
/usr/include/X11/extensions/cup.h
/usr/include/X11/extensions/cupproto.h
/usr/include/X11/extensions/dbe.h
/usr/include/X11/extensions/dbeproto.h
/usr/include/X11/extensions/dpmsconst.h
/usr/include/X11/extensions/dpmsproto.h
/usr/include/X11/extensions/ge.h
/usr/include/X11/extensions/geproto.h
/usr/include/X11/extensions/lbx.h
/usr/include/X11/extensions/lbxproto.h
/usr/include/X11/extensions/mitmiscconst.h
/usr/include/X11/extensions/mitmiscproto.h
/usr/include/X11/extensions/multibufconst.h
/usr/include/X11/extensions/multibufproto.h
/usr/include/X11/extensions/secur.h
/usr/include/X11/extensions/securproto.h
/usr/include/X11/extensions/shapeconst.h
/usr/include/X11/extensions/shapeproto.h
/usr/include/X11/extensions/shapestr.h
/usr/include/X11/extensions/shm.h
/usr/include/X11/extensions/shmproto.h
/usr/include/X11/extensions/shmstr.h
/usr/include/X11/extensions/syncconst.h
/usr/include/X11/extensions/syncproto.h
/usr/include/X11/extensions/syncstr.h
/usr/include/X11/extensions/xtestconst.h
/usr/include/X11/extensions/xtestext1const.h
/usr/include/X11/extensions/xtestext1proto.h
/usr/include/X11/extensions/xtestproto.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xextproto/*

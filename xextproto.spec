#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xextproto
Version  : 7.3.0
Release  : 10
URL      : http://xorg.freedesktop.org/releases/individual/proto/xextproto-7.3.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xextproto-7.3.0.tar.gz
Summary  : XExt extension headers
Group    : Development/Tools
License  : MIT-Opengroup
Requires: xextproto-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)
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
Provides: xextproto-devel

%description dev
dev components for the xextproto package.


%package dev32
Summary: dev32 components for the xextproto package.
Group: Default

%description dev32
dev32 components for the xextproto package.


%package doc
Summary: doc components for the xextproto package.
Group: Documentation

%description doc
doc components for the xextproto package.


%prep
%setup -q -n xextproto-7.3.0
pushd ..
cp -a xextproto-7.3.0 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
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
/usr/lib64/pkgconfig/xextproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32xextproto.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xextproto/*

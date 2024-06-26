Summary:   MIDI to WAVE converter library
Name:      libtimidity
Version:   0.2.7
Release:   1
License:   LGPL
Group:     System Environment/Libraries
Source:    %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
libTiMidity is MIDI to WAVE converter library. It based on the
TiMidity decoder from SDL_sound library. Purpose to create this
library is to avoid unnecessary dependences. SDL_sound requires
SDL and some other libraries, that not needed to process MIDI
files. In addition libTiMidity provides more suitable API to work
with MIDI songs, it enables to specify full path to the timidity
configuration file, and have function to retrieve meta data from
MIDI song.

%package devel
Summary:   The development libraries and header files for %{name}
Group:     Development/C
Requires:  %{name} = %{version}-%{release}

%description devel
These are the development libraries and header files for %{name}

%prep
%setup -q

%build
%configure
make

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf "$RPM_BUILD_ROOT"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS CHANGES COPYING README README.timidity TODO
%{_libdir}/libtimidity.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/timidity.h
%{_libdir}/libtimidity.so
%{_libdir}/libtimidity.*a
%{_libdir}/pkgconfig

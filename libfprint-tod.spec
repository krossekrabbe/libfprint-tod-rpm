Name:           libfprint-tod

Version:        1.94.2
Release:        1%{?dist}
Summary:        Fork of libfprint to expose internal Drivers API in order to create drivers as shared libraries.

License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint
ExcludeArch:    s390 s390x
Source0:        https://gitlab.freedesktop.org/3v1n0/libfprint/-/archive/v1.94.2+tod1/libfprint-v%{version}+tod1.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  gtk-doc
BuildRequires:  libgudev-devel
# For the udev.pc to install the rules
BuildRequires:  systemd
BuildRequires:  gobject-introspection-devel
# For internal CI tests; umockdev 0.13.2 has an important locking fix
BuildRequires:  python3-cairo python3-gobject cairo-devel
BuildRequires:  umockdev >= 0.13.2

%description
libfprint offers support for consumer fingerprint reader devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -S git -n libfprint-v%{version}

%build
# Include the virtual image driver for integration tests
%meson -Dx11-examples=false -Ddrivers=all
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%check
%meson_test -t 4

%files
%license COPYING
%doc NEWS TODO THANKS AUTHORS README
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_udevhwdbdir}/60-autosuspend-libfprint-2.hwdb
%{_udevrulesdir}/70-libfprint-2.rules

%files devel
%doc HACKING.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-2.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libfprint-2/

%changelog

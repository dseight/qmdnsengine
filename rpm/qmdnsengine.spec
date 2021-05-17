Name: qmdnsengine
Version: 0.2.0
Release: 1
Summary: Qt implementation of multicast DNS
License: MIT
Source: %{name}-%{version}.tar.bz2
Patch1: qmdnsengine-add-pkgconfig.patch
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(Qt5Core)
Requires: pkgconfig(Qt5Network)

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/libqmdnsengine.so.*

%files devel
%{_libdir}/libqmdnsengine.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}

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
%setup -q -n %{name}-%{version}/upstream
%patch1 -p1

%build
mkdir -p build && cd build
%cmake -DCMAKE_BUILD_TYPE=Release ..
%make_build

%install
cd build
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libqmdnsengine.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libqmdnsengine.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}

Summary:	Box2D is a 2D physics engine for games
Name:		box2d
Version:	2.4.1
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/erincatto/box2d/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	00d2c9c66da494aed947e03bff73e080
URL:		https://box2d.org/
BuildRequires:	cmake >= 3.8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Box2D is a 2D physics engine for games.

%package devel
Summary:	Header files for box2d library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for box2d library.

%prep
%setup -q

%build
%cmake -B build \
	-DBOX2D_BUILD_UNIT_TESTS:BOOL=OFF \
	-DBOX2D_BUILD_TESTBED:BOOL=OFF
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_libdir}/libbox2d.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbox2d.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbox2d.so
%{_libdir}/cmake/box2d
%{_includedir}/box2d

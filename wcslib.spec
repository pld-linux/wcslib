#
# Conditional build:
%bcond_without	apidocs		# API documentation
#
Summary:	WCSLIB - an implementation of the FITS WCS standard
Summary(pl.UTF-8):	WCSLIB - implementacja standardu FITS WCS
Name:		wcslib
Version:	5.18
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	ftp://ftp.atnf.csiro.au/pub/software/wcslib/%{name}-%{version}.tar.bz2
# Source0-md5:	67a78354be74eca4f17d3e0853d5685f
URL:		http://www.atnf.csiro.au/people/mcalabre/WCS/wcslib
BuildRequires:	cfitsio-devel
BuildRequires:	flex >= 2.5.9
BuildRequires:	gcc-fortran
BuildRequires:	pgplot-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the FITS World Coordinate System standard.

%description -l pl.UTF-8
Implementacja standardu FITS World Coordinate System.

%package devel
Summary:	Header files for WCSLIB libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek WCSLIB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cfitsio-devel

%description devel
Header files for WCSLIB libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek WCSLIB.

%package static
Summary:	Static WCSLIB libraries
Summary(pl.UTF-8):	Statyczne biblioteki WCSLIB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WCSLIB libraries.

%description static -l pl.UTF-8
Statyczne biblioteki WCSLIB.

%package apidocs
Summary:	API documentation for WCSLIB libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek WCSLIB
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for WCSLIB libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek WCSLIB.

%prep
%setup -q

%build
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# split over packages as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README THANKS
%attr(755,root,root) %{_bindir}/HPXcvt
%attr(755,root,root) %{_bindir}/fitshdr
%attr(755,root,root) %{_bindir}/wcsgrid
%attr(755,root,root) %{_bindir}/wcsware
%attr(755,root,root) %{_libdir}/libpgsbox.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpgsbox.so.5
%attr(755,root,root) %{_libdir}/libwcs.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libwcs.so.5
%{_mandir}/man1/HPXcvt.1*
%{_mandir}/man1/fitshdr.1*
%{_mandir}/man1/wcsgrid.1*
%{_mandir}/man1/wcsware.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpgsbox.so
%attr(755,root,root) %{_libdir}/libwcs.so
%{_includedir}/wcslib-%{version}
%{_includedir}/wcslib
%{_pkgconfigdir}/wcslib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpgsbox-%{version}.a
%{_libdir}/libpgsbox.a
%{_libdir}/libwcs-%{version}.a
%{_libdir}/libwcs.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc html/*
%endif

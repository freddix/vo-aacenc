Summary:	VisualOn AAC encoder library
Name:		vo-aacenc
Version:	0.1.3
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz
# Source0-md5:	b574da1d92d75fc40b0b75aa16f24ac4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library contains an encoder implementation of the Advanced Audio
Coding audio codec. The library is based on a codec implementation by
VisualOn as part of the Stagefright framework from the Google Android
project.

%package devel
Summary:	Header files for VisualOn AAC encoder library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for VisualOn AAC encoder library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvo-aacenc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NOTICE README
%attr(755,root,root) %ghost %{_libdir}/libvo-aacenc.so.?
%attr(755,root,root) %{_libdir}/libvo-aacenc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvo-aacenc.so
%{_includedir}/vo-aacenc
%{_pkgconfigdir}/vo-aacenc.pc


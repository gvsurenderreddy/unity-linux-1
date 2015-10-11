Name:       xineramaproto
Version:    1.2.1
Release:    1%{?dist}
Summary:    X.Org Xinerama extension wire protocol.
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/proto/%{name}-%{version}.tar.bz2

%description
Xinerama is an X extension that allows clients to query information
about multiple physical screens controlled by a single X server that
appear as a single screen to core X11 protocol operations.

%prep
%setup -q

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

#mv pc file to correct location
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_includedir}/X11/extensions
%{_libdir}/pkgconfig/*.pc
#%{_datadir}/licenses/%{name}/COPYING
#%{_datadir}/doc/xtrans/%{name}.xml

%changelog

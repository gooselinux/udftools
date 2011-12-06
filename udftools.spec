Summary: Linux UDF Filesystem userspace utilities
Name: udftools
Version: 1.0.0b3
Release: 12%{?dist}
License: GPLv2+
Group: Applications/Archiving
URL: http://sourceforge.net/projects/linux-udf/
Source: http://dl.sf.net/linux-udf/udftools-%{version}.tar.gz
Patch0: udftools-1.0.0b3-pktsetup-chardev.patch
Patch1: udftools-1.0.0b3-mkudffs-bigendian.patch
Patch2: udftools-1.0.0b3-wrudf-gcc4.patch
Patch3: udftools-1.0.0b3-warningfixes.patch
Patch4: udftools-1.0.0b3-fixcompile.patch
Patch5: udftools-1.0.0b3-warningfixes2.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: readline-devel, ncurses-devel

%description
Linux UDF Filesystem userspace utilities.


%prep
%setup
%patch0 -p1 -b .pktsetup-chardev
%patch1 -p1 -b .mkudffs-bigendian
%patch2 -p1 -b .wrudf-gcc4
%patch3 -p1 -b .warningfixes
%patch4 -p1 -b .fixcompile
%patch5 -p1 -b .warningfixes2


%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
./libtool --finish %{buildroot}%{_libdir}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/*
%exclude %{_libdir}/libudffs.a
%exclude %{_libdir}/libudffs.la
%{_mandir}/man?/*


%changelog
* Wed Jun 23 2010 Roman Rakus <rrakus@redhat.com> - 1.0.0b3-12
- Build with -fno-strict-aliasing CFLAG
  Resolves: #605121

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.0b3-11.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0b3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0b3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0b3-9
- Autorebuild for GCC 4.3

* Tue Aug 23 2007 Harald Hoyer <harald@redhar.com> - 1.0.0b3-8
- fixed compile issues
- added more bigendian patches
- changed license tag

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.0.0b3-7
- FC6 rebuild.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.0.0b3-6
- Add ncurses-devel build requirement, since it's not pulled in anymore.
- Add patch to fix as many trivial warnings as possible. Some stuff seems to
  still not be 64bit clean, though.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.0.0b3-5
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.0.0b3-4
- Rebuild for new gcc/glibc.
- Exclude the static library... there isn't even a header file.

* Tue May  3 2005 Matthias Saou <http://freshrpms.net/> 1.0.0b3-3
- Include patches to fix big endian issue and gcc4 compile.

* Mon Feb  7 2005 Matthias Saou <http://freshrpms.net/> 1.0.0b3-1
- Initial RPM release, based on spec file from John Treacy.
- Exclude .la file.
- Remove unneeded /sbin/ldconfig calls (only a static lib for now).


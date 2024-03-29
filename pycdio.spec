%global srcname pycdio
%global sum A Python interface to the CD Input and Control library

Name:		%{srcname}
Version:	0.20
Release:	7%{?dist}
Summary:	%{sum}

Group:		Development/Libraries
License:	GPLv3+
URL:		http://www.gnu.org/software/libcdio/
Source0:	ftp://ftp.gnu.org/pub/gnu/libcdio/%{srcname}-%{version}.tar.gz
Patch0:		%{srcname}-swig-python3.patch

BuildRequires:	python2-devel python3-devel libcdio-devel swig

%description
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%package -n python2-%{srcname}
Summary:	%{sum}
Provides:	%{srcname} = %{version}
Obsoletes:	%{srcname} < %{version}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%package -n python3-%{srcname}
Summary:	%{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%prep
%autosetup -n %{srcname}-%{version} -p 1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{srcname}
%license COPYING
%doc README.txt
%{python2_sitearch}/*

%files -n python3-%{srcname}
%license COPYING
%doc README.txt
%{python3_sitearch}/*

%changelog
* Mon Jul 31 2017 Michael Brown <mbrown@fensystems.co.uk> - 0.20-7
- Add support for Python 3
- Update spec to conform to current Python packaging guidelines

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 16 2016 Adrian Reber <adrian@lisas.de> - 0.20-4
- Rebuilt for libcdio-0.94

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov  3 2015 Adam Williamson <awilliam@redhat.com> - 0.20-1
- update to latest upstream (fixes #1269003)
- clean and modernize spec a little (note: no longer EPEL5 compatible)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 11 2014 Adrian Reber <adrian@lisas.de> - 0.19-6
- Rebuilt for libcdio-0.93

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Adrian Reber <adrian@lisas.de> - 0.19-3
- Rebuilt for libcdio-0.92

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Adrian Reber <adrian@lisas.de> - 0.19-1
- Updated to 0.19 which actually works with libcdio-0.90

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Adrian Reber <adrian@lisas.de> - 0.18-1
- Updated to 0.18 (for for libcdio-0.90 rebuild)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Adrian Reber <adrian@lisas.de> - 0.17-2
- Rebuilt for libcdio-0.83
* Fri Apr 22 2011 Jay Greguske <jgregusk@redhat.com> 0.17-1
- Fix source url
* Fri Apr 22 2011 Jay Greguske <jgregusk@redhat.com> 0.17-0
- Update to 0.17
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Fri Jan 22 2010 Adrian Reber <adrian@lisas.de> - 0.16-2
- Rebuilt for libcdio-0.82
* Wed Oct 28 2009 Jay Greguske <jgregusk@redhat.com> - 0.16-1
- Updated to version 0.16
* Mon Sep 28 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-4
- Off-by-one compensation in get_devices_* not needed anymore
* Tue Jul 28 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-3
- Added a patch to remove unnecessary shebangs
* Mon Jul 27 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-2
- Corrected the license field
* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-1
- Initial RPM release.

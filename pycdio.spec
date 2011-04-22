%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:		pycdio
Version:	0.17
Release:	1%{?dist}
Summary:	A Python interface to the CD Input and Control library

Group:		Development/Libraries
License:	GPLv3+
URL:		http://www.gnu.org/software/libcdio/
Source0:	http://pypi.python.org/packages/source/p/pycdio/pycdio-0.17.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	python-devel,python-setuptools,libcdio-devel,swig
Requires:	python

%description
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
chmod 755 %{buildroot}/%{python_sitearch}/*.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}/*
%doc README.txt

%changelog
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

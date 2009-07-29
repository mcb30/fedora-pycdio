%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:		pycdio
Version:	0.15
Release:	3%{?dist}
Summary:	A Python interface to the CD Input and Control library

Group:		Development/Libraries
License:	GPLv3+
URL:		http://www.gnu.org/software/libcdio/
Source0:	ftp://ftp.gnu.org/pub/gnu/libcdio/%{name}-%{version}.tar.gz

# Remove shebangs in the modules
# a patch was emailed and accepted on libcdio-pycdio-devel@gnu.org
Patch0:		pycdio-remove-shebangs.patch

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	python-devel,python-setuptools,libcdio-devel,swig
Requires:	python

%description
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%prep
%setup -q
%patch0

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
* Tue Jul 28 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-3
- Added a patch to remove unnecessary shebangs
* Mon Jul 27 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-2
- Corrected the license field
* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-1
- Initial RPM release.

# TODO:
# - check py3 binding:
# AttributeError: /usr/bin/python3: undefined symbol: GetMacOSStatusCommentString
#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	send2trash
Summary:	Send file to trash natively under Mac OS X, Windows and Linux
Name:		python-%{module}
Version:	1.3.0
Release:	0.1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/S/Send2Trash/Send2Trash-%{version}.tar.gz
# Source0-md5:	0fe9e60f2da76173d64ab1cdf0fd551b
URL:		http://github.com/hsoft/send2trash
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Send2Trash is a small package that sends files to the Trash (or
Recycle Bin) natively and on all platforms. On OS X, it uses native
FSMoveObjectToTrashSync Cocoa calls, on Windows, it uses native (and
ugly) SHFileOperation win32 calls. On other platforms, if PyGObject
and GIO are available, it will use this. Otherwise, it will fallback
to its own implementation of the trash specifications from
freedesktop.org.

%package -n python3-%{module}
Summary:	Send file to trash natively under Mac OS X, Windows and Linux
Group:		Libraries/Python

%description -n python3-%{module}
Send2Trash is a small package that sends files to the Trash (or
Recycle Bin) natively and on all platforms. On OS X, it uses native
FSMoveObjectToTrashSync Cocoa calls, on Windows, it uses native (and
ugly) SHFileOperation win32 calls. On other platforms, if PyGObject
and GIO are available, it will use this. Otherwise, it will fallback
to its own implementation of the trash specifications from
freedesktop.org.

%prep
%setup -q -n Send2Trash-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/send2trash
%{py_sitescriptdir}/Send2Trash-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/send2trash
%{py3_sitescriptdir}/Send2Trash-%{version}-py*.egg-info
%endif

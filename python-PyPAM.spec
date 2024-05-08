#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	PyPAM

Summary:	PAM bindings for Python
Summary(pl.UTF-8):	Wiązania pythona do obsługi PAM
Name:		python-%{module}
Version:	0.5.0
Release:	6
License:	LGPL v2.1
Group:		Development/Languages/Python
Source0:	http://www.pangalactic.org/PyPAM/%{module}-%{version}.tar.gz
# Source0-md5:	f1e7c2c56421dda28a75ace59a3c8871
Patch0:		%{name}-destructor.patch
Patch1:		%{name}-dlopen.patch
Patch2:		%{name}-nofree.patch
Patch3:		%{name}-memory-errors.patch
Patch4:		%{name}-return-value.patch
Patch5:		%{name}-python3-support.patch
URL:		http://www.pangalactic.org/PyPAM/
BuildRequires:	pam-devel >= 0.64
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	specflags	-fno-strict-aliasing

%description
PAM (Pluggable Authentication Module) bindings for Python.

%description -l pl.UTF-8
Wiązania PAM dla Pythona.

%package -n python3-%{module}
Summary:	PAM bindings for Python
Summary(pl.UTF-8):	Wiązania pythona do obsługi PAM
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
PAM (Pluggable Authentication Module) bindings for Python.

%description -n python3-%{module} -l pl.UTF-8
Wiązania PAM dla Pythona.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1 -p0

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/PAM.so
%{py_sitedir}/PyPAM-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py3_sitedir}/PAM.cpython-*.so
%{py3_sitedir}/PyPAM-%{version}-py*.egg-info
%endif

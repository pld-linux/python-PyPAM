
%define		module	PyPAM

Summary:	PAM bindings for Python
Summary(pl.UTF-8):	Wiązania pythona do obsługi PAM
Name:		python-%{module}
Version:	0.5.0
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://www.pangalactic.org/PyPAM/%{module}-%{version}.tar.gz
# Source0-md5:	f1e7c2c56421dda28a75ace59a3c8871
URL:		http://www.pangalactic.org/PyPAM/
BuildRequires:	pam-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM (Pluggable Authentication Module) bindings for Python.

%description -l pl.UTF-8
Wiązania PAM dla pythona.

%prep
%setup -q -n %{module}-%{version}
sed -i -e 's#python1.5/Python.h#python%{py_ver}/Python.h#g' PAMmodule.c

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{py_sitedir}/PAMmodule.so
%{py_sitedir}/PyPAM-%{version}-*.egg-info
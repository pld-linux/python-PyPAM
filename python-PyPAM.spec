
%define		module	PyPAM

Summary:	PAM bindings for Python
Summary(pl):	Wi±zania pythona do obs³ugi PAM
Name:		python-%{module}
Version:	0.4.2
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://www.pangalactic.org/PyPAM/%{module}-%{version}.tar.gz
# Source0-md5:	7e8c283cbd6e85e0bbff8e265a3db9e5
URL:		http://www.pangalactic.org/PyPAM/
BuildRequires:	pam-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM (Pluggable Authentication Module) bindings for Python.

%description -l pl
Wi±zania PAM dla pythona.

%prep
%setup -q -n %{module}-%{version}
sed -i -e 's#python1.5/Python.h#python%{py_ver}/Python.h#g' PAMmodule.c

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pyexecdir=%{py_sitedir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/PAMmodule.so

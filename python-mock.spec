%define	module	mock
%define name	python-%{module}
%define version 0.7.2
%define release %mkrel 1

Summary: 	A Python mocking and patching library for testing
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://www.voidspace.org.uk/python/mock/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-unittest2
BuildRequires:	python-setuptools

%description
mock is a Python module that provides a core Mock class. It removes
the need to create a host of stubs throughout your test suite. After
performing an action, you can make assertions about which methods /
attributes were used and arguments they were called with. You can also
specify return values and set needed attributes in the normal way

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README.txt html/

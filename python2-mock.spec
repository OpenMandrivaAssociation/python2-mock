%define	module	mock

Summary: 	A Python mocking and patching library for testing
Name:		python-%{module}
Version:	1.0.1
Release:	1
Source0:	http://pypi.python.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://www.voidspace.org.uk/python/mock/
BuildArch:	noarch
BuildRequires:	python2-setuptools

%description
mock is a Python module that provides a core Mock class. It removes
the need to create a host of stubs throughout your test suite. After
performing an action, you can make assertions about which methods /
attributes were used and arguments they were called with. You can also
specify return values and set needed attributes in the normal way

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE=true python2 setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc README.txt html/
%{py2_puresitedir}/mock*

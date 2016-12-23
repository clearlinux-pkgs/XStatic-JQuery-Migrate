#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-JQuery-Migrate
Version  : 1.2.1.1
Release  : 23
URL      : https://pypi.python.org/packages/source/X/XStatic-JQuery-Migrate/XStatic-JQuery-Migrate-1.2.1.1.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-JQuery-Migrate/XStatic-JQuery-Migrate-1.2.1.1.tar.gz
Summary  : JQuery-Migrate 1.2.1 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-JQuery-Migrate-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-JQuery-Migrate
--------------
JQuery-Migrate JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-JQuery-Migrate package.
Group: Default

%description python
python components for the XStatic-JQuery-Migrate package.


%prep
%setup -q -n XStatic-JQuery-Migrate-1.2.1.1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

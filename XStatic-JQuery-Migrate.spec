#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-JQuery-Migrate
Version  : 1.2.1.1
Release  : 31
URL      : http://pypi.debian.net/XStatic-JQuery-Migrate/XStatic-JQuery-Migrate-1.2.1.1.tar.gz
Source0  : http://pypi.debian.net/XStatic-JQuery-Migrate/XStatic-JQuery-Migrate-1.2.1.1.tar.gz
Summary  : JQuery-Migrate 1.2.1 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-JQuery-Migrate-python3
Requires: XStatic-JQuery-Migrate-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
--------------
        
        JQuery-Migrate JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-JQuery-Migrate package.
Group: Default
Requires: XStatic-JQuery-Migrate-python3
Provides: xstatic-jquery-migrate-python

%description python
python components for the XStatic-JQuery-Migrate package.


%package python3
Summary: python3 components for the XStatic-JQuery-Migrate package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-JQuery-Migrate package.


%prep
%setup -q -n XStatic-JQuery-Migrate-1.2.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532214576
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

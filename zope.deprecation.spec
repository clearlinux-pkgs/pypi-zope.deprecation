#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.deprecation
Version  : 4.4.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/34/da/46e92d32d545dd067b9436279d84c339e8b16de2ca393d7b892bc1e1e9fd/zope.deprecation-4.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/34/da/46e92d32d545dd067b9436279d84c339e8b16de2ca393d7b892bc1e1e9fd/zope.deprecation-4.4.0.tar.gz
Summary  : Zope Deprecation Infrastructure
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.deprecation-license = %{version}-%{release}
Requires: zope.deprecation-python = %{version}-%{release}
Requires: zope.deprecation-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
======================
``zope.deprecation``
======================
.. image:: https://img.shields.io/pypi/v/zope.deprecation.svg
:target: https://pypi.python.org/pypi/zope.deprecation/
:alt: Latest release

%package license
Summary: license components for the zope.deprecation package.
Group: Default

%description license
license components for the zope.deprecation package.


%package python
Summary: python components for the zope.deprecation package.
Group: Default
Requires: zope.deprecation-python3 = %{version}-%{release}

%description python
python components for the zope.deprecation package.


%package python3
Summary: python3 components for the zope.deprecation package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.deprecation package.


%prep
%setup -q -n zope.deprecation-4.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571005413
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.deprecation
cp %{_builddir}/zope.deprecation-4.4.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.deprecation/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.deprecation/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

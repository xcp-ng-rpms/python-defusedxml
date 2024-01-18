%global package_speccommit 4330c6dbc6e0e8939c483e151e60a74cc900e10a
%global usver 0.7.1
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
%if 0%{?xenserver} > 8
%{?!py2_build:%global __python2 :}
%{?!py2_build:%global with_python2 0}
%{?!py2_build:%global py2_install %{nil}}
%{?!py2_build:%global py2_build %{nil}}
%else
%global         with_python2 1
%endif

%if %python3_pkgversion != 34
%global         with_python3 1
%else
%global         with_python3 0
%global         __python3 :
%global         py3_build %{nil}
%global         py3_install %{nil}
%endif

%global pypi_name defusedxml
Name:           python-%{pypi_name}
Version:        0.7.1
Release:        %{?xsrel}%{?dist}
Summary:        XML bomb protection for Python stdlib modules
License:        Python
URL:            https://github.com/tiran/defusedxml
Source0: defusedxml-0.7.1.tar.gz

BuildArch:      noarch

%if 0%{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%endif

%if 0%{with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.

%package -n python2-%{pypi_name}
Summary:        XML bomb protection for Python stdlib modules
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module. This is the Python 2 build.

%if 0%{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        XML bomb protection for Python stdlib modules
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module. This is the python%{python3_pkgversion} build.

%endif

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} tests.py
%{__python3} tests.py

%if 0%{with_python2}
%files -n python2-%{pypi_name}
%doc README.txt README.html CHANGES.txt
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if 0%{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.txt README.html CHANGES.txt
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py3.*.egg-info
%endif

%changelog
* Wed Oct 18 2023 Bernhard Kaindl <bernhard.kaindl@citrix.com> - 0.7.1-1
- First imported release


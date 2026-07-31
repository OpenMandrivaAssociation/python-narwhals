%define module narwhals

Name:		python-narwhals
Version:	2.24.0
Release:	1
Summary:	Lightweight compatibility layer between dataframe libraries
License:	MIT
Group:		Development/Python
URL:		https://narwhals-dev.github.io/narwhals
Source0:	https://github.com/narwhals-dev/narwhals/archive/v%{version}/%{name}-%{version}.tar.gz
# repo - https://github.com/narwhals-dev/narwhals

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(uv-build)
BuildRequires:	python%{pyver}dist(wheel)

%description
Extremely lightweight compatibility layer between dataframe libraries

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info

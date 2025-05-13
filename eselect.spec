Name: eselect
Version: 1.0
Release: 1
Summary: Gentoo's multi-purpose configuration and management tool
License: GPLv2
URL: https://gitweb.gentoo.org/proj/eselect.git
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: bash
BuildRequires: make
BuildRequires: libtool

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
bash ./autogen.bash
%configure

%install
%make_install

%files
%{_bindir}/*
%{_datadir}/%{name}/modules/*
%{_datadir}/%{name}/libs/*
%{_mandir}/man*/*

Name:       spectacle

Summary:    RPM Spec file generator and management tool
Version:    0.32
Release:    1
Group:      Development/Tools
License:    GPLv2+
BuildArch:  noarch
URL:        https://meego.gitorious.org/meego-developer-tools/spectacle
Source0:    spectacle-%{version}.tar.gz
Source1:    autospectacle.pl
Requires:   python3-yaml
Requires:   python3-urlgrabber
Requires:   python3-cheetah
Requires:   perl
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cheetah

%description
A tool for managing and creating RPM spec files


%prep
%setup -q -n %{name}-%{version}

%build
make tmpls
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

make install-data DESTDIR=${RPM_BUILD_ROOT}
install -m 0755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}

%files
%defattr(-,root,root,-)
%doc README.md AUTHORS COPYING TODO
%doc examples/
%dir %{_datadir}/spectacle
%{_datadir}/spectacle/*
%{_bindir}/*
%{python3_sitelib}/*

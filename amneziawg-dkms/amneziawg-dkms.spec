%global debug_package %{nil}
%global commit ac946a9df100a17d342b5982d1947deef1b51952
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260403

Name:           amneziawg-dkms
Version:        1.0.%{commitdate}git%{shortcommit}
Release:        1%{?dist}
Epoch:          1
URL:            https://github.com/amnezia-vpn/amneziawg-linux-kernel-module
Summary:        AmneziaWG VPN kernel module (DKMS version)
License:        GPLv2
Group:          System Environment/Kernel
BuildArch:      noarch

Source0:        https://github.com/amnezia-vpn/amneziawg-linux-kernel-module/archive/%{commit}/amneziawg-linux-kernel-module-%{shortcommit}.tar.gz

BuildRequires:  kernel-devel
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  bc

Provides:       kmod(amneziawg.ko) = %{epoch}:%{version}-%{release}
Requires:       dkms
Requires:       kernel-devel
Requires:       make
Requires:       bc
Requires:       yum-utils
Requires:       rpm-build
Requires:       python3-devel
Requires:       git

%description
AmneziaWG is a contemporary version of the popular VPN protocol WireGuard.
It's a fork of WireGuard and offers protection against detection by Deep Packet
Inspection (DPI) systems. AmneziaWG modifies packet headers to make them
indistinguishable from regular web traffic, helping to bypass censorship in
restrictive networks.

This package provides the kernel module via DKMS.

%prep
%autosetup -p1 -n amneziawg-linux-kernel-module-%{commit}

# Fix the Makefile for CentOS7 since it ships coreutils from 2013.
sed -i 's/install .* -D -t\(.\+\) /mkdir -p \1 \&\& \0/' %{_builddir}/amneziawg-linux-kernel-module-%{commit}/src/Makefile

# Set version in dkms.conf and Makefile
sed -i "s/^PACKAGE_VERSION=.*/PACKAGE_VERSION=\"%{version}\"/" %{_builddir}/amneziawg-linux-kernel-module-%{commit}/src/dkms.conf
sed -i "s/^WIREGUARD_VERSION = .*/WIREGUARD_VERSION = %{version}/" %{_builddir}/amneziawg-linux-kernel-module-%{commit}/src/Makefile

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/amneziawg-%{version}/
make DESTDIR=%{buildroot} DKMSDIR=%{_usrsrc}/amneziawg-%{version}/ \
    -C %{_builddir}/amneziawg-linux-kernel-module-%{commit}/src dkms-install

%post
dkms add -m amneziawg -v %{version} -q --rpm_safe_upgrade || :
dkms build -m amneziawg -v %{version} -q || :
dkms install -m amneziawg -v %{version} -q --force || :
echo "amneziawg-dkms-%{version}-%{release}" > /var/lib/dkms/amneziawg/%{version}/version

%preun
dkms remove -m amneziawg -v %{version} -q --all || :

%files
%license COPYING
%doc README.md
%{_usrsrc}/amneziawg-%{version}

%changelog
* Fri Apr 03 2026 Automated Update <github-actions@github.com> - 1:1.0.20260403gitac946a9-1
- Update to git commit ac946a9
* Fri Apr 04 2025 Automated Update <github-actions@github.com> - 1:1.0.20260403gitac946a9-1
- Initial automated tracking from git commit ac946a9

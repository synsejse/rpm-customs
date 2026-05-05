%global _build_id_links none

Name:           scx-manager
Version:        1.15.10
Release:        1%{?dist}
Summary:        Qt GUI for managing sched_ext schedulers via scx_loader

License:        GPL-3.0-only
URL:            https://github.com/CachyOS/scx-manager
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/scx-manager-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  systemd-devel
BuildRequires:  fmt-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel

Requires:       scx-scheds
Requires:       scx-tools

%description
scx-manager is a small Qt-based GUI (extracted from the CachyOS Kernel
Manager) that lets users start, stop, and switch sched_ext schedulers
through the scx_loader D-Bus service.

%prep
%autosetup -n scx-manager-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%{_bindir}/scx-manager
%{_includedir}/scx-manager/schedext-window.hpp
%{_libdir}/libscxctl-ui.so.%{version}
%{_libdir}/libscxctl-ui.so.1
%{_libdir}/libscxctl-ui.so
%{_libdir}/cmake/scxctl-ui/scxctl-ui-config.cmake
%{_libdir}/cmake/scxctl-ui/scxctl-ui-config-version.cmake
%{_libdir}/cmake/scxctl-ui/scxctl-ui-targets.cmake
%{_libdir}/cmake/scxctl-ui/scxctl-ui-targets-release.cmake
%{_datadir}/applications/org.cachyos.scx-manager.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.cachyos.scx-manager.png

%changelog
* Tue May 05 2026 Kristián Kekeš <gamerix2006@gmail.com> - 1.15.10-1
- Initial package, adapted from CachyOS COPR (bieszczaders/kernel-cachyos-addons)

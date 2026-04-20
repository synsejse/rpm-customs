%global debug_package %{nil}

Name:           cinny-desktop
Version:        4.11.2
Release:        1%{?dist}
Summary:        Yet another Matrix client for desktop

License:        AGPL-3.0-only
URL:            https://cinny.in/
Source0:        https://github.com/cinnyapp/cinny-desktop/releases/download/v%{version}/Cinny_desktop-x86_64.deb
Source1:        https://raw.githubusercontent.com/cinnyapp/cinny-desktop/v%{version}/LICENSE

ExclusiveArch:  x86_64

BuildRequires:  binutils
BuildRequires:  gzip
BuildRequires:  tar

%description
Cinny is a Matrix client focusing primarily on a simple, elegant, and secure
interface. This package repackages the upstream desktop binary release.

%prep
%setup -q -c -T
ar x %{SOURCE0}
tar -xzf data.tar.gz

%build

%install
install -dm0755 %{buildroot}%{_bindir}
install -dm0755 %{buildroot}%{_datadir}/applications
install -dm0755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -dm0755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -dm0755 %{buildroot}%{_datadir}/icons/hicolor/256x256@2/apps

install -m0755 usr/bin/cinny %{buildroot}%{_bindir}/cinny
install -m0644 usr/share/applications/Cinny.desktop \
    %{buildroot}%{_datadir}/applications/Cinny.desktop
install -m0644 usr/share/icons/hicolor/32x32/apps/cinny.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/cinny.png
install -m0644 usr/share/icons/hicolor/128x128/apps/cinny.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/cinny.png
install -m0644 usr/share/icons/hicolor/256x256@2/apps/cinny.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256@2/apps/cinny.png

install -Dm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/cinny
%{_datadir}/applications/Cinny.desktop
%{_datadir}/icons/hicolor/32x32/apps/cinny.png
%{_datadir}/icons/hicolor/128x128/apps/cinny.png
%{_datadir}/icons/hicolor/256x256@2/apps/cinny.png

%changelog
* Mon Apr 20 2026 Kristián Kekeš <gamerix2006@gmail.com> - 4.11.2-1
- Initial RPM package from upstream desktop binary release

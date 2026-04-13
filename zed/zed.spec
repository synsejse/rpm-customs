%global upstream_version 0.232.2
%global prerelease     pre
%global appid          dev.zed.Zed-Preview
%global appdir         %{_libdir}/%{name}
%global bundledir      %{appdir}/zed-preview.app

Name:           zed
Version:        %{upstream_version}~%{prerelease}
Release:        1%{?dist}
Summary:        Prebuilt prerelease build of the Zed code editor

License:        GPL-3.0-or-later AND AGPL-3.0-or-later AND Apache-2.0
URL:            https://zed.dev
Source0:        https://github.com/zed-industries/zed/releases/download/v%{upstream_version}-%{prerelease}/zed-linux-x86_64.tar.gz

ExclusiveArch:  x86_64

Obsoletes:      zed-editor < %{version}-%{release}
Provides:       zed-editor = %{version}-%{release}

%description
Zed is a high-performance, multiplayer code editor from the creators of Atom
and Tree-sitter. This package repackages the upstream Linux prerelease bundle
instead of building Zed from source.

%prep
%setup -q -c -T
tar -xzf %{SOURCE0}

%build

%install
install -dm0755 %{buildroot}%{appdir}
cp -a zed-preview.app %{buildroot}%{appdir}/

install -dm0755 %{buildroot}%{_bindir}
ln -s %{bundledir}/bin/zed %{buildroot}%{_bindir}/zed
ln -s %{bundledir}/bin/zed %{buildroot}%{_bindir}/zeditor

install -dm0755 %{buildroot}%{_datadir}/applications
install -dm0755 %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -dm0755 %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps
install -m0644 zed-preview.app/share/applications/%{appid}.desktop \
    %{buildroot}%{_datadir}/applications/%{appid}.desktop
install -m0644 zed-preview.app/share/icons/hicolor/512x512/apps/zed.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/zed.png
install -m0644 zed-preview.app/share/icons/hicolor/1024x1024/apps/zed.png \
    %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/zed.png

%files
%license %{bundledir}/licenses.md
%{_bindir}/zed
%{_bindir}/zeditor
%{appdir}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/512x512/apps/zed.png
%{_datadir}/icons/hicolor/1024x1024/apps/zed.png

%changelog
* Mon Apr 13 2026 Kristián Kekeš <gamerix2006@gmail.com> - 0.232.2~pre-1
- Repackage the upstream Zed prerelease binary bundle

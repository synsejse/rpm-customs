%global _binname   zeditor
%global _appid     dev.zed.Zed

Name:           zed
Version:        0.231.1
Release:        1%{?dist}
Summary:        A high-performance, multiplayer code editor from the creators of Atom and Tree-sitter

License:        GPL-3.0-or-later AND AGPL-3.0-or-later AND Apache-2.0
URL:            https://zed.dev
Source0:        https://github.com/zed-industries/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  rust cargo
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-validation-layers
BuildRequires:  gettext
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)

Requires:       alsa-lib
Requires:       libcurl
Requires:       fontconfig
Requires:       glibc
Requires:       libgcc
Requires:       libstdc++
Requires:       libxcb
Requires:       libxkbcommon
Requires:       nodejs >= 18
Requires:       nmap-ncat
Requires:       npm
Requires:       openssl-libs
Requires:       sqlite-libs
Requires:       vulkan-loader
Requires:       mesa-vulkan-drivers
Requires:       vulkan-tools
Requires:       wayland
Requires:       zlib
Requires:       libzstd

Recommends:     clang
Recommends:     eslint
Recommends:     python3-pyright
Recommends:     rust-analyzer
Recommends:     gnome-keyring

Obsoletes:      zed-editor < %{version}-%{release}
Provides:       zed-editor = %{version}-%{release}

%description
Zed is a high-performance, multiplayer code editor from the creators of Atom
and Tree-sitter. It is designed from the ground up to take full advantage of
modern hardware, with a GPU-accelerated renderer and native support for
collaborative editing.

%prep
%autosetup -n %{name}-%{version}
cargo fetch --locked --target "$(rustc --print host-tuple)"
export DO_STARTUP_NOTIFY="true"
export APP_ICON="zed"
export APP_NAME="Zed"
export APP_CLI="%{_binname}"
export APP_ID="%{_appid}"
export APP_ARGS="%U"
envsubst < "crates/zed/resources/zed.desktop.in" > %{_appid}.desktop
./script/generate-licenses

%build
export CFLAGS="%{optflags} -ffat-lto-objects"
export CXXFLAGS="%{optflags} -ffat-lto-objects"
export RUSTFLAGS="%{build_rustflags} --remap-path-prefix $PWD=/"
export ZED_UPDATE_EXPLANATION="Updates are handled by the system package manager"
export RELEASE_VERSION="%{version}"
export PROTOC=/usr/bin/protoc
export PROTOC_INCLUDE=/usr/include
cargo build --release --frozen --package zed --package cli

%install
install -Dm0755 target/release/cli \
    %{buildroot}%{_bindir}/%{_binname}
install -Dm0755 target/release/zed \
    %{buildroot}%{_libdir}/%{name}/zed-editor
install -Dm0644 %{_appid}.desktop \
    %{buildroot}%{_datadir}/applications/%{_appid}.desktop
install -Dm0644 crates/zed/resources/app-icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{_appid}.png

%files
%license LICENSE-GPL LICENSE-AGPL LICENSE-APACHE
%doc README.md
%{_bindir}/%{_binname}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/zed-editor
%{_datadir}/applications/%{_appid}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{_appid}.png

%changelog
* Wed Apr 08 2026 Automated Update <github-actions@github.com> - 0.231.1-1
- Update to version 0.231.1
* Mon Apr 06 2026 Automated Update <github-actions@github.com> - 0.230.2-1
- Update to version 0.230.2
* Fri Apr 04 2025 Kristián Kekeš <gamerix2006@gmail.com> - 0.230.1-1
- Initial RPM spec based on upstream Arch Linux PKGBUILD

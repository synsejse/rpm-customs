Name:           cachyos-default-kernel
Version:        1.0.0
Release:        1%{?dist}
Summary:        Keep latest CachyOS kernel as default on Fedora

License:        MIT
URL:            https://github.com/synsejse/rpm-customs
BuildArch:      noarch

Source0:        99-default

Requires:       grubby
Requires:       coreutils
Requires:       grep

%description
Installs a post-install kernel hook at /etc/kernel/postinst.d/99-default that
automatically sets the newest CachyOS kernel as the default boot entry after
kernel updates.

This allows keeping Fedora's stock kernel installed as a fallback while always
defaulting to the latest CachyOS kernel.

%prep

%build

%install
install -Dpm0755 %{SOURCE0} %{buildroot}%{_sysconfdir}/kernel/postinst.d/99-default

%files
%config(noreplace) %{_sysconfdir}/kernel/postinst.d/99-default

%changelog
* Wed Apr 09 2026 Kristián Kekeš <gamerix2006@gmail.com> - 1.0.0-1
- Initial package

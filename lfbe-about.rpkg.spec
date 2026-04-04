Name:           lfbe-about
Version:        1.0.1
Release:        1%{?dist}
Summary:        About dialog for the LFBE Desktop Environment
License:        GPL-3.0-or-later
URL:            https://github.com/Emkamil/lfbe-about

%global forgeurl https://github.com/Emkamil/lfbe-about
%global tag        %{version}
%global commit     %{version}

Source0: %{forgeurl}/archive/%{tag}/%{name}-%{tag}.tar.gz

BuildRequires: rust-packaging
BuildRequires: cargo
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: gettext

%description
A modern and lightweight about dialog for the Lightweight Fast Beautiful Environment (LFBE),
built with Rust, GTK4 and Libadwaita.

%prep
%autosetup -n %{name}-%{tag}

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/lfbe-about

%changelog
* Sat Apr 04 2026 Kamil <kamil@B450-AORUS-PRO> - 1.0.1-1
- Initial release of lfbe-about

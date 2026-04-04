Name:           lfbe-about
Version:        1.0.1
Release:        1%{?dist}
Summary:        LFBE About Dialog
License:        GPL-3.0-or-later
URL:            https://github.com/Emkamil/lfbe-about

# Dynamiczne źródło generowane przez rpkg
Source:         %{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  gettext

%description
Modern about dialog for LFBE.

%prep
# Używamy -n %{name}, ponieważ rpkg zazwyczaj pakuje do folderu o nazwie projektu bez wersji
%autosetup -n %{name}

%build
# Kompilacja binarnego pliku w trybie release
cargo build --release --locked

%install
# 1. Instalacja binarki
install -D -m 0755 target/release/lfbe-about %{buildroot}%{_bindir}/lfbe-about

# 2. Instalacja licencji (zgodnie z Pana drzewem plików: data/licenses/)
mkdir -p %{buildroot}%{_datadir}/lfbe/licenses
install -p -m 0644 data/licenses/*.txt %{buildroot}%{_datadir}/lfbe/licenses/

# 3. Instalacja tłumaczeń
# Zakładamy standardową strukturę dla języka polskiego (pl)
mkdir -p %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES
install -p -m 0644 po/lfbe-about.mo %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/lfbe-about.mo

%files
# Binarka
%{_bindir}/lfbe-about
# Pliki danych (licencje)
%{_datadir}/lfbe/licenses/*.txt
# Tłumaczenia
%{_datadir}/locale/pl/LC_MESSAGES/lfbe-about.mo

%changelog
* Sat Apr 04 2026 Kamil - 1.0.1-1
- Fix build directory issues
- Add support for licenses and translations installation
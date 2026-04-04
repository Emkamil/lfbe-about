Name:           lfbe-about
Version:        1.0.0
Release:        1%{?dist}
Summary:        LFBE About Dialog
License:        GPL-3.0-or-later
URL:            https://github.com/Emkamil/lfbe-about

# To makre nakazuje rpkg spakowanie bieżącego katalogu:
Source:         {{{ git_dir_pack }}}

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

%description
Modern about dialog for LFBE.

%prep
# rpkg pakuje wszystko do katalogu o nazwie projektu
{{{ git_dir_setup_macro }}}
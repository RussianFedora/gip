Name:       gip
Version:    1.7.0
Release:    1%{?dist}
Summary:    Internet Protocol Calculator for Gnome

License:    GPLv2+

Url:        http://code.google.com/p/gip/
Source0:    https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/gip/%{name}-%{version}-1.tar.gz
Patch1:     %{name}-%{version}-ubuntu.patch
Patch2:     %{name}-%{version}-c++11.patch

BuildRequires:  gtkmm24-devel
BuildRequires:  intltool
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Gip is an application for making IP address based calculations.
For example, it can display IP addresses in binary format.
It is also possible to calculate subnets.

%prep
%autosetup -p1 -n %{name}-%{version}-1
touch configure
chmod +x configure
sed -i 's|CFLAGS="-std=c++11|CFLAGS="$(echo $CFLAGS) -std=c++11|' build.sh
sed -i 's|LFLAGS=`pkg-config $REQUIRED_LIBS --libs`|LFLAGS="$(echo $LDFLAGS) `pkg-config $REQUIRED_LIBS --libs`"|' build.sh

%build
%configure
export LIBDIR=lib
./build.sh --prefix %{_prefix}

%install
mkdir -p %{buildroot}%{_prefix}
export LIBDIR=lib
./build.sh --install --prefix %{buildroot}%{_prefix}
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_usr}/lib/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/calc.png
%{_datadir}/mime/packages/%{name}.xml


%changelog
* Wed Jun 27 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.7.0-1
- Initial release

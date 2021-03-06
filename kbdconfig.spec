Summary:	A text-based interface for setting and loading a keyboard map
Summary(pl.UTF-8):	Tekstowy interfejs do ustawiania mapy klawiatury
Name:		kbdconfig
Version:	1.9.15
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	13dcd4a235a95194230d5e1b7173f6c5
BuildRequires:	gettext-tools
BuildRequires:	newt-devel
BuildRequires:	popt-devel
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The kbdconfig utility is a terminal mode program for setting the
keyboard map for your system. Keyboard maps are necessary for using
any keyboard besides the US default keyboard. Kbdconfig will load the
selected keymap before exiting and configure your machine to use that
keymap automatically after rebooting.

You should install kbdconfig if you need a utility for changing your
keyboard map.

%description -l pl.UTF-8
kbdconfig to tekstowe narzędzie do ustawiania mapy klawiatury. Taka
mapa jest potrzebna by używać klawiatury innej niż domyślna,
amerykańska. kbdconfig wczytuje ustawioną mapę przed zakończeniem i
konfiguruje system, by używał tej mapy automatycznie po włączeniu.

%prep
%setup -q

%build
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	MANDIR=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/kbdconfig
%{_mandir}/*/*

Summary:	A text-based interface for setting and loading a keyboard map
Summary(pl):	Tekstowy interfejs do ustawiania mapy klawiatury
Name:		kbdconfig
Version:	1.9.2
Release:	2
License:	GPL
Group:		Base/Utilities
Group(de):	Gr�nds�tzlich/Werkzeuge
Group(pl):	Podstawowe/Narz�dzia
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-man_path.patch
BuildRequires:	newt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveOS:	Linux

%description
The kbdconfig utility is a terminal mode program for setting the
keyboard map for your system. Keyboard maps are necessary for using
any keyboard besides the US default keyboard. Kbdconfig will load the
selected keymap before exiting and configure your machine to use that
keymap automatically after rebooting.

You should install kbdconfig if you need a utility for changing your
keyboard map.

%description -l pl
kbdconfig to tekstowe narz�dzie do ustawiania mapy klawiatury. Taka
mapa jest potrzebna by u�ywa� klawiatury innej ni� domy�lna,
ameryka�ska. kbdconfig wczytuje ustawion� map� przed zako�czeniem i
konfiguruje system, by u�ywa� tej mapy automatycznie po w��czeniu.

%prep
%setup -q
%patch0 -p1

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} INSTROOT=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/kbdconfig
%{_mandir}/man8/kbdconfig.8*

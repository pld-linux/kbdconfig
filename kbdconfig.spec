Summary:	A text-based interface for setting and loading a keyboard map
Summary(pl):	Tekstowy interfejs do ustawiania mapy klawiatury
Name:		kbdconfig
Version:	1.9.2
Release:	1
License:	GPL
ExclusiveOS:	Linux
Group:		Base/Utilities
Group(de):	Gründsätzlich/Werkzeuge
Group(pl):	Podstawowe/Narzêdzia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	%{name}-%{version}.tar.gz

%description
The kbdconfig utility is a terminal mode program for setting the
keyboard map for your system. Keyboard maps are necessary for using
any keyboard besides the US default keyboard. Kbdconfig will load the
selected keymap before exiting and configure your machine to use that
keymap automatically after rebooting.

You should install kbdconfig if you need a utility for changing your
keyboard map.

%prep
%setup -q

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} INSTROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/kbdconfig
%{_mandir}/man8/kbdconfig.8*
%{_datadir}/locale/*/LC_MESSAGES/kbdconfig.mo

Summary: A text-based interface for setting and loading a keyboard map.
Name: kbdconfig
%define version	1.9.2
Version: %{version}
Release: 1
Copyright: GPL
ExclusiveOS: Linux
Group: System Environment/Base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source: kbdconfig-%{version}.tar.gz

%description
The kbdconfig utility is a terminal mode program for setting the keyboard
map for your system. Keyboard maps are necessary for using any keyboard
besides the US default keyboard. Kbdconfig will load the selected keymap
before exiting and configure your machine to use that keymap automatically
after rebooting.

You should install kbdconfig if you need a utility for changing your
keyboard map.

%prep
%setup -q

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make INSTROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root)/usr/sbin/kbdconfig
%attr(-,root,root)/usr/man/man8/kbdconfig.8
%attr(-,root,root)/usr/share/locale/*/LC_MESSAGES/kbdconfig.mo

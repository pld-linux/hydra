#
# TODO:	- add subversion support
#
Summary:	Parallized network authentication cracker
Summary(pl.UTF-8):	Zrównoleglony łamacz uwierzytelnień sieciowych
Name:		hydra
Version:	5.4
Release:	2
License:	GPL
Group:		Networking
Source0:	http://packetstormsecurity.org/groups/thc/%{name}-%{version}-src.tar.gz
# Source0-md5:	fa08b465d19321e77b1a0ef912eeecc1
Patch0:		%{name}-nonsl.patch
URL:		http://www.thc.org/thc-hydra/
BuildRequires:	gtk+2-devel
BuildRequires:	libssh2-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool allows for rapid dictionary attacks against network login
systems, including FTP, POP3, IMAP, Netbios, Telnet, HTTP Auth, LDAP,
NNTP, VNC, ICQ, Socks5, PCNFS, and more.

%description -l pl.UTF-8
To narzędzie pozwala na szybkie ataki słownikowe przeciwko sieciowym
systemom logowania, włączając w to FTP, POP3, IMAP, Netbios, Telnet,
HTTP Auth, LDAP, NNTP, VNC, ICQ, Socks5, PCNFS i inne.

%package xhydra
Summary:	GTK+ version of hydra
Summary(pl.UTF-8):	Wersja GTK+ programu hydra
Group:		Networking

%description xhydra
GTK+ version of hydra.

%description xhydra -l pl.UTF-8
Wersja GTK+ programu hydra.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
%configure
%{__make} \
	CC="%{__cc}" \
	XIPATHS=" -I/usr/include/subversion-1 -I/usr/include/apr -I/usr/include/apr-util" \
	XDEFINES=" -DLIBOPENSSL -DLIBPOSTGRES -DLIBSSH2" \
	XLIBS=" -lssl -lpq -lssh2 -lcrypto"

%install
rm -rf $RPM_BUILD_ROOT

install -D hydra $RPM_BUILD_ROOT%{_bindir}/hydra
install xhydra $RPM_BUILD_ROOT%{_bindir}
install pw-inspector $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENCE.HYDRA README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/pw-inspector

%files xhydra
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xhydra

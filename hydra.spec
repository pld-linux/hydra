Summary:	Parallized network authentication cracker
Summary(pl):	Zrównoleglony łamacz uwierzytelnień sieciowych
Name:		hydra
Version:	4.5
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.thc.org/releases/%{name}-%{version}-src.tar.gz
# Source0-md5:	04c45be0ded184d0f7e92c7a4a936f82
URL:		http://www.thc.org/thc-hydra/
Patch0:		%{name}-nonsl.patch
BuildRequires:	gtk+2-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool allows for rapid dictionary attacks against network login
systems, including FTP, POP3, IMAP, Netbios, Telnet, HTTP Auth, LDAP,
NNTP, VNC, ICQ, Socks5, PCNFS, and more.

%description -l pl
To narzędzie pozwala na szybkie ataki słownikowe przeciwko sieciowym
systemom logowania, włączając w to FTP, POP3, IMAP, Netbios, Telnet,
HTTP Auth, LDAP, NNTP, VNC, ICQ, Socks5, PCNFS i inne.

%package xhydra
Summary:	GTK+ version of hydra
Summary(pl):	Wersja GTK+ programu hydra
Group:		Networking

%description xhydra
GTK+ version of hydra.

%description xhydra -l pl
Wersja GTK+ programu hydra.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
%configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -D hydra $RPM_BUILD_ROOT%{_bindir}/hydra
install xhydra $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENCE.HYDRA README TODO
%attr(755,root,root) %{_bindir}/%{name}

%files xhydra
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xhydra

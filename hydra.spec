Summary:	Parallized network authentication cracker
Summary(pl):	Zrównoleglony łamasz uwierzytelnień sieciowych
Name:		hydra
Version:	2.2
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://www.thc.org/releases/%{name}-%{version}.tar.gz
URL:		http://www.thc.org/
Patch0:		%{name}-nonsl.patch
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool allows for rapid dictionary attacks against network login
systems, including FTP, POP3, IMAP, Netbios, Telnet, HTTP Auth, LDAP,
NNTP, VNC, ICQ, Socks5, PCNFS, and more.

%description -l pl
To narzędzie pozwala na szybkie ataki słownikowe przeciwko sieciowym
systemom logowania, włączając w to FTP, POP3, IMAP, Netbios, Telnet,
HTTP Auth, LDAP, NNTP, VNC, ICQ, Socks5, PCNFS i inne.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D hydra $RPM_BUILD_ROOT%{_bindir}/hydra

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README LICENCE.HYDRA
%attr(755,root,root) %{_bindir}/*

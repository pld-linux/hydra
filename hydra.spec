Summary:	Parallized network authentication cracker
Summary(pl):	Zr�wnoleglony �amasz uwierzytelnie� sieciowych
Name:		hydra
Version:	2.2
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://www.thc.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	05042c1add6155ea48233df05a1e37ae
URL:		http://www.thc.org/
Patch0:		%{name}-nonsl.patch
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool allows for rapid dictionary attacks against network login
systems, including FTP, POP3, IMAP, Netbios, Telnet, HTTP Auth, LDAP,
NNTP, VNC, ICQ, Socks5, PCNFS, and more.

%description -l pl
To narz�dzie pozwala na szybkie ataki s�ownikowe przeciwko sieciowym
systemom logowania, w��czaj�c w to FTP, POP3, IMAP, Netbios, Telnet,
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

#
# TODO:	- add subversion support
#
Summary:	Parallized network authentication cracker
Summary(pl.UTF-8):	Zrównoleglony łamacz uwierzytelnień sieciowych
Name:		hydra
Version:	8.6
Release:	4
License:	GPL
Group:		Networking
Source0:	https://github.com/vanhauser-thc/THC-Archive/blob/master/Tools/%{name}-%{version}.tar.gz?raw=true&/%{name}-%{version}.tar.gz
# Source0-md5:	5d909cfea627a1f2482b82dfbd64956c
Patch0:		%{name}-nonsl.patch
Patch1:		x32.patch
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
Requires:	hydra

%description xhydra
GTK+ version of hydra.

%description xhydra -l pl.UTF-8
Wersja GTK+ programu hydra.

%prep
%setup -q
%patch0 -p1
%ifarch x32
%patch1 -p1
%endif

%build
# this is not autoconf
WSSL_LIB_PATH=%{_libdir} \
./configure \
	--prefix=%{_prefix} \
	--fhs

%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dpl4hydra.sh hydra pw-inspector xhydra $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{_bindir}/hydra
%attr(755,root,root) %{_bindir}/dpl4hydra.sh
%attr(755,root,root) %{_bindir}/pw-inspector

%files xhydra
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xhydra

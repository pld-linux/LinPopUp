Summary:	Linux enhanced port of winpopup
Summary(pl):	Port winpopup'a pod Linux'a
Name:		LinPopUp
Version:	1.2.0
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	ftp://littleigloo.org/pub/linpopup/%{name}-%{version}.src.tar.gz
Patch0:		%{name}-prefix.patch
URL:		http://www.littleigloo.org/
Icon:		LinPopUp.gif
BuildRequires:	gtk+-devel
Requires:	samba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
LinPopUp is a Xwindow graphical port of Winpopup, running over Samba.
It permits to communicate with a windows computer that runs Winpopup,
sending or receiving message. (It also provides an alternative way to
communicate between Linux computers that run Samba). Please note that
LinPopUp is not only a port, as it includes several enhanced features.
Also note that it requires to have Samba installed to be fully
functionnal.

%description -l pl
LinPopUp umo¿liwia wysy³anie krótkich kominikatów tekstowych przy
wykorzystaniu Samby. Pozwala na komunikacjê z osobami pos³uguj±cymi
siê Winpopup'em.

%prep
%setup -q
%patch -p1

%build
cd src
%{__make} \
	DESTDIR="" \
	PREFIX="%{_prefix}" \
	DOC_DIR="%{_defaultdocdir}/%{name}-%{version}" \
	INSTALL_MANPATH='$(DESTDIR)%{_mandir}' \
	DATA_DIR='$(DESTDIR)/var/lib/linpopup' \
	CFLAGS="%{rpmcflags} " \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/linpopup}

(cd src; make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	PREFIX="%{_prefix}" \
	INSTALL_MANPATH='$(DESTDIR)%{_mandir}' \
	DATA_DIR='$(DESTDIR)/var/lib/linpopup' \
	DOC_DIR="$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}" )

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/linpopup.1
echo ".so LinPopUp.1" >$RPM_BUILD_ROOT%{_mandir}/man1/linpopup.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{name}-%{version}

%dir /var/lib/linpopup

%attr(755,root,root) %{_bindir}/*
%attr(666,nobody,nobody) /var/lib/linpopup/messages.dat
%{_mandir}/man1/*
%{_datadir}/LinPopUp

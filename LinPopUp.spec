Summary:	Linux enhanced port of winpopup
Summary(pl):	Port winpopup'a pod Linux'a
Name:		LinPopUp
Version:	1.0.2
Release:	1
Copyright:	GPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Source:		ftp://littleigloo.org/pub/linpopup/%{name}-%{version}.src.tar.bz2
Patch:		LinPopUp-prefix.patch
URL:		http://www.littleigloo.org/
Icon:		LinPopUp.gif
BuildPrereq:	glib-devel
BuildPrereq:	gtk+-devel
BuildPrereq:	XFree86-devel
Requires:	samba
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6
%define _mandir /usr/X11R6/man

%description
LinPopUp is a Xwindow graphical port of Winpopup, running over Samba. It
permits to communicate with a windows computer that runs Winpopup, sending
or receiving message. (It also provides an alternative way to communicate
between Linux computers that run Samba). Please note that LinPopUp is not
only a port, as it includes several enhanced features. Also note that it
requires to have Samba installed to be fully functionnal.

%description -l pl
LinPopUp umo�liwia wysy�anie kr�tkich kominikat�w tekstowych przy
wykorzystaniu Samby. Pozwala na komunikacj� z osobami pos�uguj�cymi si�
Winpopup'em.

%prep
%setup -q
%patch -p1

%build
cd src
make 	DESTDIR="" \
	PREFIX="%{_prefix}" \
	DOC_DIR="%{_defaultdocdir}/%{name}-%{version}" \
	INSTALL_MANPATH='$(DESTDIR)%{_mandir}' \
	DATA_DIR='$(DESTDIR)/var/state/linpopup' \
	CFLAGS="$RPM_OPT_FLAGS " \
	LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/linpopup}

(cd src; make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	PREFIX="%{_prefix}" \
	INSTALL_MANPATH='$(DESTDIR)%{_mandir}' \
	DATA_DIR='$(DESTDIR)/var/state/linpopup' \
	DOC_DIR="$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}" )

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/linpopup.1
echo ".so LinPopUp.1" >$RPM_BUILD_ROOT%{_mandir}/man1/linpopup.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{name}-%{version}

%dir /var/state/linpopup

%attr(755,root,root) %{_bindir}/*
%attr(666,nobody,nobody) /var/state/linpopup/messages.dat
%{_mandir}/man1/*
%{_datadir}/LinPopUp

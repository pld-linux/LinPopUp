Summary:	Linux enhanced port of winpopup
Summary(pl):	Port winpopup'a pod Linux'a
Name:		LinPopUp
Version:	0.9.9
Release:	1
Copyright:	GPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Source:		ftp://littleigloo.org/pub/linpopup/%{name}-%{version}.src.tar.bz2
Patch:		LinPopUp-prefix.patch
URL:		http://www.littleigloo.org/
Icon:		linpopup.gif
Requires:	samba
BuildRoot:	/tmp/%{name}-%{version}-root

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
make \
	DESTDIR="" \
	PREFIX="/usr/X11R6" \
	DOC_DIR="/usr/doc/%{name}-%{version}"
	CFLAGS="$RPM_OPT_FLAGS " \
	LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/X11R6/{bin,man/man1,share},var/lib/linpopup}

(cd src; make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	PREFIX="/usr/X11R6" \
	DOC_DIR="$RPM_BUILD_ROOT//usr/doc/%{name}-%{version}" )

rm -f $RPM_BUILD_ROOT/usr/X11R6/man/man1/linpopup.1
echo ".so LinPopUp.1" >$RPM_BUILD_ROOT/usr/X11R6/man/man1/linpopup.1

rm -f $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}/{COPYING,INSTALL,MANUAL}

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/* \
	$RPM_BUILD_ROOT/usr/doc/%{name}-%{version}/*

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS.gz BUGS.gz NEWS.gz THANKS.gz docs/*
%doc /usr/doc/%{name}-%{version}

%dir /var/lib/linpopup

%attr(755,root,root) /usr/X11R6/bin/*
%attr(666,nobody,nobody) /var/lib/linpopup/messages.dat
/usr/X11R6/man/man1/*
/usr/X11R6/share/LinPopUp

%changelog
* Fri Mar 19 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.9.9-1]
- add LinPopUp-prefix.patch: allow build rpm with no-root account
- remove autogenerated requires
- changes in %file section

* Tue Feb  9 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [0.9.6-2d]
- added gzipping documentation
- sloted BuildRoot into PLD standard
- added LDFLAGS=-s
- cosmetic changes

* Sat Jan 22 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.6-1d]
- added "rm -rf $RPM_BUILD_ROOT" on top %install,
- gzipping instead bzipping2 man pages,

* Sat Jan 21 1999 Artur Frysiak <wiget@usa.net>
- initial release

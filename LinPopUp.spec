Summary:     Linux enhanced port of winpopup
Summary(pl): Port winpopup'a pod Linux'a
Name:        LinPopUp
Version:     0.9.6
Release:     2d
Copyright:   GPL
Group:       Networking
Group(pl):   Sieæ
Source:      ftp://littleigloo.org/pub/linpopup/%{name}-%{version}.src.tar.bz2
URL:         http://www.littleigloo.org/
Icon:        linpopup.gif
Requires:    samba
Requires:    XFree86-libs
Requires:    gtk+
Requires:    glib
BuildRoot:   /tmp/%{name}-%{version}-root

%description
LinPopUp is a Xwindow graphical port of Winpopup, running over Samba. It
permits to communicate with a windows computer that runs Winpopup, sending
or receiving message. (It also provides an alternative way to communicate
between Linux computers that run Samba). Please note that LinPopUp is not
only a port, as it includes several enhanced features. Also note that it
requires to have Samba installed to be fully functionnal.

%description -l pl
LinPopUp umo¿liwia wysy³anie krótkich kominikatów tekstowych przy
wykorzystaniu Samby. Pozwala na komunikacjê z osobami pos³uguj±cymi siê
Winpopup'em.

%prep
%setup -q

%build
cd src

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s
make DESTDIR=/usr/X11R6 SHARE_PATH=/var/lib/linpopup/ 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/X11R6/{bin,man/man1},var/lib/linpopup}

cd src
make install \
	DESTDIR=$RPM_BUILD_ROOT/usr/X11R6
	SHARE_PATH=$RPM_BUILD_ROOT/var/lib/linpopup

rm -rf $RPM_BUILD_ROOT/var/lib/linpopup/docs
ln -s $RPM_BUILD_ROOT/usr/doc/%{name}-%{version} $RPM_BUILD_ROOT/var/lib/linpopup/docs

rm -f $RPM_BUILD_ROOT/usr/X11R6/man/man1/linpopup.1
echo ".so LinPopUp.1" >$RPM_BUILD_ROOT/usr/X11R6/man/man1/linpopup.1

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/*
gzip -9nf AUTHORS BUGS NEWS THANKS docs/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.gz BUGS.gz NEWS.gz THANKS.gz docs/*
%dir /var/lib/linpopup

%attr(755,root,root) /usr/X11R6/bin/*
%attr(644,root, man) /usr/X11R6/man/man1/*
%attr(666,nobody,nobody) /var/lib/linpopup/messages.dat

/var/lib/linpopup/misc

%changelog
* Tue Feb  9 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [0.9.6-2d]
- added gzipping documentation
- sloted BuildRoot into PLD standard
- added LDFLAGS=-s
- cosmetic changes

* Sat Jan 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.6-1d]
- added "rm -rf $RPM_BUILD_ROOT" on top %install,
- gzipping instead bzipping2 man pages,

* Sat Jan 23 1999 Artur Frysiak <wiget@usa.net>
- initial release

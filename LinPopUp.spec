Summary:     Linux enhanced port of winpopup
Summary(pl): Port winpopup'a pod Linux'a
Name:        LinPopUp
Version:     0.9.6
Release:     1d
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
BuildRoot:   /tmp/%{name}-%{version}-%{release}

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
make DESTDIR=/usr/X11R6 SHARE_PATH=/var/lib/linpopup/ CFLAGS="$RPM_OPT_FLAGS "

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS THANKS docs/*
%attr(755,root,root) /usr/X11R6/bin/*

%attr(644,root, man) /usr/X11R6/man/man1/*

%dir /var/lib/linpopup
/var/lib/linpopup/misc
%attr(666,nobody,nobody) /var/lib/linpopup/messages.dat

%changelog
* Sat Jan 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.6-1d]
- added "rm -rf $RPM_BUILD_ROOT" on top %install,
- gzipping instead bzipping2 man pages,

* Sat Jan 23 1999 Artur Frysiak <wiget@usa.net>
- initial release

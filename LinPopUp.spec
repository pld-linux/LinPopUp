# TODO:
# - evil permissions on /var/lib/linpopup/messages.dat
# - nobody user MUST NOT own anything
Summary:	Linux enhanced port of winpopup
Summary(pl):	Port programu winpopup pod Linuksa
Name:		LinPopUp
Version:	1.2.0
Release:	7
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.chez.com/littleigloo/files/%{name}-%{version}.src.tar.gz
# Source0-md5:	26503ac44971e334cbbb0a79dd796d93
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-prefix.patch
URL:		http://www.littleigloo.org/software_002.php3
BuildRequires:	gtk+-devel
Requires:	samba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinPopUp is a Xwindow graphical port of Winpopup, running over Samba.
It permits to communicate with a Windows computer that runs Winpopup,
sending or receiving message. (It also provides an alternative way to
communicate between Linux computers that run Samba). Please note that
LinPopUp is not only a port, as it includes several enhanced features.
Also note that it requires to have Samba installed to be fully
functional.

%description -l pl
LinPopUp umo¿liwia wysy³anie krótkich komunikatów tekstowych przy
wykorzystaniu Samby spod X Window. Pozwala na komunikacjê z osobami
pos³uguj±cymi siê Winpopupem pod Windows. (Jest tak¿e alternatywnym
sposobem na komunikacjê miêdzy u¿ytkownikami Linuksa z Samb±.)
LinPopUp nie jest tylko portem - zawiera te¿ parê rozszerzeñ.

%prep
%setup -q
%patch0 -p1

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/linpopup} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install -C src \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	INSTALL_MANPATH='$(DESTDIR)%{_mandir}' \
	DATA_DIR='$(DESTDIR)/var/lib/linpopup' \
	DOC_DIR="$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}"

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/linpopup.1
echo ".so LinPopUp.1" >$RPM_BUILD_ROOT%{_mandir}/man1/linpopup.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog INSTALL NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(666,nobody,nobody) /var/lib/linpopup/messages.dat
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/*
%{_datadir}/LinPopUp
%dir /var/lib/linpopup

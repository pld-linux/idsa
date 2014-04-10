# NOTE: no longer maintained
Summary:	IDS/A - reference monitor, logger and intrusion detection system
Summary(pl.UTF-8):	ISA/a - monitor odwołań, logger i system wykrywania intruzów
Name:		idsa
Version:	0.93.1
Release:	0.1
License:	GPL v2
Group:		Applications/System
# originally http://jade.cs.uct.ac.za/idsa/download/, but no longer existing
Source0:	http://old-releases.ubuntu.com/ubuntu/pool/universe/i/idsa/%{name}_%{version}.orig.tar.gz
# Source0-md5:	9039c703020b844e0f3b35466c8d8035
Patch0:		%{name}-guile.patch
Patch1:		%{name}-gcc.patch
Patch2:		%{name}-destdir.patch
URL:		http://jade.cs.uct.ac.za/idsa/
BuildRequires:	apache1-devel >= 1.3
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	guile-devel >= 2
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IDS/A is a combined system logger, reference monitor, and intrusion
detection system for applications. It makes it possible not only to
monitor but also adjust application activity. Features include a
powerful logging component and an extensible and modular access
control subsystem which can driven by misuse signatures, anomaly
detection modules, or even a human operator.

%description -l pl.UTF-8
IDS/A to połączenie loggera systemowego, monitora odwołań oraz systemu
wykrywania intruzów dla aplikacji. Umożliwia nie tylko monitorowanie,
ale także modyfikowanie aktywności aplikacji. Właściwości obejmują
potężny komponent logujący oraz rozszerzalny i modularny podsystem
kontroli dostępu, który może być sterowany przez sygnatury nadużyć,
moduły wykrywania anomalii, a nawet człowieka nadzorującego.

%package libs
Summary:	IDS/A shared library
Summary(pl.UTF-8):	Biblioteka współdzielona IDS/A
Group:		Libraries

%description libs
IDS/A shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona IDS/A.

%package devel
Summary:	Header files for IDS/A library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki IDS/A
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for IDS/A library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki IDS/A.

%package guile
Summary:	Guile module for IDS/A
Summary(pl.UTF-8):	Moduł Guile dla IDS/A
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description guile
Guile module for IDS/A allows you to write Scheme programs to allow
or deny an incoming event, as well as correlate related events.

%description guile -l pl.UTF-8
Moduł Guile dla IDS/A pozwala na pisanie programów w języku Scheme
decydujących o zezwoleniu lub odrzuceniu przychodzącego zdarzenia, a
także kojarzeniu powiązanych zdarzeń.

%package gtk
Summary:	Interactive access control with GTK+ GUI for IDS/A
Summary(pl.UTF-8):	Interaktywna kontrola dostępu dla IDS/A przy użyciu GUI GTK+
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
This GTK+ program allows you to make interactive access control
decisions for IDS/A. A console version with the same functionality is
included in the main idsa package.

%description gtk -l pl.UTF-8
Ten program GTK+ pozwala interaktywnie podejmować decyzje dotyczące
kontroli dostępu dla IDS/A. Konsolowa wersja o tej samej
funkcjonalności jest dołączona do głównego pakietu idsa.

%package -n apache1-mod_idsa
Summary:	IDS/A module for Apache 1.x
Summary(pl.UTF-8):	Moduł IDS/A dla Apache'a 1.x
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description -n apache1-mod_idsa
IDS/A Apache module makes it possible for idsad to make access control
decisions for Apache requests.

%description -n apache1-mod_idsa -l pl.UTF-8
Moduł IDS/A dla Apache'a pozwala demonowi idsad podejmowąć decyzje
dotyczące kontroli dostępu dla żądań Apache'a.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_13 \
	--with-apxs=/usr/sbin/apxs1 \
	--with-pamdir=/%{_lib}/security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{BLURB,CREDITS,TODO,WARNING}
%attr(755,root,root) %{_bindir}/idsalog
%attr(755,root,root) %{_bindir}/idsaguardtty
%attr(755,root,root) %{_bindir}/idsascaffold
%attr(755,root,root) %{_bindir}/idsasocket
%attr(755,root,root) %{_bindir}/idsaxmlheader
%attr(755,root,root) %{_sbindir}/idsad
%attr(755,root,root) %{_sbindir}/idsaexec
%attr(755,root,root) %{_sbindir}/idsaklogd
%attr(755,root,root) %{_sbindir}/idsapid
%attr(755,root,root) %{_sbindir}/idsapipe
%attr(755,root,root) %{_sbindir}/idsarlogd
%attr(755,root,root) %{_sbindir}/idsasyslogd
%attr(755,root,root) %{_sbindir}/idsatcpd
%attr(755,root,root) %{_sbindir}/idsatcplogd
%attr(755,root,root) /%{_lib}/security/pam_idsa.so
%attr(755,root,root) %{_libdir}/snoopy.so
%dir %{_libdir}/idsa
%attr(755,root,root) %{_libdir}/idsa/mod_*.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/idsad.conf
%{_mandir}/man5/idsad.conf.5*
%{_mandir}/man8/idsad.8*
%{_mandir}/man8/idsaexec.8*
%{_mandir}/man8/idsaguardtty.8*
%{_mandir}/man8/idsaklogd.8*
%{_mandir}/man8/idsalog.8*
%{_mandir}/man8/idsapid.8*
%{_mandir}/man8/idsapipe.8*
%{_mandir}/man8/idsarlogd.8*
%{_mandir}/man8/idsasyslogd.8*
%{_mandir}/man8/idsatcpd.8*
%{_mandir}/man8/idsatcplogd.8*
%{_mandir}/man8/mod_counter.8*
%{_mandir}/man8/mod_interactive.8*
%{_mandir}/man8/mod_keep.8*
%{_mandir}/man8/mod_log.8*
%{_mandir}/man8/mod_regex.8*
%{_mandir}/man8/mod_time.8*
%{_mandir}/man8/mod_timer.8*
%{_mandir}/man8/mod_true.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libidsa.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libidsa.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libidsa.so
%{_includedir}/idsa.h
%{_includedir}/idsa_internal.h
%{_mandir}/man3/idsa_*.3*

%files guile
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/idsaguile
%{_datadir}/idsa
%{_mandir}/man8/idsaguile.8*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/idsaguardgtk
%{_mandir}/man8/idsaguardgtk.8*

%files -n apache1-mod_idsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/apache1/mod_idsa.so

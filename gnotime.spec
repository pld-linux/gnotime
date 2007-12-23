
#TODO:
# fix desktop file

Summary:	GnoTime - a time tracker
Summary(pl.UTF-8):	GnoTime - program do śledzenia czasu
Name:		gnotime
Version:	2.2.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gttr/%{name}-%{version}.tar.gz
# Source0-md5:	067c3579411cd98e0b18fec0b36475a6
Patch0:		%{name}-gtkhtml.patch
URL:		http://www.linas.org/linux/gtt/gtt.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkhtml-devel >= 3.2.3
BuildRequires:	guile-devel >= 1.6.4
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qof-devel
Requires(post):	GConf2
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	/usr/bin/scrollkeeper-update
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnoTime is a combination stop-watch, diary, consultant billing system
and project manager.  You can measure the amount of time you spend on
a task, associate a memo with it, set a billing rate, print an
invoice, as well as track that status of other projects.

GnoTime used to be called GTT and GTimeTracker, and used to be a part
of gnome-utils, before being renamed and split out into its own
package.

%description -l pl.UTF-8
GnoTime jest kombinacją stopera, pamiętnika, systemu rozliczeniowego
i zarządcy projektu. Możesz odmierzać czas spędzony nad zadaniem,
związać z nim notatnik, ustawić przelicznik kosztów, wydrukować
fakturę, jak również śledzić status innych projektów.

GnoTime był kiedyś nazywany GTT lub GTimeTracker i stanowił część
gnome-utils, zanim został przemianowany i oddzielił się do osobnego
pakietu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}-2.0
%find_lang %{name} --with-gnome
cat %{name}-2.0.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/*.desktop

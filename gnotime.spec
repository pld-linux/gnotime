
#TODO:
# fix desktop file

Summary:	GnoTime - a time tracker
Summary(pl):	GnoTime - program do �ledzenia czasu
Name:		gnotime
Version:	2.2.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gttr/%{name}-%{version}.tar.gz
# Source0-md5:	e2aad191b62b41da7f2176a028f1aaf9
URL:		http://www.linas.org/linux/gtt/gtt.html
BuildRequires:	autoconf
BuildRequires:	automake
# AM_PATH_GLIB macro (abused?)
BuildRequires:	glib-devel >= -1.2.10
BuildRequires:	guile-devel >= 1.6.4
BuildRequires:	gtkhtml-devel >= 3.2.3
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libgtkhtml-devel >= 2.6.2
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnoTime is a combination stop-watch, diary, consultant billing system
and project manager.  You can measure the amount of time you spend on
a task, associate a memo with it, set a billing rate, print an
invoice, as well as track that status of other projects.

GnoTime used to be called GTT and GTimeTracker, and used to be a part
of gnome-utils, before being renamed and split out into its own
package.

%description -l pl
GnoTime jest kombinacj� stopera, pami�tnika, systemu rozliczeniowego
i zarz�dcy projektu. Mo�esz odmierza� czas sp�dzony nad zadaniem,
zwi�za� z nim notatnik, ustawi� przelicznik koszt�w, wydrukowa�
faktur�, jak r�wnie� �ledzi� status innych projekt�w.

GnoTime by� kiedy� nazywany GTT lub GTimeTracker i stanowi� cz��
gnome-utils, zanim zosta� przemianowany i oddzieli� si� do osobnego
pakietu.

%package devel
Summary:	Header files for GnomeTime
Summary:	Pliki nag��wkowe GnomeTime
Group:		Development

%description devel
Header files for GnomeTime

%description -l pl devel
Pliki nag��wkowe GnomeTime

%prep
%setup -q

%build
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}
%{_libdir}/*
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/*.h

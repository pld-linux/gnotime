Summary:	GnoTime - a time tracker
Summary(pl):	GnoTime - program do ¶ledzenia czasu
Name:		gnotime
Version:	2.1.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gttr/%{name}-%{version}.tar.gz
# Source0-md5:	f5543b00fb2646e7d2d1619a2aeed31d
URL:		http://www.linas.org/linux/gtt/gtt.html
BuildRequires:	autoconf
BuildRequires:	automake
# AM_PATH_GLIB macro (abused?)
BuildRequires:	glib-devel
BuildRequires:	guile-devel >= 1.3.4
BuildRequires:	libgnomeui-devel >= 2.0.3
BuildRequires:	libgtkhtml-devel >= 2.0.0
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
GnoTime jest kombinacj± stopera, pamiêtnika, systemu rozliczeniowego
i zarz±dcy projektu. Mo¿esz odmierzaæ czas spêdzony nad zadaniem,
zwi±zaæ z nim notatnik, ustawiæ przelicznik kosztów, wydrukowaæ
fakturê, jak równie¿ ¶ledziæ status innych projektów.

GnoTime by³ kiedy¶ nazywany GTT lub GTimeTracker i stanowi³ czê¶æ
gnome-utils, zanim zosta³ przemianowany i oddzieli³ siê do osobnego
pakietu.

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
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Applications/* $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_datadir}/gnome/help/gtt/* $RPM_BUILD_ROOT%{_datadir}/gnome/help/gnotime
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/help/gtt

%find_lang %{name}-2.0
%find_lang %{name} --with-gnome
cat %{name}-2.0.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/*

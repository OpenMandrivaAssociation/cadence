Name:           Cadence
Version:        @SERVICE@
Release:        0
Summary:        A JACK Audio Toolbox
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://kxstudio.sourceforge.net/cadence
Source:         %{name}-%{version}.tar.xz
BuildRequires:  alsa-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  python3-qt5
BuildRequires:  python3-qt5-devel
BuildRequires:  dbus-1-python3-devel
BuildRequires:  libjack-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires:       a2jmidid
Requires:       jack_capture
Requires:       ladish
Requires:       dbus-1-python3
Recommends:     pulseaudio-module-jack
Recommends:     zita-a2jbridge

%description
 Cadence is a set of tools useful for audio production.
Cadence itself is also an application (the main one), which this page will document.
There are other applications that are part of the Cadence suite, they are usually named as the "Cadence tools".
They are:

    Catarina
    Catia
    Claudia

Some of these also have sub-tools, such as Cadence-JackMeter and Claudia-Launcher.

%prep
%setup -q -n Cadence-%{version}

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
%if 0%{?suse_version}
#sed -i 's:pyuic4:py3uic4:' Makefile
sed -i 's:wildcard /:wildcard $(DESTDIR)/:' Makefile
%endif
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d
make install DESTDIR=%{buildroot} PREFIX="%{_prefix}"
%if 0%{?suse_version}
 %suse_update_desktop_file -r cadence AudioVideo Music
 %suse_update_desktop_file -r catarina AudioVideo Music
 %suse_update_desktop_file -r catia AudioVideo Music
 %suse_update_desktop_file -r claudia AudioVideo Music
 %suse_update_desktop_file -r claudia-launcher AudioVideo Music
%endif

%files
%license COPYING
%doc TODO INSTALL.md README.md
%{_bindir}/*
%{_sysconfdir}/xdg/autostart/cadence-session-start.desktop
%if 0%{?suse_version}
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit/xinitrc.d
%{_sysconfdir}/X11/xinit/xinitrc.d/*
%endif

%if %{defined fedora}
%dir %{_sysconfdir}/X11/Xsession.d
%{_sysconfdir}/X11/Xsession.d/*
%endif

%dir %{_datadir}/cadence
%{_datadir}/cadence/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/

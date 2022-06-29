%define _empty_manifest_terminate_build 0

%define oname Cadence

Name:           cadence
Version:        0.9.2
Release:        1
Summary:        A JACK Audio Toolbox
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://kx.studio/Applications:Cadence
Source:         https://github.com/falkTX/Cadence/archive/refs/tags/v%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  python-qt5
BuildRequires:  python-qt5-devel
BuildRequires:  pkgconfig(dbus-python)
BuildRequires:  pkgconfig(jack)
BuildRequires:  unzip
#BuildRequires:  update-desktop-files
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
%autosetup -n %{oname}-%{version} -p1

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
#%if 0%{?suse_version}
#sed -i 's:pyuic4:py3uic4:' Makefile
#sed -i 's:wildcard /:wildcard $(DESTDIR)/:' Makefile
#%endif
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d
make install DESTDIR=%{buildroot} PREFIX="%{_prefix}"


%files
%license COPYING
%doc TODO INSTALL.md README.md
%{_bindir}/*
%{_sysconfdir}/xdg/autostart/cadence-session-start.desktop
%{_sysconfdir}/X11/xinit/xinitrc.d/61-cadence-session-inject.sh
%dir %{_datadir}/cadence
%{_datadir}/cadence/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/

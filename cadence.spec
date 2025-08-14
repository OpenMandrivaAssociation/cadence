%global	debug_package %{nil}
%global	__requires_exclude /usr/bin/pulseaudio

%define	oname Cadence-ladi

Summary:	Set of tools useful for audio production
Name:	cadence
Version:	1.9.4
Release:	1
License:	GPLv2+
Group:	Sound
Url:			https://github.com/LADI/Cadence/tree/ladi-claudia
Source0:	https://github.com/LADI/Cadence/archive/refs/tags/%{oname}-%{name}-%{version}.tar.gz
Source100:	cadence.rpmlintrc
Patch0:		cadence-0.8.1-mga-fixDesktopFiles.patch
BuildRequires:	python-qt5
BuildRequires:	python-qt5-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(python3) >= 3.5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
# Cannot be noarch because of the binaries in cadence-tools
#BuildArch:	noarch
Requires:	jackit
Requires:	ladish
Requires:	pulseaudio
Requires:	python >= 3.5
Requires:	python-dbus
Requires:	python-qt5-core
Requires:	python-qt5-dbus
Requires:	python-qt5-gui
Requires:	python-qt5-opengl
Requires:	python-qt5-svg
Requires:	python-qt5-widgets
Requires:	python-qt5-xml
Requires:	%{name}-data = %{EVRD}
Requires:	%{name}-tools = %{EVRD}
Requires:	claudia = %{EVRD}
Requires:	catarina = %{EVRD}
Requires:	catia = %{EVRD}
Recommends:		a2jmidid
Recommends:		jack_capture
Recommends:		pulseaudio-module-jack

%description
Cadence is a set of tools useful for audio production. It was developed by
falkTX, using Python3 and Qt5 (and some C++ where needed). The suite
is now maintained by the LADI project.
This package contains the main Cadence application.

%files
%doc COPYING NEWS.adoc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/src/%{name}.py
%{_datadir}/%{name}/src/ui_cadence.py
%{_datadir}/%{name}/src/ui_cadence_*.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_sysconfdir}/xdg/autostart/%{name}-session-start.desktop
%{_sysconfdir}/X11/xinit/xinitrc.d/61-%{name}-session-inject.sh

#--------------------------------------------------------------------

%package data
Summary:	Set of tools useful for audio production

%description data
Cadence is a set of tools useful for audio production.
This package contains the shared data and python modules.

%files data
%{_datadir}/%{name}/pulse2loopback/*.pa
%{_datadir}/%{name}/src/shared.py
%{_datadir}/%{name}/src/shared_cadence.py
%{_datadir}/%{name}/src/shared_canvasjack.py
%{_datadir}/%{name}/src/shared_settings.py
%{_datadir}/%{name}/src/resources_rc.py
%{_datadir}/%{name}/src/ui_settings_app.py
%{_datadir}/%{name}/src/jacklib.py
%{_datadir}/%{name}/src/jacklib_helpers.py
%{_datadir}/%{name}/src/patchcanvas.py
%{_datadir}/%{name}/src/patchcanvas_theme.py
%{_datadir}/%{name}/src/systray.py
%{_datadir}/%{name}/src/canvaspreviewframe.py
%{_datadir}/%{name}/src/clickablelabel.py

#--------------------------------------------------------------------

%package tools
Summary:	Set of tools useful for audio production
Requires:	%{name}-data = %{EVRD}
# Really a Requires, but this is in Extra
Recommends:		jack_capture

%description tools
Cadence is a set of tools useful for audio production.
This package contains the small tools used in Cadence and Claudia.

%files tools
%{_bindir}/%{name}-*
%{_datadir}/%{name}/src/cadence_aloop_daemon.py
%{_datadir}/%{name}/src/cadence_session_start.py
%{_datadir}/%{name}/src/jacksettings.py
%{_datadir}/%{name}/src/logs.py
%{_datadir}/%{name}/src/render.py
%{_datadir}/%{name}/src/ui_logs.py
%{_datadir}/%{name}/src/ui_render.py
%{_datadir}/%{name}/src/ui_settings_jack.py
%{_datadir}/%{name}/pulse2jack/

#--------------------------------------------------------------------

%package -n catarina
Summary:	Set of tools useful for audio production
Requires:	%{name}-data = %{EVRD}

%description -n catarina
Catarina is a testing ground for the 'PatchCanvas' module used in the Cadence
tools.

%files -n catarina
%{_bindir}/catarina
%{_datadir}/%{name}/src/catarina.py
%{_datadir}/%{name}/src/ui_catarina.py
%{_datadir}/%{name}/src/ui_catarina_*.py
%{_datadir}/applications/catarina.desktop
%{_datadir}/icons/hicolor/*/apps/catarina.*

#--------------------------------------------------------------------

%package -n catia
Summary:	JACK Audio Patchbay with A2J Bridge integration from Cadence
Requires:	%{name}-tools = %{EVRD}
Recommends:	a2jmidid

%description -n catia
Catia is a nice JACK Audio Patchbay with A2J Bridge integration. It also
includes Jack Transport support and the ability to render Jack projects.

%files -n catia
%{_bindir}/catia
%{_datadir}/%{name}/src/catia.py
%{_datadir}/%{name}/src/ui_catia.py
%{_datadir}/applications/catia.desktop
%{_datadir}/icons/hicolor/*/apps/catia.*

#--------------------------------------------------------------------

%package -n claudia
Summary:	Graphical User Interface to LADISH from Cadence
Requires:	%{name}-tools = %{EVRD}
Requires:	ladish
Recommends:		a2jmidid

%description -n claudia
Claudia is a Graphical User Interface to LADISH. It has more features than
gladish, including Jack Transport, Configurable Canvas, App Templates,
Render projects (real-time or freewheel mode).

%files -n claudia
%{_bindir}/claudia
%{_bindir}/claudia-launcher
%{_datadir}/%{name}/src/claudia.py
%{_datadir}/%{name}/src/claudia_database.py
%{_datadir}/%{name}/src/claudia_launcher.py
%{_datadir}/%{name}/src/ui_claudia.py
%{_datadir}/%{name}/src/ui_claudia_*.py
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/templates/
%{_datadir}/applications/claudia*.desktop
%{_datadir}/icons/hicolor/*/apps/claudia*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{name}-%{version}

# Remove env from python shebangs
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
find . -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python3|#!%{__python3}|'


%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
%make_build


%install
%make_install PREFIX=%{_prefix}

# Fix perms
chmod +x %{buildroot}%{_datadir}/%{name}/{pulse2loopback,pulse2jack}/*.pa
chmod +x %{buildroot}%{_datadir}/%{name}/src/*.py
chmod -x %{buildroot}%{_datadir}/%{name}/src/resources_rc.py
chmod -x %{buildroot}%{_datadir}/%{name}/src/ui_*
chmod -x %{buildroot}%{_datadir}/%{name}/templates/LMMS.mmp
chmod -x %{buildroot}%{_datadir}/%{name}/templates/Carla.carxp

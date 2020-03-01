# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-amazfish

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Amazfit Bip interface application
Version:    1.2.0
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-amazfish.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   kdb-sqlite3-driver >= 3.1.0
Requires:   libKDb3-3 >= 3.1.0
Requires:   kcoreaddons >= 5.31.0
Requires:   libicu
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Contacts)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(mlite5)
BuildRequires:  pkgconfig(libmkcal-qt5)
BuildRequires:  pkgconfig(libkcalcoren-qt5)
BuildRequires:  kdb-devel >= 3.1.0
BuildRequires:  kcoreaddons-devel >= 5.31.0
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qttools-linguist
BuildRequires:  desktop-file-utils

%description
Short description of my Sailfish OS Application


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}-ui
%{_bindir}/%{name}d
%{_datadir}/%{name}-ui
%{_datadir}/applications/%{name}-ui.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-ui.png
/usr/lib/systemd/user/harbour-amazfish.service
/usr/share/mapplauncherd/privileges.d/harbour-amazfishd.privileges
# >> files
# << files

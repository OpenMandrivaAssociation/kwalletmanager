%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE Wallet Management Tool
Name:		plasma6-kwalletmanager
Version:	24.01.90
Release:	3
License:	GPLv2 LGPLv2
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/system/kwalletmanager/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kwalletmanager-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Auth)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
Conflicts:	kdeutils4-core < 4.6.72


%description
KDE Wallet Manager is for management of the wallets installed on the
system. The KDE wallet subsystem provides a convenient and secure way
to manage all your passwords.

%files -f kwalletmanager.lang -f kcmkwallet.lang -f kwallet5.lang
%doc TODO
%{_bindir}/kwalletmanager5
%{_libdir}/libexec/kf6/kauth/kcm_kwallet_helper5
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwallet5.so
%{_datadir}/applications/kwalletmanager5-kwalletd.desktop
%{_datadir}/applications/org.kde.kwalletmanager5.desktop
%{_datadir}/dbus-1/services/org.kde.kwalletmanager5.service
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet5.conf
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.kde.kwalletmanager5.appdata.xml
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_datadir}/qlogging-categories6/kwalletmanager.categories

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kwalletmanager-%{?git:master}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kwalletmanager
%find_lang kcmkwallet
%find_lang kwallet5 --with-html

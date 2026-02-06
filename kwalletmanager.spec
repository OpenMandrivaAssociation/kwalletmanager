#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE Wallet Management Tool
Name:		kwalletmanager
Version:	25.12.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2 LGPLv2
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/system/kwalletmanager/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kwalletmanager/-/archive/%{gitbranch}/kwalletmanager-%{gitbranchd}.tar.bz2#/kwalletmanager-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kwalletmanager-%{version}.tar.xz
%endif
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
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6StatusNotifierItem)

%rename plasma6-kwalletmanager

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE Wallet Manager is for management of the wallets installed on the
system. The KDE wallet subsystem provides a convenient and secure way
to manage all your passwords.

%files -f %{name}.lang
%doc TODO
%{_bindir}/kwalletmanager5
%{_libdir}/libexec/kf6/kauth/kcm_kwallet_helper5
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwallet5.so
%{_datadir}/applications/kwalletmanager5-kwalletd.desktop
%{_datadir}/applications/org.kde.kwalletmanager.desktop
%{_datadir}/dbus-1/services/org.kde.kwalletmanager.service
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet5.conf
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.kde.kwalletmanager5.appdata.xml
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_datadir}/qlogging-categories6/kwalletmanager.categories

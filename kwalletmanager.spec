%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE Wallet Management Tool
Name:		kwalletmanager
Version:	23.04.3
Release:	1
License:	GPLv2 LGPLv2
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/system/kwalletmanager/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DBusAddons)
Conflicts:	kdeutils4-core < 4.5.72


%description
KDE Wallet Manager is for management of the wallets installed on the
system. The KDE wallet subsystem provides a convenient and secure way
to manage all your passwords.

%files -f kwalletmanager.lang -f kcmkwallet.lang -f kwallet5.lang
%doc TODO
%{_datadir}/qlogging-categories5/kwalletmanager.categories
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet5.conf
%{_bindir}/kwalletmanager5
%{_libdir}/libexec/kauth/kcm_kwallet_helper5
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwallet5.so
%{_datadir}/applications/kwalletmanager5-kwalletd.desktop
%{_datadir}/applications/org.kde.kwalletmanager5.desktop
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_datadir}/kservices5/kwalletmanager5_show.desktop
%{_datadir}/metainfo/org.kde.kwalletmanager5.appdata.xml
%{_datadir}/icons/*/*/*/*
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_datadir}/dbus-1/services/org.kde.kwalletmanager5.service

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kwalletmanager
%find_lang kcmkwallet
%find_lang kwallet5 --with-html

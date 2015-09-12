Summary:	KDE Wallet Management Tool
Name:		kwalletmanager
Version:	15.08.0
Release:	2
License:	GPLv2 LGPLv2
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/system/kwalletmanager/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%files
%doc COPYING COPYING.LIB TODO
%doc %{_docdir}/HTML/en/kwallet5
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet5.conf
%{_bindir}/kwalletmanager5
%{_libdir}/libexec/kauth/kcm_kwallet_helper5
%{_libdir}/qt5/plugins/kcm_kwallet5.so
%{_datadir}/applications/kwalletmanager5-kwalletd.desktop
%{_datadir}/applications/org.kde.kwalletmanager5.desktop
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_datadir}/kservices5/kwalletconfig5.desktop
%{_datadir}/kservices5/kwalletmanager5_show.desktop
%{_datadir}/kwalletmanager5
%{_datadir}/kxmlgui5/kwalletmanager5
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_datadir}/icons/*/*/*/*

#------------------------------------------------------------------------------

%prep
%setup -q -n kwalletmanager-%{version}

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

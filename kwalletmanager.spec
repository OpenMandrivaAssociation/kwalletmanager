Summary:	KDE Wallet Management Tool
Name:		kwalletmanager
Version:	15.04.2
Release:	1
License:	GPLv2 LGPLv2
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/system/kwalletmanager/
Source:		http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
Conflicts:	kdeutils4-core < 4.5.72
Requires:	kde-runtime

%description
KDE Wallet Manager is for management of the wallets installed on the
system. The KDE wallet subsystem provides a convenient and secure way
to manage all your passwords.

%files
%doc COPYING COPYING.LIB TODO
%doc %{_kde_docdir}/HTML/en/kwallet/
%{_kde_bindir}/kwalletmanager
%{_kde_appsdir}/kwalletmanager
%{_kde_libdir}/kde4/libexec/kcm_kwallet_helper
%{_kde_libdir}/kde4/kcm_kwallet.so
%{_kde_iconsdir}/*/*/apps/kwalletmanager2.*
%{_kde_iconsdir}/*/*/apps/kwalletmanager.*
%{_kde_applicationsdir}/kwalletmanager-kwalletd.desktop
%{_kde_applicationsdir}/kwalletmanager.desktop
%{_kde_services}/kwalletconfig.desktop
%{_kde_services}/kwalletmanager_show.desktop
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet.policy

#------------------------------------------------------------------------------

%prep
%setup -q -n kwalletmanager-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std

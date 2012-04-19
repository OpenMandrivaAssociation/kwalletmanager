Name:       kwallet
Summary:    KDE Wallet Management Tool
Version: 4.8.2
Release: 1
Group:      Graphical desktop/KDE
License:    GPLv2 LGPLv2
URL:        http://www.kde.org/applications/system/kwalletmanager/
Source0:    ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%name-%{version}.tar.xz


BuildRequires: kdelibs4-devel >= 2:%version

Conflicts: kdeutils4-core < 4.5.72
Requires: kdebase4-runtime

%description
KDE Wallet Manager is for management of the wallets installed on the
system. The KDE wallet subsystem provides a convenient and secure way
to manage all your passwords.

%files
%_kde_appsdir/kwalletmanager/
%_kde_bindir/kwalletmanager
%_kde_libdir/kde4/kcm_kwallet.so
%_kde_iconsdir/*/*/apps/kwalletmanager2.*
%_kde_iconsdir/*/*/apps/kwalletmanager.*
%_kde_applicationsdir/kwalletmanager-kwalletd.desktop
%_kde_applicationsdir/kwalletmanager.desktop
%_kde_services/kwalletconfig.desktop
%_kde_services/kwalletmanager_show.desktop
%doc COPYING COPYING.LIB TODO
%doc %_kde_docdir/HTML/en/kwallet/

#------------------------------------------------------------------------------

%prep
%setup -q
%build
%cmake_kde4  -DKDE4_ENABLE_FINAL=ON
%make

%install
%makeinstall_std -C build


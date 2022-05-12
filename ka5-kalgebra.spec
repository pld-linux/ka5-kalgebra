#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kalgebra
Summary:	Kalgebra
Name:		ka5-%{kaname}
Version:	22.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	811f4e91c1fcd2f212b02154f9c897d9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebEngine-devel >= 5.15.5
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-analitza-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExclusiveArch:	i686  %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAlgebra is a fully featured calculator that lets you plot different
types of 2D and 3D functions and to calculate easy (and not so easy)
calculations, such as addition, trigonometric functions or
derivatives.

The application has been thought to be progressively understood for
students, so that starting to use it doesn't get in the way. The
language is deeply integrated with the UI, providing a dictionary with
representations for all the available operations, code highlighting
and code completion.

%description -l pl.UTF-8
KAlgebra jest wszechstronnym kalkulatorem, pozwalającym rysować różne
typy funkcji dwu- i trójwymiarowych i przeliczać łatwe (i nie tylko)
operacje matematycze, jak dodawanie, funkcje trygonometryczne i
pochodne.

Aplikacja została pomyślana tak, aby była stopniowo rozumiana przez
studentów. Język jest głęboko zintegrowany z interfejsem użykownika,
dostarczając słownik z reprezentacją wszystkich dostępnych operacji, a
także podświetlanie kodu i podpowiadanie dopełnień.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calgebra
%attr(755,root,root) %{_bindir}/kalgebra
%attr(755,root,root) %{_bindir}/kalgebramobile
%{_desktopdir}/org.kde.kalgebramobile.desktop
%{_iconsdir}/hicolor/64x64/apps/kalgebra.png
%{_iconsdir}/hicolor/scalable/apps/kalgebra.svgz
%{_datadir}/metainfo/org.kde.kalgebramobile.appdata.xml
%{_desktopdir}/org.kde.kalgebra.desktop
%{_datadir}/katepart5/syntax/kalgebra.xml
%{_datadir}/kservices5/graphsplasmoid.desktop
%{_datadir}/metainfo/org.kde.kalgebra.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid

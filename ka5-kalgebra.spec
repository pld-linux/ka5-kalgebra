%define		kdeappsver	19.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kalgebra
Summary:	Kalgebra
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5fa47becf50214e5543c64e7ae93d3eb
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
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-analitza-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

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
%{_desktopdir}/org.kde.kalgebra.desktop
%{_desktopdir}/org.kde.kalgebramobile.desktop
%{_iconsdir}/hicolor/64x64/apps/kalgebra.png
%{_iconsdir}/hicolor/scalable/apps/kalgebra.svgz
%dir %{_datadir}/kalgebramobile
%dir %{_datadir}/kalgebramobile/plugins
%{_datadir}/kalgebramobile/plugins/About.qml
%{_datadir}/kalgebramobile/plugins/Console.qml
%{_datadir}/kalgebramobile/plugins/Dictionary.qml
%{_datadir}/kalgebramobile/plugins/Plot2D.qml
%{_datadir}/kalgebramobile/plugins/Plot3D.qml
%{_datadir}/kalgebramobile/plugins/Tables.qml
%{_datadir}/kalgebramobile/plugins/VariablesView.qml
%{_datadir}/kalgebramobile/plugins/kalgebraabout.json
%{_datadir}/kalgebramobile/plugins/kalgebraconsole.json
%{_datadir}/kalgebramobile/plugins/kalgebradictionary.json
%{_datadir}/kalgebramobile/plugins/kalgebraplot2d.json
%{_datadir}/kalgebramobile/plugins/kalgebraplot3d.json
%{_datadir}/kalgebramobile/plugins/kalgebratables.json
%{_datadir}/kalgebramobile/plugins/kalgebravariables.json
%dir %{_datadir}/kalgebramobile/plugins/widgets
#%%{_datadir}/kalgebramobile/plugins/widgets/Action.qml
%{_datadir}/kalgebramobile/plugins/widgets/AddButton.qml
#%%{_datadir}/kalgebramobile/plugins/widgets/Button.qml
#%%{_datadir}/kalgebramobile/plugins/widgets/CalcButton.qml
#%%{_datadir}/kalgebramobile/plugins/widgets/ComboBox.qml
#%%{_datadir}/kalgebramobile/plugins/widgets/Dialog.qml
%{_datadir}/kalgebramobile/plugins/widgets/ExpressionInput.qml
%{_datadir}/kalgebramobile/plugins/widgets/KAlgebraMobile.qml
%{_datadir}/kalgebramobile/plugins/widgets/KAlgebraPage.qml
#%%{_datadir}/kalgebramobile/plugins/widgets/Label.qml
%{_datadir}/kalgebramobile/plugins/widgets/RealInput.qml
#%%{_datadir}/kalgebramobile/plugins/widgets/SimpleListView.qml
%{_datadir}/kalgebramobile/plugins/widgets/qmldir
%{_datadir}/katepart5/syntax/kalgebra.xml
%{_datadir}/kservices5/graphsplasmoid.desktop
%{_datadir}/metainfo/org.kde.kalgebra.appdata.xml
%{_datadir}/metainfo/org.kde.kalgebramobile.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid
%dir %{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/contents/ui/config.ui
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.graphsplasmoid/metadata.desktop

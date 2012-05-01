%define name	mysqlcc
%define	rel	1

Name: 		%{name}
Version:	1.0.1
License:	GPL
Group:		Databases
Summary:	MySQL Control Center
URL:		http://www.trellik.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	qt3-devel mysql-devel patch imagemagick
Release:	%mkrel 1
Source:		%{name}-%{version}-src.tar.bz2

%description
mysqlcc is a platform independent graphical MySQL administration client.
It is based on Trolltech's Qt toolkit.

%prep
%setup -n %{name}-%{version}-src -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
%configure
export QTDIR=%{_libdir}/qt3
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
install -m 755 mysqlcc $RPM_BUILD_ROOT%{prefix}/bin
install -m 644 {*.wav,syntax.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 translations/*.{qm,ts} \
               $RPM_BUILD_ROOT%{_datadir}/%{name}/translations

#Menu entry
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
needs="x11" \
section="Databases" \
title="MySQLCC" \
longtitle="MySQLCC" \
command="%{_bindir}/mysqlcc" needs="X11" \
icon="%{name}.png"
EOF

#Menu icons
mkdir -p %{buildroot}/{%{_miconsdir},%{_liconsdir},%{_iconsdir}}
convert xpm/applicationIcon.xpm -resize 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert xpm/applicationIcon.xpm $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert xpm/applicationIcon.xpm -resize 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changelog.txt INSTALL.txt LICENSE.txt README.txt TODO.txt
%{_bindir}/mysqlcc
%{_datadir}/%{name}
%{_iconsdir}/%{name}.*
%{_miconsdir}/%{name}.*
%{_liconsdir}/%{name}.*
%{_menudir}/%{name}
j
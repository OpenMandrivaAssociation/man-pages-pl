%define LNG pl

Summary:	Man pages in polish language
Name:		man-pages-%{LNG}
# Previous (now dead) project was at 0.27
# back in 2007, shipped until OMLx 4.1
Epoch:		1
Version:	0.7
Release:	1
License:	GPLv2
Group:		System/Internationalization
Url:		http://sourceforge.net/projects/manpages-pl/
Source0:	http://sourceforge.net/projects/manpages-pl/files/manpages-pl-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	man
Requires:	locales-%{LNG}
Requires:	man
Requires(pre):	sed grep man

%description
A collection of man pages for Linux in polish language.

%prep
%autosetup -p1 -n manpages-%{LNG}-%{version}

%build

%install
%make_install INSTALL="install -p"

# Provided by procps-ng package
rm $RPM_BUILD_ROOT%{_mandir}/pl/man1/kill.1*
rm $RPM_BUILD_ROOT%{_mandir}/pl/man1/uptime.1*
rm $RPM_BUILD_ROOT%{_mandir}/pl/man8/pidof.8*

LANG=%{LNG} DESTDIR=%{buildroot} %{_bindir}/mandb %{buildroot}%{_mandir}/%{LNG}

mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly
cat > %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron << EOF
#!/bin/bash
LANG=%{LNG} %{_bindir}/mandb %{_mandir}/%{LNG}
exit 0
EOF

chmod a+x %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron

mkdir -p  %{buildroot}/var/cache/man/%{LNG}

touch %{buildroot}/var/cache/man/%{LNG}/whatis

%post
%create_ghostfile /var/cache/man/%{LNG}/whatis root root 644

%files
%dir /var/cache/man/%{LNG}
%ghost %config(noreplace) /var/cache/man/%{LNG}/whatis
%{_mandir}/%{LNG}/man*
%{_mandir}/%{LNG}/cat*
%{_mandir}/%{LNG}/index.db*
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron

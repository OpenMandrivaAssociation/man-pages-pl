%define LNG pl
%define releasedate 28-06-2007

Summary:	Man pages in polish language
Name:		man-pages-%{LNG}
Version:	0.6
Release:	11
License:	GPLv2
Group:		System/Internationalization
Url:		http://ptm.linux.pl
Source0:	http:/ptm.linux.pl/man-PL%{releasedate}.tar.bz2
BuildArch:	noarch
BuildRequires:	man
Requires:	locales-%{LNG}
Requires:	man
Requires(pre):	sed grep man
Autoreqprov:	false

%description
A collection of man pages for Linux in polish language.

%prep
%setup -qn pl_PL

%build
for i in 1 2 3 4 5 6 7 8 9 n; do
        rm -rf man$i/CVS
done

sh ./autogen.sh

%make

%install
mkdir -p %{buildroot}%{_mandir}/%{LNG}/

for i in 1 2 3 4 5 6 7 8 9 n; do
	cp -adpvrf man$i %{buildroot}%{_mandir}/%{LNG}/
done

# those files conflict whith rpm package
#rm %{buildroot}%{_mandir}/pl/man{1/gendiff.1,8/rpm{2cpio,,build,cache,deps,graph}.8}

# those files conflict whith dpkg package
#rm %{buildroot}%{_mandir}/pl/man{1/dpkg-deb.1,8/dpkg{-split,}.8}

# spechelper fails here!!!
#find %{buildroot}/%_mandir -type f -exec bzip2 -9f {} \;

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

# these are provided by vim7:
#rm -f %{buildroot}%{_mandir}/%{LNG}/man1/{evim.,ex.,{,r}{view,vim}.,vimdiff,vimtutor}*

%post
%create_ghostfile /var/cache/man/%{LNG}/whatis root root 644

%files
%doc FAQ ChangeLog readme.english
%dir %{_mandir}/%{LNG}
%dir /var/cache/man/%{LNG}
%ghost %config(noreplace) /var/cache/man/%{LNG}/whatis
%{_mandir}/%{LNG}/man*
%{_mandir}/%{LNG}/cat*
%{_mandir}/%{LNG}/CACHEDIR.TAG*
%{_mandir}/%{LNG}/index.db*
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/cron.weekly/makewhatis-%{LNG}.cron


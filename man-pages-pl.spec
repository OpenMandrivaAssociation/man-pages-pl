%define LANG pl
%define releasedate 26-01-2007

Summary:	Man pages in polish language
Name:		man-pages-%LANG
Version:	0.5
Release:	%mkrel 1
License:	GPL
Group:		System/Internationalization
Source:		http:/ptm.linux.pl/man-PL%{releasedate}.tar.bz2
URL:		http://ptm.linux.pl/
BuildRequires:	man => 1.5m2
Requires:	locales-%LANG, man => 1.5j-8mdk
Requires(pre):	sed grep man
Obsoletes:	man-%LANG, manpages-%LANG
Provides:	man-%LANG, manpages-%LANG
Conflicts:	rpm < 4.4.1-2mdk
Conflicts:	vim-common < 7.0-2mdk
Autoreqprov:	false
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_mandir}/%LANG/
mkdir -p %{buildroot}/var/catman/%LANG/cat{1,2,3,4,5,6,7,8,9,n}

for i in 1 2 3 4 5 6 7 8 9 n; do
	cp -adpvrf man$i %{buildroot}%{_mandir}/%LANG/
done

# those files conflict whith rpm package
#rm %{buildroot}%{_mandir}/pl/man{1/gendiff.1,8/rpm{2cpio,,build,cache,deps,graph}.8}

# those files conflict whith dpkg package
#rm %{buildroot}%{_mandir}/pl/man{1/dpkg-deb.1,8/dpkg{-split,}.8}

# spechelper fails here!!!
#find $RPM_BUILD_ROOT/%_mandir -type f -exec bzip2 -9f {} \;

LANG=%LANG DESTDIR=%{buildroot} /usr/sbin/makewhatis %{buildroot}%{_mandir}/%LANG

mkdir -p %{buildroot}/etc/cron.weekly
cat > %{buildroot}/etc/cron.weekly/makewhatis-%LANG.cron << EOF
#!/bin/bash
LANG=%LANG /usr/sbin/makewhatis %{_mandir}/%LANG
exit 0
EOF

chmod a+x %{buildroot}/etc/cron.weekly/makewhatis-%LANG.cron

mkdir -p  %{buildroot}/var/cache/man/%LANG

# these are provided by vim7:
#rm -f %{buildroot}%{_mandir}/%LANG/man1/{evim.,ex.,{,r}{view,vim}.,vimdiff,vimtutor}*

%postun
# 0 means deleting the package
if [ "$1" = "0" ]; then
   ## Force removing of /var/catman/%LANG, if there isn't any man page
   ## directory /%_mandir/%LANG
   if [ ! -d %_mandir/%LANG ] ; then
       rm -rf /var/catman/%LANG
   fi
fi


%clean
rm -rf %{buildroot}

%files
%defattr(644,root,man,755)
%doc FAQ ChangeLog readme.english
%dir %{_mandir}/%LANG
%dir /var/cache/man/%LANG
%config(noreplace) /var/cache/man/%LANG/whatis
%{_mandir}/%LANG/man*
%attr(755,root,man)/var/catman/%LANG
%config(noreplace) %attr(755,root,root)/etc/cron.weekly/makewhatis-%LANG.cron

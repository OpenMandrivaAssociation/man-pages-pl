%define LNG pl
%define releasedate 28-06-2007

Summary:	Man pages in polish language
Name:		man-pages-%LNG
Version:	0.6
Release:	11
License:	GPL
Group:		System/Internationalization
Source:		http:/ptm.linux.pl/man-PL%{releasedate}.tar.bz2
URL:		http://ptm.linux.pl
BuildRequires:	man => 1.5m2
Requires:	locales-%LNG, man => 1.5j-8mdk
Requires(pre):	sed grep man
Obsoletes:	man-%LNG, manpages-%LNG
Provides:	man-%LNG, manpages-%LNG
Conflicts:	rpm < 4.4.1-2mdk
Conflicts:	vim-common < 7.0-2mdk
Autoreqprov:	false
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

mkdir -p %{buildroot}%{_mandir}/%LNG/

for i in 1 2 3 4 5 6 7 8 9 n; do
	cp -adpvrf man$i %{buildroot}%{_mandir}/%LNG/
done

# those files conflict whith rpm package
#rm %{buildroot}%{_mandir}/pl/man{1/gendiff.1,8/rpm{2cpio,,build,cache,deps,graph}.8}

# those files conflict whith dpkg package
#rm %{buildroot}%{_mandir}/pl/man{1/dpkg-deb.1,8/dpkg{-split,}.8}

# spechelper fails here!!!
#find %{buildroot}/%_mandir -type f -exec bzip2 -9f {} \;

LANG=%LNG DESTDIR=%{buildroot} %{_bindir}/mandb %{buildroot}%{_mandir}/%LNG

mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly
cat > %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron << EOF
#!/bin/bash
LANG=%LNG %{_bindir}/mandb %{_mandir}/%LNG
exit 0
EOF

chmod a+x %{buildroot}%{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron

mkdir -p  %{buildroot}/var/cache/man/%LNG

touch %{buildroot}/var/cache/man/%LNG/whatis

# these are provided by vim7:
#rm -f %{buildroot}%{_mandir}/%LNG/man1/{evim.,ex.,{,r}{view,vim}.,vimdiff,vimtutor}*

%post
%create_ghostfile /var/cache/man/%LNG/whatis root root 644

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,man,755)
%doc FAQ ChangeLog readme.english
%dir %{_mandir}/%LNG
%dir /var/cache/man/%LNG
%ghost %config(noreplace) /var/cache/man/%LNG/whatis
%{_mandir}/%LNG/man*
#%{_mandir}/%LNG/whatis
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/cron.weekly/makewhatis-%LNG.cron


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-9mdv2011.0
+ Revision: 666374
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-8mdv2011.0
+ Revision: 609325
- rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-7mdv2011.0
+ Revision: 609308
- fix build
- fix typos
- fix build
- rebuild
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.6-5mdv2009.1
+ Revision: 351582
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2009.0
+ Revision: 223192
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.6-3mdv2008.1
+ Revision: 152976
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jul 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6-1mdv2008.0
+ Revision: 52100
- new version
- drop /var/catman (wildly obsolete)

* Mon Apr 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5-1mdv2008.0
+ Revision: 19643
- drop Source1
- replace Icon string with Source in spec file
- update to the release from 26-01-2007
- spec file clean


* Wed May 10 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.4-11mdk
- fix more conflicts

* Wed May 10 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.4-10mdk
- use %%mkrel
- fix conflict with vim

* Wed May 11 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-9mdk
- fix conflict with new rpm (#11568)

* Fri Aug 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-8mdk
- 20040401 snapshot

* Thu May 15 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-7mdk
- further conflict cleaning

* Thu May 15 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-6mdk
- fix conflict with dpkg


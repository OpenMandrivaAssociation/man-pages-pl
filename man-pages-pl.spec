%define LNG pl
%define releasedate 28-06-2007

Summary:	Man pages in polish language
Name:		man-pages-%{LNG}
Version:	0.6
Release:	10
License:	GPL
Group:		System/Internationalization
Source0:	http:/ptm.linux.pl/man-PL%{releasedate}.tar.bz2
URL:		http://ptm.linux.pl
BuildRequires:	man => 1.5m2
Requires:	locales-%{LNG} man => 1.5j-8mdk
Obsoletes:	man-%{LNG} manpages-%{LNG}
Provides:	man-%{LNG} manpages-%{LNG}
Conflicts:	rpm < 4.4.1-2mdk
Conflicts:	vim-common < 7.0-2mdk
Autoreqprov:	false
BuildArch:	noarch

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

mkdir -p  %{buildroot}/var/cache/man/%{LNG}

# these are provided by vim7:
#rm -f %{buildroot}%{_mandir}/%LNG/man1/{evim.,ex.,{,r}{view,vim}.,vimdiff,vimtutor}*

# provided by 'mc' package
rm -f %{buildroot}%{_mandir}/%{LNG}/man1/mc.1*

%files
%defattr(644,root,man,755)
%doc FAQ ChangeLog readme.english
%dir %{_mandir}/%{LNG}
%dir /var/cache/man/%{LNG}
%{_mandir}/%{LNG}/man*

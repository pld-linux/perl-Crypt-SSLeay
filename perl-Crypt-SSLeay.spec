%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-SSLeay perl module
Summary(pl):	Modu³ perla Crypt-SSLeay
Name:		perl-Crypt-SSLeay
Version:	0.15
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-SSLeay-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	openssl-devel >= 0.9.4-2
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-SSLeay perl module.

%description -l pl
Modul perla Crypt-SSLeay.

%prep
%setup -q -n Crypt-SSLeay-%{version}

%build
yes "" | perl Makefile.PL

make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Crypt/SSLeay/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Crypt/SSLeay
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz

%{perl_sitearch}/Crypt/SSLeay.pm
%{perl_sitearch}/Crypt/SSLeay
%{perl_sitearch}/Net/SSL.pm

%dir %{perl_sitearch}/auto/Crypt/SSLeay
%{perl_sitearch}/auto/Crypt/SSLeay/.packlist
%{perl_sitearch}/auto/Crypt/SSLeay/SSLeay.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/SSLeay/SSLeay.so

%{_mandir}/man3/*

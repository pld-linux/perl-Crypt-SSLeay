%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SSLeay
Summary:	Crypt::SSLeay Perl module
Summary(cs):	Modul Crypt::SSLeay pro Perl
Summary(da):	Perlmodul Crypt::SSLeay
Summary(de):	Crypt::SSLeay Perl Modul
Summary(es):	Módulo de Perl Crypt::SSLeay
Summary(fr):	Module Perl Crypt::SSLeay
Summary(it):	Modulo di Perl Crypt::SSLeay
Summary(ja):	Crypt::SSLeay Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::SSLeay ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::SSLeay
Summary(pl):	Modu³ Perla Crypt::SSLeay
Summary(pt):	Módulo de Perl Crypt::SSLeay
Summary(pt_BR):	Módulo Perl Crypt::SSLeay
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::SSLeay
Summary(sv):	Crypt::SSLeay Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::SSLeay
Summary(zh_CN):	Crypt::SSLeay Perl Ä£¿é
Name:		perl-Crypt-SSLeay
Version:	0.41
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::SSLeay perl module.

%description -l cs
Modul Crypt::SSLeay pro Perl.

%description -l da
Perlmodul Crypt::SSLeay.

%description -l de
Crypt::SSLeay Perl Modul.

%description -l es
Módulo de Perl Crypt::SSLeay.

%description -l fr
Module Perl Crypt::SSLeay.

%description -l it
Modulo di Perl Crypt::SSLeay.

%description -l ja
Crypt::SSLeay Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Crypt::SSLeay ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Crypt::SSLeay.

%description -l pl
Modu³ Perla Crypt::SSLeay.

%description -l pt
Módulo de Perl Crypt::SSLeay.

%description -l pt_BR
Módulo Perl Crypt::SSLeay.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Crypt::SSLeay.

%description -l sv
Crypt::SSLeay Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Crypt::SSLeay.

%description -l zh_CN
Crypt::SSLeay Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
yes "" | perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_sitearch}/Crypt/SSLeay.pm
%{perl_sitearch}/Crypt/SSLeay
%{perl_sitearch}/Net/SSL.pm
%dir %{perl_sitearch}/auto/Crypt/SSLeay
%{perl_sitearch}/auto/Crypt/SSLeay/SSLeay.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/SSLeay/SSLeay.so
%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SSLeay
Summary:	Crypt::SSLeay Perl module
Summary(cs):	Modul Crypt::SSLeay pro Perl
Summary(da):	Perlmodul Crypt::SSLeay
Summary(de):	Crypt::SSLeay Perl Modul
Summary(es):	M�dulo de Perl Crypt::SSLeay
Summary(fr):	Module Perl Crypt::SSLeay
Summary(it):	Modulo di Perl Crypt::SSLeay
Summary(ja):	Crypt::SSLeay Perl �⥸�塼��
Summary(ko):	Crypt::SSLeay �� ����
Summary(no):	Perlmodul Crypt::SSLeay
Summary(pl):	Modu� Perla Crypt::SSLeay
Summary(pt):	M�dulo de Perl Crypt::SSLeay
Summary(pt_BR):	M�dulo Perl Crypt::SSLeay
Summary(ru):	������ ��� Perl Crypt::SSLeay
Summary(sv):	Crypt::SSLeay Perlmodul
Summary(uk):	������ ��� Perl Crypt::SSLeay
Summary(zh_CN):	Crypt::SSLeay Perl ģ��
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
M�dulo de Perl Crypt::SSLeay.

%description -l fr
Module Perl Crypt::SSLeay.

%description -l it
Modulo di Perl Crypt::SSLeay.

%description -l ja
Crypt::SSLeay Perl �⥸�塼��

%description -l ko
Crypt::SSLeay �� ����.

%description -l no
Perlmodul Crypt::SSLeay.

%description -l pl
Modu� Perla Crypt::SSLeay.

%description -l pt
M�dulo de Perl Crypt::SSLeay.

%description -l pt_BR
M�dulo Perl Crypt::SSLeay.

%description -l ru
������ ��� Perl Crypt::SSLeay.

%description -l sv
Crypt::SSLeay Perlmodul.

%description -l uk
������ ��� Perl Crypt::SSLeay.

%description -l zh_CN
Crypt::SSLeay Perl ģ��

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

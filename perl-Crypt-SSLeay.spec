%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	SSLeay
Summary:	Crypt::SSLeay perl module
Summary(pl):	Modu³ perla Crypt::SSLeay
Name:		perl-Crypt-SSLeay
Version:	0.35
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	openssl-devel >= 0.9.6a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::SSLeay perl module.

%description -l pl
Modul perla Crypt::SSLeay.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
yes "" | perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Crypt/SSLeay.pm
%{perl_sitearch}/Crypt/SSLeay
%{perl_sitearch}/Net/SSL.pm
%dir %{perl_sitearch}/auto/Crypt/SSLeay
%{perl_sitearch}/auto/Crypt/SSLeay/SSLeay.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/SSLeay/SSLeay.so
%{_mandir}/man3/*

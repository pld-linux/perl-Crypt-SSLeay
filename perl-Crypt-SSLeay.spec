#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SSLeay
Summary:	Crypt::SSLeay - OpenSSL glue that provides LWP https support
Summary(pl):	Crypt::SSLeay - obs³uga https dla LWP przez po³±czenie z OpenSSL
Name:		perl-Crypt-SSLeay
Version:	0.49
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This perl module provides support for the https protocol under LWP,
so that a LWP::UserAgent can make https GET & HEAD & POST requests.

The Crypt::SSLeay package contains Net::SSL, which is automatically
loaded by LWP::Protocol::https on https requests, and provides the
necessary SSL glue for that module to work.

%description -l pl
Ten modu³ Perla dostarcza obs³ugê protoko³u https dla LWP, dziêki
czemu LWP::UserAgent mo¿e wykonywaæ zapytania GET i POST po https.

Pakiet Crypt::SSLeay zawiera modu³ Net::SSL, automatycznie ³adowany
przez LWP::Protocol::https w przypadku zapytañ https, oraz dostarcza
niezbêdnych do jego dzia³ania sk³adników.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
yes "" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorarch}/Crypt/SSLeay.pm
%{perl_vendorarch}/Crypt/SSLeay
%{perl_vendorarch}/Net/SSL.pm
%dir %{perl_vendorarch}/auto/Crypt/SSLeay
%{perl_vendorarch}/auto/Crypt/SSLeay/SSLeay.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/SSLeay/SSLeay.so
%{_mandir}/man3/*

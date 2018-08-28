#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SSLeay
Summary:	Crypt::SSLeay - OpenSSL glue that provides LWP HTTPS support
Summary(cs.UTF-8):	Crypt::SSLeay - spojení OpenSSL, které poskytuje podporu HTTPS pro LWP
Summary(da.UTF-8):	Crypt::SSLeay - OpenSSL-klister som giver understøttelse for LWP HTTPS
Summary(de.UTF-8):	Crypt::SSLeay - OpenSSL Elemente für LWP HTTPS Support
Summary(es.UTF-8):	Crypt::SSLeay - Enlace OpenSSL que proporciona soporte HTTPS LWP
Summary(fr.UTF-8):	Crypt::SSLeay - colle OpenSSL fournissant une prise en charge LWP HTTPS
Summary(it.UTF-8):	Crypt::SSLeay - OpenSSL glue che fornisce supporto per LWP HTTPS
Summary(ja.UTF-8):	Crypt::SSLeay - LWP HTTPSのサポートを提供するOpenSSL glue
Summary(ko.UTF-8):	Crypt::SSLeay - LWP HTTPS 지원을 제공하는 OpenSSL 접착(glue) 입니다
Summary(pl.UTF-8):	Crypt::SSLeay - obsługa HTTPS dla LWP przez połączenie z OpenSSL
Summary(pt.UTF-8):	Crypt::SSLeay - a interface de OpenSSL que oferece o suporte em LWP de HTTPS
Summary(pt_BR.UTF-8):	Crypt::SSLeay - a interface de OpenSSL que oferece o suporte em LWP de HTTPS
Summary(sv.UTF-8):	Crypt::SSLeay - OpenSSL-klister som gör stöd för LWP HTTPS
Summary(tr.UTF-8):	Crypt::SSLeay - LWP HTTPS desteği sağlayan OpenSSL bağlantısı
Summary(zh_CN.UTF-8):	Crypt::SSLeay - 提供 LWP HTTPS 支持的 OpenSSL 胶水
Summary(zh_TW.UTF-8):	Crypt::SSLeay - 提供 LWP HTTPS 支援的 OpenSSL glue。
Name:		perl-Crypt-SSLeay
Version:	0.72
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	77d955c9056dbb12413d95d8852a9cdf
Patch0:		no-dot-in-inc.patch
URL:		http://search.cpan.org/dist/Crypt-SSLeay/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-ExtUtils-CBuilder >= 0.280205
BuildRequires:	perl-Path-Class >= 0.35
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Try-Tiny >= 0.19
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Conflicts:	perl-LWP-Protocol-https < 6.02
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This perl module provides support for the HTTPS protocol under LWP,
so that a LWP::UserAgent can make HTTPS GET & HEAD & POST requests.

The Crypt::SSLeay package contains Net::SSL, which is automatically
loaded by LWP::Protocol::https on HTTPS requests, and provides the
necessary SSL glue for that module to work.

%description -l cs.UTF-8
Tento modul Perlu nabízí podporu pro protokol HTTPS pod LWP, takže
LWP::UserAgent může provádět HTTPS požadavky GET & HEAD & POST. Pro
informace o požadavcích POST si prosím přečtěte perldoc LWP.

Balíček Crypt::SSLeay obsahuje Net::SSL, který je automaticky nahrán
LWP::Protocol::https při požadavcích HTTPS, a nabízí potřebné spojení
SSL, aby tento modul fungoval.

%description -l da.UTF-8
Dette perlmodul giver understøttelse for protokollen HTTPS under LWP,
så en LWP::UserAgent kan lave HTTPS-forespørgslerne GET & HEAD & POST.
Se perldoc LWP for mere information om POST-forespørgsler.

Pakken Crypt::SSLeay indeholder Net::SSL som automatisk læses ind af
LWP::Protocol::https ved HTTPS-forespørgsler, og giver det nødvendige
SSL-klister til at det modul kan fungere.

%description -l de.UTF-8
Dieses Perl-Modul liefert Support für das HTTPS-Protokoll unter LWP,
so dass ein LWP::UserAgent HTTPS GET & HEAD & POST Anfragen ausführen
kann. Weitere Informationen über POST-Anfragen sindin perldoc LWP
enthalten.

Das Crypt::SSLeay Paket enthält Net::SSL, das bei HTTPS-Anfragen
automatisch von LWP::Protocol::https geladen wird, und bietet die
erforderlichen SSL-Elemente für das Modul.

%description -l es.UTF-8
Este módulo perl proporciona soporte para el protocolo HTTPS bajo LWP,
de manera que LWP::UserAgent pueda crear peticiones GET & HEAD & POST.
Consulte perldoc LWP para más información sobre las peticiones POST.

El paquete Crypt::SSLeay contiene Net::SSL, que se descarga
automáticamente por LWP::Protocol::https en las peticiones HTTPS y
proporciona los elementos necesarios SSL para que funcione el módulo.

%description -l fr.UTF-8
Le module perl fournit un support pour le protocole HTTPS sous LWP, de
manière à ce qu'un LWP::UserAgent puisse exécuter les requêtes GET &
HEAD & POST. Veuillez consulter perldoc LWP pour obtenir de plus
amples informations concernant les requêtes POST.

Le paquetage Crypt::SSLeay contient Net::SSL, qui est chargé
automatiquement par LWP::Protocol::https sur les requêtes HTTPS, et
fournit la colle SSL nécessaire pour faire fonctionner ce module.

%description -l it.UTF-8
Questo modulo di perl supporta il protocollo HTTPS in LWP, in modo che
un LWP::UserAgent possa effettuare richieste GET & HEAD & POST HTTP.
Consultare perldoc LWP per ulteriori informazioni sulle richieste
POST.

Il pacchetto Crypt::SSLeay contiene Net::SSL, che viene caricato
automaticamente da LWP::Protocol::https sulle richieste HTTP e
fornisce la colla SSL necessaria per far funzionare quel modulo.

%description -l ja.UTF-8
この perlモジュールは、LWPの元でHTTPSプロトコル用のサポートを提供しま
す。ですから、LWP::UserAgent は HTTPS GET & HEAD & POSTリクエストを
作成できます。 POSTリクエストの詳細については perldoc LWPを
御覧下さい。 理 末スト Crypt::SSLeayパッケージには、hリクエストにより
LWP::Protocol::https で自動的にロードされるNet::SSLを含んでいます。そ
して、モジュールが動作するよう に 必要なSSL glueを提供します。

%description -l ko.UTF-8
이 perl 모듈은 LWP::UserAgent가 HTTPS GET, HEAD, POST 요청을 생성할 수
있도록 LWP 하에서 HTTPS 프로토콜에 대한 지원을 제공합니다. POST 요청에
대한 보다 많은 정보를 원하시면, perldoc LWP를 참조하시기 바랍니다.

Crypt::SSLeay 패키지에는 HTTPS 요청에 따라 LWP::Protocol::https에 의해
자동으로 로딩되는 Net::SSL가 포함되어 있으며, 해당 모듈이 작동하는데
필요한 SSL 접착 (glue)을 제공합니다.

%description -l pl.UTF-8
Ten moduł Perla dostarcza obsługę protokołu HTTPS dla LWP, dzięki
czemu LWP::UserAgent może wykonywać zapytania GET i POST po HTTPS.

Pakiet Crypt::SSLeay zawiera moduł Net::SSL, automatycznie ładowany
przez LWP::Protocol::https w przypadku zapytań HTTPS, oraz dostarcza
niezbędnych do jego działania składników.

%description -l pt.UTF-8
Este módulo de Perl providencia o suporte para o protocolo HTTP em
LWP, de modo a que um LWP::UserAgent possa fazer pedidos de HTTPS de
GET & HEAD & POST. Veja o LWP do 'perldoc' para mais informações sobre
os pedidos de POST.

O pacote Crypt::SSLeay contém o Net::SSL, que é carregado
automaticamente pelo LWP::Protocol::https nos pedidos de HTTPS, e que
fornece a lógica de interacção com o SSL necessária para o módulo
funcionar.

%description -l pt_BR.UTF-8
Este módulo de Perl providencia o suporte para o protocolo HTTP em
LWP, de modo a que um LWP::UserAgent possa fazer pedidos de HTTPS de
GET & HEAD & POST. Veja o LWP do 'perldoc' para mais informações sobre
os pedidos de POST.

O pacote Crypt::SSLeay contém o Net::SSL, que é carregado
automaticamente pelo LWP::Protocol::https nos pedidos de HTTPS, e que
fornece a lógica de interacção com o SSL necessária para o módulo
funcionar.

%description -l sv.UTF-8
Denna perlmodul ger stöd för protokollet HTTPS under LWP, så att en
LWP::UserAgent kan göra HTTPS-begäran GET & HEAD & POST.  Se perldoc
LWP för mer information om POST-begäran.

Paketet Crypt::SSLeay innehåller Net::SSL som automatiskt läses in av
LWP::Protocol::https vid HTTPS-begäran, och ger det nödvändiga
SSL-klistret för att den mudulen skall fungera.

%description -l zh_CN.UTF-8
该 Perl 模块提供对 LWP 下的 HTTPS 协议的支持，因此
 LWP::UserAgent 能够进行HTTPS GET & HEAD & POST
请求。请参阅 perldoc LWP 来获取关于 POST 请求的详
细信息。

Crypt::SSLeay 软件包包含 Net::SSL(它在 HTTPS 请求时
被 LWP::Protocol::https 自动载入)，并且为该模块的运行
提供了必要的 SSL 胶水。

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
yes "" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorarch}/Crypt/SSLeay.pm
%{perl_vendorarch}/Crypt/SSLeay
%{perl_vendorarch}/Net/SSL.pm
%dir %{perl_vendorarch}/auto/Crypt/SSLeay
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/SSLeay/SSLeay.so
%{_mandir}/man3/Crypt::SSLeay*.3pm*
%{_mandir}/man3/Net::SSL.3pm*

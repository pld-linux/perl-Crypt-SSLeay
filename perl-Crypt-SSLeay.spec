#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SSLeay
Summary:	Crypt::SSLeay - OpenSSL glue that provides LWP HTTPS support
Summary(cs):	Crypt::SSLeay - spojení OpenSSL, které poskytuje podporu HTTPS pro LWP
Summary(da):	Crypt::SSLeay - OpenSSL-klister som giver understøttelse for LWP HTTPS
Summary(de):	Crypt::SSLeay - OpenSSL Elemente für LWP HTTPS Support
Summary(es):	Crypt::SSLeay - Enlace OpenSSL que proporciona soporte HTTPS LWP
Summary(fr):	Crypt::SSLeay - colle OpenSSL fournissant une prise en charge LWP HTTPS
Summary(it):	Crypt::SSLeay - OpenSSL glue che fornisce supporto per LWP HTTPS
Summary(ja):	Crypt::SSLeay - LWP HTTPS¤Î¥µ¥Ý¡¼¥È¤òÄó¶¡¤¹¤ëOpenSSL glue
Summary(ko):	Crypt::SSLeay - LWP HTTPS Áö¿øÀ» Á¦°øÇÏ´Â OpenSSL Á¢Âø(glue) ÀÔ´Ï´Ù
Summary(pl):	Crypt::SSLeay - obs³uga HTTPS dla LWP przez po³±czenie z OpenSSL
Summary(pt):	Crypt::SSLeay - a interface de OpenSSL que oferece o suporte em LWP de HTTPS
Summary(pt_BR):	Crypt::SSLeay - a interface de OpenSSL que oferece o suporte em LWP de HTTPS
Summary(sv):	Crypt::SSLeay - OpenSSL-klister som gör stöd för LWP HTTPS
Summary(tr):	Crypt::SSLeay - LWP HTTPS desteði saðlayan OpenSSL baðlantýsý
Summary(zh_CN):	Crypt::SSLeay - Ìá¹© LWP HTTPS Ö§³ÖµÄ OpenSSL ½ºË®
Summary(zh_TW):	Crypt::SSLeay - ´£¨Ñ LWP HTTPS ¤ä´©ªº OpenSSL glue¡C
Name:		perl-Crypt-SSLeay
Version:	0.51
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e276fd3970d573139fe56695a7b747bd
Patch0:		%{name}-init.patch
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This perl module provides support for the HTTPS protocol under LWP,
so that a LWP::UserAgent can make HTTPS GET & HEAD & POST requests.

The Crypt::SSLeay package contains Net::SSL, which is automatically
loaded by LWP::Protocol::https on HTTPS requests, and provides the
necessary SSL glue for that module to work.

%description -l cs
Tento modul Perlu nabízí podporu pro protokol HTTPS pod LWP, tak¾e
LWP::UserAgent mù¾e provádìt HTTPS po¾adavky GET & HEAD & POST. Pro
informace o po¾adavcích POST si prosím pøeètìte perldoc LWP.

Balíèek Crypt::SSLeay obsahuje Net::SSL, který je automaticky nahrán
LWP::Protocol::https pøi po¾adavcích HTTPS, a nabízí potøebné spojení
SSL, aby tento modul fungoval.

%description -l da
Dette perlmodul giver understøttelse for protokollen HTTPS under LWP,
så en LWP::UserAgent kan lave HTTPS-forespørgslerne GET & HEAD & POST.
Se perldoc LWP for mere information om POST-forespørgsler.

Pakken Crypt::SSLeay indeholder Net::SSL som automatisk læses ind af
LWP::Protocol::https ved HTTPS-forespørgsler, og giver det nødvendige
SSL-klister til at det modul kan fungere.

%description -l de
Dieses Perl-Modul liefert Support für das HTTPS-Protokoll unter LWP,
so dass ein LWP::UserAgent HTTPS GET & HEAD & POST Anfragen ausführen
kann. Weitere Informationen über POST-Anfragen sindin perldoc LWP
enthalten.

Das Crypt::SSLeay Paket enthält Net::SSL, das bei HTTPS-Anfragen
automatisch von LWP::Protocol::https geladen wird, und bietet die
erforderlichen SSL-Elemente für das Modul.

%description -l es
Este módulo perl proporciona soporte para el protocolo HTTPS bajo LWP,
de manera que LWP::UserAgent pueda crear peticiones GET & HEAD & POST.
Consulte perldoc LWP para más información sobre las peticiones POST.

El paquete Crypt::SSLeay contiene Net::SSL, que se descarga
automáticamente por LWP::Protocol::https en las peticiones HTTPS y
proporciona los elementos necesarios SSL para que funcione el módulo.

%description -l fr
Le module perl fournit un support pour le protocole HTTPS sous LWP, de
manière à ce qu'un LWP::UserAgent puisse exécuter les requêtes GET &
HEAD & POST. Veuillez consulter perldoc LWP pour obtenir de plus
amples informations concernant les requêtes POST.

Le paquetage Crypt::SSLeay contient Net::SSL, qui est chargé
automatiquement par LWP::Protocol::https sur les requêtes HTTPS, et
fournit la colle SSL nécessaire pour faire fonctionner ce module.

%description -l it
Questo modulo di perl supporta il protocollo HTTPS in LWP, in modo che
un LWP::UserAgent possa effettuare richieste GET & HEAD & POST HTTP.
Consultare perldoc LWP per ulteriori informazioni sulle richieste
POST.

Il pacchetto Crypt::SSLeay contiene Net::SSL, che viene caricato
automaticamente da LWP::Protocol::https sulle richieste HTTP e
fornisce la colla SSL necessaria per far funzionare quel modulo.

%description -l ja
¤³¤Î perl¥â¥¸¥å¡¼¥ë¤Ï¡¢LWP¤Î¸µ¤ÇHTTPS¥×¥í¥È¥³¥ëÍÑ¤Î¥µ¥Ý¡¼¥È¤òÄó¶¡¤·¤Þ
¤¹¡£¤Ç¤¹¤«¤é¡¢LWP::UserAgent ¤Ï HTTPS GET & HEAD & POST¥ê¥¯¥¨¥¹¥È¤ò
ºîÀ®¤Ç¤­¤Þ¤¹¡£ POST¥ê¥¯¥¨¥¹¥È¤Î¾ÜºÙ¤Ë¤Ä¤¤¤Æ¤Ï perldoc LWP¤ò
¸æÍ÷²¼¤µ¤¤¡£ Íý Ëö¥¹¥È Crypt::SSLeay¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï¡¢h¥ê¥¯¥¨¥¹¥È¤Ë¤è¤ê
LWP::Protocol::https ¤Ç¼«Æ°Åª¤Ë¥í¡¼¥É¤µ¤ì¤ëNet::SSL¤ò´Þ¤ó¤Ç¤¤¤Þ¤¹¡£¤½
¤·¤Æ¡¢¥â¥¸¥å¡¼¥ë¤¬Æ°ºî¤¹¤ë¤è¤¦ ¤Ë É¬Í×¤ÊSSL glue¤òÄó¶¡¤·¤Þ¤¹¡£

%description -l ko
ÀÌ perl ¸ðµâÀº LWP::UserAgent°¡ HTTPS GET, HEAD, POST ¿äÃ»À» »ý¼ºÇÒ ¼ö
ÀÖµµ·Ï LWP ÇÏ¿¡¼­ HTTPS ÇÁ·ÎÅäÄÝ¿¡ ´ëÇÑ Áö¿øÀ» Á¦°øÇÕ´Ï´Ù. POST ¿äÃ»¿¡
´ëÇÑ º¸´Ù ¸¹Àº Á¤º¸¸¦ ¿øÇÏ½Ã¸é, perldoc LWP¸¦ ÂüÁ¶ÇÏ½Ã±â ¹Ù¶ø´Ï´Ù.

Crypt::SSLeay ÆÐÅ°Áö¿¡´Â HTTPS ¿äÃ»¿¡ µû¶ó LWP::Protocol::https¿¡ ÀÇÇØ
ÀÚµ¿À¸·Î ·ÎµùµÇ´Â Net::SSL°¡ Æ÷ÇÔµÇ¾î ÀÖÀ¸¸ç, ÇØ´ç ¸ðµâÀÌ ÀÛµ¿ÇÏ´Âµ¥
ÇÊ¿äÇÑ SSL Á¢Âø (glue)À» Á¦°øÇÕ´Ï´Ù.

%description -l pl
Ten modu³ Perla dostarcza obs³ugê protoko³u HTTPS dla LWP, dziêki
czemu LWP::UserAgent mo¿e wykonywaæ zapytania GET i POST po HTTPS.

Pakiet Crypt::SSLeay zawiera modu³ Net::SSL, automatycznie ³adowany
przez LWP::Protocol::https w przypadku zapytañ HTTPS, oraz dostarcza
niezbêdnych do jego dzia³ania sk³adników.

%description -l pt
Este módulo de Perl providencia o suporte para o protocolo HTTP em
LWP, de modo a que um LWP::UserAgent possa fazer pedidos de HTTPS de
GET & HEAD & POST. Veja o LWP do 'perldoc' para mais informações sobre
os pedidos de POST.

O pacote Crypt::SSLeay contém o Net::SSL, que é carregado
automaticamente pelo LWP::Protocol::https nos pedidos de HTTPS, e que
fornece a lógica de interacção com o SSL necessária para o módulo
funcionar.

%description -l pt_BR
Este módulo de Perl providencia o suporte para o protocolo HTTP em
LWP, de modo a que um LWP::UserAgent possa fazer pedidos de HTTPS de
GET & HEAD & POST. Veja o LWP do 'perldoc' para mais informações sobre
os pedidos de POST.

O pacote Crypt::SSLeay contém o Net::SSL, que é carregado
automaticamente pelo LWP::Protocol::https nos pedidos de HTTPS, e que
fornece a lógica de interacção com o SSL necessária para o módulo
funcionar.

%description -l sv
Denna perlmodul ger stöd för protokollet HTTPS under LWP, så att en
LWP::UserAgent kan göra HTTPS-begäran GET & HEAD & POST.  Se perldoc
LWP för mer information om POST-begäran.

Paketet Crypt::SSLeay innehåller Net::SSL som automatiskt läses in av
LWP::Protocol::https vid HTTPS-begäran, och ger det nödvändiga
SSL-klistret för att den mudulen skall fungera.

%description -l zh_CN
¸Ã Perl Ä£¿éÌá¹©¶Ô LWP ÏÂµÄ HTTPS Ð­ÒéµÄÖ§³Ö£¬Òò´Ë
 LWP::UserAgent ÄÜ¹»½øÐÐHTTPS GET & HEAD & POST
ÇëÇó¡£Çë²ÎÔÄ perldoc LWP À´»ñÈ¡¹ØÓÚ POST ÇëÇóµÄÏê
Ï¸ÐÅÏ¢¡£

Crypt::SSLeay Èí¼þ°ü°üº¬ Net::SSL(ËüÔÚ HTTPS ÇëÇóÊ±
±» LWP::Protocol::https ×Ô¶¯ÔØÈë)£¬²¢ÇÒÎª¸ÃÄ£¿éµÄÔËÐÐ
Ìá¹©ÁË±ØÒªµÄ SSL ½ºË®¡£

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
yes "" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%doc CHANGES README
%{perl_vendorarch}/Crypt/SSLeay.pm
%{perl_vendorarch}/Crypt/SSLeay
%{perl_vendorarch}/Net/SSL.pm
%dir %{perl_vendorarch}/auto/Crypt/SSLeay
%{perl_vendorarch}/auto/Crypt/SSLeay/SSLeay.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/SSLeay/SSLeay.so
%{_mandir}/man3/*

#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SSLeay
Summary:	Crypt::SSLeay - OpenSSL glue that provides LWP https support
Summary(cs):	Crypt::SSLeay - spojen� OpenSSL, kter� poskytuje podporu https pro LWP
Summary(da):	Crypt::SSLeay - OpenSSL-klister som giver underst�ttelse for LWP https
Summary(de):	Crypt::SSLeay - OpenSSL Elemente f�r LWP https Support
Summary(es):	Crypt::SSLeay - Enlace OpenSSL que proporciona soporte https LWP
Summary(fr):	Crypt::SSLeay - colle OpenSSL fournissant une prise en charge LWP https
Summary(it):	Crypt::SSLeay - OpenSSL glue che fornisce supporto per LWP https
Summary(ja):	Crypt::SSLeay - LWP https�Υ��ݡ��Ȥ��󶡤���OpenSSL glue
Summary(ko):	Crypt::SSLeay - LWP https ������ �����ϴ� OpenSSL ����(glue) �Դϴ�
Summary(pl):	Crypt::SSLeay - obs�uga https dla LWP przez po��czenie z OpenSSL
Summary(pt):	Crypt::SSLeay - a interface de OpenSSL que oferece o suporte em LWP de HTTPS
Summary(pt_BR):	Crypt::SSLeay - a interface de OpenSSL que oferece o suporte em LWP de HTTPS
Summary(sv):	Crypt::SSLeay - OpenSSL-klister som g�r st�d f�r LWP https
Summary(tr):	Crypt::SSLeay - LWP https deste�i sa�layan OpenSSL ba�lant�s�
Summary(zh_CN):	Crypt::SSLeay - �ṩ LWP https ֧�ֵ� OpenSSL ��ˮ
Summary(zh_TW):	Crypt::SSLeay - ���� LWP https �䴩�� OpenSSL glue�C
Name:		perl-Crypt-SSLeay
Version:	0.51
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e276fd3970d573139fe56695a7b747bd
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This perl module provides support for the https protocol under LWP,
so that a LWP::UserAgent can make https GET & HEAD & POST requests.

The Crypt::SSLeay package contains Net::SSL, which is automatically
loaded by LWP::Protocol::https on https requests, and provides the
necessary SSL glue for that module to work.

%description -l cs
Tento modul Perlu nab�z� podporu pro protokol https pod LWP, tak�e
LWP::UserAgent m��e prov�d�t https po�adavky GET & HEAD & POST. Pro
informace o po�adavc�ch POST si pros�m p�e�t�te perldoc LWP.

Bal��ek Crypt::SSLeay obsahuje Net::SSL, kter� je automaticky nahr�n
LWP::Protocol::https p�i po�adavc�ch https, a nab�z� pot�ebn� spojen�
SSL, aby tento modul fungoval.

%description -l da
Dette perlmodul giver underst�ttelse for protokollen https under LWP,
s� en LWP::UserAgent kan lave https-foresp�rgslerne GET & HEAD & POST.
Se perldoc LWP for mere information om POST-foresp�rgsler.

Pakken Crypt::SSLeay indeholder Net::SSL som automatisk l�ses ind af
LWP::Protocol::https ved https-foresp�rgsler, og giver det n�dvendige
SSL-klister til at det modul kan fungere.

%description -l de
Dieses Perl-Modul liefert Support f�r das https-Protokoll unter LWP,
so dass ein LWP::UserAgent https GET & HEAD & POST Anfragen ausf�hren
kann. Weitere Informationen �ber POST-Anfragen sindin perldoc LWP
enthalten.

Das Crypt::SSLeay Paket enth�lt Net::SSL, das bei https-Anfragen
automatisch von LWP::Protocol::https geladen wird, und bietet die
erforderlichen SSL-Elemente f�r das Modul.

%description -l es
Este m�dulo perl proporciona soporte para el protocolo https bajo LWP,
de manera que LWP::UserAgent pueda crear peticiones GET & HEAD & POST.
Consulte perldoc LWP para m�s informaci�n sobre las peticiones POST.

El paquete Crypt::SSLeay contiene Net::SSL, que se descarga
autom�ticamente por LWP::Protocol::https en las peticiones https y
proporciona los elementos necesarios SSL para que funcione el m�dulo.

%description -l fr
Le module perl fournit un support pour le protocole https sous LWP, de
mani�re � ce qu'un LWP::UserAgent puisse ex�cuter les requ�tes GET &
HEAD & POST. Veuillez consulter perldoc LWP pour obtenir de plus
amples informations concernant les requ�tes POST.

Le paquetage Crypt::SSLeay contient Net::SSL, qui est charg�
automatiquement par LWP::Protocol::https sur les requ�tes https, et
fournit la colle SSL n�cessaire pour faire fonctionner ce module.

%description -l it
Questo modulo di perl supporta il protocollo https in LWP, in modo che
un LWP::UserAgent possa effettuare richieste GET & HEAD & POST http.
Consultare perldoc LWP per ulteriori informazioni sulle richieste
POST.

Il pacchetto Crypt::SSLeay contiene Net::SSL, che viene caricato
automaticamente da LWP::Protocol::https sulle richieste http e
fornisce la colla SSL necessaria per far funzionare quel modulo.

%description -l ja
���� perl�⥸�塼��ϡ�LWP�θ���https�ץ�ȥ����ѤΥ��ݡ��Ȥ��󶡤���
�����Ǥ����顢LWP::UserAgent �� https GET & HEAD & POST�ꥯ�����Ȥ�
�����Ǥ��ޤ��� POST�ꥯ�����Ȥξܺ٤ˤĤ��Ƥ� perldoc LWP��
������������ �� ������ Crypt::SSLeay�ѥå������ˤϡ�h�ꥯ�����Ȥˤ��
LWP::Protocol::https �Ǽ�ưŪ�˥��ɤ����Net::SSL��ޤ�Ǥ��ޤ�����
���ơ��⥸�塼�뤬ư���褦 �� ɬ�פ�SSL glue���󶡤��ޤ���

%description -l ko
�� perl ����� LWP::UserAgent�� https GET, HEAD, POST ��û�� ������ ��
�ֵ��� LWP �Ͽ��� https �������ݿ� ���� ������ �����մϴ�. POST ��û��
���� ���� ���� ������ ���Ͻø�, perldoc LWP�� �����Ͻñ� �ٶ��ϴ�.

Crypt::SSLeay ��Ű������ https ��û�� ���� LWP::Protocol::https�� ����
�ڵ����� �ε��Ǵ� Net::SSL�� ���ԵǾ� ������, �ش� ����� �۵��ϴµ�
�ʿ��� SSL ���� (glue)�� �����մϴ�.

%description -l pl
Ten modu� Perla dostarcza obs�ug� protoko�u https dla LWP, dzi�ki
czemu LWP::UserAgent mo�e wykonywa� zapytania GET i POST po https.

Pakiet Crypt::SSLeay zawiera modu� Net::SSL, automatycznie �adowany
przez LWP::Protocol::https w przypadku zapyta� https, oraz dostarcza
niezb�dnych do jego dzia�ania sk�adnik�w.

%description -l pt
Este m�dulo de Perl providencia o suporte para o protocolo HTTP em
LWP, de modo a que um LWP::UserAgent possa fazer pedidos de HTTPS de
GET & HEAD & POST. Veja o LWP do 'perldoc' para mais informa��es sobre
os pedidos de POST.

O pacote Crypt::SSLeay cont�m o Net::SSL, que � carregado
automaticamente pelo LWP::Protocol::https nos pedidos de HTTPS, e que
fornece a l�gica de interac��o com o SSL necess�ria para o m�dulo
funcionar.

%description -l pt_BR
Este m�dulo de Perl providencia o suporte para o protocolo HTTP em
LWP, de modo a que um LWP::UserAgent possa fazer pedidos de HTTPS de
GET & HEAD & POST. Veja o LWP do 'perldoc' para mais informa��es sobre
os pedidos de POST.

O pacote Crypt::SSLeay cont�m o Net::SSL, que � carregado
automaticamente pelo LWP::Protocol::https nos pedidos de HTTPS, e que
fornece a l�gica de interac��o com o SSL necess�ria para o m�dulo
funcionar.

%description -l sv
Denna perlmodul ger st�d f�r protokollet https under LWP, s� att en
LWP::UserAgent kan g�ra https-beg�ran GET & HEAD & POST.  Se perldoc
LWP f�r mer information om POST-beg�ran.

Paketet Crypt::SSLeay inneh�ller Net::SSL som automatiskt l�ses in av
LWP::Protocol::https vid https-beg�ran, och ger det n�dv�ndiga
SSL-klistret f�r att den mudulen skall fungera.

%description -l zh_CN
�� Perl ģ���ṩ�� LWP �µ� https Э���֧�֣����
 LWP::UserAgent �ܹ�����https GET & HEAD & POST
��������� perldoc LWP ����ȡ���� POST �������
ϸ��Ϣ��

Crypt::SSLeay ��������� Net::SSL(���� https ����ʱ
�� LWP::Protocol::https �Զ�����)������Ϊ��ģ�������
�ṩ�˱�Ҫ�� SSL ��ˮ��

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

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Logger
Summary:	POE::Component::Logger - a POE logging class
Summary(pl):	POE::Component::Logger - klasa loguj±ca dla POE
Name:		perl-POE-Component-Logger
Version:	1.00
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b36cfad2d2d446103cbcf671270681ff
URL:		http://poe.perl.org/
BuildRequires:	perl-POE
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Log-Dispatch-Config
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A highly flexible logger component for POE that uses Log::Dispatch and
Log::Dispatch::Config for ultimate flexibility and power.

%description -l pl
Bardzo elastyczny komponent loguj±cy dla POE, u¿ywaj±cy Log::Dispatch
i Log::Dispatch::Config dla maksymalnej elastyczno¶ci i mocy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Logger.pm
%{_mandir}/man3/*

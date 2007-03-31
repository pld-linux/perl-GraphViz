#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GraphViz
Summary:	GraphViz Perl module - interface to the GraphViz graphing tool
Summary(pl.UTF-8):	Moduł Perla GraphViz - interfejs do narzędzia grafowego GraphViz
Name:		perl-GraphViz
Version:	2.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GraphViz/%{pdir}-%{version}.tar.gz
# Source0-md5:	bb89286643e01631d1b7b0179ef120d6
Patch0:		%{name}-path.patch
URL:		http://search.cpan.org/dist/GraphViz/
%if %{with tests}
BuildRequires:	graphviz
%endif
BuildRequires:	perl-Graph
BuildRequires:	perl-IPC-Run >= 0.6
BuildRequires:	perl-Math-Bezier
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	graphviz
Requires:	perl-IPC-Run >= 0.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# needed only for GraphViz::XML
%define		_noautoreq	'perl(XML::Twig)'

%description
This modules provides an interface to layout and generate images of
directed graphs in a variety of formats (PostScript, PNG, etc.) using
the "dot" and "neato" programs from the GraphViz project.

%description -l pl.UTF-8
Ten moduł udostępnia interfejs do planowania i generowania obrazów
skierowanych grafów w różnych formatach (PostScript, PNG itd.) przy
użyciu programów "dot" i "neato" z projektu GraphViz.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/Devel/*.pm
%{perl_vendorlib}/GraphViz.pm
%{perl_vendorlib}/GraphViz
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.graphviz
%{_examplesdir}/%{name}-%{version}/*.output
%{_examplesdir}/%{name}-%{version}/*.out
%{_examplesdir}/%{name}-%{version}/README

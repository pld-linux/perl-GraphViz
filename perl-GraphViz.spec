#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	GraphViz
Summary:	GraphViz Perl module - interface to the GraphViz graphing tool
Summary(pl):	Modu³ Perla GraphViz - interfejs do narzêdzia grafowego GraphViz
Name:		perl-GraphViz
Version:	1.7
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	graphviz
%endif
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Graph
BuildRequires:	perl-IPC-Run >= 0.6
BuildRequires:	perl-Math-Bezier
BuildRequires:	rpm-perlprov >= 3.0.3-16
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

%description -l pl
Ten modu³ udostêpnia interfejs do planowania i generowania obrazów
skierowanych grafów w ró¿nych formatach (PostScript, PNG itd.) przy
u¿yciu programów "dot" i "neato" z projektu GraphViz.

%prep
%setup -q -n %{pdir}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

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
%doc Changes README TODO
%{perl_sitelib}/Devel/*.pm
%{perl_sitelib}/GraphViz.pm
%{perl_sitelib}/GraphViz
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.graphviz
%{_examplesdir}/%{name}-%{version}/*.output
%{_examplesdir}/%{name}-%{version}/*.ttf
%{_examplesdir}/%{name}-%{version}/*.out
%{_examplesdir}/%{name}-%{version}/README

#
# Conditional build:
%bcond_without	doc			# don't build ri/rdoc

%define pkgname htmlentities
Summary:	Library for encoding and decoding XML and HTML entities
Summary(pl.UTF-8):	Biblioteka do kodowania i dekodowania elementów XML i HTML
Name:		ruby-%{pkgname}
Version:	4.4.2
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	74a2bb87b41327ab23998536cf61bce9
URL:		https://github.com/threedaymonk/htmlentities
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTMLEntities is a simple library to facilitate encoding and decoding
of named (&yacute; and so on) or numerical (&#123; or &#x12a;)
entities in HTML and XHTML documents.

%description -l pl.UTF-8
HTMLEntities to prosta biblioteka ułatwiająca kodowanie i dekodowanie
nazwanych (&yacute; itp.) lub liczbowych (&#123; lub &#x12a;)
elementów w dokumentach HTML i XHTML.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with doc}
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -rf ri/created.rid
rm -rf ri/cache.ri
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%if %{with doc}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt History.txt
%{ruby_vendorlibdir}/htmlentities.rb
%{ruby_vendorlibdir}/htmlentities
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%if %{with doc}
%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/HTMLEntities
%endif

Summary:	Library for encoding and decoding XML and HTML entities
Summary(pl.UTF-8):	Biblioteka do kodowania i dekodowania elementów XML i HTML
Name:		ruby-htmlentities
Version:	4.0.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/18492/htmlentities-4.0.0.gem
# Source0-md5:	8490050367c95d63f83049852f7e93a8
URL:		http://htmlentities.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTMLEntities is a simple library to facilitate encoding and decoding
of named (&yacute; and so on) or numerical (&#123; or &#x12a;)
entities in HTML and XHTML documents.

%description -l pl.UTF-8
HTMLEntities to prosta biblioteka ułatwiająca kodowanie i dekodowanie
nazwanych (&yacute; itp.) lub liczbowych (&#123; lub &#x12a;)
elementów w dokumentach HTML i XHTML.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/htmlentities*
%{ruby_ridir}/*

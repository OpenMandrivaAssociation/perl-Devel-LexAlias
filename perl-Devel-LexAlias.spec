%define realname Devel-LexAlias
%define name	perl-%{realname}
%define version	0.04
%define release	%mkrel 4

Summary:	Alias lexical variables
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		%{realname}-%{version}.tar.bz2
BuildRequires:	perl(Devel::Caller)
BuildRequires:  perl-devel
Buildroot:	%{_tmppath}/%{name}-root

%description
Devel::LexAlias provides the ability to alias a lexical variable in a
subroutines scope to one of your choosing.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorarch}/Devel/*
%{perl_vendorarch}/auto/Devel/*

%clean
rm -rf $RPM_BUILD_ROOT


%define upstream_name    Devel-LexAlias
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Alias lexical variables
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-LexAlias-%{upstream_version}.tar.gz

BuildRequires:	perl(Devel::Caller)
BuildRequires:	perl-devel

%description
Devel::LexAlias provides the ability to alias a lexical variable in a
subroutines scope to one of your choosing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{perl_vendorarch}/Devel/*
%{perl_vendorarch}/auto/Devel/*


%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.40.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.40.0-4
+ Revision: 681401
- mass rebuild

* Tue Jul 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.0-3mdv2011.0
+ Revision: 555794
- rebuild for perl 5.12
- rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 406980
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.04-6mdv2009.0
+ Revision: 256634
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.04-4mdv2008.1
+ Revision: 152062
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-3mdv2008.0
+ Revision: 86353
- rebuild


* Sat Mar 25 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- Add BuildRequires

* Fri Mar 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- First Mandriva release



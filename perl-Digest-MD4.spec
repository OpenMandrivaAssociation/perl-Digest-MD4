%define upstream_name    Digest-MD4
%define upstream_version 1.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.9
Release:	1

Summary:	Perl interface to the MD4 Algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Digest/Digest-MD4-1.9.tar.gz

BuildRequires:	perl-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
The Digest-MD4 module allows you to use the MD4 Message Digest algorithm from
within Perl programs. The algorithm takes as input a message of arbitrary
length and produces as output a 128-bit "fingerprint" or "message digest" of
the input.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README rfc1320.txt
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto/Digest
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.500.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.500.0-3
+ Revision: 681421
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.500.0-2mdv2011.0
+ Revision: 555243
- rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.500.0-1mdv2010.1
+ Revision: 504812
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.5-7mdv2010.0
+ Revision: 430413
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.5-6mdv2009.0
+ Revision: 256683
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.5-4mdv2008.1
+ Revision: 152065
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-3mdv2008.0
+ Revision: 86355
- rebuild


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-2mdv2007.0
- spec cleanup
- %%mkrel

* Tue Aug 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdk
- new version 
- fix sources url for rpmbuildupdate

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdk
- initial Mandriva package



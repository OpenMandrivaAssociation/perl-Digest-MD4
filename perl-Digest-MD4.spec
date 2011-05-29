%define upstream_name    Digest-MD4
%define upstream_version 1.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Perl interface to the MD4 Algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Digest/%{upstream_name}-%{upstream_version}.tar.bz2

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

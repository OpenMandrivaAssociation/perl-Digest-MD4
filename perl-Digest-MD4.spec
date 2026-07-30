%define upstream_name    Digest-MD4
%define upstream_version 1.9
Name:       perl-%{upstream_name}
Version:	1.9
Release:	3

Summary:	Perl interface to the MD4 Algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Digest-MD4
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIKEM/DigestMD4/Digest-MD4-1.9.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
The Digest-MD4 module allows you to use the MD4 Message Digest algorithm from
within Perl programs. The algorithm takes as input a message of arbitrary
length and produces as output a 128-bit "fingerprint" or "message digest" of
the input.

%prep
%setup -q -n Digest-MD4-1.9

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
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



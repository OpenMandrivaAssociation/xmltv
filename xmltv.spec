Name:		xmltv
Version:	0.5.61
Release:	%mkrel 1
Summary:	A set of utilities to manage your TV viewing
URL:		http://wiki.xmltv.org
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch2:		xmltv-0.5.59-jp-utf8.patch
Patch4:		xmltv-0.5.59-Makefile.patch
Patch7:		xmltv-0.5.59-None.pm_strict.patch
Patch11:	xmltv-0.5.59-noask.patch
License:	GPLv2+
Group:		Video
BuildArch:	noarch
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-CGI
BuildRequires:  perl-Data-Dump
BuildRequires:	perl-DateManip => 5.42
BuildRequires:	perl-DateTime-Format-Strptime
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-LinkExtractor
BuildRequires:	perl-HTML-TableExtract => 1.08
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTTP-Cache-Transparent
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-libwww-perl => 5.65
BuildRequires:	perl-Lingua-Preferred
BuildRequires:	perl-Lingua-EN-Numbers-Ordinate
BuildRequires:	perl-Linux-DVB
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-Term-ProgressBar >= 2.03
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-Kakasi
BuildRequires:	perl-TimeDate
BuildRequires:	perl-Tk-TableMatrix
BuildRequires:	perl-Unicode-String
BuildRequires:	perl-Unicode-UTF8simple
BuildRequires:	perl-WWW-Mechanize >= 1.02
BuildRequires:	perl-XML-DOM
BuildRequires:	perl-XML-LibXML
BuildRequires:	perl-XML-LibXSLT
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-XML-Twig => 3.09
BuildRequires:	perl-XML-Writer >= 0.4.6
Requires:	perl-HTML-Parser >= 3.34
Obsoletes:	%{name}-grabbers-re < %{version}-%{release}

%description
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

There are five backends at present, grabbing TV listings for Canada,
the USA, the UK, Germany, Austria, Sweden and Norway. There are
filters to sort the listings by date, to remove shows that have
already been broadcast, and a couple of programmes to organize your
viewing by storing preferences of what shows you watch. There are a
couple of backends to produce printed output.

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}-%{version}
%{_bindir}/tv_cat
%{_bindir}/tv_extractinfo_en
%{_bindir}/tv_find_grabbers
%{_bindir}/tv_grep
%{_bindir}/tv_imdb
%{_bindir}/tv_remove_some_overlapping
%{_bindir}/tv_sort
%{_bindir}/tv_split
%{_bindir}/tv_to_latex
%{_bindir}/tv_to_text
%{_bindir}/tv_validate_file
%{_bindir}/tv_validate_grabber
%{_mandir}/man1/tv_cat.1*
%{_mandir}/man1/tv_extractinfo_en.1*
%{_mandir}/man1/tv_find_grabbers.1*
%{_mandir}/man1/tv_grep.1*
%{_mandir}/man1/tv_imdb.1*
%{_mandir}/man1/tv_remove_some_overlapping.1*
%{_mandir}/man1/tv_sort.1*
%{_mandir}/man1/tv_split.1*
%{_mandir}/man1/tv_to_latex.1*
%{_mandir}/man1/tv_to_text.1*
%{_mandir}/man1/tv_validate_file.1*
%{_mandir}/man1/tv_validate_grabber.1*
%dir %{_datadir}/xmltv/
%{_datadir}/xmltv/xmltv.dtd
%{_datadir}/xmltv/xmltv-lineup.dtd

%package -n	perl-XMLTV
Summary:	Perl modules for managing your TV viewing
Group:		Development/Perl

%description -n perl-XMLTV
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains the perl modules from xmltv.

%files -n perl-XMLTV
%defattr(-,root,root)
%{perl_vendorlib}/XMLTV.pm
%{perl_vendorlib}/XMLTV
%{_mandir}/man3/*

%package	grabbers-ar
Summary:	Argentenian grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-ar
This package contains the argentinian grabbers for xmltv.

%files grabbers-ar
%defattr(-,root,root)
%{_bindir}/tv_extractinfo_ar
%{_bindir}/tv_grab_ar
%{_mandir}/man1/tv_extractinfo_ar*.1*
%{_mandir}/man1/tv_grab_ar*.1*

#package	grabbers-au
#Summary:	Australian grabbers for xmltv
#Group:		Video
#Provides:	xmltv-grabbers

#description grabbers-au
#This package contains the australian grabbers for xmltv.

#files grabbers-au
#defattr(-,root,root)
#{_bindir}/tv_grab_au
#{_mandir}/man1/tv_grab_au*.1*
#{_datadir}/xmltv/tv_grab_au/channel_ids

#package	grabbers-be
#Summary:	Belgian grabbers for xmltv
#Group:		Video
#Provides:	xmltv-grabbers

#description grabbers-be
#This package contains the belgian grabbers for xmltv.

#files grabbers-be
#defattr(-,root,root)
#{_bindir}/tv_grab_be
#{_mandir}/man1/tv_grab_be*.1*
#{_datadir}/xmltv/tv_grab_be/channel_ids_fr
#{_datadir}/xmltv/tv_grab_be/channel_ids_nl

%if 0
%package	grabbers-br
Summary:	Brazillian grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-br
This package contains the brazillian grabbers for xmltv.

%files grabbers-br
%defattr(-,root,root)
#{_bindir}/tv_grab_br
%{_bindir}/tv_grab_br_net
%{_mandir}/man1/tv_grab_br*.1*
%endif

%package	grabbers-ch
Summary:	Swiss grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-ch
This package contains the swiss grabbers for xmltv.

%files grabbers-ch
%defattr(-,root,root)
%{_bindir}/tv_grab_ch_*
%{_mandir}/man1/tv_grab_ch_*.1*
#%{_datadir}/xmltv/tv_grab_ch_*/channel_ids

%package	grabbers-combiner
Summary:	Grabber to grab data from multiple grabbers at once
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-combiner
This package contains a grabber to grab data from multiple grabbers at once.

%files grabbers-combiner
%defattr(-,root,root)
%{_bindir}/tv_grab_combiner
%{_mandir}/man1/tv_grab_combiner.1*
#%{_datadir}/xmltv/tv_grab_ch_*/channel_ids

#package	grabbers-de
#Summary:	German grabbers for xmltv
#Group:		Video
#Provides:	xmltv-grabbers

#description grabbers-de
#This package contains the german grabbers for xmltv.

#files grabbers-de
#defattr(-,root,root)
#{_bindir}/tv_grab_de*
#{_mandir}/man1/tv_grab_de*.1*
#{_datadir}/xmltv/tv_grab_de_tvtoday

%package	grabbers-dk
Summary:	Danish grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-dk
This package contains the danish grabbers for xmltv.

%files grabbers-dk
%defattr(-,root,root)
%{_bindir}/tv_grab_dk_dr
%{_mandir}/man1/tv_grab_dk_dr.1*

%package	grabbers-dtv_la
Summary:	Latin American grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-dtv_la
This package contains the latin american grabbers for xmltv.

%files grabbers-dtv_la
%defattr(-,root,root)
%{_bindir}/tv_grab_dtv_la
%{_mandir}/man1/tv_grab_dtv_la.1*

%package	grabbers-ee
Summary:	Estonian grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-ee
This package contains the estonian grabbers for xmltv.

%files grabbers-ee
%defattr(-,root,root)
%{_bindir}/tv_grab_ee*
%{_mandir}/man1/tv_grab_ee*.1*

%package	grabbers-es
Summary:	Spanish grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-es
This package contains the spanish grabbers for xmltv.

%files grabbers-es
%defattr(-,root,root)
%{_bindir}/tv_grab_es*
%{_mandir}/man1/tv_grab_es*.1*

%package	grabbers-eu
Summary:	European grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-eu
This package contains the european grabbers for xmltv.

%files grabbers-eu
%defattr(-,root,root)
%{_bindir}/tv_grab_eu_epgdata
%{_mandir}/man1/tv_grab_eu_epgdata.1*
%{_datadir}/xmltv/tv_grab_eu_epgdata/channel_ids

%package	grabbers-fi
Summary:	Finnish grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-fi
This package contains the finnish grabbers for xmltv.

%files grabbers-fi
%defattr(-,root,root)
%{_bindir}/tv_grab_fi*
%{_mandir}/man1/tv_grab_fi*.1*

%package	grabbers-fr
Summary:	French grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers
Requires:	perl(HTML::TreeBuilder)

%description grabbers-fr
This package contains the french grabbers for xmltv.

%files grabbers-fr
%defattr(-,root,root)
%{_bindir}/tv_grab_fr
%{_bindir}/tv_grab_fr_kazer
%{_mandir}/man1/tv_grab_fr*.1*

%package	grabbers-hr
Summary:	Croatia grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-hr
This package contains the Croatia grabbers for xmltv.

%files grabbers-hr
%defattr(-,root,root)
%{_bindir}/tv_grab_hr
%{_mandir}/man1/tv_grab_hr.1*

%package	grabbers-huro
Summary:	Hungarian-Romanian grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-huro
This package contains the hungarian-romanian grabbers for xmltv.
It also includes Czech and Romanian support.

%files grabbers-huro
%defattr(-,root,root)
%{_bindir}/tv_grab_huro
%{_mandir}/man1/tv_grab_huro.1*
%{_datadir}/xmltv/tv_grab_huro/jobmap
%{_datadir}/xmltv/tv_grab_huro/catmap.hu
%{_datadir}/xmltv/tv_grab_huro/catmap.ro
%{_datadir}/xmltv/tv_grab_huro/catmap.cz
%{_datadir}/xmltv/tv_grab_huro/catmap.sk


%package	grabbers-il
Summary:	Israeli grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-il
This package contains the israeli grabbers for xmltv.

%files grabbers-il
%defattr(-,root,root)
%{_bindir}/tv_grab_il*
%{_mandir}/man1/tv_grab_il*.1*

%package grabbers-in
Summary:        Indian grabbers for xmltv
Group:          Video
Provides:	xmltv-grabbers

%description grabbers-in
This package contains the indian grabbers for xmltv.

%files grabbers-in
%defattr(-,root,root)
%{_bindir}/tv_grab_in*
%{_mandir}/man1/tv_grab_in*.1*

%package	grabbers-is
Summary:	Icelandic grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-is
This package contains the icelandic grabbers for xmltv.

%files grabbers-is
%defattr(-,root,root)
%{_bindir}/tv_grab_is*
%{_mandir}/man1/tv_grab_is*.1*

%package	grabbers-it
Summary:	Italian grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-it
This package contains the italian grabbers for xmltv.

%files grabbers-it
%defattr(-,root,root)
%{_bindir}/tv_grab_it*
%{_mandir}/man1/tv_grab_it*.1*
%{_datadir}/xmltv/tv_grab_it*

%if 0
%package	grabbers-jp
Summary:	Japanese grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-jp
This package contains the japanese grabbers for xmltv.

%files grabbers-jp
%defattr(-,root,root)
%{_bindir}/tv_grab_jp
%{_mandir}/man1/tv_grab_jp.1*
%endif

%package	grabbers-na
Summary:	North-american grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-na
This package contains the north-american grabbers for xmltv.

%files grabbers-na
%defattr(-,root,root)
%{_bindir}/tv_grab_na*
%{_mandir}/man1/tv_grab_na*.1*

#package	grabbers-nc
#Summary:	Nouvelle Caledonie (France) grabbers for xmltv
#Group:		Video
#Provides:	xmltv-grabbers

#description grabbers-nc
#This package contains the nouvelle caledonie (france) grabbers for xmltv.

#files grabbers-nc
#defattr(-,root,root)
#{_bindir}/tv_grab_nc
#{_mandir}/man1/tv_grab_nc.1*

%package	grabbers-nl
Summary:	Dutch grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-nl
This package contains the dutch grabbers for xmltv.

%files grabbers-nl
%defattr(-,root,root)
%{_bindir}/tv_grab_nl*
%{_mandir}/man1/tv_grab_nl*.1*

%package	grabbers-no
Summary:	Norwegian grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-no
This package contains the norwegian grabbers for xmltv.

%files grabbers-no
%defattr(-,root,root)
%{_bindir}/tv_grab_no*
%{_mandir}/man1/tv_grab_no*.1*

%package	grabbers-pt
Summary:	Portugese grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-pt
This package contains the portugese grabbers for xmltv.

%files grabbers-pt
%defattr(-,root,root)
%{_bindir}/tv_grab_pt*
%{_mandir}/man1/tv_grab_pt*.1*

#%package	grabbers-re
#Summary:	Reunion island grabbers for xmltv
#Group:		Video
#Provides:	xmltv-grabbers

#%description grabbers-re
#This package contains the Reunion Island (France) grabbers for xmltv.

#%files grabbers-re
#%defattr(-,root,root)
#%{_bindir}/tv_grab_re*
#%{_mandir}/man1/tv_grab_re*.1*

%package	grabbers-se
Summary:	Swedish grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-se
This package contains the swedish grabbers for xmltv.

%files grabbers-se
%defattr(-,root,root)
%{_bindir}/tv_grab_se*
%{_mandir}/man1/tv_grab_se*.1*

%package	grabbers-uk
Summary:	English grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-uk
This package contains the english grabbers for xmltv.

%files grabbers-uk
%defattr(-,root,root)
%{_bindir}/tv_grab_uk*
%{_mandir}/man1/tv_grab_uk*.1*
%{_datadir}/xmltv/tv_grab_uk*

%package	grabbers-za
Summary:	South-African grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-za
This package contains the south-african grabbers for xmltv.

%files grabbers-za
%defattr(-,root,root)
%{_bindir}/tv_grab_za*
%{_mandir}/man1/tv_grab_za*.1*

%package	gui
Summary:	Graphical frontends to xmltv
Group:		Video

%description gui
XMLTV is a set of utilities to manage your TV viewing. They work with
TV listings stored in the XMLTV format, which is based on XML. The
idea is to separate out the backend (getting the listings) from the
frontend (displaying them for the user), and to implement useful
operations like picking out your favourite programmes as filters that
read and write XML documents.

This package contains graphical frontends to xmltv.

%files gui
%defattr(-,root,root)
%{_bindir}/tv_check
%{_mandir}/man1/tv_check.1*

%package -n tv_to_potatoe
Summary:	Convert XML to the potatoe guide view tool
Group:		Video

%description -n tv_to_potatoe
Convert XML to the potatoe guide view tool.

%files -n tv_to_potatoe
%defattr(-,root,root)
%{_bindir}/tv_to_potatoe
%{_mandir}/man1/tv_to_potatoe.1*

%prep
%setup -q -n %{name}-%{version}
%patch2 -p0
%patch4 -p0
%patch7 -p1 -b .strict
%patch11 -p1 -b .noask

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}

%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%changelog
* Fri Jun 24 2011 Jani Välimaa <wally@mandriva.org> 0.5.61-1mdv2011.0
+ Revision: 686933
- new version 0.5.61
- drop broken tv_grab_re
- readd tv_grab_ar
- add tv_grab_fr_kazer to French grabbers

* Tue Dec 21 2010 Jani Välimaa <wally@mandriva.org> 0.5.59-4mdv2011.0
+ Revision: 623670
- drop P10
- use latest tv_grab_fi from upstream cvs

* Thu Dec 09 2010 Jani Välimaa <wally@mandriva.org> 0.5.59-3mdv2011.0
+ Revision: 618143
- yet more tv_grab_fi fixes
- own unowned dir

* Sat Dec 04 2010 Jani Välimaa <wally@mandriva.org> 0.5.59-2mdv2011.0
+ Revision: 609553
- more tv_grab_fi fixes

* Wed Dec 01 2010 Jani Välimaa <wally@mandriva.org> 0.5.59-1mdv2011.0
+ Revision: 604556
- add missing BRs
- new version 0.5.59
- drop upstream applied patch
- add patch to fix tv_grab_fi due to site change
- add patch to "fix" interactive build
- re-enable grabbers-il and grabbers-nl packages
- add grabbers-in subpackage
- enable tests again
- clean .spec a bit

* Mon Mar 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.56-4mdv2010.1
+ Revision: 512855
- add upstream patch to workaround broken tv_grab_na_dd.in due to latest
  perl-Date-Manip changes (fix mdv bug #56506)

* Sun Feb 07 2010 Jérôme Brenier <incubusss@mandriva.org> 0.5.56-3mdv2010.1
+ Revision: 501552
- add BR perl-DateTime-Format-Strptime and perl-Linux-DVB

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Frederik Himpe <fhimpe@mandriva.org>
    - Update to new version 0.5.56 (South African grabber is back)

* Thu Mar 19 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.55-1mdv2009.1
+ Revision: 357732
- Update to new version 0.5.55
- Disable za, jp and br packages: dropped upstream because they don't
  work
- Add Czech and Slovenian support to huro subpackage

* Fri Jan 16 2009 Guillaume Bedot <littletux@mandriva.org> 0.5.54-1mdv2009.1
+ Revision: 330225
- tv_grab_be removed upstream
- Release 0.5.54

* Mon Jan 12 2009 Guillaume Bedot <littletux@mandriva.org> 0.5.53-1mdv2009.1
+ Revision: 328496
- Fix license
- Fixed URL

  + Stefan van der Eijk <stefan@mandriva.org>
    - 0.5.53

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.5.51-4mdv2009.0
+ Revision: 262464
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.5.51-3mdv2009.0
+ Revision: 257188
- rebuild

* Mon Feb 18 2008 Stefan van der Eijk <stefan@mandriva.org> 0.5.51-1mdv2008.1
+ Revision: 170089
- remove grabbers-nc
- 0.5.51

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 08 2007 Stefan van der Eijk <stefan@mandriva.org> 0.5.50-1mdv2008.1
+ Revision: 116436
- fix path to eu channel_ids
- add discription for grabbers-eu package
- add grabbers-eu package
- disable grabbers-il package
- disable perl-Text-Bidi BuildRequires due to dep issue
- adjust BuildRequires for Israeli grabber
- 0.5.50

* Thu Oct 04 2007 Stefan van der Eijk <stefan@mandriva.org> 0.5.49-1mdv2008.1
+ Revision: 95376
- remove unused patches
- 0.5.49

* Thu Aug 23 2007 Stefan van der Eijk <stefan@mandriva.org> 0.5.48-2mdv2008.0
+ Revision: 69314
- fix http://qa.mandriva.com/show_bug.cgi?id=32746

* Tue Aug 21 2007 Stefan van der Eijk <stefan@mandriva.org> 0.5.48-1mdv2008.0
+ Revision: 68689
- 0.5.48

* Sun Aug 19 2007 Stefan van der Eijk <stefan@mandriva.org> 0.5.47-1mdv2008.0
+ Revision: 66513
- disable make test due to YPBINDPROC_DOMAIN: Domain not bound errors on Mandriva build system
- 0.5.47

* Tue Jul 10 2007 Stefan van der Eijk <stefan@mandriva.org> 0.5.46-1mdv2008.0
+ Revision: 51083
- fix typo in .spec file
- add new grabbers to .spec file
- fix typo in grabbers-es package
- remove grabbers-de package (copyright issue in Germany?)
- 0.5.46
- disable patch1


* Sun Jan 07 2007 Stefan van der Eijk <stefan@mandriva.org> 0.5.45-2mdv2007.0
+ Revision: 105018
- disable patch3 (nl_default_days)

* Mon Dec 04 2006 Stefan van der Eijk <stefan@mandriva.org> 0.5.45-1mdv2007.1
+ Revision: 90454
- 0.5.45

* Sat Nov 04 2006 Stefan van der Eijk <stefan@mandriva.org> 0.5.44-3mdv2007.1
+ Revision: 76524
- sync
- rebuild for 2007.1, decompress patches
- Import xmltv

* Mon Jul 17 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5.44-2
- grabbers-fr: Requires: perl(HTML::TreeBuilder) (#23730)

* Sun Jun 25 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5.44-1
- 0.5.44

* Mon Jun 19 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5.43-2
- add BuildRequires: perl-Locale-Hebrew for the israeli grabber
- patch7: comment out "use strict" from None.pm, it breaks stuff
- reorganize .spec file

* Thu Jun 15 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5.43-1mdk
- 0.5.43

* Sat Apr 15 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5.42-5mdk
- fix Dutch grabber

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5.42-4mdk
- Patch5 (CVS): fix french grabber

* Sun Feb 26 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5.42-3mdk
- commented out all locales Requires (please complain if they are needed)
- removed locales Requires for Sweden (not needed) (#21346)
- add patch4 (perl 5.8.8 issue?)

* Sun Jan 08 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5.42-2mdk
- Remove patch4, it is really no longer needed

* Sun Jan 08 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5.42-1mdk
- New release 0.5.42
- disable patch 4, as it seems to be fixed upstream (please test):
  "tv_grab_fr: fixed for site changes."

* Sun Jan 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5.41-3mdk
- Patch4: update french grabber with latest CVS version

* Sat Dec 31 2005 Stefan van der Eijk <stefan@eijk.nu> 0.5.41-2mdk
- fix bug #19604
- no such package as locales-za

* Fri Dec 02 2005 Stefan van der Eijk <stefan@eijk.nu> 0.5.41-1mdk
- 0.5.41

* Fri Jul 01 2005 Stefan van der Eijk <stefan@mandrakes.org> 0.5.40-2mdk
- patch3: change default number of days for nl grabber

* Sun Jun 05 2005 Stefan van der Eijk <stefan@mandrakes.org> 0.5.40-1mdk
- 0.5.40
- fix typo in 0.5.39-1mdk changelog

* Tue May 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.5.39-2mdk
- Patch 2: fix syntax error with perl 5.8.7

* Mon Mar 14 2005 Stefan van der Eijk <stefan@mandrakes.org> 0.5.39-1mdk
- 0.5.39

* Mon Jan 24 2005 Stefan van der Eijk <stefan@mandrakes.org> 0.5.38-2mdk
- extra BuildRequires for 2nd sweedish grabber
- add portugese grabber package
- make package rpmbuildupdate aware

* Mon Jan 24 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.5.38-1mdk
- 0.5.38

* Wed Dec 01 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.5.37-3mdk 
- all grabbers subpackage provide xmltv-grabbers

* Tue Nov 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.5.37-2mdk 
- split grabbers to reduce dependencies
- some spec cleanup
- added locales dependencies, as suggested by rpmlint (not sure it is a good idea however)

* Mon Nov 29 2004 Stefan van der Eijk <stefan@mandrake.org> 0.5.37-1mdk
- 0.5.37

* Wed Oct 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.36-1mdk
- 0.5.36

* Wed Sep 29 2004 Stefan van der Eijk <stefan@mandrake.org> 0.5.35-1mdk
- 0.5.35
- added BuildRequires for tv_grab_uk_bleb

* Tue May 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.34-1mdk
- 0.5.34
- fr grabbers are now merged upstream

* Sun May 23 2004 Stefan van der Eijk <stefan@mandrake.org> 0.5.33-1mdk
- 0.5.33
- drop patch0
- BuildRequires: perl-WWW-Mechanize (tv_grab_na_icons)

* Thu Apr 22 2004 Stefan van der Eijk <stefan@eijk.nu> 0.5.32-4mdk
- add BuildRequires: perl-HTML-LinkExtractor for tv_grab_no
- add BuildRequires: perl-XML-LibXML for tv_grab_se

* Mon Apr 19 2004 Stefan van der Eijk <stefan@eijk.nu> 0.5.32-3mdk
- add BuildRequires: perl-SOAP-Lite for tv_grab_na_dd
- add BuildRequires: perl-Text-Kakasi for tv_grab_jp
- todo: add BuildRequires: perl-HTML-Entities
  perl-HTML-LinkExtractor for tv_grab_no

* Sun Apr 18 2004 Stefan van der Eijk <stefan@eijk.nu> 0.5.32-2mdk
- SOURCE1: XMLTV::Europe_TZ -->  XMLTV::DST

* Fri Apr 16 2004 Stefan van der Eijk <stefan@eijk.nu> 0.5.32-1mdk
- 0.5.32

* Tue Apr 13 2004 Stefan van der Eijk <stefan@eijk.nu> 0.5.31-1mdk
- 0.5.31

* Sun Feb 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.29-1mdk
- 0.5.29

* Mon Feb 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.28-1mdk
- 0.5.28

* Sat Jan 17 2004 Stefan van der Eijk <stefan@eijk.nu> 0.5.27-1mdk
- merge changes from thac's package


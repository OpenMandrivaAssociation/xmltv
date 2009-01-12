%define name	xmltv
%define version 0.5.53
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A set of utilities to manage your TV viewing
#URL:		http://membled.com/work/apps/xmltv/
URL:		http://wiki.xmltv.org
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch2:		xmltv-0.5.39-jp-utf8.patch
Patch4:		xmltv-0.5.42-Makefile.patch
Patch7:		xmltv-0.5.3-None.pm_strict.patch
License:	GPLv2+
Group:		Video
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-CGI
BuildRequires:	perl-DateManip => 5.42
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-LinkExtractor
BuildRequires:	perl-HTML-TableExtract => 1.08
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTTP-Cache-Transparent
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-libwww-perl => 5.65
BuildRequires:	perl-Lingua-Preferred
BuildRequires:	perl-Lingua-EN-Numbers-Ordinate
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-Term-ProgressBar >= 2.03
BuildRequires:	perl-Term-ReadKey
#BuildRequires:	perl-Text-Bidi
BuildRequires:	perl-Text-Kakasi
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
%{_datadir}/xmltv/xmltv.dtd
%{_docdir}/%{name}-%{version}

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

%package	grabbers-be
Summary:	Belgian grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-be
This package contains the belgian grabbers for xmltv.

%files grabbers-be
%defattr(-,root,root)
%{_bindir}/tv_grab_be
%{_mandir}/man1/tv_grab_be*.1*
%{_datadir}/xmltv/tv_grab_be/channel_ids_fr
%{_datadir}/xmltv/tv_grab_be/channel_ids_nl

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
%{_datadir}/xmltv/tv_grab_ch_*/channel_ids

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
%{_datadir}/xmltv/tv_grab_ch_*/channel_ids

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
%{_mandir}/man1/tv_grab_eu_epgdata.1.lzma
%{_datadir}/xmltv/tv_grab_eu_epgdata/channel_ids

%package	grabbers-fi
Summary:	Finish grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-fi
This package contains the finish grabbers for xmltv.

%files grabbers-fi
%defattr(-,root,root)
%{_bindir}/tv_grab_fi
%{_mandir}/man1/tv_grab_fi.1*

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
%{_mandir}/man1/tv_grab_fr.1*

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

%files grabbers-huro
%defattr(-,root,root)
%{_bindir}/tv_grab_huro
%{_mandir}/man1/tv_grab_huro.1*
%{_datadir}/xmltv/tv_grab_huro/jobmap
%{_datadir}/xmltv/tv_grab_huro/catmap.hu
%{_datadir}/xmltv/tv_grab_huro/catmap.ro

#package	grabbers-il
#Summary:	Israeli grabbers for xmltv
#Group:		Video
#Provides:	xmltv-grabbers

#description grabbers-il
#This package contains the israeli grabbers for xmltv.

#files grabbers-il
#defattr(-,root,root)
#{_bindir}/tv_grab_il*
#{_mandir}/man1/tv_grab_il*.1*

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

#%package	grabbers-nl
#Summary:	Dutch grabbers for xmltv
#Group:		Video
#Provides:	xmltv-grabbers

#description grabbers-nl
#This package contains the dutch grabbers for xmltv.

#files grabbers-nl
#defattr(-,root,root)
#{_bindir}/tv_grab_nl*
#{_mandir}/man1/tv_grab_nl*.1*

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
%{_bindir}/tv_grab_pt
%{_mandir}/man1/tv_grab_pt.1*

%package	grabbers-re
Summary:	Reunion island grabbers for xmltv
Group:		Video
Provides:	xmltv-grabbers

%description grabbers-re
This package contains the Reunion Island (France) grabbers for xmltv.

%files grabbers-re
%defattr(-,root,root)
%{_bindir}/tv_grab_re*
%{_mandir}/man1/tv_grab_re*.1*

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

%build
export PREFIX=/usr
%{__perl} Makefile.PL INSTALLDIRS=vendor 'PREFIX=$(MYDESTDIR)'%{_prefix} <<EOF
yes
EOF

%{__make}
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT



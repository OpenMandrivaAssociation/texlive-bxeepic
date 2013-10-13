# revision 30559
# category Package
# catalog-ctan /macros/latex/contrib/bxeepic
# catalog-date 2013-05-18 23:56:07 +0200
# catalog-license other-free
# catalog-version 0.2
Name:		texlive-bxeepic
Version:	0.2
Release:	1
Summary:	Eepic facilities using pict2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxeepic
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxeepic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxeepic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an eepic driver to use pict2e facilities.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bxeepic/bxdpxp2e.def
%{_texmfdistdir}/tex/latex/bxeepic/bxeepic.sty
%doc %{_texmfdistdir}/doc/latex/bxeepic/LICENSE
%doc %{_texmfdistdir}/doc/latex/bxeepic/README
%doc %{_texmfdistdir}/doc/latex/bxeepic/sample-bxeepic.pdf
%doc %{_texmfdistdir}/doc/latex/bxeepic/sample-bxeepic.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

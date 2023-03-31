Name:		texlive-bxeepic
Version:	30559
Release:	2
Summary:	Eepic facilities using pict2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxeepic
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxeepic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxeepic.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

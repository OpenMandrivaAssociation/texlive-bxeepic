%global tl_name bxeepic
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Eepic facilities using pict2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxeepic
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxeepic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxeepic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an eepic driver to use pict2e facilities.


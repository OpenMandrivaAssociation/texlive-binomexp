%global tl_name binomexp
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Calculate Pascals triangle
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/binomexp
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package calculates and prints rows of Pascal's triangle. It may be
used: simply to print successive rows of the triangle, or to print the
rows inside an array or tabular.


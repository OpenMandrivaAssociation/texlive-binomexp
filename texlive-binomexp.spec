Name:		texlive-binomexp
Version:	15878
Release:	2
Summary:	Calculate Pascal's triangle
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/binomexp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package calculates and prints rows of Pascal's triangle. It
may be used: - simply to print successive rows of the triangle,
or - to print the rows inside an array or tabular.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/binomexp/binomexp.sty
%doc %{_texmfdistdir}/doc/latex/binomexp/README
%doc %{_texmfdistdir}/doc/latex/binomexp/binomexp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/binomexp/binomexp.dtx
%doc %{_texmfdistdir}/source/latex/binomexp/binomexp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

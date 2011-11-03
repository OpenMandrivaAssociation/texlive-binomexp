# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/binomexp
# catalog-date 2007-03-05 14:17:42 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-binomexp
Version:	1.0
Release:	1
Summary:	Calculate Pascal's triangle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/binomexp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binomexp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package calculates and prints rows of Pascal's triangle. It
may be used: - simply to print successive rows of the triangle,
or - to print the rows inside an array or tabular.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/binomexp/binomexp.sty
%doc %{_texmfdistdir}/doc/latex/binomexp/README
%doc %{_texmfdistdir}/doc/latex/binomexp/binomexp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/binomexp/binomexp.dtx
%doc %{_texmfdistdir}/source/latex/binomexp/binomexp.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

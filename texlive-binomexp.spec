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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package calculates and prints rows of Pascal's triangle. It may be
used: simply to print successive rows of the triangle, or to print the
rows inside an array or tabular.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/binomexp
%dir %{_datadir}/texmf-dist/source/latex/binomexp
%dir %{_datadir}/texmf-dist/tex/latex/binomexp
%doc %{_datadir}/texmf-dist/doc/latex/binomexp/README
%doc %{_datadir}/texmf-dist/doc/latex/binomexp/binomexp.pdf
%doc %{_datadir}/texmf-dist/source/latex/binomexp/binomexp.dtx
%doc %{_datadir}/texmf-dist/source/latex/binomexp/binomexp.ins
%{_datadir}/texmf-dist/tex/latex/binomexp/binomexp.sty
